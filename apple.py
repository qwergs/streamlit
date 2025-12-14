#%% 
import streamlit as st

st.title('1번 스트림릿')
# %%
import streamlit as st


st.set_page_config(
    page_title="하교수의 Streamlit",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": None,
        "About": None,
    },
)
# %%
# 사이드바 설정
st.sidebar.title('다양한 사이드바 위젯들')

st.sidebar.checkbox('외국인 포함')
st.sidebar.checkbox('고령인구 포함')
st.sidebar.divider()  # 👉 구분선
st.sidebar.radio('데이터 타입', ['전체', '남성', '여성'])
st.sidebar.slider('나이', 0, 100, (20, 50))
st.sidebar.selectbox('지역', ['서울', '경기', '인천', '대전', '대구', '부산', '광주'])
# %%
