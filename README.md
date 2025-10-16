
# Student Success Predictive System

**Goal:** To analyze and visualize factors influencing student academic success using interactive data-driven exploration.

---

## Project Overview

This project presents an **interactive data exploration and visualization web application** built with **Streamlit** to uncover insights from student academic data.

The system allows users to:

* Explore relationships between demographic, academic, and behavioral variables.
* Visualize correlations, feature importance, and summary insights.
* Support evidence-based decision-making for student success strategies.

---

## Objectives

1. **Data Understanding** — Explore dataset structure and attribute summaries.
2. **Exploratory Data Analysis (EDA)** — Identify trends and patterns.
3. **Correlation Study** — Quantify relationships among numeric features.
4. **Feature Analysis** — Examine key factors affecting student performance.
5. **Summary Report** — Present key findings and interpretations concisely.

---

## Target Audience

* **University Researchers** studying factors influencing student performance.
* **Educators & Administrators** identifying at-risk students.
* **Data Science Students** learning data analysis and visualization workflows.
* **Policy Analysts** evaluating educational outcome determinants.

---

## Methodology

1. **Data Loading & Cleaning**

   * Dataset loaded via `config.py` path configuration.
   * Columns standardized and formatted for consistency.

2. **Exploratory Data Analysis (EDA)**

   * Displayed feature distributions, outliers, and group comparisons.
   * Visualized categorical and numerical variables using Seaborn & Matplotlib.

3. **Correlation Study**

   * Highlighted relationships among numeric features using heatmaps.
   * Revealed strong dependencies and redundancies in academic indicators.

4. **Feature Analysis**

   * Identified variables most associated with student outcomes.
   * Explored feature-target correlations for insight extraction.

5. **Summary Report**

   * Compiled key findings and interpretations from all pages.
   * Provided a clear overview of data-driven insights and next steps.

---

## Key Insights

* **Study time, absences, and failures** strongly influence final outcomes.
* **Parental education** and **family support** correlate with academic success.
* **Gender and age distribution** show subtle but measurable patterns.
* **Correlation heatmaps** highlight meaningful variable interactions.

---

## Technology Stack

| Category             | Tools Used          |
| -------------------- | ------------------- |
| Programming Language | Python 3.10+        |
| Framework            | Streamlit           |
| Data Manipulation    | Pandas              |
| Visualization        | Seaborn, Matplotlib |
| Config Management    | Custom `config.py`  |

---

## Folder Structure

```
student_success_app/
│
├── assets/
│
├── config.py
│
├── data/
│   ├── student_data.csv
│   └── student_data.xlsx
│
├── Home.py
│
├── pages/
│   ├── 1_Data_Overview.py
│   ├── 2_EDA_Insights.py
│   ├── 3_Feature_Analysis.py
│   ├── 4_Correlation_Study.py
│   └── 5_Summary_Report.py
│
├── utils/
│
├── README.md
└── requirements.txt
```

---

## Installation & Setup

**1. Clone or copy the project**

```bash
git clone https://github.com/preetilnarayan/student_success_app.git
cd student_success_app
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Set dataset path in `config.py`**

```python
STUDENT_DATA_PATH = r"PATH_TO_YOUR_CSV_FILE"
```

**4. Run the Streamlit app**

```bash
streamlit run Home.py
```

---

## Example Visualizations

| Visualization               | Description                                   |
| --------------------------- | --------------------------------------------- |
| **Target Distribution**  | Analyze student outcome balance.              |
| **Gender vs Target**  | Compare academic success by gender.           |
| **Age Histogram**        | Study performance trends across age groups.   |
| **Correlation Heatmap**  | Visualize feature relationships.              |
| **Pairplots & Boxplots** | Identify inter-feature patterns and variance. |

---

## Requirements

| Package    | Recommended Version |
| ---------- | ------------------- |
| Python     | ≥ 3.10              |
| Streamlit  | ≥ 1.36              |
| Pandas     | ≥ 2.2               |
| Seaborn    | ≥ 0.13              |
| Matplotlib | ≥ 3.8               |

---

## Author

**Preeti Lakshmi Narayan**
M.S. Data Science | Michigan State University

---

## References

* UCI Machine Learning Repository: *Student Performance Dataset*
* Streamlit Documentation: [https://docs.streamlit.io](https://docs.streamlit.io)
* Seaborn Visualization Guide: [https://seaborn.pydata.org](https://seaborn.pydata.org)