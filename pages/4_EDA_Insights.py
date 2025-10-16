import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from config import STUDENT_DATA_PATH

st.title("Exploratory Data Analysis (EDA) & Insights")

try:
    # Load and clean dataset
    df = pd.read_csv(STUDENT_DATA_PATH, sep=';', skipinitialspace=True)
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(r'\s+', ' ', regex=True)

    # Encode Target if present
    if 'Target' in df.columns:
        df['Target_encoded'] = df['Target'].astype('category').cat.codes

    # Sidebar filters
    st.sidebar.header("Filters & Options")

    # Filter by Target
    if 'Target' in df.columns:
        selected_target = st.sidebar.multiselect(
            "Select Target", df['Target'].unique(), default=df['Target'].unique()
        )
        df = df[df['Target'].isin(selected_target)]

    # Filter by Gender
    if 'Gender' in df.columns:
        selected_gender = st.sidebar.multiselect(
            "Select Gender", df['Gender'].unique(), default=df['Gender'].unique()
        )
        df = df[df['Gender'].isin(selected_gender)]

    # Sidebar slider for pairplot sample size
    pairplot_sample = st.sidebar.slider(
        "Pairplot sample size", min_value=50, max_value=200, value=150
    )

    # Target Distribution
    st.subheader("Target Distribution")
    if 'Target' in df.columns:
        plt.figure(figsize=(6, 4))
        sns.countplot(x='Target', data=df, palette='pastel')
        plt.title("Target Distribution (Success vs Dropout)")
        st.pyplot(plt.gcf())
        plt.clf()
    else:
        st.info("No 'Target' column found in dataset.")

    # Gender vs Target
    if 'Gender' in df.columns and 'Target' in df.columns:
        st.subheader("Gender vs Target")
        plt.figure(figsize=(6, 4))
        sns.countplot(x='Gender', hue='Target', data=df, palette='Set2')
        plt.title("Gender Comparison by Target")
        st.pyplot(plt.gcf())
        plt.clf()

    # Age Distribution
    if 'Age at enrollment' in df.columns:
        st.subheader("Age Distribution")
        gender_map = {0: 'Male', 1: 'Female'}
        df_plot = df.copy()
        df['Gender_label'] = df['Gender'].map(gender_map).fillna(df['Gender'])
        plt.figure(figsize=(6, 4))
        sns.histplot(df['Age at enrollment'], kde=True, color='green', bins=20)
        plt.title("Age at Enrollment Distribution")
        st.pyplot(plt.gcf())
        plt.clf()

    # Mean ± SD Bar Plots for Top Correlated Features
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    exclude_cols = ['Application order', 'Unemployment rate', 'Inflation rate', 'GDP']
    numeric_cols = [col for col in numeric_cols if col not in exclude_cols]

    if 'Target_encoded' in df.columns and len(numeric_cols) > 1:
        df_numeric = df[numeric_cols + ['Target_encoded']].copy()
        corr = df_numeric.corr()['Target_encoded'].abs().sort_values(ascending=False)[1:5]  # Top 4 features
        top_corr_cols = corr.index.tolist()

        st.subheader("Feature-wise Mean ± SD by Target")
        st.caption("Displays average values of each feature across Target categories, with error bars for standard deviation.")

        for col in top_corr_cols:
            plt.figure(figsize=(6, 4))
            sns.barplot(
                x='Target',
                y=col,
                data=df,
                palette='coolwarm',
                ci='sd'  # Show mean ± standard deviation
            )
            plt.title(f"{col} by Target (Mean ± SD)")
            st.pyplot(plt.gcf())
            plt.clf()

        # Pairplot for top correlated numeric columns (sampled)
        st.subheader("Pairplot for Top Correlated Numeric Columns (Sample)")
        sample_df = df[top_corr_cols[:4] + ['Target_encoded']].dropna().sample(
            min(pairplot_sample, len(df)), random_state=30
        )
        custom_palette = ["#d30000", "#00be30", "#f9fd00"]
        sns.pairplot(sample_df, hue='Target_encoded', palette=custom_palette, diag_kind='kde')
        st.pyplot(plt.gcf())
        plt.clf()
    else:
        st.info("Not enough numeric data for visualization.")

except FileNotFoundError:
    st.error(f"Dataset not found at: `{STUDENT_DATA_PATH}`")
