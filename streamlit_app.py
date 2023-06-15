import streamlit as st

# 应用的标题文字
st.header('st.button')

# 我们会使用条件分支语句 if 和 else 来显示不同的消息
if st.button('Say hello'):
    st.write('Why hello there')
else:
    st.write('Goodbye')
