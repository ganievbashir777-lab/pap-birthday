import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

# Настройка страницы
st.set_page_config(page_title="PAPA_OS: Matrix Edition", page_icon="💚", layout="centered")

# Дизайн терминала с Матричным дождем
st.markdown("""
<style>
    /* Весь фон для эффекта матрицы */
    .stApp {
        background-color: #050505;
        overflow: hidden; /* Скрываем прокрутку, если матрица слишком большая */
    }
    
    /* Контейнер для Матричного дождя */
    .matrix-background {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: -1; /* За матричным дождем будет основной контент */
        opacity: 0.2; /* Делаем его полупрозрачным */
        pointer-events: none; /* Чтобы не мешал нажимать кнопки */
    }

    /* Анимация падающих символов */
    @keyframes matrix-fall {
        from { transform: translateY(-100%); }
        to { transform: translateY(100%); }
    }
    .matrix-column {
        position: absolute;
        width: 15px; /* Ширина колонки */
        font-family: 'Consolas', 'Courier New', monospace;
        font-size: 16px;
        color: #00ff41;
        white-space: pre;
        animation: matrix-fall linear infinite;
    }
    
    .terminal-text {
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 8px #00ff41;
        line-height: 1.6;
        background-color: rgba(5,5,5,0.7); /* Фон для читабельности текста */
        padding: 5px;
        border-radius: 3px;
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
        background: linear-gradient(145deg, rgba(10,10,10,0.8), rgba(17,17,17,0.9)); /* Полупрозрачный фон */
        box-shadow: 0 0 25px rgba(0, 255, 65, 0.3);
    }
</style>

<div class="matrix-background" id="matrix-container"></div>

<script>
    const container = document.getElementById('matrix-container');
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-[]{};:'\",.<>/?`~";
    const numColumns = Math.floor(window.innerWidth / 15); // 15px ширина колонки
    
    for (let i = 0; i < numColumns; i++) {
        const column = document.createElement('div');
        column.className = 'matrix-column';
        column.style.left = `${i * 15}px`;
        column.style.animationDuration = `${Math.random() * 5 + 5}s`; // Длительность анимации
        column.style.animationDelay = `-${Math.random() * 5}s`; // Чтобы не все сразу стартовали
        
        let columnText = '';
        for (let j = 0; j < 50; j++) { // 50 символов в колонке
            columnText += chars.charAt(Math.floor(Math.random() * chars.length)) + '\\n';
        }
        column.innerText = columnText;
        container.appendChild(column);
    }
</script>
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
    
    if st.button("ПОЛУЧИТЬ ЕЩЕ ОДНО ПОЖЕЛАНИЕ"):
        st.session_state.display_wish = random.choice(random_wishes)
        st.rerun()
