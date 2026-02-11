import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="С Днем Рождения, Папа!", page_icon="🎂", layout="centered")

# CSS для праздничного оформления
st.markdown("""
<style>
    /* Праздничный фон */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* Стиль карточки */
    .main-card {
        background-color: white;
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        text-align: center;
        border: none;
        margin-top: 50px;
    }

    h1 {
        color: #2d3436;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        font-weight: 800;
    }

    .wish-text {
        font-size: 1.3rem;
        color: #636e72;
        line-height: 1.6;
        font-style: italic;
        margin: 20px 0;
    }

    .info-text {
        color: #b2bec3;
        font-size: 0.9rem;
        margin-top: 30px;
    }

    /* Кнопка */
    .stButton>button {
        background: linear-gradient(to right, #6a11cb 0%, #2575fc 100%) !important;
        color: white !important;
        border: none !important;
        padding: 15px 30px !important;
        border-radius: 50px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(37, 117, 252, 0.3);
    }

    header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if 'step' not in st.session_state:
    st.session_state.step = 'start'

# --- ЭТАП 1: ПРИВЕТСТВИЕ ---
if st.session_state.step == 'start':
    st.markdown("""
    <div class="main-card">
        <h1 style="font-size: 50px;">🎁</h1>
        <h1>Папа, у меня есть кое-что для тебя!</h1>
        <p style="color: #636e72; font-size: 1.2rem;">Я подготовил небольшой сюрприз в честь твоего дня рождения.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("ОТКРЫТЬ ПОДАРОК"):
        st.session_state.step = 'loading'
        st.rerun()

# --- ЭТАП 2: КРАСИВОЕ ОЖИДАНИЕ ---
elif st.session_state.step == 'loading':
    st.markdown("<div class='main-card'>", unsafe_allow_html=True)
    st.markdown("<h2>Готовим поздравление...</h2>", unsafe_allow_html=True)
    
    # Красивый индикатор
    progress_bar = st.progress(0)
    for percent_complete in range(100):
        time.sleep(0.02)
        progress_bar.progress(percent_complete + 1)
    
    st.session_state.step = 'final'
    st.rerun()

# --- ЭТАП 3: ФИНАЛЬНАЯ ОТКРЫТКА ---
elif st.session_state.step == 'final':
    # Запускаем праздник!
    st.balloons()
    st.snow() # Добавим немного "волшебства" в виде летящих снежинок/звездочек
    
    wishes = [
        "Дорогой папа, поздравляю тебя с днем рождения! Желаю тебе самого крепкого здоровья, долгих лет жизни и чтобы каждый день приносил только радость. Ты — лучший пример для меня!",
        "С днем рождения, папа! Пусть твоя жизнь будет наполнена светом и теплом. Желаю удачи во всех делах, бодрости духа и отличного настроения в нашем любимом Кайраккуме!",
        "Папа, спасибо тебе за твою мудрость и поддержку. Желаю тебе финансового благополучия, душевного спокойствия и чтобы все твои мечты обязательно сбывались!",
        "Поздравляю! Желаю тебе всегда оставаться таким же сильным и добрым. Пусть здоровье никогда не подводит, а дом всегда будет полной чашей. Мы тебя любим!",
        "Самый лучший папа, с твоим днем! Желаю тебе побольше поводов для улыбок, приятных сюрпризов от жизни и верных друзей рядом. С праздником!"
    ]

    if 'msg' not in st.session_state:
        st.session_state.msg = random.choice(wishes)

    now = datetime.datetime.now().strftime("%d.%m.%Y")

    st.markdown(f"""
    <div class="main-card">
        <h1 style="color: #6a11cb;">С Днём Рождения! 🎂</h1>
        <p class="wish-text">"{st.session_state.msg}"</p>
        <hr style="border: 0; border-top: 1px solid #eee; margin: 30px 0;">
        <div style="text-align: left; color: #2d3436;">
            <p><b>Для кого:</b> Любимому папе</p>
            <p><b>От кого:</b> {NAME}</p>
            <p><b>Дата:</b> {now}</p>
            <p><b>Место:</b> Кайраккум</p>
        </div>
        <p class="info-text">Сделано с любовью на Python специально для тебя ❤️</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("ПОЛУЧИТЬ ЕЩЕ ОДНО ПОЖЕЛАНИЕ ✨"):
        st.session_state.msg = random.choice(wishes)
        st.rerun()
