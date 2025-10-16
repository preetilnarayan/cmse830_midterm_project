import streamlit as st
import pandas as pd
from config import STUDENT_DATA_PATH

st.title("Data Overview")

# Initialize df as None
df = None

# Try to read the default dataset
try:
    df = pd.read_csv(STUDENT_DATA_PATH, sep=';', skipinitialspace=True)
    st.success(f"Dataset loaded successfully")
except FileNotFoundError:
    st.warning(f"Default dataset not found at: `{STUDENT_DATA_PATH}`")
    uploaded_file = st.file_uploader("Upload your CSV dataset here", type="csv")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file, sep=';', skipinitialspace=True)
        st.success("Dataset uploaded successfully!")

# Proceed only if dataset is available
if df is not None:
    # Clean column names
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace(r'\s+', ' ', regex=True)

    # Dataset Preview
    st.write("### Dataset Preview")
    st.dataframe(df.style.highlight_max(color='yellow').format(precision=2), height=400)

    # Dataset Information
    st.write("### Dataset Information")
    st.write(f"**Rows:** {df.shape[0]} | **Columns:** {df.shape[1]}")

    # Column Details
    st.write("### Column Details")
    col_info = pd.DataFrame({
        "Column Name": df.columns,
        "Data Type": df.dtypes.astype(str),
        "Missing Values": df.isna().sum().values
    })
    st.dataframe(col_info, height=300)

    # Summary Statistics
    st.write("### Summary Statistics")
    st.dataframe(df.describe(include='all').transpose().style.background_gradient(axis=0), height=400)

