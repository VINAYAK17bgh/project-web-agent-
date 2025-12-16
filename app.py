import streamlit as st
import pandas as pd
from scoring import calculate_score

st.set_page_config(page_title="AI Lead Qualification Demo", layout="wide")

st.title("AI Web Agent – Lead Qualification for 3D In-Vitro Models")

st.markdown("""
This demo shows how an AI-powered business development agent
identifies, enriches, and ranks biotech leads using scientific and business signals.
""")

df = pd.read_csv("leads.csv")
df["Propensity_Score"] = df.apply(calculate_score, axis=1)
df = df.sort_values("Propensity_Score", ascending=False)

search = st.text_input("Search by name, title, company, or location")

if search:
    df = df[df.apply(lambda row: search.lower() in row.to_string().lower(), axis=1)]

st.dataframe(df, use_container_width=True)

st.download_button(
    "Download Ranked Leads",
    df.to_csv(index=False),
    "ranked_leads.csv"
)

