#%% 
import streamlit as st

st.title('데이터 시각화 3차 시험')
# %%
import streamlit as st


# st.set_page_config(
#     page_title="이건상의 Streamlit",
#     layout="wide",
#     initial_sidebar_state="expanded",
#     menu_items={
#         "Get Help": 'https://docs.streamlit.io',
#         "Report a bug": 'https://streamlit.io',
#         "About": None,
#     },
# )
# # %%
# # 사이드바 설정
# # st.sidebar.title('다양한 사이드바 위젯들')

# # st.sidebar.checkbox('외국인 포함')
# # st.sidebar.checkbox('고령인구 포함')
# # st.sidebar.divider()  # 👉 구분선
# # st.sidebar.radio('데이터 타입', ['전체', '남성', '여성'])
# # st.sidebar.slider('나이', 0, 100, (20, 50))
# # st.sidebar.selectbox('지역', ['서울', '경기', '인천', '대전', '대구', '부산', '광주'])

st.title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.markdown('## 마크다운 : st.markdown()')
st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')

st.write('# 마크다운 H1 : st.write()')
st.write('### 마크다운 H3 : st.write()')
st.write('')  # 빈 줄 추가

st.write(':red[빨간색 텍스트]')
st.write(':blue[파란색 텍스트]')

# Streamlit Magic
"# 마크다운 헤더"
"- 이건상"
"- 이건상 2"

"""
### 마크다운 헤더3
- 시각화
- 전처리
  - 123423521
"""

st.video('https://www.youtube.com/watch?v=-QWu77OP2gI&list=RD-QWu77OP2gI&start_radio=1')

### :orange[정보: st.info()]
st.info("This is a purely informational message", icon="ℹ️")

### :orange[경고: st.warning()]
st.warning("This is a warning message", icon="⚠️")

### :orange[에러: st.error()]
st.error("This is an error message", icon="⛔")

### :orange[성공: st.success()]
st.success("This is a success message", icon="✅")


#%% 2. Pandas 데이터프레임 출력
import pandas as pd

"### :orange[Pandas 데이터프레임]"

df = pd.DataFrame(
    {
        "id": [1, 2, 3],
        "name": ["Alice", "Bob", "Charlie"],
        "age": [24, 34, 45],
    }
)

df  # 👉 데이터프레임 출력 (Streamlit Magic)

#%% 1. 지표(Metric)
import streamlit as st

"### :orange[지표(Metric)]"

col1, col2, col3 = st.columns(3)  # 3개의 컬럼 생성

col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")


#%% 2. Streamlit 기본 그래프
import pandas as pd
import numpy as np

"## :blue[Streamlit 그래프]"

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

"### :orange[st.area_chart()]"
st.area_chart(chart_data)

"### :orange[st.line_chart()]"
st.line_chart(chart_data)

"### :orange[st.bar_chart()]"
st.bar_chart(chart_data)

"### :orange[st.scatter_chart()]"
st.scatter_chart(chart_data)


#%% 3. 지도 시각화 (st.map)
"### :orange[st.map()]"

df = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [37.55, 126.92],
    columns=["lat", "lon"]
)

st.map(df)
#%% 1. Matplotlib: st.pyplot()
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

"### :orange[Matplotlib: st.pyplot()]"

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

st.pyplot(fig)  # 👉 차트 출력

st.divider()  # 👉 구분선


#%% 2. Altair: st.altair_chart()
import altair as alt
import pandas as pd

"### :orange[Altair: st.altair_chart()]"

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

c = (
    alt.Chart(chart_data)
    .mark_circle()
    .encode(
        x="a",
        y="b",
        size="c",
        color="c",
        tooltip=["a", "b", "c"]
    )
)

st.altair_chart(c, use_container_width=True)


#%% 3. Plotly: st.plotly_chart()
import plotly.express as px

"### :orange[Plotly: st.plotly_chart()]"

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length")

st.plotly_chart(fig, key="iris", on_select="rerun")
#%% 페이지 레이아웃 - 컬럼
import streamlit as st

"### :orange[컬럼: st.columns()]"

col_1, col_2, col_3 = st.columns([1, 2, 1])  # 컬럼 인스턴스 생성: 1:2:1 비율로 컬럼을 나눔

with col_1:
    st.write("## 1번 컬럼")
    st.checkbox("이것은 1번 컬럼에 속한 체크박스 1")
    st.checkbox("이것은 1번 컬럼에 속한 체크박스 2")

