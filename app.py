import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="PAPA_OS: Final Edition", page_icon="📟", layout="centered")

# CSS для стиля Матрицы и Бинарного дождя
st.markdown("""
<style>
    .stApp {
        background-color: #000000;
    }

    /* Эффект бинарного дождя вместо снега */
    .binary-rain {
        position: fixed;
        top: -100px;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
    }

    .binary-drop {
        position: absolute;
        color: #00ff41;
        font-family: 'Courier New', monospace;
        font-size: 20px;
        user-select: none;
        animation: fall linear infinite;
    }

    @keyframes fall {
        to {
            transform: translateY(110vh);
        }
    }

    .wish-card {
        position: relative;
        z-index: 10;
        border: 2px solid #00ff41;
        padding: 30px;
        border-radius: 10px;
        background-color: rgba(5, 5, 5, 0.9);
        box-shadow: 0 0 40px rgba(0, 255, 65, 0.2);
        margin-top: 50px;
    }

    .terminal-text {
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 5px #00ff41;
    }

    .stButton>button {
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        background-color: transparent !important;
        box-shadow: 0 0 15px #00ff41;
        width: 100%;
    }
    
    .stButton>button:hover {
        background-color: #00ff41 !important;
        color: black !important;
        box-shadow: 0 0 50px #00ff41;
    }
</style>

<div class="binary-rain" id="rain"></div>

<script>
    const rainContainer = document.getElementById('rain');
    function createDrop() {
        const drop = document.createElement('div');
        drop.className = 'binary-drop';
        drop.innerText = Math.round(Math.random()); // Выдает 0 или 1
        drop.style.left = Math.random() * 100 + 'vw';
        drop.style.animationDuration = Math.random() * 2 + 1 + 's'; // Скорость падения
        drop.style.opacity = Math.random();
        
        rainContainer.appendChild(drop);
        
        setTimeout(() => {
            drop.remove();
        }, 3000);
    }
    setInterval(createDrop, 50); // Частота появления
</script>
""", unsafe_allow_html=True)

random_wishes = [
    "Дорогой папа, желаю тебе крепкого и несокрушимого здоровья! Ты — наш главный сервер и опора. Пусть твоя энергия никогда не иссякает, а каждый день в Кайраккуме приносит радость!",
    "Желаю успеха во всех твоих делах! Пусть любые трудности обходятся стороной, а жизнь будет наполнена только позитивными событиями. Финансового благополучия и удачи!",
    "Пусть наш дом всегда будет для тебя местом силы, где тебя всегда ждут и любят. Желаю тебе спокойствия, мудрости и долгих лет счастливой жизни!",
    "С днем рождения, лучший отец! Желаю тебе оставаться таким же сильным и надежным. Пусть всё задуманное сбывается, а счастье множится с каждым днем!",
    "Желаю тебе бодрости духа и отличного настроения! Пусть каждый новый год жизни приносит только добрые новости и яркие моменты. Мы тобой гордимся!"
]

if 'stage' not in st.session_state:
    st.session_state.stage = 'loading'

if st.session_state.stage == 'loading':
    st.markdown("<h2 class='terminal-text' style='text-align:center;'>DECRYPTING BIRTHDAY_DATA...</h2>", unsafe_allow_html=True)
    progress_bar = st.progress(0)
    
    logs = [
        "Accessing core kernel...",
        "Searching for 'PAPA_ID'...",
        "Bypassing firewall [OK]",
        "Location: Tajikistan, Kayrakkum detected...",
        "Unpacking wishes..."
    ]
    
    for i, log in enumerate(logs):
        st.markdown(f"<p class='terminal-text' style='font-size:13px;'>[SYS]: {log}</p>", unsafe_allow_html=True)
        progress_bar.progress((i + 1) * 100 // len(logs))
        time.sleep(0.6)
    
    st.session_state.stage = 'final'
    st.rerun()

elif st.session_state.stage == 'final':
    # st.snow() УДАЛЕНО, заменено на бинарный дождь в HTML/JS блоке выше
    
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>🔓 ACCESS GRANTED</h1>", unsafe_allow_html=True)
    
    tz = datetime.timezone(datetime.timedelta(hours=5))
    date_str = datetime.datetime.now(tz).strftime("%d.%m.%Y")
    
    if 'display_wish' not in st.session_state:
        st.session_state.display_wish = random.choice(random_wishes)

    st.markdown(f"""
    <div class="wish-card">
        <h2 style="color:#00ff41; text-align:center; font-family: Courier New;">SECRET REPORT FOR PAPA</h2>
        <p class="terminal-text">
        <b>ОБЪЕКТ:</b> ЛУЧШИЙ ОТЕЦ В МИРЕ <br>
        <b>ЛОКАЦИЯ:</b> КАЙРАККУМ <br>
        <b>ДАТА:</b> {date_str} <br>
        -------------------------------------------<br>
        <b>СООБЩЕНИЕ:</b><br>
        {st.session_state.display_wish}<br>
        -------------------------------------------<br><br>
        <b>ДЕВЕЛОПЕР:</b> {NAME} <br>
        <i>Система работает стабильно. С праздником!</i>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("СГЕНЕРИРОВАТЬ НОВОЕ ПОЖЕЛАНИЕ"):
        st.session_state.display_wish = random.choice(random_wishes)
        st.rerun()
