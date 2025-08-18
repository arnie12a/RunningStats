import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime

st.title("Marathon Training Tracker")

# Read local CSV file
try:
    df = pd.read_csv("runs.csv")
except FileNotFoundError:
    st.error("The file 'runs.csv' was not found in the project directory.")
    st.stop()

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Display the raw data
st.subheader("Your Run Log")
st.dataframe(df)

# ---- Weekly Mileage ----
weekly_miles = df.groupby('WeekNumber')['Distance'].sum().reset_index()
st.subheader("Weekly Mileage")
fig1 = px.bar(weekly_miles, x='WeekNumber', y='Distance', title="Total Distance per Week")
st.plotly_chart(fig1)

# ---- Average Pace Trend ----
df['PaceSeconds'] = pd.to_timedelta("00:" + df['AveragePace']).dt.total_seconds()
st.subheader("Average Pace Over Time (in seconds)")
fig2 = px.line(df, x='Date', y='PaceSeconds', markers=True, title="Pace Trend")
fig2.update_layout(yaxis_title="Pace (seconds)")
st.plotly_chart(fig2)

# ---- Summary Stats ----
st.subheader("Summary Stats")
total_miles = df['Distance'].sum()
avg_pace_overall = df['PaceSeconds'].mean()
st.write(f"**Total Miles Run:** {total_miles:.2f}")
st.write(f"**Average Pace Overall:** {avg_pace_overall:.2f} seconds per mile")
