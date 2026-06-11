import streamlit as st
import time
import pandas as pd
import datetime

# 1. 페이지 설정 및 다크모드 지향 테마 감성
st.set_page_config(
    page_title="MindFlow - 나만의 멘탈 케어 공간",
    page_icon="🧠",
    layout="centered"
)

# 세션 상태(Session State) 초기화 - 새로고침해도 데이터가 유지되도록 함
if "mood_history" not in st.session_state:
    st.session_state.mood_history = []

# --- 헤더 섹션 ---
st.title("🧠 MindFlow : 실시간 번아웃 방지 센터")
st.write("오늘 하루, 당신의 마음 상태는 어떤가요? 감정을 기록하고 즉각적인 리프레시 가이드를 받아보세요.")
st.divider()

# --- STEP 1: 현재 상태 진단 ---
st.subheader("1. 현재 나의 상태는?")

col1, col2 = st.columns(2)

with col1:
    energy_level = st.slider("⚡ 에너지 충전도 (0% = 방전, 100% = 열정 가득)", 0, 100, 50)
    stress_level = st.slider("🔥 스트레스 지수 (0% = 평온, 100% = 폭발 직전)", 0, 100, 30)

with col2:
    current_mood = st.selectbox(
        "🎭 현재 지배적인 감정은?",
        ["평온함 😊", "집중/몰입 🎯", "불안/초조 😰", "지침/무기력 😴", "짜증/화남 😡"]
    )
    focus_time = st.number_input("⏳ 오늘 연속으로 업무(공부)한 시간 (시간 단위)", min_value=0.0, max_value=16.0, value=2.0, step=0.5)

# 상태 저장 버튼
if st.button("📊 현재 상태 기록하기", use_container_width=True):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    st.session_state.mood_history.append({
        "시간": now,
        "에너지": energy_level,
        "스트레스": stress_level,
        "감정": current_mood
    })
    st.toast("오늘의 마음 한 조각이 기록되었습니다! ✨")

st.divider()

# --- STEP 2: 실시간 맞춤형 처방 (인터랙션의 핵심) ---
st.subheader("2. 당신을 위한 실시간 멘탈 처방전 💊")

# 번아웃 위험도 계산 알고리즘 (간단한 규칙 기반)
burnout_score = (stress_level * 0.6) + ((100 - energy_level) * 0.4) + (focus_time * 5)

if burnout_score >= 70:
    st.error(f"🚨 **위험: 번아웃 경보! (지수: {burnout_score:.1f})** 현재 심각한 과부하 상태일 수 있습니다. 당장 화면을 끄고 쉬세요!")
    
    # 애니메이션 효과를 활용한 호흡 가이드 컴포넌트
    st.info("🧘‍♂️ **[🚨 긴급 처방] 4-7-8 호흡법을 시작합니다.** 아래 타이머에 맞춰 숨을 고르세요.")
    if st.button("🫁 1분 호흡 타이머 시작"):
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # 4초 흡입 - 7초 유지 - 8초 배
