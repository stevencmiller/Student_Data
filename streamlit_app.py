import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="AI Student Dashboard", layout="wide")

st.title("🎓 AI-Powered Student Success Dashboard")

# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio("Go to", ["📊 Dashboard", "🧠 AI Insights", "📁 Upload Data"])

# Load CSV
@st.cache_data
def load_data():
    try:
        return pd.read_csv("data/student_data.csv")
    except:
        return pd.DataFrame()

df = load_data()

# Dashboard View
if page == "📊 Dashboard":
    st.subheader("Key Metrics")

    if df.empty:
        st.warning("No data found. Please upload a student CSV file.")
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Students", len(df))
        col2.metric("Avg GPA", round(df["GPA"].mean(), 2))
        col3.metric("At Risk", df[df["RiskLevel"] == "High"].shape[0])

        st.subheader("GPA Distribution")
        chart = alt.Chart(df).mark_bar().encode(
            x=alt.X("GPA", bin=True),
            y='count()',
            tooltip=['GPA']
        ).properties(width=600)
        st.altair_chart(chart)

# AI Insights View
elif page == "🧠 AI Insights":
    st.subheader("AI Recommendations (Coming Soon)")
    st.info("This section will provide student-specific insights and early warning flags.")

# Upload View
elif page == "📁 Upload Data":
    st.subheader("Upload Student CSV")
    uploaded = st.file_uploader("Choose CSV", type="csv")
    if uploaded:
        df = pd.read_csv(uploaded)
        df.to_csv("data/student_data.csv", index=False)
        st.success("File uploaded! Switch to Dashboard tab to view.")
