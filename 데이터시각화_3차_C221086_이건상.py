import streamlit as st

st.title('데이터 시각화 3차 시험')
st.header('주제 : 케데헌에 대한 기사 수집 후 관련 단어로 텍스트 시각화')


"""
### `초간단 사용 방법`
- 왼쪽에 사이드바를 통해 각 그래프에 해당되는 요소들을 조절 가능함
"""


"""
### 케데헌 주제곡 : Gloden
"""
st.video('https://www.youtube.com/watch?v=UkFLk0-xf58&list=RDUkFLk0-xf58&start_radio=1')


import pandas as pd 
df = pd.read_csv('KDH.csv' , encoding = 'utf-8')
filtered_edges =pd.read_csv('filtered_edges.csv')

import networkx as nx
from wordcloud import WordCloud
from collections import Counter
import os
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


"""
## 키워드 네트워크 시각화 1
- 사용 위젯
    - 노드 크기 변경
    - 엣지 크기 
"""

FONT_PATH = "Apple 산돌고딕 Neo/AppleSDGothicNeoB.ttf"
assert os.path.exists(FONT_PATH), f"폰트 파일 없음: {FONT_PATH}"

font_name = fm.FontProperties(fname=FONT_PATH).get_name()
plt.rcParams["font.family"] = font_name
plt.rcParams["axes.unicode_minus"] = False



node_scale = st.sidebar.slider("1번째 네트워크 시각화 노드 크기 배수", 10, 500, 100, step=10)
edge_scale = st.sidebar.slider("1번째 네트워크 시각화 엣지 두께 배수", 1, 50, 5)

G = nx.Graph()


# weighted_edges = [(n1, n2, w) for (n1, n2), w in filtered_edges.items()]
weighted_edges = list(filtered_edges[["source", "target", "weight"]].itertuples(index=False, name=None))

G.add_weighted_edges_from(weighted_edges)

pos = nx.spring_layout(G, k=0.3, iterations=50, seed=42)

deg = dict(G.degree())
node_sizes = [max(50, deg[n] * node_scale) for n in G.nodes()]
node_colors = ["red" if deg[n] >= 10 else "yellow" for n in G.nodes()]
edge_widths = [max(0.5, G[u][v]["weight"] * edge_scale * 0.05) for u, v in G.edges()]

fig, ax = plt.subplots(figsize=(15, 15))
# nx.draw_networkx(G, pos, ax=ax, with_labels=True,
#                  node_size=node_sizes, node_color=node_colors,
#                  width=edge_widths, edge_color="green",
#                  font_size=12, alpha=0.8)
# ax.set_title("케데헌 키워드")
# ax.axis("off")

font_prop = fm.FontProperties(fname=FONT_PATH)

# 노드/엣지는 NetworkX로 그리고
nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes, node_color=node_colors, alpha=0.8)
nx.draw_networkx_edges(G, pos, ax=ax, width=edge_widths, edge_color="green", alpha=0.6)

# 라벨은 직접 그리기(여기서 폰트 강제)
for n, (x, y) in pos.items():
    ax.text(x, y, str(n), fontproperties=font_prop, fontsize=12,
            ha="center", va="center")
ax.text(
    0.5, 1.02, "케데헌 키워드 네트워크",
    transform=ax.transAxes,   # 축 기준 좌표
    ha="center", va="bottom",
    fontsize=18,
    fontproperties=font_prop
)
st.pyplot(fig)
plt.close(fig)



"""
## 워드클라우드(기본) 1
"""

# from wordcloud import WordCloud
# from collections import Counter
# with open('all_processed_nouns.txt', 'r', encoding='utf-8') as f:
#     all_nouns =  f.read().splitlines()

# flat = [w for doc in all_nouns for w in doc]
# freq = Counter(flat)

# wc = WordCloud(font_path='Apple 산돌고딕 Neo/AppleSDGothicNeoB.ttf').generate_from_frequencies(freq)
import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from collections import Counter

