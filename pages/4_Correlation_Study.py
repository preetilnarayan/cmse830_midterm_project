import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from config import STUDENT_DATA_PATH

st.title("Correlation Study (Interactive)")

try:
    # Load and clean dataset
    df = pd.read_csv(STUDENT_DATA_PATH, sep=';', skipinitialspace=True)
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(r'\s+', ' ', regex=True)

    # Sidebar for interactivity
    st.sidebar.header("Settings")
    
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    exclude_cols = ['Application order', 'Unemployment rate', 'Inflation rate', 'GDP']
    numeric_cols = [col for col in numeric_cols if col not in exclude_cols]

    selected_features = st.sidebar.multiselect(
        "Select numeric features for correlation",
        options=numeric_cols,
        default=numeric_cols
    )

    show_abs = st.sidebar.checkbox("Show absolute correlation?", value=True)
    top_n = st.sidebar.slider("Number of top features to display", 1, min(len(selected_features), 15), 10)
    figsize_x = st.sidebar.slider("Figure width", 5, 20, 10)
    figsize_y = st.sidebar.slider("Figure height", 5, 15, 6)

    if len(selected_features) > 1:
        df_corr = df[selected_features].copy()

        # Include Target if exists
        if 'Target' in df.columns:
            df_corr['Target'] = df['Target'].astype('category').cat.codes
            corr_matrix = df_corr.corr()
            corr_with_target = corr_matrix['Target']

            if show_abs:
                corr_with_target = corr_with_target.abs()

            top_features = corr_with_target.sort_values(ascending=False).head(top_n).index.tolist()
            df_top = df_corr[top_features]
        else:
            corr_matrix = df_corr.corr()
            if show_abs:
                corr_matrix = corr_matrix.abs()
            mean_corr = corr_matrix.mean().sort_values(ascending=False)
            top_features = mean_corr.head(top_n).index.tolist()
            df_top = df_corr[top_features]

        # Plot heatmap
        st.write("### Correlation Heatmap")
        plt.figure(figsize=(figsize_x, figsize_y))
        sns.heatmap(df_top.corr(), annot=True, fmt=".2f", cmap='coolwarm', linewidths=0.5)
        st.pyplot(plt.gcf())
        plt.clf()

        st.write(f"Top correlated features displayed: **{', '.join(top_features)}**")
    else:
        st.warning("Please select at least 2 features for correlation.")

except FileNotFoundError:
    st.error(f"Dataset not found at: `{STUDENT_DATA_PATH}`")
