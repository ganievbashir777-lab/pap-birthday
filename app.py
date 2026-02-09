import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="PAPA_OS: Real Matrix", page_icon="📟", layout="centered")

# Функция для генерации "Матричного дождя" через SVG
def get_matrix_svg():
    cols = 50  # Количество колонок
    svg_elements = ""
    for i in range(cols):
        x_pos = i * 20
        duration = random.uniform(3, 8)  # Скорость падения
        delay = random.uniform(0, 5)     # Задержка старта
        # Сами цифры
        binary_str = "".join(random.choice(["0", "1", " "]) for _ in range(25))
        svg_elements += f"""
        <text x="{x_pos}" y="-100" fill="#00ff41" font-family="monospace" font-size="18" opacity="0.4">
            {binary_str}
            <animate attributeName="y" from="-500" to="1000" dur="{duration}s" begin="-{delay}s" repeatCount="indefinite" />
        </text>
        """
    
    return f"""<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg"><style>text {{ writing-mode: tb; glyph-orientation-vertical: 0; }}</style>{svg_elements}</svg>"""

# Очистка SVG для вставки в CSS
matrix_bg = get_matrix_svg().replace("\n", "").replace("#", "%23")

# Применяем стили
st.markdown(f"""
<style>
    .stApp {{
        background-color: #000000;
        background-image: url('data:image/svg+xml;utf8,{matrix_bg}');
        background-size: cover;
    }}

    .wish-card {{
        position: relative;
        z-index: 10;
        border: 2px solid #00ff41;
        padding: 30px;
        border-radius: 10px;
        background-color: rgba(5, 5, 5, 0.95);
        box-shadow: 0 0 40px rgba(0, 255, 65, 0.5);
        margin-top: 50px;
    }}

    .terminal-text {{
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 10px #00ff41;
    }}

    .stButton>button {{
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        background-color: black !important;
        box-shadow: 0 0 15px #00ff41;
        width: 100%;
        font-weight: bold;
        transition: 0.3s;
    }}
    
    .stButton>button:hover {{
        background-color: #00ff41 !important;
        color: black !important;
        box-shadow: 0 0 50px #00ff41;
    }}

    header, footer {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

random_wishes = [
    "Папа, желаю тебе стального здоровья! Пусть твоя энергия никогда не иссякает, а каждый день в нашем Кайраккуме приносит только добрые новости. Ты — лучший!",
    "Желаю огромного успеха в делах! Пусть любые преграды исчезают, как ошибки в коде. Счастья, финансовой свободы и бодрости духа тебе каждый день!",
    "С днем рождения! Желаю, чтобы в жизни всегда был 'зеленый свет' для всех твоих идей. Мы тебя очень любим и всегда будем рядом. Ты — наша гордость!",
    "Пусть каждый год жизни делает тебя только сильнее и мудрее. Желаю радости, крепких нервов и исполнения самых заветных желаний. Оставайся всегда таким же крутым!",
    "Дорогой папа, спасибо тебе за всё! Желаю, чтобы твоё сердце всегда было наполнено радостью, а дом — теплом. Здоровья тебе на долгие-долгие годы!"
]

if 'stage' not in st.session_state:
    st.session_state.stage = 'loading'

# 1. Этап загрузки
if st.session_state.stage == 'loading':
    st.markdown("<h2 class='terminal-text' style='text-align:center;'>INITIALIZING MATRIX STREAM...</h2>", unsafe_allow_html=True)
    progress_bar = st.progress(0)
    status = st.empty()
    logs = ["Bypassing security...", "Loading Kayrakkum logs...", "Syncing Father_DB...", "READY."]
    
    for i, log in enumerate(logs):
        status.markdown(f"<p class='terminal-text' style='font-size:14px;'>[SYSTEM]: {log}</p>", unsafe_allow_html=True)
        progress_bar.progress((i + 1) * 100 // len(logs))
        time.sleep(0.6)
    
    st.session_state.stage = 'final'
    st.rerun()

# 2. Финальное поздравление
elif st.session_state.stage == 'final':
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>ACCESS GRANTED</h1>", unsafe_allow_html=True)
    
    tz = datetime.timezone(datetime.timedelta(hours=5))
    date_str = datetime.datetime.now(tz).strftime("%d.%m.%Y")
    
    if 'display_wish' not in st.session_state:
        st.session_state.display_wish = random.choice(random_wishes)

    st.markdown(f"""
    <div class="wish-card">
        <h2 style="color:#00ff41; text-align:center; font-family: Courier New;">С ДНЕМ РОЖДЕНИЯ, ПАПА! 🎉</h2>
        <p class="terminal-text" style="font-size: 18px;">
        <b>СТАТУС:</b> САМЫЙ ЛУЧШИЙ <br>
        <b>МЕСТО:</b> КАЙРАККУМ <br>
        <b>ДАТА:</b> {date_str} <br>
        -------------------------------------------<br>
        <b>ПОЗДРАВЛЕНИЕ:</b><br>
        {st.session_state.display_wish}<br>
        -------------------------------------------<br><br>
        <b>АВТОР:</b> {NAME} <br>
        <i>Проект выполнен на Python специально для тебя.</i>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("СГЕНЕРИРОВАТЬ ЕЩЕ ОДНО ПОЖЕЛАНИЕ"):
        st.session_state.display_wish = random.choice(random_wishes)
        st.rerun()