with open('all_processed_nouns.txt', 'r', encoding='utf-8') as f:
    all_nouns = f.read().splitlines()

# (중요) 지금 코드는 한 글자씩 쪼갭니다. 단어면 split() 쓰세요.
flat = []
for line in all_nouns:
    flat.extend(line.split())

freq = Counter(flat)

topN = 150
freq_top = dict(freq.most_common(topN))

wc = WordCloud(
    font_path='Apple 산돌고딕 Neo/AppleSDGothicNeoB.ttf',
    width=900, height=500,
    background_color="white",
    max_words=topN,
    relative_scaling=0.5
).generate_from_frequencies(freq_top)

# wc = WordCloud(
#     font_path='Apple 산돌고딕 Neo/AppleSDGothicNeoB.ttf',
#     width=900, height=500,
#     background_color="white",
#     prefer_horizontal=0.7
# ).generate_from_frequencies(freq)

fig, ax = plt.subplots(figsize=(12, 6))
ax.imshow(wc, interpolation="bilinear")
ax.axis("off")
st.pyplot(fig)




"""
## 키워드 네트워크 시각화 2
- 사용 위젯
    - 노드 색상 변경
    - 엣지 색상 변경  
"""

import streamlit as st
import networkx as nx
import plotly.graph_objects as go


# 색 선택
node_color = st.color_picker("노드 색을 선택하세요", "#00f900")
edge_color = st.color_picker("엣지 색을 선택하세요", "#808080")

# 스케일
node_scale = st.sidebar.slider("2번째 네트워크 시각화 노드 크기 배수", 10, 40, 20, step=1)
edge_scale = st.sidebar.slider("2번째 네트워크 시각화 엣지 두께 배수", 1, 30, 10, step=1)

# 레이아웃(원형)
pos = nx.circular_layout(G)

# 노드 좌표/크기
nodes = list(G.nodes())
x_nodes = [pos[n][0] for n in nodes]
y_nodes = [pos[n][1] for n in nodes]
deg = dict(G.degree())

# Plotly marker size는 px라서 너무 커지기 쉬움: sqrt로 완화 권장
node_sizes = [max(6, (deg[n] ** 0.5) * node_scale) for n in nodes]

# -------------------------
# 엣지 트레이스: "엣지별 두께" 반영하려면 엣지마다 trace가 필요합니다.
# 엣지가 너무 많으면 느려집니다. (그래프를 수천 개씩 그리는 건 인간 욕심입니다.)
# -------------------------
edge_traces = []
for u, v, data in G.edges(data=True):
    w = data.get("weight", 1.0)
    width = max(0.5, w * edge_scale * 0.05)

    edge_traces.append(
        go.Scatter(
            x=[pos[u][0], pos[v][0]],
            y=[pos[u][1], pos[v][1]],
            mode="lines",
            line=dict(color=edge_color, width=width),
            hoverinfo="skip",
            showlegend=False,
        )
    )

# 노드 트레이스
node_trace = go.Scatter(
    x=x_nodes,
    y=y_nodes,
    mode="markers+text",
    text=[str(n) for n in nodes],
    textposition="middle center",
    hovertext=[f"{n}<br>degree={deg[n]}" for n in nodes],
    hoverinfo="text",
    marker=dict(
        size=node_sizes,
        color=node_color,
        line=dict(width=1, color="#333333"),
        opacity=0.8
    ),
    textfont=dict(color="black"),
    showlegend=False,
)

fig = go.Figure(data=edge_traces + [node_trace])

fig.update_layout(
    title="케데헌키워드",
    title_x=0.5,
    paper_bgcolor="white",
    plot_bgcolor="white",
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    margin=dict(l=10, r=10, t=60, b=10),
    height = 800
)

# 원형이 찌그러지지 않게 비율 고정
fig.update_yaxes(scaleanchor="x", scaleratio=1)

st.plotly_chart(fig, use_container_width=True)

