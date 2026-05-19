# 📊 HR Attrition Analysis

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557c?style=for-the-badge)
![Seaborn](https://img.shields.io/badge/Seaborn-Visualization-4c9be8?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

**A complete end-to-end HR Employee Attrition Analysis project using Python, MySQL, and Data Visualization.**

[📁 View Project](https://github.com/codebyavneesh/hr-attrition-analysis) • [👤 Author](#-author) • [📸 Screenshots](#-screenshots)

</div>

---

## 📌 Project Overview

Employee attrition is one of the biggest challenges faced by HR departments. This project analyzes employee attrition data to uncover key patterns and insights — such as which departments, job roles, age groups, and salary ranges have the highest attrition rates.

The goal is to help organizations make **data-driven decisions** to improve employee retention.

---

## 🎯 Key Objectives

- 🔍 Identify which factors contribute most to employee attrition
- 📈 Analyze attrition trends across departments, job roles, and salary brackets
- 💡 Provide actionable insights through clear visualizations
- 🗄️ Store and query data efficiently using MySQL

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| **Python 3.8+** | Core programming language |
| **Pandas** | Data loading, cleaning & analysis |
| **MySQL** | Database storage & querying |
| **SQLAlchemy** | Python-MySQL connector/ORM |
| **Matplotlib** | Data visualization |
| **Seaborn** | Statistical plots & heatmaps |
| **Jupyter Notebook** | Interactive development environment |

---

## 📁 Project Structure

```
hr-attrition-analysis/
│
├── 📂 dataset/
│   └── emp_attrition.csv          # Raw employee attrition dataset
│
├── 📂 screenshots/
│   ├── age_vs_attrition.png
│   ├── attrition_rate_of_overtime.png
│   ├── average_salary_by_jobrol.png
│   ├── department_wise_employee.png
│   ├── monthlyIncome_vs_attrition.png
│   └── top_5_jobrols_with_highest_attrition.png
│
├── 📓 hr_attrition_project.ipynb  # Main Jupyter Notebook
└── 📄 README.md
```

---

## 📸 Screenshots

### 👥 Age vs Attrition
![Age vs Attrition](https://github.com/codebyavneesh/hr-attrition-analysis/blob/main/hr-attrition-analysis/screenshots/age_vs_attrition.png?raw=true)

### ⏰ Attrition Rate by Overtime
![Overtime Attrition](https://github.com/codebyavneesh/hr-attrition-analysis/blob/main/hr-attrition-analysis/screenshots/attrition_rate_of_overtime.png?raw=true)

### 💰 Average Salary by Job Role
![Salary by Job Role](https://github.com/codebyavneesh/hr-attrition-analysis/blob/main/hr-attrition-analysis/screenshots/average_salary_by_jobrol.png?raw=true)

### 🏢 Department-wise Employee Distribution
![Department wise](https://github.com/codebyavneesh/hr-attrition-analysis/blob/main/hr-attrition-analysis/screenshots/department_wise_employee.png?raw=true)

### 💵 Monthly Income vs Attrition
![Monthly Income](https://github.com/codebyavneesh/hr-attrition-analysis/blob/main/hr-attrition-analysis/screenshots/monthlyIncome_vs_attrition.png?raw=true)

### 🏆 Top 5 Job Roles with Highest Attrition
![Top Job Roles](https://github.com/codebyavneesh/hr-attrition-analysis/blob/main/hr-attrition-analysis/screenshots/top_5_jobrols_with_highest_attrition.png?raw=true)

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/codebyavneesh/hr-attrition-analysis.git
cd hr-attrition-analysis
```

### 2. Install Required Libraries
```bash
pip install pandas matplotlib seaborn sqlalchemy mysql-connector-python
```

### 3. MySQL Setup
Make sure MySQL is installed and running on your system, then update these variables in the notebook:
```python
DB_USER     = "root"
DB_PASSWORD = "root"
DB_HOST     = "localhost"
DB_NAME     = "hr_analysis"
```

### 4. Run the Notebook
```bash
jupyter notebook hr_attrition_project.ipynb
```

---

## 🔍 Key Insights

- 📌 **Overtime employees** have significantly higher attrition rates
- 📌 **Sales Representatives** and **Laboratory Technicians** are among the top attrition-prone job roles
- 📌 **Younger employees (age 25–35)** tend to leave more frequently
- 📌 **Lower monthly income** strongly correlates with higher attrition
- 📌 **Sales department** has the highest overall attrition compared to other departments

---

## 🚀 How It Works

1. **Data Loading** — CSV dataset loaded using Pandas
2. **Database Import** — Data pushed to MySQL using SQLAlchemy
3. **Data Cleaning** — Handling nulls, data types, duplicates
4. **Analysis** — Groupby, aggregations, correlation analysis
5. **Visualization** — Charts generated using Matplotlib & Seaborn

---

## 👤 Author

<div align="center">

**codebyavneesh**

[![GitHub](https://img.shields.io/badge/GitHub-codebyavneesh-181717?style=for-the-badge&logo=github)](https://github.com/codebyavneesh)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-codebyavneesh-0077B5?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/codebyavneesh/)

</div>

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<div align="center">
⭐ Agar ye project helpful laga toh <strong>Star</strong> zaroor karo!
</div>
