# ------------------------------
# Student Grades Analyzer (Upgraded)
# ------------------------------
# Features:
# - Reads grades from CSV
# - Numeric conversion + analysis
# - Exports processed results (CSV/Excel)
# - Calculates mean, median, mode, std dev
# - Supports weighted grading rules
# - Visualization (matplotlib + seaborn)
# - GUI (Tkinter)
# - Web Dashboard (Flask + Plotly)
# - ML model to predict performance
# ------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from statistics import median, mode
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import tkinter as tk
from tkinter import filedialog, messagebox
from flask import Flask, render_template_string
import plotly.express as px

# ------------------------------
# Step 1: Load dataset
# ------------------------------
BASE_DIR = os.path.dirname(__file__)
df = pd.read_csv(os.path.join(BASE_DIR, "student_grades.csv"))

print("Raw Dataset Preview:")
print(df.head(), "\n")

# ------------------------------
# Step 2: Convert letter grades to numeric
# ------------------------------
grade_mapping = {"A": 95, "B": 85, "C": 75, "D": 65, "F": 50}
df["NumericGrade"] = df["Grade"].map(grade_mapping)

# ------------------------------
# Step 3: Pivot Table (students as rows, courses as columns)
# ------------------------------
pivot_df = df.pivot(index="Student ID", columns="Course", values="NumericGrade")

# Simple average
pivot_df["Average"] = pivot_df.mean(axis=1)

# Weighted average example (Math weighted higher)
weights = {"Math": 0.4, "Science": 0.3, "English": 0.3}
pivot_df["WeightedAverage"] = pivot_df.apply(
    lambda row: sum(row.get(subj, 0) * w for subj, w in weights.items()) / sum(weights.values()),
    axis=1
)

# Status
pivot_df["Status"] = pivot_df["WeightedAverage"].apply(lambda x: "Pass" if x >= 75 else "Fail")

print("Processed Student Data:")
print(pivot_df.head(), "\n")

# ------------------------------
# Step 4: Analysis
# ------------------------------
subject_means = pivot_df.drop(columns=["Average", "WeightedAverage", "Status"]).mean()
top_students = pivot_df.sort_values(by="WeightedAverage", ascending=False).head(5)
status_counts = pivot_df["Status"].value_counts()

print("Average Score per Subject:")
print(subject_means, "\n")

print("Top 5 Students:")
print(top_students[["WeightedAverage", "Status"]], "\n")

print("Pass/Fail Counts:")
print(status_counts, "\n")

print("Extra Stats:")
print("Median Average:", median(pivot_df["WeightedAverage"]))
print("Mode Average:", mode(pivot_df["WeightedAverage"]))
print("Std Dev Average:", pivot_df["WeightedAverage"].std(), "\n")

# ------------------------------
# Step 5: Export results
# ------------------------------
pivot_df.to_csv(os.path.join(BASE_DIR, "processed_results.csv"))
pivot_df.to_excel(os.path.join(BASE_DIR, "processed_results.xlsx"))

# ------------------------------
# Step 6: Visualizations
# ------------------------------
plt.figure(figsize=(8,5))
sns.histplot(pivot_df["WeightedAverage"], bins=5, kde=True)
plt.title("Distribution of Student Weighted Averages")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x=subject_means.index, y=subject_means.values)
plt.title("Average Score per Subject")
plt.show()

plt.figure(figsize=(6,4))
sns.countplot(x="Status", data=pivot_df)
plt.title("Pass vs Fail")
plt.show()

plt.figure(figsize=(10,6))
sns.boxplot(x="Course", y="NumericGrade", data=df)
plt.title("Grade Distribution per Subject")
plt.show()

# ------------------------------
# Step 7: Machine Learning Prediction
# ------------------------------
X = pivot_df.drop(columns=["Status"])
y = pivot_df["Status"].map({"Pass": 1, "Fail": 0})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print("ML Performance Report:")
print(classification_report(y_test, y_pred), "\n")

# ------------------------------
# Step 8: GUI (Tkinter)
# ------------------------------
def open_file():
    filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    if filepath:
        df = pd.read_csv(filepath)
        messagebox.showinfo("File Loaded", f"Loaded {len(df)} rows")

root = tk.Tk()
root.title("Student Grades Analyzer")
tk.Button(root, text="Open CSV", command=open_file).pack(pady=10)
tk.Button(root, text="Quit", command=root.destroy).pack(pady=10)
# root.mainloop()  # Uncomment to run GUI

# ------------------------------
# Step 9: Web Dashboard (Flask + Plotly)
# ------------------------------
app = Flask(__name__)

@app.route("/")
def dashboard():
    fig = px.histogram(pivot_df, x="WeightedAverage", nbins=10, title="Distribution of Student Weighted Averages")
    graph_html = fig.to_html(full_html=False)
    return render_template_string("""
        <html>
        <head><title>Student Dashboard</title></head>
        <body>
        <h1>Student Performance Dashboard</h1>
        {{ graph|safe }}
        </body>
        </html>
    """, graph=graph_html)

# To run Flask server: Uncomment below
if __name__ == "__main__":
    app.run(debug=True)
