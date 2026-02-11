import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="PAPA_OS: Private Access", page_icon="📟", layout="centered")

# Функция создания матрицы
def get_matrix_bg():
    cols = 60
    svg_txt = ""
    for i in range(cols):
        x = i * (100 / cols)
        dur = random.uniform(2, 6)
        dly = random.uniform(0, 5)
        chars = "".join(random.choice(["0", "1"]) for _ in range(25))
        svg_txt += f'<text x="{x}%" y="-10%" fill="%2300ff41" font-family="monospace" font-size="22" opacity="0.25" style="writing-mode: tb; glyph-orientation-vertical: 0;">{chars}<animate attributeName="y" from="-50%" to="110%" dur="{dur}s" begin="-{dly}s" repeatCount="indefinite" /></text>'
    svg = f'<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">{svg_txt}</svg>'
    return svg.replace('"', "'").replace("\n", "")

matrix_data = get_matrix_bg()

# CSS Стили
st.markdown(f"""
<style>
    .stApp {{
        background-color: #000000;
        background-image: url("data:image/svg+xml;utf8,{matrix_data}");
        background-size: cover;
    }}
    .wish-card, .login-card {{
        position: relative;
        z-index: 100;
        border: 2px solid #00ff41;
        padding: 40px;
        border-radius: 15px;
        background-color: rgba(0, 0, 0, 0.95);
        box-shadow: 0 0 50px rgba(0, 255, 65, 0.4);
        margin-top: 100px;
        text-align: center;
    }}
    .terminal-text {{
        color: #00ff41;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 10px #00ff41;
    }}
    .stButton>button {{
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        background-color: transparent !important;
        box-shadow: 0 0 15px #00ff41;
        padding: 10px 30px !important;
        font-family: 'Courier New', monospace;
        font-size: 20px !important;
        font-weight: bold;
    }}
    .stButton>button:hover {{
        background-color: #00ff41 !important;
        color: black !important;
        box-shadow: 0 0 40px #00ff41;
    }}
    header, footer {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

# Управление этапами (session_state)
if 'step' not in st.session_state:
    st.session_state.step = 'start'

# --- ЭТАП 1: КНОПКА ВХОДА ---
if st.session_state.step == 'start':
    st.markdown("""
    <div class="login-card">
        <h1 class="terminal-text">СИСТЕМА ЗАБЛОКИРОВАНА</h1>
        <p class="terminal-text">Обнаружен секретный архив: <b>ДЕНЬ РОЖДЕНИЯ ПАПЫ</b></p>
        <p class="terminal-text">Требуется подтверждение личности...</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("ПОЛУЧИТЬ ДОСТУП"):
        st.session_state.step = 'loading'
        st.rerun()

# --- ЭТАП 2: ЗАГРУЗКА ---
elif st.session_state.step == 'loading':
    st.markdown("<div class='login-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='terminal-text'>ВЗЛОМ СИСТЕМЫ...</h2>", unsafe_allow_html=True)
    bar = st.progress(0)
    status = st.empty()
    logs = ["Подключение к серверу...", "Обход защиты...", "Загрузка поздравлений...", "Успешно!"]
    
    for i, log in enumerate(logs):
        status.markdown(f"<p class='terminal-text'>[LOG]: {log}</p>", unsafe_allow_html=True)
        bar.progress((i + 1) * 25)
        time.sleep(0.8)
    
    st.session_state.step = 'final'
    st.rerun()

# --- ЭТАП 3: ФИНАЛ ---
elif st.session_state.step == 'final':
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>🔓 ДОСТУП РАЗРЕШЕН</h1>", unsafe_allow_html=True)
    
    wishes = [
        "Дорогой папа, желаю тебе крепкого и несокрушимого здоровья! Ты — наша главная опора. Пусть твоя энергия никогда не иссякает!",
        "Желаю огромного успеха во всех делах! Пусть любые трудности отступают перед твоей мудростью. Счастья и только добрых новостей!",
        "С днем рождения! Желаю, чтобы в жизни всегда был 'зеленый свет' для твоих целей. Мы тебя очень любим и гордимся тобой!",
        "Пусть каждый новый год приносит новые силы и радость. Желаю душевного спокойствия, удачи и побольше времени на отдых!",
        "Самый лучший отец, с праздником! Пусть наш дом всегда будет для тебя местом силы и уюта. Здоровья тебе на долгие годы!"
    ]

    if 'msg' not in st.session_state:
        st.session_state.msg = random.choice(wishes)

    tz = datetime.timezone(datetime.timedelta(hours=5))
    now = datetime.datetime.now(tz).strftime("%d.%m.%Y")

    st.markdown(f"""
    <div class="wish-card">
        <h2 style="color:#00ff41; text-align:center;">С ДНЕМ РОЖДЕНИЯ! 🎉</h2>
        <div class="terminal-text" style="text-align: left;">
            <p><b>СТАТУС:</b> САМЫЙ ЛУЧШИЙ ПАПА</p>
            <p><b>ЛОКАЦИЯ:</b> КАЙРАККУМ</p>
            <p><b>ДАТА:</b> {now}</p>
            <p>-------------------------------------------</p>
            <p style="font-size: 1.1em; line-height: 1.5;">{st.session_state.msg}</p>
            <p>-------------------------------------------</p>
            <p><b>АВТОР:</b> {NAME}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ЕЩЕ ОДНО ПОЖЕЛАНИЕ"):
        st.session_state.msg = random.choice(wishes)
        st.rerun()
