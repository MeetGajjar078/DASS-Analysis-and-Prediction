# DASS Analysis and Prediction

This repository analyzes the **Depression, Anxiety, and Stress Scales (DASS)** dataset and develops predictive models to classify emotional states into severity levels. Additionally, an interactive web application was created using Streamlit to provide real-time insights and predictions.

---

## Overview

The DASS dataset contains responses to a structured questionnaire designed to measure negative emotional states such as depression, anxiety, and stress. This project:
- Performs an exploratory data analysis (EDA) to uncover patterns and trends.
- Builds machine learning models to classify emotional states into severity levels.
- Provides an interactive web application for real-time predictions and data visualizations.

---

## Features

### 1. Exploratory Data Analysis (EDA)
- Visualizes the distribution of responses across depression, anxiety, and stress subscales.
- Identifies demographic patterns such as age, education, and gender influencing emotional states.
- Highlights correlations between features using heatmaps.

### 2. Predictive Modeling
- Machine learning models (Random Forest, Logistic Regression, Gradient Boosting) classify emotional states into:
  - Normal
  - Mild
  - Moderate
  - Severe
  - Extremely Severe
- Supports predictions for Depression, Anxiety, and Stress.

### 3. Interactive Web Application
- **DASS Information**: Explains the DASS framework.
- **Prediction Panel**: Allows users to input responses and predict emotional states.
- **Information Gathering**: Collects demographic data for further analysis.
- **Dynamic Visualizations**: Displays interactive pie and bar charts.

---

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - Streamlit (Web Application)
  - Scikit-learn (Machine Learning)
  - Pandas (Data Processing)
  - Matplotlib & Seaborn (Visualization)

---

## Getting Started

### Prerequisites
Ensure you have Python 3.8 or later installed along with the required libraries. Install dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
