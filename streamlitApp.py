import streamlit as st
import pandas as pd
import plotly.express as px

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

# Line Chart — Mileage over time using Plotly
st.subheader("Mileage Over Time")
df_sorted = df.sort_values("Date")
fig = px.line(df_sorted, x="Date", y="Distance", markers=True,
              title="Daily Distance")
st.plotly_chart(fig)

# Bar Chart — Mileage by Day of Week
st.subheader("Average Distance by Day of Week")
distance_by_day = df.groupby("DayOfWeek")["Distance"].mean().reset_index()
fig2 = px.bar(distance_by_day, x="DayOfWeek", y="Distance",
              title="Average Distance per Day")
st.plotly_chart(fig2)

# Scatter — Effort vs Distance (how hard were the runs?)
st.subheader("Effort vs Distance")
fig3 = px.scatter(df, x="Distance", y="Effort", hover_data=["Notes"],
                  title="Effort vs Distance")
st.plotly_chart(fig3)
