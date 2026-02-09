import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="PAPA_OS: Matrix Edition", page_icon="💚", layout="centered")

# Исправленный CSS с анимацией матричного дождя
st.markdown("""
<style>
    /* Фон страницы */
    .stApp {
        background-color: #000000;
        background-image: linear-gradient(rgba(0, 255, 65, 0.1) 1px, transparent 1px),
                          linear-gradient(90deg, rgba(0, 255, 65, 0.1) 1px, transparent 1px);
        background-size: 20px 20px;
    }

    /* Эффект падающих символов на чистом CSS */
    .matrix-rain {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 0;
        background: linear-gradient(180deg, 
            rgba(0,0,0,0) 0%, 
            rgba(0,255,65,0.2) 50%, 
            rgba(0,0,0,0) 100%);
        background-size: 100% 80%;
        animation: rain 3s linear infinite;
    }

    @keyframes rain {
        0% { background-position: 0% -100%; }
        100% { background-position: 0% 100%; }
    }

    /* Стиль карточки, чтобы она была поверх дождя */
    .wish-card {
        position: relative;
        z-index: 10;
        border: 2px solid #00ff41;
        padding: 25px;
        border-radius: 15px;
        background-color: rgba(10, 10, 10, 0.9);
        box-shadow: 0 0 30px rgba(0, 255, 65, 0.4);
        margin-top: 20px;
    }

    .terminal-text {
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 5px #00ff41;
    }

    .stButton>button {
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        background-color: black !important;
        box-shadow: 0 0 10px #00ff41;
        width: 100%;
    }
    
    .stButton>button:hover {
        background-color: #00ff41 !important;
        color: black !important;
        box-shadow: 0 0 40px #00ff41;
    }
</style>

<div class="matrix-rain"></div>
""", unsafe_allow_html=True)

random_wishes = [
    "Дорогой папа, желаю тебе крепкого здоровья! Пусть энергии хватает на все идеи, а каждый день начинается с бодрости. Ты для нас — пример силы!",
    "Желаю большого успеха в делах! Пусть любая работа спорится, а трудности отступают перед твоим опытом. Финансового благополучия тебе!",
    "Пусть наш дом всегда будет для тебя местом силы и уюта. Мы тебя очень любим и всегда поддержим. Душевного спокойствия тебе!",
    "Желаю только добрых новостей! Пусть рядом всегда будут верные друзья, а жизнь наполняется приятными сюрпризами. Гордимся тобой!",
    "С днем рождения! Желаю сохранять твою крутую выдержку и уверенность. Пусть каждый год приносит новые цели и силы для их достижения!"
]

if 'stage' not in st.session_state:
    st.session_state.stage = 'loading'

if st.session_state.stage == 'loading':
    st.markdown("<h2 class='terminal-text' style='text-align:center;'>INITIALIZING MATRIX...</h2>", unsafe_allow_html=True)
    progress_bar = st.progress(0)
    
    logs = ["Bypassing security...", "Loading Kayrakkum logs...", "Accessing Father_DB...", "System ready."]
    for i, log in enumerate(logs):
        st.markdown(f"<p class='terminal-text' style='font-size:12px;'>[SYS]: {log}</p>", unsafe_allow_html=True)
        progress_bar.progress((i + 1) * 100 // len(logs))
        time.sleep(0.6)
    
    st.session_state.stage = 'final'
    st.rerun()

elif st.session_state.stage == 'final':
    st.snow()
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>SYSTEM UNLOCKED</h1>", unsafe_allow_html=True)
    
    tz = datetime.timezone(datetime.timedelta(hours=5))
    date_str = datetime.datetime.now(tz).strftime("%d.%m.%Y")
    
    if 'display_wish' not in st.session_state:
        st.session_state.display_wish = random.choice(random_wishes)

    st.markdown(f"""
    <div class="wish-card">
        <h2 style="color:#00ff41; text-align:center; font-family: Courier New;">ОТЧЕТ ДЛЯ ПАПЫ</h2>
        <p class="terminal-text">
        <b>СТАТУС:</b> ЛУЧШИЙ ОТЕЦ <br>
        <b>ГОРОД:</b> КАЙРАККУМ <br>
        <b>ДАТА:</b> {date_str} <br>
        -------------------------------------------<br>
        {st.session_state.display_wish}<br>
        -------------------------------------------<br><br>
        <b>АВТОР:</b> {NAME}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("СЛЕДУЮЩЕЕ ПОЖЕЛАНИЕ"):
        st.session_state.display_wish = random.choice(random_wishes)
        st.rerun()
