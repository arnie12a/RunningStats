from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

CSV_FILE = "runs.csv"

# Ensure CSV file exists with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Date", "WeekNumber", "DayOfWeek", "WorkoutType", "Distance",
            "Time", "AveragePace", "Calories", "Location", "Weather", "Effort", "Notes"
        ])

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        form_data = [
            request.form.get("Date"),
            request.form.get("WeekNumber"),
            request.form.get("DayOfWeek"),
            request.form.get("WorkoutType"),
            request.form.get("Distance"),
            request.form.get("Time"),
            request.form.get("AveragePace"),
            request.form.get("Calories"),
            request.form.get("Location"),
            request.form.get("Weather"),
            request.form.get("Effort"),
            request.form.get("Notes"),
        ]

        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(form_data)

        return redirect("/")  # reload the form

    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
