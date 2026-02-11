import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="С Днем Рождения, Папа!", page_icon="🎂", layout="centered")

# CSS для возвращения стилей кнопок и их позиционирования
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* Центрирование контента */
    [data-testid="stVerticalBlock"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 85vh;
    }

    /* 1. СТИЛЬ ПЕРВОЙ КНОПКИ-ОТКРЫТКИ */
    .envelope-container div.stButton > button {
        background-color: white !important;
        border: 4px dashed #6a11cb !important;
        border-radius: 30px !important;
        padding: 60px 40px !important;
        width: 350px !important;
        height: 250px !important;
        box-shadow: 0 15px 40px rgba(106, 17, 203, 0.2) !important;
        transition: all 0.3s ease !important;
        color: #6a11cb !important;
        font-family: 'Roboto', sans-serif !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
    }

    .envelope-container div.stButton > button:hover {
        transform: translateY(-10px) scale(1.02) !important;
        box-shadow: 0 20px 50px rgba(106, 17, 203, 0.3) !important;
        border-style: solid !important;
    }

    /* 2. СТИЛЬ МАЛЕНЬКОЙ КНОПКИ СЛЕВА (НА ВТОРОМ ЭКРАНЕ) */
    .left-btn div.stButton > button {
        background: linear-gradient(to right, #6a11cb 0%, #2575fc 100%) !important;
        color: white !important;
        border: none !important;
        padding: 10px 25px !important;
        border-radius: 50px !important;
        font-family: 'Roboto', sans-serif !important;
        font-size: 0.9rem !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        width: auto !important;
        margin-top: 10px !important;
    }

    .left-btn div.stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 10px 20px rgba(37, 117, 252, 0.3) !important;
    }

    /* Выравнивание контейнера маленькой кнопки влево */
    .left-btn {
        display: flex;
        justify-content: flex-start;
        width: 100%;
        max-width: 550px;
    }

    /* Стиль карточки */
    .main-card {
        background-color: white;
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        text-align: left;
        max-width: 550px;
        width: 100%;
        animation: fadeIn 0.8s ease-out;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .card-title {
        font-family: 'Pacifico', cursive;
        color: #6a11cb;
        font-size: 2.8rem;
        text-align: center;
        margin-bottom: 20px;
    }

    .wish-text {
        font-family: 'Roboto', sans-serif;
        font-size: 1.3rem;
        color: #444;
        line-height: 1.6;
        font-style: italic;
        background: #f9f9f9;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #6a11cb;
        margin-bottom: 20px;
    }

    header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if 'opened' not in st.session_state:
    st.session_state.opened = False

# --- ЭКРАН 1: ЗАКРЫТАЯ ОТКРЫТКА ---
if not st.session_state.opened:
    st.markdown("<h1 style='font-family: Pacifico; color: #6a11cb; text-align: center;'>Для тебя, Папа! ❤️</h1>", unsafe_allow_html=True)
    
    st.markdown('<div class="envelope-container">', unsafe_allow_html=True)
    if st.button("✉️\n\nНАЖМИ, ЧТОБЫ ОТКРЫТЬ"):
        st.session_state.opened = True
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# --- ЭКРАН 2: САМО ПОЗДРАВЛЕНИЕ ---
else:
    st.snow() 

    wishes = [
        "Дорогой папа, поздравляю тебя с днем рождения! Желаю тебе самого крепкого здоровья, долгих лет жизни и чтобы каждый день приносил только радость. Ты — лучший пример для меня!",
        "С днем рождения, папа! Пусть твоя жизнь будет наполнена светом и теплом. Желаю удачи во всех делах, бодрости духа и отличного настроения!",
        "Папа, спасибо тебе за твою мудрость и поддержку. Желаю тебе финансового благополучия, душевного спокойствия и чтобы все твои мечты обязательно сбывались!",
        "Самый лучший папа, с праздником! Пусть этот год принесет тебе много радости и новых успехов. Мы тебя очень любим!"
    ]

    if 'msg' not in st.session_state:
        st.session_state.msg = random.choice(wishes)

    now = datetime.datetime.now().strftime("%d.%m.%Y")

    st.markdown(f"""
    <div class="main-card">
        <div class="card-title">С Днём Рождения! 🎂</div>
        <div class="wish-text">
            "{st.session_state.msg}"
        </div>
        <div style="border-top: 1px solid #eee; padding-top: 15px; color: #7f8c8d; font-family: 'Roboto'; font-size: 0.9rem;">
            <p><b>Для кого:</b> Любимому папе</p>
            <p><b>От кого:</b> {NAME}</p>
            <p><b>Дата:</b> {now}</p>
            <p><b>Место:</b> Кайраккум</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Маленькая кнопка в левом углу
    st.markdown('<div class="left-btn">', unsafe_allow_html=True)
    if st.button("Прочитать другое ✨"):
        st.session_state.msg = random.choice(wishes)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
