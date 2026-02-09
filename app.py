import streamlit as st
import time
import datetime

# Настройка страницы
st.set_page_config(page_title="Для папы", page_icon="❤️", layout="centered")

# CSS остается для стиля, но мы сделаем его чуть мягче
st.markdown("""
<style>
    .stApp {
        background-color: #050505;
    }
    .terminal-text {
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 5px #00ff41;
        line-height: 1.6;
    }
    .stButton>button {
        color: #00ff41 !important;
        border: 1px solid #00ff41 !important;
        background-color: transparent !important;
        font-family: 'Courier New', Courier, monospace !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00ff41 !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #00ff41;
    }
</style>
""", unsafe_allow_html=True)

def type_text(text, delay=0.04):
    placeholder = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f"<p class='terminal-text'>{displayed_text}</p>", unsafe_allow_html=True)
        time.sleep(delay)

if 'stage' not in st.session_state:
    st.session_state.stage = 'boot'

# 1. Начало
if st.session_state.stage == 'boot':
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>SYSTEM_START...</h1>", unsafe_allow_html=True)
    st.write("")
    if st.button("ОТКРЫТЬ СООБЩЕНИЕ"):
        st.session_state.stage = 'loading'
        st.rerun()

# 2. Загрузка
elif st.session_state.stage == 'loading':
    st.markdown("<p class='terminal-text'>[ЗАГРУЗКА]: Подключение к базе данных поздравлений...</p>", unsafe_allow_html=True)
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
        if i == 30: st.write("`[OK] Поиск самых важных слов...`")
        if i == 70: st.write("`[OK] Формирование пожеланий...`")
    
    time.sleep(0.5)
    st.session_state.stage = 'final'
    st.rerun()

# 3. Человеческое поздравление
elif st.session_state.stage == 'final':
    st.markdown("<h1 class='terminal-text' style='color:#00ff41;'>[ ДОСТУП РАЗРЕШЕН ]</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Время Таджикистана
    tz_tajikistan = datetime.timezone(datetime.timedelta(hours=5))
    current_time = datetime.datetime.now(tz_tajikistan)
    date_string = current_time.strftime("%d.%m.%Y")
    
    type_text("Сообщение для лучшего папы:")
    
    st.markdown(f"""
    <div style="border: 2px solid #00ff41; padding: 25px; border-radius: 10px; background-color: #0a0a0a;">
        <h2 style="color:#00ff41; font-family:Courier New; text-align:center;">С ДНЕМ РОЖДЕНИЯ!</h2>
        <p style="color:#00ff41; font-family:Courier New; font-size: 18px;">
        <b>ОТ КОГО:</b> Твой сын <br>
        <b>ОТКУДА:</b> Кайраккум <br>
        <b>ДАТА:</b> {date_string} <br><br>
        <b>ТЕКСТ:</b> <br>
        Дорогой папа! <br><br>
        От всей души поздравляю тебя с днем рождения! <br>
        Я очень благодарен тебе за твою поддержку, за твои советы и за всё то, что ты для меня делаешь. <br><br>
        Желаю тебе в первую очередь крепкого здоровья, долгих лет жизни и чтобы каждый твой день был наполнен радостью. Пусть в делах всегда сопутствует удача, а дома всегда будет уют и спокойствие. <br><br>
        Оставайся всегда таким же сильным и мудрым человеком. Я горжусь тем, что ты мой отец!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("ПРОЧИТАНО (ВЫХОД)"):
        st.session_state.stage = 'boot'
        st.rerun()
