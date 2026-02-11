import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="PAPA_OS", page_icon="📟", layout="centered")

# Функция создания матрицы (защищенная)
def get_matrix_bg():
    cols = 40
    svg_txt = ""
    for i in range(cols):
        x = i * 25
        dur = random.uniform(2, 5)
        dly = random.uniform(0, 5)
        # Генерируем символы
        chars = "".join(random.choice(["0", "1"]) for _ in range(20))
        svg_txt += f'<text x="{x}" y="-10%" fill="%2300ff41" font-family="monospace" font-size="20" opacity="0.3">{chars}<animate attributeName="y" from="-10%" to="110%" dur="{dur}s" begin="-{dly}s" repeatCount="indefinite" /></text>'
    
    svg = f'<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">{svg_txt}</svg>'
    return svg.replace('"', "'")

# Интерфейс и стили
matrix_data = get_matrix_bg()

st.markdown(f"""
<style>
    .stApp {{
        background-color: #000000;
        background-image: url("data:image/svg+xml;utf8,{matrix_data}");
        background-size: cover;
    }}
    .wish-card {{
        position: relative;
        z-index: 99;
        border: 2px solid #00ff41;
        padding: 30px;
        border-radius: 15px;
        background-color: rgba(0, 0, 0, 0.9);
        box-shadow: 0 0 50px rgba(0, 255, 65, 0.4);
        margin-top: 50px;
        font-family: 'Courier New', monospace;
    }}
    .terminal-text {{
        color: #00ff41;
        text-shadow: 0 0 10px #00ff41;
    }}
    .stButton>button {{
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        background-color: transparent !important;
        box-shadow: 0 0 15px #00ff41;
        width: 100%;
        font-family: 'Courier New', monospace;
    }}
    .stButton>button:hover {{
        background-color: #00ff41 !important;
        color: black !important;
    }}
    header, footer {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

# Логика работы
if 'init' not in st.session_state:
    st.session_state.init = False

if not st.session_state.init:
    st.markdown("<h2 class='terminal-text' style='text-align:center;'>CONNECTING TO SYSTEM...</h2>", unsafe_allow_html=True)
    bar = st.progress(0)
    for p in range(101):
        time.sleep(0.01)
        bar.progress(p)
    st.session_state.init = True
    st.rerun()

# Основной экран
st.markdown("<h1 class='terminal-text' style='text-align:center;'>🔓 ACCESS GRANTED</h1>", unsafe_allow_html=True)

wishes = [
    "Папа, желаю тебе крепкого здоровья! Пусть твоя энергия никогда не иссякает, а каждый день в Кайраккуме приносит только радость. Ты лучший!",
    "Желаю огромного успеха в делах! Пусть любые преграды исчезают. Счастья, финансовой свободы и бодрости духа!",
    "С днем рождения! Желаю, чтобы в жизни всегда был 'зеленый свет' для всех твоих идей. Мы тебя любим!",
    "Пусть каждый год делает тебя только сильнее. Желаю радости, крепких нервов и исполнения заветных желаний!",
    "Дорогой папа, спасибо тебе за всё! Пусть дом всегда будет наполнен теплом и уютом. С праздником!"
]

if 'msg' not in st.session_state:
    st.session_state.msg = random.choice(wishes)

tz = datetime.timezone(datetime.timedelta(hours=5))
now = datetime.datetime.now(tz).strftime("%d.%m.%Y")

st.markdown(f"""
<div class="wish-card">
    <h2 style="color:#00ff41; text-align:center;">С ДНЕМ РОЖДЕНИЯ, ПАПА! 🎉</h2>
    <div class="terminal-text">
        <p><b>СТАТУС:</b> САМЫЙ ЛУЧШИЙ</p>
        <p><b>МЕСТО:</b> КАЙРАККУМ</p>
        <p><b>ДАТА:</b> {now}</p>
        <p>-------------------------------------------</p>
        <p><b>ПОСЛАНИЕ:</b></p>
        <p>{st.session_state.msg}</p>
        <p>-------------------------------------------</p>
        <p><b>АВТОР:</b> {NAME}</p>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")
if st.button("СГЕНЕРИРОВАТЬ НОВОЕ ПОЖЕЛАНИЕ"):
    st.session_state.msg = random.choice(wishes)
    st.rerun()