with col_2:
    st.write("## 2번 컬럼")
    st.radio(
        "2번 컬럼의 라디오 버튼",
        ["radio 1", "radio 2", "radio 3"]
    )
    # 사이드바에 이미 라디오 버튼이 생성되어 있기 때문에,
    # 여기서는 라디오 버튼의 내용을 변경해야 오류가 발생하지 않음

col_3.write("## 3번 컬럼")
col_3.selectbox(
    "3번 컬럼의 셀렉트박스",
    ["select 1", "select 2", "select 3"]
)
# 사이드바에 이미 셀렉트박스가 생성되어 있기 때문에,
# 여기서는 셀렉트박스의 내용을 변경해야 오류가 발생하지 않음

# %%
#%% 페이지 레이아웃 - 탭(st.tabs)
import streamlit as st

"### :orange[탭: st.tabs()]"

# 탭 인스턴스 생성: 3개의 탭 생성
tab_1, tab_2, tab_3 = st.tabs(["Python", "R", "Julia"])


#%% 탭 1: Python
with tab_1:
    st.write(
        """
        ```python
        import pandas as pd

        df = pd.DataFrame(
            {'id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [24, 34, 45]
        }
    )
    ```
    """
    )
with tab_2:
    st.write(
        """
        ```r
        df = pd.DataFrame(
            {'id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [24, 34, 45]
        }
    )
    ```
    """
    )

with tab_3:
    st.write(
        """
        ```julia
        using DataFrames
        
        df = pd.DataFrame(
            {'id': [1, 2, 3],
            'name': ['Alice', 'Bob', 'Charlie'],
            'age': [24, 34, 45]
        }
    )
    ```
    """
    )
# %%
with st.expander('확장 레이아웃'):
    st.write('이곳은 확장 레이아웃입니다.')
    st.write('확장 레이아웃은 특정 컨텐츠를 숨기거나 보여줄 때 사용됩니다.')

#%% 사용자 입력
import streamlit as st

"## :blue[사용자 입력]"


#%% 텍스트 입력
"### :orange[텍스트 입력]"
text = st.text_input("여기에 텍스트를 입력하세요")
st.write(f"입력된 텍스트: {text}")


#%% 숫자 입력
"### :orange[숫자 입력]"
number = st.number_input("여기에 숫자를 입력하세요")
st.write(f"입력된 숫자: {number}")


#%% 날짜 입력
"### :orange[날짜 입력]"
date = st.date_input("날짜를 선택하세요")
st.write(f"선택된 날짜: {date}")


#%% 시간 입력
"### :orange[시간 입력]"
time = st.time_input("시간을 선택하세요")
st.write(f"선택된 시간: {time}")


#%% 파일 업로드
"### :orange[파일 업로드]"
file = st.file_uploader("파일을 업로드하세요")

# 파일을 임시적으로 사용하는 방법
if file:
    st.write(f"업로드된 파일: {file}")


#%% 파일 저장
import os

if file:
    # 파일을 저장할 경로 지정
    file_path = os.path.join("../data", file.name)

    # 파일 저장
    with open(file_path, "wb") as f:  # 'wb'는 바이너리 쓰기 모드
        f.write(file.getbuffer())

    st.success(f"파일이 저장되었습니다: {file_path}")
# %%
#%% 버튼
import streamlit as st

"## :blue[버튼]"


#%% 기본 버튼: st.button()
"### :orange[기본 버튼: st.button()]"

button = st.button("일반 버튼")
if button:
    st.write("버튼이 클릭되었습니다.")


primary_button = st.button("주요 버튼", type="primary")
if primary_button:
    st.write("주요 버튼이 클릭되었습니다.")


#%% 다운로드 버튼: st.download_button()
"### :orange[다운로드 버튼: st.download_button()]"

# with open("./data/python.png", "rb") as file:
#     st.download_button(
#         label="이미지 파일 다운로드",   # 버튼 라벨
#         data=file,                      # 다운로드할 파일
#         file_name="image.png",          # 다운로드 파일명
#         mime="image/png"                # 파일 형식
#     )


#%% 피드백 버튼: st.feedback()
"### :orange[피드백 버튼: st.feedback()]"

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"당신은 {sentiment_mapping[selected]} star(s)을 선택하였습니다.")


