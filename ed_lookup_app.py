import pandas as pd
import streamlit as st

st.title("Kings County AD/ED Committee Count Lookup")
st.caption("2024 Kings County Democratic Party Call — Democratic enrollment & County Committee seats by AD/ED")

@st.cache_data
def load_data():
    return pd.read_csv("KingsCounty_ED_Master.csv", dtype={"VoteTally": "Int64"})

df = load_data()

ad = st.selectbox("Assembly District (AD)", sorted(df["AD"].unique()))
eds = sorted(df.loc[df["AD"] == ad, "ED"])
ed = st.selectbox("Election District (ED)", eds)

row = df[(df["AD"] == ad) & (df["ED"] == ed)].iloc[0]

col1, col2, col3 = st.columns(3)
col1.metric("Democratic", int(row["Democratic"]))
col2.metric("County Committee Count", int(row["CountyCommitteeCount"]))
tally = row["VoteTally"]
col3.metric("Vote Tally", int(tally) if pd.notna(tally) else "N/A")