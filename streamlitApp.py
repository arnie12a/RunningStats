import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Marathon Training Dashboard")

# Load CSV
df = pd.read_csv("runs.csv", parse_dates=["Date"])

# Raw data preview
st.subheader("Raw Data")
st.dataframe(df)

# Summary Stats
total_distance = df["Distance"].sum()
total_calories = df["Calories"].sum()
avg_effort = df["Effort"].mean()

st.subheader("Summary Stats")
col1, col2, col3 = st.columns(3)
col1.metric("Total Miles", f"{total_distance:.2f}")
col2.metric("Total Calories", int(total_calories))
col3.metric("Avg Effort", f"{avg_effort:.1f}")

# 1 — Daily Mileage over Time
st.subheader("Daily Mileage Over Time")
df_sorted = df.sort_values("Date")
plt.figure(figsize=(10,4))
plt.plot(df_sorted["Date"], df_sorted["Distance"], marker='o', linestyle='-')
plt.xlabel("Date")
plt.ylabel("Distance (miles)")
plt.title("Daily Distance Over Time")
plt.grid(True)
st.pyplot(plt)

# 2 — Average Distance by Day of Week
st.subheader("Average Distance by Day of Week")
distance_by_day = df.groupby("DayOfWeek")["Distance"].mean()
plt.figure(figsize=(8,4))
distance_by_day = distance_by_day.reindex(["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
plt.bar(distance_by_day.index, distance_by_day.values, color='skyblue')
plt.ylabel("Average Distance (miles)")
plt.title("Average Distance per Day of Week")
plt.xticks(rotation=45)
st.pyplot(plt)

# 3 — Effort vs Distance Scatter
st.subheader("Effort vs Distance")
plt.figure(figsize=(8,5))
plt.scatter(df["Distance"], df["Effort"], c='orange')
plt.xlabel("Distance (miles)")
plt.ylabel("Effort")
plt.title("Effort vs Distance")
plt.grid(True)
st.pyplot(plt)

# 4 — Optional: Weekly Total Mileage
st.subheader("Weekly Total Mileage")
df["WeekNumber"] = df["WeekNumber"].astype(int)
weekly_mileage = df.groupby("WeekNumber")["Distance"].sum()
plt.figure(figsize=(8,4))
plt.bar(weekly_mileage.index, weekly_mileage.values, color='green')
plt.xlabel("Week Number")
plt.ylabel("Total Distance (miles)")
plt.title("Total Weekly Mileage")
st.pyplot(plt)
