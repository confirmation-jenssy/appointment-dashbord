import streamlit as st
import pandas as pd

st.set_page_config(page_title="Appointment Command Center", layout="wide")

page = st.sidebar.radio("Navigation", ["Home", "Confirmation Reports"])

if page == "Home":
    st.title("📅 Appointment Command Center")
    st.subheader("Tomorrow")

    col1, col2, col3 = st.columns(3)
    col1.metric("CA", 43)
    col2.metric("OR", 12)
    col3.metric("WA", 4)

    st.metric("Total", 59)

elif page == "Confirmation Reports":
    st.title("📊 Confirmation Reports")

    daily_reports = {
        "6/12/2026": {
            "Total Leads": 39,
            "Confirmed": 20,
            "Conversion": "51.28%",
            "Tommy": 17,
            "Elite": 1,
            "Kousha": 2,
            "No Answer": 10,
            "Reschedule": 2,
            "Rejected": 10,
            "Cancelled": 7
        },
        "6/11/2026": {
            "Total Leads": 58,
            "Confirmed": 40,
            "Conversion": "68.96%",
            "Tommy": 36,
            "Elite": 3,
            "Kousha": 1,
            "No Answer": 6,
            "Reschedule": 2,
            "Rejected": 11,
            "Cancelled": 8
        }
    }

    selected_day = st.selectbox("Select Date", list(daily_reports.keys()))
    report = daily_reports[selected_day]

    st.header(f"Daily Report - {selected_day}")

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Leads", report["Total Leads"])
    c2.metric("Confirmed", report["Confirmed"])
    c3.metric("Conversion", report["Conversion"])

    st.progress(report["Confirmed"] / report["Total Leads"])

    st.subheader("Lead Breakdown")

    c1, c2, c3 = st.columns(3)
    c1.metric("Tommy", report["Tommy"])
    c2.metric("Elite", report["Elite"])
    c3.metric("Kousha", report["Kousha"])

    st.subheader("Unconfirmed Outcomes")

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("No Answer", report["No Answer"])
    c2.metric("Rejected", report["Rejected"])
    c3.metric("Cancelled", report["Cancelled"])
    c4.metric("Reschedule", report["Reschedule"])

    st.divider()

    st.header("Weekly Report")

    weekly = {"Leads": 272, "Confirmed": 159, "Conversion": "58.46%"}

    c1, c2, c3 = st.columns(3)
    c1.metric("Weekly Leads", weekly["Leads"])
    c2.metric("Weekly Confirmed", weekly["Confirmed"])
    c3.metric("Weekly Conversion", weekly["Conversion"])

    trend_df = pd.DataFrame({
        "Day": ["6/8", "6/9", "6/10", "6/11", "6/12"],
        "Confirmed": [37, 31, 31, 40, 20]
    })

    st.subheader("Weekly Breakdown")

st.dataframe(
    trend_df,
    use_container_width=True,
    hide_index=True
)

st.line_chart(trend_df.set_index("Day"))

st.divider()

st.header("Monthly Report")
st.info("Monthly reporting section coming next.")
