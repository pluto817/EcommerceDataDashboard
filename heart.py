import streamlit as st
import plotly.express as px
import numpy as np
import pandas as pd
import time
# 页面基础设置（粉色系超甜）
st.set_page_config(
    page_title="给XX的专属爱心 💘",  # 把XX改成朋友名字
    page_icon="❤️",
    layout="centered"
)

# 自定义粉色系样式
st.markdown("""
<style>
    .stApp {background-color: #fff5f7;}
    .heart-title {color: #e63946; font-size: 36px; text-align: center;}
    .msg-box {background-color: #ffe5ec; padding: 20px; border-radius: 10px;}
    .stButton>button {background-color: #ff6b6b; color: white; border-radius: 5px;}
</style>
""", unsafe_allow_html=True)

# 1. 动态爱心（核心视觉）
st.markdown('<div class="heart-title">💘 专属爱心，请查收 💘</div>', unsafe_allow_html=True)

def generate_heart():
    """用数学公式生成爱心坐标"""
    t = np.linspace(0, 2*np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t)
    return pd.DataFrame({'x': x, 'y': y})

# 动态渐变爱心
df_heart = generate_heart()
fig = px.line(
    df_heart, x='x', y='y',
    template="plotly_white",
    title="❤️ 友谊天长地久 ❤️"
)
fig.update_traces(
    line_color='#ff4d6d',
    line_width=6,
    hoverinfo='none'
)
fig.update_layout(
    width=500,
    height=400,
    showlegend=False,
    plot_bgcolor='rgba(0,0,0,0)'
)
st.plotly_chart(fig, use_container_width=True)

# 2. 互动祝福模块
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="msg-box">', unsafe_allow_html=True)

# 输入专属祝福
friend_name = st.text_input("朋友的名字", value="宝子")
custom_msg = st.text_area(
    f"想对{friend_name}说的话",
    value=f"{friend_name}～谢谢你出现在我的生活里，愿我们的友谊像这个爱心一样，永远完整 💖"
)

# 点击触发特效
if st.button(f"点击送给{friend_name} 🎁"):
    with st.spinner("正在打包爱心..."):
        time.sleep(1)
    st.success(f"❤️ 爱心已成功送给{friend_name}！")
    st.balloons()  # 气球特效
    st.snow()      # 雪花/爱心特效（看版本）
    st.toast(f"{friend_name}收到你的心意啦～", icon="❤️")

st.markdown('</div>', unsafe_allow_html=True)

# 3. 小彩蛋：隐藏的互动
with st.expander("🔍 点击解锁小彩蛋"):
    st.write("偷偷告诉你：双击爱心可以变色哦～")
    color = st.color_picker("选一个你喜欢的爱心颜色", "#ff4d6d")
    if st.button("预览颜色"):
        fig.update_traces(line_color=color)
        st.plotly_chart(fig, use_container_width=True)