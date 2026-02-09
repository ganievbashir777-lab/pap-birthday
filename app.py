import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="PAPA_OS: Binary Rain", page_icon="📟", layout="centered")

# Мощный CSS для бинарного дождя и стиля терминала
st.markdown("""
<style>
    /* Основной фон */
    .stApp {
        background-color: #000000;
        overflow: hidden;
    }

    /* Создаем эффект падающих чисел через фоновую анимацию */
    .stApp::before {
        content: "1 0 1 1 0 0 1 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 1 0 1 0 1 1 0 0 1 1 0 1 0 1 0 1 1 0 0 1 0 1 0 1 1 0 1 0 0 1 0 1 1 0 1 1 0 1 0 1 0 1 1 0 0";
        position: fixed;
        top: -100px;
        left: 0;
        width: 100%;
        font-family: 'Courier New', monospace;
        font-size: 20px;
        color: rgba(0, 255, 65, 0.15);
        word-wrap: break-word;
        line-height: 1;
        white-space: pre-wrap;
        animation: rain 10s linear infinite;
        z-index: 0;
        display: block;
    }

    @keyframes rain {
        from { transform: translateY(0); }
        to { transform: translateY(100vh); }
    }

    /* Карточка с поздравлением */
    .wish-card {
        position: relative;
        z-index: 10;
        border: 2px solid #00ff41;
        padding: 30px;
        border-radius: 10px;
        background-color: rgba(5, 5, 5, 0.9);
        box-shadow: 0 0 30px rgba(0, 255, 65, 0.3);
        margin-top: 50px;
    }

    .terminal-text {
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 5px #00ff41;
    }

    /* Кнопки */
    .stButton>button {
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        background-color: black !important;
        box-shadow: 0 0 10px #00ff41;
        width: 100%;
        font-weight: bold;
    }
    
    .stButton>button:hover {
        background-color: #00ff41 !important;
        color: black !important;
        box-shadow: 0 0 50px #00ff41;
    }

    /* Скрываем лишние элементы Streamlit для красоты */
    header {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

random_wishes = [
    "Папа, желаю тебе стального здоровья! Пусть твоя внутренняя энергия никогда не иссякает, а каждый день в нашем Кайраккуме приносит только добрые новости. Ты — лучший!",
    "Желаю огромного успеха в делах! Пусть любые преграды исчезают, как ошибки в коде. Счастья, финансовой свободы и бодрости духа тебе каждый день!",
    "С днем рождения! Желаю, чтобы в жизни всегда был 'зеленый свет' для всех твоих идей. Мы тебя очень любим и всегда будем рядом. Ты — наша гордость!",
    "Пусть каждый год жизни делает тебя только сильнее и мудрее. Желаю радости, крепких нервов и исполнения самых заветных желаний. Оставайся всегда таким же крутым!",
    "Дорогой папа, спасибо тебе за всё! Желаю, чтобы твоё сердце всегда было наполнено радостью, а дом — теплом. Здоровья тебе на долгие-долгие годы!"
]

if 'stage' not in st.session_state:
    st.session_state.stage = 'loading'

# 1. Загрузка
if st.session_state.stage == 'loading':
    st.markdown("<h2 class='terminal-text' style='text-align:center;'>INITIATING BINARY_DECRYPT...</h2>", unsafe_allow_html=True)
    
    progress_bar = st.progress(0)
    status = st.empty()
    
    logs = ["Checking System...", "Bypassing Firewall...", "Accessing Father_Records...", "Location: Kayrakkum OK", "READY."]
    
    for i, log in enumerate(logs):
        status.markdown(f"<p class='terminal-text' style='font-size:14px;'>[SYSTEM]: {log}</p>", unsafe_allow_html=True)
        progress_bar.progress((i + 1) * 100 // len(logs))
        time.sleep(0.7)
    
    st.session_state.stage = 'final'
    st.rerun()

# 2. Финал
elif st.session_state.stage == 'final':
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>ACCESS GRANTED</h1>", unsafe_allow_html=True)
    
    # Настройка времени Таджикистана
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
        <i>Проект выполнен на языке Python специально для тебя.</i>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("СГЕНЕРИРОВАТЬ ЕЩЕ ОДНО ПОЖЕЛАНИЕ"):
        st.session_state.display_wish = random.choice(random_wishes)
        st.rerun()
