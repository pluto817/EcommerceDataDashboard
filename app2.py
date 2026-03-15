import streamlit as st
import pandas as pd
import plotly.express as px

# 读取数据
df = pd.read_csv("ecommerce_sales_data.csv")
df = df.dropna()

st.title("电商销售数据大屏")

# 总览
st.subheader("销售总览")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("总订单数", len(df))
with col2:
    st.metric("总销售额", f"{df['Sales'].sum():.2f}")
with col3:
    st.metric("总利润", f"{df['Profit'].sum():.2f}")

# 地区分布
st.subheader("地区销售分布")
region_sales = df.groupby("Region")["Sales"].sum().reset_index()
fig1 = px.pie(region_sales, values="Sales", names="Region", title="各地区销售额")
st.plotly_chart(fig1)

# 类别排行
st.subheader("类别销售排行")
cate_sales = df.groupby("Category")["Sales"].sum().sort_values(ascending=False).reset_index()
fig2 = px.bar(cate_sales, x="Category", y="Sales", title="各类别销售额")
st.plotly_chart(fig2)