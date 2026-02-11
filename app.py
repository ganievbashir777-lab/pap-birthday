import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="С Днем Рождения, Папа!", page_icon="❤️", layout="centered")

# ПОЛНЫЙ CSS ДЛЯ ЦЕНТРИРОВАНИЯ И СТИЛЯ КНОПОК
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;700&display=swap');

    /* Фон всей страницы */
    .stApp {
        background: linear-gradient(135deg, #fff5f5 0%, #f0f4ff 100%);
    }

    /* Магия центрирования: заставляем основной контейнер быть на весь экран и центрировать всё внутри */
    [data-testid="stVerticalBlock"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
    }

    /* Стиль ГЛАВНОЙ КНОПКИ-КОНВЕРТА */
    .main-envelope-btn div.stButton > button {
        background-color: white !important;
        border: 3px dashed #ffadad !important;
        border-radius: 25px !important;
        padding: 50px 20px !important;
        width: 320px !important;
        height: 220px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.15) !important;
        color: #ff6b6b !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        display: flex !important;
        flex-direction: column !important;
        align-items: center !important;
        justify-content: center !important;
        margin: 0 auto !important;
    }

    .main-envelope-btn div.stButton > button:hover {
        transform: translateY(-10px) !important;
        box-shadow: 0 15px 45px rgba(255, 107, 107, 0.3) !important;
        border-style: solid !important;
    }

    /* Стиль НИЖНЕЙ КНОПКИ (маленькая и аккуратная, как в 1-м варианте) */
    .small-refresh-btn div.stButton > button {
        background-color: #ff6b6b !important;
        color: white !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 50px !important;
        font-size: 0.9rem !important;
        width: auto !important;
        height: auto !important;
        margin-top: 20px !important;
        box-shadow: 0 5px 15px rgba(255, 107, 107, 0.2) !important;
    }

    /* Заголовки */
    .main-title {
        font-family: 'Pacifico', cursive;
        color: #ff6b6b;
        font-size: 3.2rem;
        text-align: center;
        margin-bottom: 5px;
    }

    .sub-text {
        font-family: 'Roboto', sans-serif;
        color: #7f8c8d;
        font-size: 1.1rem;
        text-align: center;
        margin-bottom: 30px;
    }

    /* Карточка поздравления */
    .wish-card {
        background: white;
        padding: 35px;
        border-radius: 30px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.08);
        max-width: 500px;
        width: 100%;
        text-align: left;
    }

    .wish-header {
        font-family: 'Pacifico', cursive;
        color: #ff6b6b;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 20px;
    }

    .wish-text {
        font-family: 'Roboto', sans-serif;
        font-size: 1.3rem;
        color: #2c3e50;
        line-height: 1.5;
        background: #fff9f9;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #ff6b6b;
    }

    header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if 'opened' not in st.session_state:
    st.session_state.opened = False

# --- ЛОГИКА ЭКРАНОВ ---

if not st.session_state.opened:
    # ЭКРАН 1: КОНВЕРТ СТРОГО ПО ЦЕНТРУ
    st.markdown('<h1 class="main-title">С Днём Рождения, Папа!</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Нажми на конверт, чтобы открыть</p>', unsafe_allow_html=True)
    
    # Оборачиваем кнопку в спец-класс для стиля конверта
    st.markdown('<div class="main-envelope-btn">', unsafe_allow_html=True)
    if st.button("📩\n\nОТКРЫТЬ ПИСЬМО"):
        st.session_state.opened = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # ЭКРАН 2: ОТКРЫТОЕ ПОЗДРАВЛЕНИЕ
    st.balloons() 
    st.snow()
    
    wishes = [
        "Дорогой папа, поздравляю тебя с днем рождения! Желаю тебе самого крепкого здоровья, долгих лет жизни и чтобы каждый день приносил только радость. Ты — лучший пример для меня!",
        "С днем рождения, папа! Пусть твоя жизнь будет наполнена светом и теплом. Желаю удачи во всех делах, бодрости духа и отличного настроения!",
        "Папа, спасибо тебе за твою мудрость и поддержку. Желаю тебе финансового благополучия, душевного спокойствия и чтобы все твои мечты обязательно сбывались!",
        "Самый лучший папа, с праздником! Пусть каждый день в Кайраккуме радует тебя солнцем и теплом. Мы тебя очень любим!"
    ]

    if 'current_wish' not in st.session_state:
        st.session_state.current_wish = random.choice(wishes)

    now = datetime.datetime.now().strftime("%d.%m.%Y")

    st.markdown(f"""
    <div class="wish-card">
        <div class="wish-header">Для тебя! ❤️</div>
        <div class="wish-text">
            {st.session_state.current_wish}
        </div>
        <div style="margin-top: 25px; font-family: 'Roboto'; border-top: 1px solid #eee; padding-top: 15px; color: #7f8c8d; font-size: 0.9rem;">
            <p><b>От кого:</b> {NAME}</p>
            <p><b>Дата:</b> {now}</p>
            <p><b>Место:</b> Кайраккум</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Оборачиваем кнопку в спец-класс для маленького размера
    st.markdown('<div class="small-refresh-btn">', unsafe_allow_html=True)
    if st.button("Прочитать другое ✨"):
        st.session_state.current_wish = random.choice(wishes)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