# Variable dictionary with collapsible descriptions for Mother and Father occupations
variable_dict = {
    "Mother's occupation": {
        "Role": "Feature",
        "Type": "Integer",
        "Demographic": "Occupation",
        "Description": """<details>
<summary>Show codes</summary>
0 - Student | 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers | 2 - Specialists in Intellectual and Scientific Activities | 3 - Intermediate Level Technicians and Professions | 4 - Administrative staff | 5 - Personal Services, Security and Safety Workers and Sellers | 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry | 7 - Skilled Workers in Industry, Construction and Craftsmen | 8 - Installation and Machine Operators and Assembly Workers | 9 - Unskilled Workers | 10 - Armed Forces Professions | 90 - Other Situation | 99 - (blank) | 122 - Health professionals | 123 - teachers | 125 - Specialists in ICT | 131 - Intermediate level science and engineering technicians | 132 - Technicians and professionals of intermediate level of health | 134 - Intermediate level technicians from legal, social, sports, cultural and similar services | 141 - Office workers, secretaries, data processing operators | 143 - Data, accounting, financial services and registry operators | 144 - Other administrative support staff | 151 - Personal service workers | 152 - sellers | 153 - Personal care workers | 171 - Skilled construction workers | 173 - Skilled workers in printing, jewelers, artisans | 175 - Workers in food processing, woodworking, clothing, etc. | 191 - Cleaning workers | 192 - Unskilled workers in agriculture, fisheries, forestry | 193 - Unskilled workers in extractive industry, construction, manufacturing, transport | 194 - Meal preparation assistants
</details>""",
        "Units": "",
        "Missing Values": "no"
    },
    "Father's occupation": {
        "Role": "Feature",
        "Type": "Integer",
        "Demographic": "Occupation",
        "Description": """<details>
<summary>Show codes</summary>
0 - Student | 1 - Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers | 2 - Specialists in Intellectual and Scientific Activities | 3 - Intermediate Level Technicians and Professions | 4 - Administrative staff | 5 - Personal Services, Security and Safety Workers and Sellers | 6 - Farmers and Skilled Workers in Agriculture, Fisheries and Forestry | 7 - Skilled Workers in Industry, Construction and Craftsmen | 8 - Installation and Machine Operators and Assembly Workers | 9 - Unskilled Workers | 10 - Armed Forces Professions | 90 - Other Situation | 99 - (blank) | 101 - Armed Forces Officers | 102 - Armed Forces Sergeants | 103 - Other Armed Forces personnel | 112 - Directors of administrative and commercial services | 114 - Hotel, catering, trade and other services directors | 121 - Specialists in physical sciences, mathematics, engineering | 122 - Health professionals | 123 - teachers | 124 - Specialists in finance, accounting, public and commercial relations | 131 - Intermediate level science and engineering technicians | 132 - Technicians and professionals of intermediate level of health | 134 - Intermediate level technicians from legal, social, sports, cultural and similar services | 135 - ICT technicians | 141 - Office workers, secretaries, data processing operators | 143 - Data, accounting, statistical, financial services, registry operators | 144 - Other administrative support staff | 151 - Personal service workers | 152 - sellers | 153 - Personal care workers | 154 - Protection and security services personnel | 161 - Market-oriented farmers and skilled agricultural and animal production workers | 163 - Farmers, livestock keepers, fishermen, hunters, subsistence | 171 - Skilled construction workers, except electricians | 172 - Skilled workers in metallurgy, metalworking | 174 - Skilled workers in electricity and electronics | 175 - Workers in food processing, woodworking, clothing, other industries | 181 - Fixed plant and machine operators | 182 - Assembly workers | 183 - Vehicle drivers and mobile equipment operators | 192 - Unskilled workers in agriculture, animal production, fisheries and forestry | 193 - Unskilled workers in extractive industry, construction, manufacturing, transport | 194 - Meal preparation assistants | 195 - Street vendors (except food)
</details>""",
        "Units": "",
        "Missing Values": "no"
    },
    "Admission grade": {"Role":"Feature","Type":"Continuous","Demographic":"","Description":"Admission grade (0-200)","Units":"","Missing Values":"no"},
    "Displaced": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"1 – yes, 0 – no","Units":"","Missing Values":"no"},
    "Educational special needs": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"1 – yes, 0 – no","Units":"","Missing Values":"no"},
    "Debtor": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"1 – yes, 0 – no","Units":"","Missing Values":"no"},
    "Tuition fees up to date": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"1 – yes, 0 – no","Units":"","Missing Values":"no"},
    "Gender": {"Role":"Feature","Type":"Integer","Demographic":"Gender","Description":"1 – male, 0 – female","Units":"","Missing Values":"no"},
    "Scholarship holder": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"1 – yes, 0 – no","Units":"","Missing Values":"no"},
    "Age at enrollment": {"Role":"Feature","Type":"Integer","Demographic":"Age","Description":"Age of student at enrollment","Units":"","Missing Values":"no"},
    "International": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"1 – yes, 0 – no","Units":"","Missing Values":"no"},
    "Curricular units 1st sem (credited)": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"Number of curricular units credited in 1st semester","Units":"","Missing Values":"no"},
    "Curricular units 1st sem (enrolled)": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"Number of curricular units enrolled in 1st semester","Units":"","Missing Values":"no"},
    "Curricular units 1st sem (evaluations)": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"Number of evaluations in 1st semester","Units":"","Missing Values":"no"},
    "Curricular units 1st sem (approved)": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"Number of units approved in 1st semester","Units":"","Missing Values":"no"},
    "Curricular units 1st sem (grade)": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"Average grade in 1st semester (0-20)","Units":"","Missing Values":"no"},
    "Curricular units 1st sem (without evaluations)": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"Units without evaluations in 1st semester","Units":"","Missing Values":"no"},
    "Curricular units 2nd sem (credited)": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"Number of curricular units credited in 2nd semester","Units":"","Missing Values":"no"},
    "Curricular units 2nd sem (enrolled)": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"Number of curricular units enrolled in 2nd semester","Units":"","Missing Values":"no"},
    "Curricular units 2nd sem (evaluations)": {"Role":"Feature","Type":"Integer","Demographic":"","Description":"Number of evaluations in 2nd semester","Units":"","Missing Values":"no"}
}

# Convert dictionary to DataFrame for tabular display
var_df = pd.DataFrame.from_dict(variable_dict, orient='index')
var_df.reset_index(inplace=True)
var_df.rename(columns={'index': 'Variable Name'}, inplace=True)

# Display variable description table at the end
st.write("### Variable Description")
st.write(var_df.to_html(escape=False), unsafe_allow_html=True)