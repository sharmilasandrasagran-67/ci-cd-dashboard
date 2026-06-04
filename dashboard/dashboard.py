import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Stakeholder Dashboard")

st.write(
    "This dashboard displays the processed dataset and allows stakeholders "
    "to search and filter records interactively."
)

BASE_DIR = Path(__file__).resolve().parent.parent
data_path = BASE_DIR / "data" / "processed_dataset.csv"

@st.cache_data
def load_data():
    return pd.read_csv(data_path)

data = load_data()

if data.empty:
    st.warning("No data to display.")
    st.stop()

st.subheader("Full Dataset")
st.dataframe(data)

st.sidebar.header("Search and Filter Options")

search_term = st.sidebar.text_input("Search by any field")

filtered_data = data.copy()

if search_term:
    filtered_data = filtered_data[
        filtered_data.apply(
            lambda row: row.astype(str)
            .str.contains(search_term, case=False, na=False)
            .any(),
            axis=1
        )
    ]

if "age" in filtered_data.columns and not filtered_data.empty:
    min_age = int(filtered_data["age"].min())
    max_age = int(filtered_data["age"].max())

    if min_age == max_age:
        st.sidebar.info(f"Only one age value available: {min_age}")
        age_range = (min_age, max_age)
    else:
        age_range = st.sidebar.slider(
            "Select Age Range",
            min_age,
            max_age,
            value=(min_age, max_age)
        )

    filtered_data = filtered_data[
        (filtered_data["age"] >= age_range[0]) &
        (filtered_data["age"] <= age_range[1])
    ]

st.subheader("Filtered Results")

if filtered_data.empty:
    st.warning("No records match the selected search or filter.")
else:
    st.dataframe(filtered_data)
