# Project 04: Student Grade Analyzer

---

## Overview

This is a **Python-based Student Grade Analyzer** that processes student records from a CSV file and generates both statistical insights and visualizations.  

It works with a CSV file in the format:

```
Student ID, Course, Grade
1, Math, A
1, Science, B
2, Math, C

```

---

### Features:
- Converts **letter grades (A–F)** into numeric scores  
- Builds a **pivot table** of students vs. subjects  
- Calculates each student’s **average grade**  
- Classifies students as **Pass/Fail** (average ≥ 75 = Pass)  
- Computes **average score per subject**  
- Identifies the **Top 5 students**  
- Generates **visualizations**:
  - Distribution of averages  
  - Average score per subject  
  - Pass vs Fail counts  
  - Boxplot of grade distribution per subject  

This project is part of my **Python Progress Tracker**, where I focus on building skills in **data analysis, visualization, and automation**.

---

## Dependencies

Make sure you have the following installed:

pip install pandas matplotlib seaborn

---

## Future Enhancements

Export processed results to CSV/Excel

Add median, mode, and standard deviation calculations

More advanced grading rules (e.g., weighted averages)

Interactive GUI version (Tkinter/PyQt)

Web-based dashboard (Flask/Django + Chart.js/Plotly)

Student performance prediction using Machine Learning

---