sentiment_mapping = [":material/thumb_down:", ":material/thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"당신은 {sentiment_mapping[selected]}을 선택하였습니다.")


#%% 링크 버튼: st.link_button()
"### :orange[링크 버튼: st.link_button()]"

# st.link_button("갤러리 링크", "https://streamlit.io/gallery")

#%% 선택 위젯
import streamlit as st

"## :blue[선택]"


#%% 체크박스: st.checkbox()
"### :orange[체크박스]"

check = st.checkbox("여기를 체크하세요")
if check:
    st.write("체크되었습니다.")


#%% 라디오 버튼: st.radio()
"### :orange[라디오 버튼]"

radio = st.radio("여기에서 선택하세요", ["선택 1", "선택 2", "선택 3"])
st.write(radio + "가 선택되었습니다.")


#%% 셀렉트 박스: st.selectbox()
"### :orange[셀렉트 박스]"

select = st.selectbox("여기에서 선택하세요", ["선택 1", "선택 2", "선택 3"])
st.write(select + "가 선택되었습니다.")


#%% 멀티 셀렉트 박스: st.multiselect()
"### :orange[멀티 셀렉트 박스]"

multi = st.multiselect("여기에서 여러 값을 선택하세요", ["선택 1", "선택 2", "선택 3"])
st.write(f"{type(multi)} = {multi}가 선택되었습니다.")


# %%
#%% 슬라이더, 선택 슬라이더, 컬러 피커
import streamlit as st

"## :orange[슬라이더]"

# 슬라이더는 선택된 값을 반환
slider = st.slider("여기에서 값을 선택하세요", 0, 100, 50)
st.write(f"현재의 값은 {slider} 입니다.")


#%% 선택 슬라이더
"## :orange[선택 슬라이더]"

range_slider = st.select_slider(
    "여기에서 값을 선택하세요",
    options=range(101),
    value=(25, 75)
)
st.write(f"현재의 값은 {range_slider} 입니다.")


#%% 컬러 피커
"## :orange[컬러 피커]"

color = st.color_picker("색을 선택하세요", "#00f900")
st.write(f"선택된 색은 {color} 입니다.")


#%% 프로그래스 바
import time

"## :orange[프로그래스 바]"

button1 = st.button("실시")  # 버튼은 클릭 여부를 반환
if button1:
    progress = st.progress(0)
    for i in range(101):
        progress.progress(i)
        if i % 20 == 0:
            st.write(f"진행 상태: {i}%")
        time.sleep(0.05)


#%% 스피너
"## :orange[스피너]"

button2 = st.button("로딩")  # 버튼은 클릭 여부를 반환
if button2:
    with st.spinner("로딩 중입니다..."):
        time.sleep(3)
        st.success("로딩 완료!")

#%% 애니메이션
import streamlit as st

"### :orange[풍선 애니메이션]"

button4 = st.button("풍선을 띄워보세요")  # 버튼은 클릭 여부를 반환
if button4:
    st.balloons()  # 풍선 애니메이션 출력

#%% 눈 애니메이션
"### :orange[눈 애니메이션]"

button5 = st.button("눈을 내려 보세요")  # 버튼은 클릭 여부를 반환
if button5:
    st.snow()  # 눈 애니메이션 출력

#%% 캐싱: st.cache_data
import streamlit as st
import time


@st.cache_data
def long_running_function(param1):
    time.sleep(5)
    return param1 * param1

#%% 캐싱 동작 확인
start = time.time()

# 숫자 입력은 입력된 값을 반환
num_1 = st.number_input("입력한 숫자의 제곱을 계산합니다.")

st.write(
    f"num_1의 제곱은 {long_running_function(num_1)} 입니다. "
    + f"계산시간은 {time.time() - start:.2f}초 소요"
)

st.write("📌 :green[캐싱이 적용되면 동일한 계산은 저장된 결과를 사용하여 빠르게 처리함]")
# %%
#%% 세션 상태(Session State)
import streamlit as st
import pandas as pd
import numpy as np


#%% Session_state를 사용하지 않은 경우
df = pd.DataFrame(np.random.randn(20, 2), columns=["x", "y"])

st.write("### :orange[Session_state를 사용하지 않은 경우]")
color1 = st.color_picker("Color1", "#FF0000")
st.divider()  # 구분선
st.scatter_chart(df, x="x", y="y", color=color1)


#%% Session_state를 사용한 경우
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(
        np.random.randn(20, 2), columns=["x", "y"]
    )

st.write("### :orange[Session_state를 사용한 경우]")
color2 = st.color_picker("Color2", "#FF0000")
st.divider()  # 구분선
st.scatter_chart(st.session_state.df, x="x", y="y", color=color2)

st.write("📌 :green[Session_state를 사용하면, 저장된 state를 사용하므로 값이 고정됨]")
# %%
