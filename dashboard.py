import streamlit as st

from monday_api import get_monday_items
from reporting import build_report

st.set_page_config(
    page_title="Appointment Dashboard",
    layout="wide"
)

items = get_monday_items()

st.write("Items Returned:", len(items))

for item in items[:10]:
    st.write(item["name"])

st.write(items[0])

report = build_report(items)

report = build_report(items)

st.title("Appointment Dashboard")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Confirmed", report["confirmed"])
c2.metric("Same Day", report["same_day"])
c3.metric("Same Day %", f'{report["same_day_percent"]}%')
c4.metric("Conversion %", f'{report["conversion"]}%')

st.divider()

c1, c2, c3 = st.columns(3)

c1.metric("Tommy", report["tommy"])
c2.metric("Elite", report["elite"])
c3.metric("Universal", report["universal"])

st.divider()

c1, c2, c3, c4 = st.columns(4)

c1.metric("No Answer", report["no_answer"])
c2.metric("Cancelled", report["cancelled"])
c3.metric("Reschedule", report["reschedule"])
c4.metric("Rejected", report["rejected"])

st.divider()

c1, c2, c3 = st.columns(3)

c1.metric("McCormick", report["mccormick"])
c2.metric("Nova", report["nova"])
c3.metric("Safe & Green", report["safegreen"])
