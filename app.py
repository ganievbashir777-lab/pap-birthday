import streamlit as st
import time
import datetime
import random

# Настройка страницы
st.set_page_config(page_title="Для папы", page_icon="❤️", layout="centered")

# Дизайн терминала
st.markdown("""
<style>
    .stApp { background-color: #050505; }
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
        width: 100%;
        border-radius: 0px;
    }
    .stButton>button:hover {
        background-color: #00ff41 !important;
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# Список рандомных пожеланий
random_wishes = [
    "Желаю тебе крепкого здоровья, чтобы его хватало на все твои планы и идеи!",
    "Пусть в делах всегда сопутствует удача, а каждое начинание завершается успехом.",
    "Желаю как можно больше поводов для искренних улыбок и радости каждый день.",
    "Пусть наш дом всегда остается для тебя местом силы, уюта и тепла.",
    "Желаю неиссякаемой энергии, бодрости духа и всегда отличного настроения!",
    "Пусть жизнь будет наполнена только приятными сюрпризами и добрыми новостями.",
    "Желаю, чтобы всё, о чем ты мечтаешь, обязательно сбывалось в самый нужный момент."
]

def type_text(text, delay=0.04):
    placeholder = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f"<p class='terminal-text'>{displayed_text}</p>", unsafe_allow_html=True)
        time.sleep(delay)

if 'stage' not in st.session_state:
    st.session_state.stage = 'boot'
if 'current_wish' not in st.session_state:
    st.session_state.current_wish = random.choice(random_wishes)

# 1. Начало
if st.session_state.stage == 'boot':
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>SYSTEM_BOOT_INIT...</h1>", unsafe_allow_html=True)
    if st.button("ОТКРЫТЬ ПОСЛАНИЕ"):
        st.session_state.current_wish = random.choice(random_wishes) # Выбираем новое при каждом открытии
        st.session_state.stage = 'loading'
        st.rerun()

# 2. Загрузка
elif st.session_state.stage == 'loading':
    st.markdown("<p class='terminal-text'>[ЗАГРУЗКА]: Выбор случайного пожелания из базы данных...</p>", unsafe_allow_html=True)
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.02)
        progress_bar.progress(i + 1)
    st.session_state.stage = 'final'
    st.rerun()

# 3. Финал
elif st.session_state.stage == 'final':
    st.markdown("<h1 class='terminal-text' style='color:#00ff41;'>[ ДОСТУП РАЗРЕШЕН ]</h1>", unsafe_allow_html=True)
    
    tz_tajikistan = datetime.timezone(datetime.timedelta(hours=5))
    date_string = datetime.datetime.now(tz_tajikistan).strftime("%d.%m.%Y")
    
    st.markdown(f"""
    <div style="border: 2px solid #00ff41; padding: 25px; border-radius: 10px; background-color: #0a0a0a;">
        <h2 style="color:#00ff41; font-family:Courier New; text-align:center;">С ДНЕМ РОЖДЕНИЯ, ПАПА!</h2>
        <p style="color:#00ff41; font-family:Courier New;">
        <b>ОТ КОГО:</b> Твой сын <br>
        <b>ЛОКАЦИЯ:</b> Кайраккум <br>
        <b>ДАТА:</b> {date_string} <br><br>
        <b>ЛИЧНОЕ ПОЖЕЛАНИЕ:</b> <br>
        {st.session_state.current_wish} <br><br>
        --- <br>
        Дорогой папа, я тебя очень люблю и горжусь тобой. Оставайся всегда таким же сильным и мудрым!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ПОЛУЧИТЬ ЕЩЕ ОДНО ПОЖЕЛАНИЕ"):
        st.session_state.stage = 'boot'
        st.rerun()
