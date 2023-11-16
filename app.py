import streamlit as st

st.title("Streamlit勉強中") # タイトル
st.header("見出し") # ヘッダー
st.subheader('小見出し')
st.write("hogehoge") # 表示

st.markdown("# マークダウンでもかけるよ！（h1）") # マークダウンで表示
st.markdown("## 正直MDが便利すぎるんじゃないか？（h1）")
st.text("text") # テキスト表示