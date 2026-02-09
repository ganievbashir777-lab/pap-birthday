import streamlit as st
import time
import datetime
import random

# Настройка страницы
st.set_page_config(page_title="PAPA_OS: Restricted Access", page_icon="🔐", layout="centered")

# Дизайн терминала
st.markdown("""
<style>
    .stApp { background-color: #050505; }
    .terminal-text {
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 8px #00ff41;
    }
    .stButton>button {
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        background-color: transparent !important;
        box-shadow: 0 0 10px #00ff41;
        transition: 0.3s;
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

# Список поздравлений
random_wishes = [
    "Папа, желаю тебе стального здоровья и бесконечной энергии! Пусть каждый день в Кайраккуме приносит только радость, а все твои планы реализуются на 100%. Ты — наша главная опора!",
    "С днем рождения! Желаю, чтобы удача всегда была на твоей стороне, а в доме всегда царили мир, тепло и достаток. Пусть каждый новый год жизни будет круче предыдущего!",
    "Желаю тебе всегда оставаться таким же мудрым и сильным. Пусть сердце будет спокойным, а поводов для гордости за нас — как можно больше. Мы тебя очень любим!",
    "Пусть твои руки никогда не знают усталости, а глаза всегда светятся от счастья. Желаю тебе благополучия, верных друзей рядом и исполнения самых заветных желаний!",
    "Самого лучшего отца — с днем рождения! Желаю тебе долгих лет жизни, бодрости духа и чтобы каждый твой совет всегда попадал прямо в цель. Спасибо за всё!"
]

if 'stage' not in st.session_state:
    st.session_state.stage = 'security_1'

# --- ШАГ 1: ВОПРОС ПРО СЫНА ---
if st.session_state.stage == 'security_1':
    st.markdown("<h2 class='terminal-text'>[SECURITY LEVEL 1]</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='terminal-text'>КТО НАПИСАЛ ЭТОТ КОД СПЕЦИАЛЬНО ДЛЯ ТЕБЯ?</p>", unsafe_allow_html=True)
    ans1 = st.text_input("Введите ответ:", placeholder="Подсказка: твой сын")
    
    if st.button("ПРОВЕРИТЬ"):
        if ans1.lower().strip() in ["сын", "мой сын", "ты", "мой любимый сын"]:
            st.success("ДОСТУП ЧАСТИЧНО РАЗРЕШЕН...")
            time.sleep(1)
            st.session_state.stage = 'security_2'
            st.rerun()
        else:
            st.error("ОШИБКА: СИСТЕМА НЕ УЗНАЕТ ВАС.")

# --- ШАГ 2: ШУТОЧНЫЙ ВОПРОС ---
elif st.session_state.stage == 'security_2':
    st.markdown("<h2 class='terminal-text'>[SECURITY LEVEL 2]</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='terminal-text'>ВЫБЕРИТЕ СВОЙ ТЕКУЩИЙ СТАТУС:</p>", unsafe_allow_html=True)
    ans2 = st.radio("", ["Просто человек", "Обычный папа", "САМЫЙ ЛУЧШИЙ ПАПА В МИРЕ"])
    
    if st.button("ПОДТВЕРДИТЬ СТАТУС"):
        if ans2 == "САМЫЙ ЛУЧШИЙ ПАПА В МИРЕ":
            st.success("СТАТУС ПОДТВЕРЖДЕН. ИДЕТ ДЕШИФРОВКА...")
            time.sleep(1)
            st.session_state.stage = 'mood'
            st.rerun()
        else:
            st.warning("СИСТЕМА ЗНАЕТ, ЧТО ВЫ СКРОМНИЧАЕТЕ. ПОПРОБУЙТЕ ЕЩЕ РАЗ!")

# --- ШАГ 3: КАЛИБРОВКА СЧАСТЬЯ ---
elif st.session_state.stage == 'mood':
    st.markdown("<h2 class='terminal-text'>[SYSTEM CALIBRATION]</h2>", unsafe_allow_html=True)
    st.write("Настройте уровень праздничного настроения:")
    happiness = st.slider("", 0, 100, 100)
    
    if st.button("ОТКРЫТЬ ПОЗДРАВЛЕНИЕ"):
        if happiness > 50:
            st.balloons()
        st.session_state.stage = 'final'
        st.rerun()

# --- ШАГ 4: ФИНАЛ ---
elif st.session_state.stage == 'final':
    st.snow()
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>🎉 ACCESS GRANTED 🎉</h1>", unsafe_allow_html=True)
    
    # Время для Кайраккума
    tz = datetime.timezone(datetime.timedelta(hours=5))
    date_str = datetime.datetime.now(tz).strftime("%d.%m.%Y")
    
    if 'display_wish' not in st.session_state:
        st.session_state.display_wish = random.choice(random_wishes)

    st.markdown(f"""
    <div class="wish-card">
        <h2 style="color:#00ff41; text-align:center; font-family: Courier New;">ОТЧЕТ ДЛЯ ПАПЫ</h2>
        <p style="color:#00ff41; font-family:Courier New; font-size: 16px;">
        <b>СТАТУС:</b> ГЛАВНЫЙ ЧЕЛОВЕК <br>
        <b>ГОРОД:</b> КАЙРАККУМ <br>
        <b>ДАТА:</b> {date_str} <br>
        -------------------------------------------<br>
        <b>ТЕКСТ ПОЗДРАВЛЕНИЯ:</b><br>
        {st.session_state.display_wish}<br>
        -------------------------------------------<br><br>
        <b>ПОДПИСЬ:</b> Твой сын. <br>
        <i>Код написан на языке Python специально для тебя!</i>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ПОЛУЧИТЬ НОВОЕ ПОЗДРАВЛЕНИЕ"):
        st.session_state.display_wish = random.choice(random_wishes)
        st.rerun()
