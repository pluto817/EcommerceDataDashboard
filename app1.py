# 导入 Streamlit 库，约定俗成简写成 st
import streamlit as st

# 1. 加标题（网页最显眼的文字）
st.title("我的第一个 Streamlit 应用 🎈")

# 2. 加普通文本
st.write("这是用 Streamlit 写的第一个网页，不用懂任何前端！")

# 3. 加一个交互式滑块
age = st.slider("请选择你的年龄",  # 滑块提示文字
                min_value=0,      # 最小值
                max_value=100,    # 最大值
                value=25)         # 默认值

# 4. 显示滑块选择的结果
st.write(f"你选择的年龄是：{age} 岁")