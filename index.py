'''
streamlit多页面程序的入口文件
'''
import streamlit as st
st.title("AI大模型应用产品网")
col,col1 = st.columns(2)
#语言模型应用程序功能入口
with col:
    st.image("https://b0.bdstatic.com/7a8dd8cf0f8136450c63d02ed7b9db2d.jpg@h_1280",use_column_width=True)
    flag = st.button("608绘言",use_container_width=True)
    if flag:
        st.switch_page("pages/demo03.py")

with col1:
    st.image("https://wx1.sinaimg.cn/mw690/90440ed7ly1gw66ww1aj2s1j21kw1kwn9c.jpg",use_column_width=True)
    flag = st.button("608汇言",use_container_width=True)
    if flag:
        st.switch_page("pages/textToImage.py")


# c1, c2, c3, c4 ,c5= st.columns(5)
#
# with c1:
#     flag = st.button("基础版")
#     if flag:
#         st.switch_page("pages/demo.py")
#
# with c2:
#     flag1 = st.button("进阶版1")
#     if flag1:
#         st.switch_page("pages/demo01.py")
#
# with c3:
#     flag2 = st.button("进阶版2")
#     if flag2:
#         st.switch_page("pages/demo02.py")
#
# with c4:
#     flag3 = st.button("最终版")
#     if flag3:
#         st.switch_page("pages/demo03.py")
#
# with c5:
#     flag4 = st.button("文生图")
#     if flag4:
#         st.switch_page("pages/textToImage.py")