"""
## 워드클라우드 2 
#### plotly 사용 
"""
import streamlit as st
import plotly.graph_objects as go
from wordcloud import WordCloud
from collections import Counter

FONT_PATH = 'Apple 산돌고딕 Neo/AppleSDGothicNeoB.ttf'

with open('all_processed_nouns.txt', 'r', encoding='utf-8') as f:
    all_nouns = f.read().splitlines()

flat = []
for line in all_nouns:
    flat.extend(line.split())

flat = [w for w in flat if len(w) >= 2]
freq = Counter(flat)

bg_color = st.color_picker("배경색", "#ffffff")
topN = st.sidebar.slider("표시 단어 수 (Top N)", 30, 200, 80, step=10)
min_font = st.sidebar.slider("최소 글자 크기", 4, 50, 10, step=1)
max_font = st.sidebar.slider("최대 글자 크기", 20, 300, 120, step=5)
rel_scale = st.sidebar.slider("빈도 반영 강도", 0.0, 1.0, 0.9, step=0.1)

if min_font >= max_font:
    st.error("최소 글자 크기는 최대 글자 크기보다 작아야 합니다.")
    st.stop()

freq_top = dict(freq.most_common(topN))

wc = WordCloud(
    font_path=FONT_PATH,
    background_color=bg_color,
    width=1500, height=1500,
    max_words=topN,
    min_font_size=min_font,
    max_font_size=max_font,
    relative_scaling=rel_scale,
    prefer_horizontal=0.5,
    collocations=False
).generate_from_frequencies(freq_top)

# PIL 이미지로 받기
img = wc.to_image()

# Plotly에 이미지로 삽입
fig = go.Figure()
fig.add_layout_image(
    dict(
        source=img,
        xref="x", yref="y",
        x=0, y=1,
        sizex=1, sizey=1,
        sizing="contain",
        layer="below",
    )
)

fig.update_xaxes(visible=False, range=[0, 1])
fig.update_yaxes(visible=False, range=[0, 1], scaleanchor="x")
fig.update_layout(margin=dict(l=0, r=0, t=20, b=0), height=520)

st.plotly_chart(fig, use_container_width=True)


"""
### `결과 : 케이팝, 데몬, 애니메이션이라는 단어의 비중이 가장 컸다`

- 음악과 연관되는 단어들 테일러, 트와이스, 스위프트, 골든 등 데몬헌터스의 주제가인 골든이 얼마나 영향력이 있었고 
- 케데헌의 ost가 얼마나 유행했는지 알 수 있었다. 
- 해당 애니메이션이 넷플릭스에서 방영되어 넷플릭스의 비중도 높은 것을 확인 할 수 있었다. 
- 케데헌은 이름에서부터 언급되었듯 케이팝 데몬 헌터스라는 제목을 가지고 있다. 
- 이를 통해 케이팝이 얼마나 많은 영향력이 있는지 알 수 있고, 케이팝이 전 세계 시장에서 얼마나 대중적인지 대략적으로 알 수 있는 지표가 될 수도 있다고 생각하다. 
- 그 외에 애니메이션과 관련된 단어들이 다수 등장하는 것을 볼 수 있었다. 
"""


"""
## 간단한 설문 조사 및 평가
"""

"### :red[피드백 버튼: st.feedback()]"

sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.feedback("stars")
if selected is not None:
    st.markdown(f"당신은 {sentiment_mapping[selected]} star(s)을 선택하였습니다.")


sentiment_mapping = [":thumb_down:", ":thumb_up:"]
selected = st.feedback("thumbs")
if selected is not None:
    st.markdown(f"당신은 {sentiment_mapping[selected]}을 선택하였습니다.")

"### :blue[텍스트 입력]"
text = st.text_input("피드백을 남겨주세요😃!")
st.write(f"입력된 텍스트: {text}")


## gpt 링크 : https://chatgpt.com/share/693fab53-1d90-800e-9ce8-a7648e4b258b
## 스트림릿 링크 : https://github.com/qwergs/streamlit