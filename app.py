import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

# Настройка страницы
st.set_page_config(page_title="Для папы", page_icon="❤️", layout="centered")

# Дизайн терминала
st.markdown("""
<style>
    .stApp { background-color: #050505; }
    .terminal-text {
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 8px #00ff41;
        line-height: 1.6;
    }
    .stButton>button {
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        background-color: transparent !important;
        box-shadow: 0 0 10px #00ff41;
        transition: 0.3s;
        font-family: 'Courier New', Courier, monospace;
    }
    .stButton>button:hover {
        background-color: #00ff41 !important;
        color: black !important;
        box-shadow: 0 0 30px #00ff41;
    }
    .wish-card {
        border: 2px solid #00ff41;
        padding: 25px;
        border-radius: 15px;
        background: linear-gradient(145deg, #0a0a0a, #111111);
        box-shadow: 0 0 25px rgba(0, 255, 65, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Список длинных и душевных поздравлений
random_wishes = [
    "Дорогой папа, желаю тебе прежде всего крепкого и несокрушимого здоровья! Пусть энергии хватает на все твои идеи, а каждый день начинается с бодрости. Ты для нас — пример силы и мудрости!",
    "В этот день хочу пожелать тебе большого успеха во всех делах. Пусть любая работа спорится, а трудности отступают. Желаю тебе благополучия, стабильности и только добрых новостей!",
    "Пусть наш дом всегда будет для тебя местом силы и уюта. Мы тебя очень любим и всегда поддержим. Желаю тебе душевного спокойствия, радости и побольше времени на отдых в кругу семьи!",
    "Желаю, чтобы жизнь была наполнена только приятными событиями. Пусть рядом всегда будут верные друзья. Я желаю тебе как можно больше поводов для гордости, а мы будем радовать тебя успехами!",
    "С днем рождения, самый лучший отец! Желаю тебе всегда сохранять твою выдержку и уверенность. Пусть каждый год приносит новые цели и силы для их достижения. Спасибо за всё!"
]

if 'stage' not in st.session_state:
    st.session_state.stage = 'loading'

# --- ШАГ 1: АНИМАЦИЯ ЗАГРУЗКИ ---
if st.session_state.stage == 'loading':
    st.markdown("<h2 class='terminal-text' style='text-align:center;'>PAPA_OS v3.0: INITIALIZING...</h2>", unsafe_allow_html=True)
    st.write("")
    
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    logs = [
        "Connecting to Family_Server...",
        "Scanning for 'Best Father' records...",
        "Location: Tajikistan, Kayrakkum... Verified.",
        "Generating unique wishes...",
        "Accessing security protocols... Bypassed.",
        "System ready."
    ]
    
    for i, log in enumerate(logs):
        status_text.markdown(f"<p class='terminal-text' style='font-size:12px;'>[SYSTEM]: {log}</p>", unsafe_allow_html=True)
        progress_bar.progress((i + 1) * 100 // len(logs))
        time.sleep(0.7)
    
    st.session_state.stage = 'final'
    st.rerun()

# --- ШАГ 2: ФИНАЛЬНОЕ ПОЗДРАВЛЕНИЕ ---
elif st.session_state.stage == 'final':
    st.snow() # Праздничный эффект
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>🎉 С ДНЕМ РОЖДЕНИЯ! 🎉</h1>", unsafe_allow_html=True)
    
    # Расчет даты для Кайраккума
    tz = datetime.timezone(datetime.timedelta(hours=5))
    date_str = datetime.datetime.now(tz).strftime("%d.%m.%Y")
    
    if 'display_wish' not in st.session_state:
        st.session_state.display_wish = random.choice(random_wishes)

    st.markdown(f"""
    <div class="wish-card">
        <h2 style="color:#00ff41; text-align:center; font-family: Courier New;">ЛИЧНЫЙ ОТЧЕТ</h2>
        <p style="color:#00ff41; font-family:Courier New; font-size: 16px;">
        <b>ПОЛУЧАТЕЛЬ:</b> ЛУЧШИЙ ПАПА <br>
        <b>ЛОКАЦИЯ:</b> КАЙРАККУМ <br>
        <b>ДАТА:</b> {date_str} <br>
        -------------------------------------------<br>
        <b>ПОСЛАНИЕ:</b><br>
        {st.session_state.display_wish}<br>
        -------------------------------------------<br><br>
        <b>АВТОР:</b> {NAME} <br>
        <i>Этот проект написан на языке Python специально в твою честь!</i>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("ПОЛУЧИТЬ ЕЩЕ ОДНО ПОЖЕЛАНИЕ"):
        st.session_state.display_wish = random.choice(random_wishes)
        st.rerun()
