import streamlit as st
import boto3
import pandas as pd
import time

# -------------------------------
# AWS CONFIG
# -------------------------------
TABLE_NAME = "ColdStorageData"
REGION = "us-east-1"

dynamodb = boto3.resource("dynamodb", region_name=REGION)
table = dynamodb.Table(TABLE_NAME)

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Cold Storage Dashboard", layout="wide")

st.title("❄️ Cold Storage Monitoring Dashboard")

# -------------------------------
# LOAD DATA
# -------------------------------
def load_data():
    response = table.scan()
    items = response.get("Items", [])

    if not items:
        return pd.DataFrame()

    df = pd.DataFrame(items)

    # Convert types safely
    df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
    df["humidity"] = pd.to_numeric(df["humidity"], errors="coerce")
    df["time"] = pd.to_numeric(df["time"], errors="coerce")

    # Drop bad rows
    df = df.dropna()

    # Convert time
    df["time"] = pd.to_datetime(df["time"], unit="s")

    # Sort
    df = df.sort_values(by="time")

    return df


df = load_data()

# -------------------------------
# EMPTY CHECK
# -------------------------------
if df.empty:
    st.error("❌ No data found in DynamoDB")
    st.stop()

# -------------------------------
# FILTER
# -------------------------------
st.sidebar.header("⚙️ Controls")
limit = st.sidebar.slider("Show last N records", 10, 200, 50)

df = df.tail(limit)

# -------------------------------
# LAST UPDATE TIME
# -------------------------------
st.caption(f"Last updated: {time.strftime('%H:%M:%S')}")

# -------------------------------
# CURRENT STATUS
# -------------------------------
latest = df.iloc[-1]

col1, col2, col3 = st.columns(3)

col1.metric("🌡 Current Temp (°C)", round(latest["temperature"], 2))
col2.metric("💧 Humidity (%)", round(latest["humidity"], 2))
col3.metric("🕒 Latest Time", str(latest["time"].time()))

# STATUS ALERT
if latest["temperature"] > 8:
    st.error("🚨 STATUS: CRITICAL (Temperature too high)")
else:
    st.success("✅ STATUS: NORMAL")

# -------------------------------
# STATISTICS
# -------------------------------
st.subheader("📊 Statistics")

avg_temp = df["temperature"].mean()
max_temp = df["temperature"].max()
min_temp = df["temperature"].min()

col1, col2, col3 = st.columns(3)

col1.metric("Average Temp", round(avg_temp, 2))
col2.metric("Max Temp", round(max_temp, 2))
col3.metric("Min Temp", round(min_temp, 2))

# Trend warning
if df["temperature"].tail(5).mean() > 8:
    st.warning("⚠️ Sustained high temperature detected")

# -------------------------------
# GRAPHS
# -------------------------------
st.subheader("📈 Temperature Trend")
st.line_chart(df.set_index("time")["temperature"])

st.subheader("💧 Humidity Trend")
st.line_chart(df.set_index("time")["humidity"])

# -------------------------------
# ALERT HISTORY
# -------------------------------
st.subheader("🚨 Alert History (Temp > 8°C)")

alerts = df[df["temperature"] > 8]

if alerts.empty:
    st.success("No alerts recorded")
else:
    st.dataframe(alerts)

# -------------------------------
# RAW DATA
# -------------------------------
st.subheader("📋 Raw Data")

# Clean column names
df_display = df.rename(columns={
    "temperature": "Temperature (°C)",
    "humidity": "Humidity (%)",
    "time": "Time"
})

st.dataframe(df_display)
