import streamlit as st
import streamlit.components.v1 as components

# index.html 파일을 읽어와서 스트림릿 화면에 꽉 차게 띄워주는 명령어입니다.
with open("index.html", "r", encoding="utf-8") as f:
    components.html(f.read(), height=1000, scrolling=True)