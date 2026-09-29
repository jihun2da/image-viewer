import streamlit as st
import streamlit.components.v1 as components

# [핵심 추가 코드] 스트림릿의 기본 좁은 화면을 '전체 화면(wide)'으로 강제 확장합니다.
st.set_page_config(layout="wide")

# index.html 파일을 읽어와서 화면에 꽉 차게 띄워줍니다.
with open("index.html", "r", encoding="utf-8") as f:
    components.html(f.read(), height=1000, scrolling=True)
