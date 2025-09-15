# ------------------------------
# Student Grades Analyzer
# ------------------------------
# Works with a CSV in the format:
# Student ID, Course, Grade
# Example:
# 1, Math, A
# 1, Science, B
# ------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ------------------------------
# Step 1: Load the dataset
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
# Step 3: Pivot table (students as rows, courses as columns)
# ------------------------------
pivot_df = df.pivot(index="Student ID", columns="Course", values="NumericGrade")

# Calculate average grade per student
pivot_df["Average"] = pivot_df.mean(axis=1)

# Classify Pass/Fail (rule: average >= 75 is Pass)
pivot_df["Status"] = pivot_df["Average"].apply(lambda x: "Pass" if x >= 75 else "Fail")

print("Processed Student Data:")
print(pivot_df.head(), "\n")

# ------------------------------
# Step 4: Analysis
# ------------------------------
# Average score per subject
subject_means = pivot_df.drop(columns=["Average", "Status"]).mean()

# Top 5 students
top_students = pivot_df.sort_values(by="Average", ascending=False).head(5)

# Pass/Fail counts
status_counts = pivot_df["Status"].value_counts()

print("Average Score per Subject:")
print(subject_means, "\n")

print("Top 5 Students:")
print(top_students[["Average", "Status"]], "\n")

print("Pass/Fail Counts:")
print(status_counts, "\n")

# ------------------------------
# Step 5: Visualizations
# ------------------------------

# Distribution of averages
plt.figure(figsize=(8,5))
sns.histplot(pivot_df["Average"], bins=5, kde=True)
plt.title("Distribution of Student Averages")
plt.xlabel("Average Grade")
plt.ylabel("Number of Students")
plt.show()

# Bar chart of subject averages
plt.figure(figsize=(8,5))
sns.barplot(x=subject_means.index, y=subject_means.values)
plt.title("Average Score per Subject")
plt.ylabel("Score")
plt.show()

# Pass vs Fail counts
plt.figure(figsize=(6,4))
sns.countplot(x="Status", data=pivot_df)
plt.title("Pass vs Fail")
plt.show()

# Boxplot per course
plt.figure(figsize=(10,6))
sns.boxplot(x="Course", y="NumericGrade", data=df)
plt.title("Grade Distribution per Subject")
plt.show()
