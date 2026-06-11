import streamlit as st
import plotly.express as px
import pandas as pd
import time

# 1. 페이지 기본 설정 및 스타일링
st.set_page_config(
    page_title="AromaCraft AI | AI 향수 조향 연구소",
    page_icon="🧪",
    layout="wide"
)

# 커스텀 CSS로 폰트 및 디자인 고급화
st.markdown("""
    <style>
    .main { background-color: #fcfbf9; }
    .stButton>button {
        background-color: #2C3E50; color: white;
        border-radius: 20px; padding: 10px 25px;
        font-weight: bold; border: none; transition: 0.3s;
    }
    .stButton>button:hover { background-color: #1A252F; transform: scale(1.05); }
    h1 { color: #2C3E50; font-family: 'Georgia', serif; }
    h3 { color: #34495E; }
    </style>
""", unsafe_allow_html=True)

# 2. 헤더 섹션
st.title("🧪 AromaCraft AI")
st.subheader("당신의 감정과 공간을 향기로 빚어내는 AI 가상 조향 연구소")
st.write("---")

# 3. 사이드바 - 사용자 입력 (무드 및 취향 설정)
st.sidebar.header("✨ 향기 프로파일링")

mood = st.sidebar.select_slider(
    "오늘 당신의 마음 상태는 어떤가요?",
    options=["차분하고 정적인", "포근하고 안락한", "생기 있고 활기찬", "몽환적이고 신비로운", "도시적이고 세련된"]
)

season = st.sidebar.selectbox("향수가 머무를 계절을 골라주세요.", ["봄 (Spring)", "여름 (Summer)", "가을 (Autumn)", "겨울 (Winter)"])
place = st.sidebar.text_input("이 향이 채워질 공간이나 상황은? (예: 비 오는 날의 서재, 해질녘 해변)", "새벽녘 침실")
intensity = st.sidebar.slider("향의 지속성 및 강도", 1, 5, 3)

submit_btn = st.sidebar.button("🔮 나만의 향수 조향하기")

# 4. 메인 화면 로직
if submit_btn:
    with st.spinner("🧙‍♂️ AI 조향사가 최적의 원료를 블렌딩하고 있습니다..."):
        # 실제 환경에서는 이곳에 OpenAI API나 LLM을 연동하여 프롬프트를 보냅니다.
        # 여기서는 퀄리티 높은 목업 데이터로 흐름을 구현했습니다.
        time.sleep(2.5) 
        
        # 가상의 AI 분석 결과 생성
        perfume_name = f"L'Équilibre de {place.split()[0]}" if place else "Aroma N°5"
        concept_desc = f"{mood} 감성과 {season}의 공기를 담아, '{place}'라는 공간에 완벽히 스며드는 커스텀 향수입니다."
        
        # 가상의 노트 데이터 (원래는 LLM이 JSON 형태로 반환하도록 설계)
        notes_data = {
            "노트 분류": ["Top Note", "Middle Note", "Base Note"],
            "주요 원료": ["시트러스 베르가못 & 네롤리", "프렌치 라벤더 & 다마스크 로즈", "샌달우드 & 화이트 머스크"],
            "배합 비율 (%)": [35, 40, 25]
        }
        df_notes = pd.DataFrame(notes_data)
        
        # 레이더 차트용 가상 성향 데이터
        radar_data = {
            "Characteristic": ["우디 (Woody)", "플로럴 (Floral)", "시트러스 (Citrus)", "스파이시 (Spicy)", "머스크 (Musky)", "그린 (Green)"],
            "Value": [6, 4, 8, 2, 7, 5] if "차분" in mood else [8, 2, 3, 5, 9, 4]
        }
        df_radar = pd.DataFrame(radar_data)

    # 결과 레이아웃 배치 (2단 컬럼)
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown(f"## 🏷️ {perfume_name}")
        st.markdown(f"*{concept_desc}*")
        st.write("---")
        
        st.markdown
