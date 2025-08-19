import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Marathon Training Dashboard")

### Load Data ###
df = pd.read_csv("runs.csv")
goals_df = pd.read_csv("goals.csv")

df['Date'] = pd.to_datetime(df['Date'])

# ----------------------------
# Section 1: Actual vs Goal
# ----------------------------
st.header("Actual vs Planned Weekly Mileage")

# Calculate actual mileage by week
weekly_actual = df.groupby('WeekNumber')['Distance'].sum().reset_index()
weekly_actual.rename(columns={'Distance': 'ActualMileage'}, inplace=True)

# Merge with goals.csv
weekly_compare = pd.merge(goals_df, weekly_actual, on='WeekNumber', how='left')

# Add progress percentage
weekly_compare['PercentOfGoal'] = (
    weekly_compare['ActualMileage'] / weekly_compare['WeeklyMilage'] * 100
).round(1)

st.dataframe(weekly_compare)

fig_compare = px.bar(
    weekly_compare,
    x='WeekNumber',
    y=['WeeklyMilage', 'ActualMileage'],
    barmode='group',
    title="Planned vs Actual Mileage"
)
st.plotly_chart(fig_compare)

# ----------------------------
# Section 2: Weekly Mileage Trend
# ----------------------------
st.header("Weekly Mileage Trend Over Time")

fig_trend = px.line(
    weekly_actual,
    x='WeekNumber',
    y='ActualMileage',
    markers=True,
    title="Weekly Mileage Trend"
)
fig_trend.update_layout(yaxis_title="Miles")
st.plotly_chart(fig_trend)

# ----------------------------
# Section 3: Cumulative Totals
# ----------------------------
st.header("Cumulative Totals")

total_miles = df['Distance'].sum()
total_calories = df['Calories'].sum()

# Convert Time column to total seconds, flexible parsing
def time_to_seconds(t):
    parts = t.split(':')
    if len(parts) == 2:
        return pd.to_timedelta("00:" + t).total_seconds()
    else:
        return pd.to_timedelta(t).total_seconds()

df['TimeSeconds'] = df['Time'].apply(time_to_seconds)
total_seconds = df['TimeSeconds'].sum()
hours = int(total_seconds // 3600)
mins = int((total_seconds % 3600) // 60)

st.write(f"**Total Miles Run:** {total_miles:.2f} miles")
st.write(f"**Total Calories Burned:** {total_calories} calories")
st.write(f"**Total Time Spent Running:** {hours}h {mins}m")

# Average Pace Overall
def pace_to_seconds(pace_str):
    parts = pace_str.split(':')
    if len(parts) == 2:
        return int(parts[0]) * 60 + int(parts[1])
    else:
        td = pd.to_timedelta(pace_str)
        return int(td.total_seconds())

df['PaceSeconds'] = df['AveragePace'].apply(pace_to_seconds)
avg_pace_seconds = df['PaceSeconds'].mean()
avg_minutes = int(avg_pace_seconds // 60)
avg_seconds = int(avg_pace_seconds % 60)
avg_pace_formatted = f"{avg_minutes:02d}:{avg_seconds:02d}"

st.write(f"**Average Pace Overall:** {avg_pace_formatted} per mile")
