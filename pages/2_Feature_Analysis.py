import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from config import STUDENT_DATA_PATH

st.title("Feature Analysis")

try:
    # Load and clean dataset
    df = pd.read_csv(STUDENT_DATA_PATH, sep=';', skipinitialspace=True)
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(r'\s+', ' ', regex=True)

    if 'Target' in df.columns:
        # Select numeric columns only
        df_numeric = df.select_dtypes(include=['int64', 'float64']).copy()
        df_numeric['Target'] = df['Target'].astype('category').cat.codes

        # Sidebar controls for interactivity
        st.sidebar.header("Settings")
        selected_features = st.sidebar.multiselect(
            "Select numeric features to analyze",
            options=df_numeric.columns.tolist(),
            default=df_numeric.columns.tolist()
        )

        show_abs = st.sidebar.checkbox("Show absolute correlation?", value=True)
        sort_desc = st.sidebar.checkbox("Sort by correlation descending?", value=True)

        if len(selected_features) > 1:
            # Compute correlation with Target
            corr = df_numeric[selected_features].corr()['Target']

            if show_abs:
                corr = corr.abs()

            if sort_desc:
                corr = corr.sort_values(ascending=False)

            st.write("### Correlation with Target")
            st.dataframe(
                corr.to_frame().style.background_gradient(cmap='coolwarm').format(precision=2),
                height=400
            )

            # Plot top N correlations using Matplotlib
            top_n = st.sidebar.slider(
                "Select number of top features to plot",
                min_value=1, max_value=len(corr)-1, value=5
            )
            top_corr = corr.drop('Target').head(top_n)

            st.write("### Top Correlated Features (Bar Chart)")
            fig, ax = plt.subplots(figsize=(8, 4))
            top_corr.plot(kind='bar', color='skyblue', ax=ax)
            ax.set_ylabel('Correlation with Target')
            ax.set_xlabel('Features')
            ax.set_title('Top Correlated Features')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig)

        else:
            st.warning("Please select at least 2 features to analyze correlation.")
    else:
        st.info("No Target column found in the dataset.")

except FileNotFoundError:
    st.error(f"Dataset not found at: `{STUDENT_DATA_PATH}`")
