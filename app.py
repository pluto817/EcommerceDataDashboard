import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="监控平台", layout="wide")
st.title("📊 实时监控可视化平台")

data = pd.DataFrame({
    "时间": ["00:00", "04:00", "08:00", "12:00", "16:00", "20:00"],
    "数值": [120, 320, 550, 800, 620, 410]
})

st.dataframe(data)
fig = px.line(data, x="时间", y="数值", title="实时数据趋势")
st.plotly_chart(fig)