import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="С Днем Рождения, Папа!", page_icon="❤️", layout="centered")

# CSS для центрирования и красоты
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;700&display=swap');

    /* Выравнивание всего контента по центру экрана */
    .main {
        display: flex;
        justify-content: center;
        align-items: center;
    }

    /* Магия центрирования через блок stApp */
    [data-testid="stAppViewContainer"] > .main {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        height: 100vh; /* Занимает всю высоту окна */
    }

    .stApp {
        background: linear-gradient(135deg, #fff5f5 0%, #f0f4ff 100%);
    }

    /* Заголовок */
    .main-title {
        font-family: 'Pacifico', cursive;
        color: #ff6b6b !important;
        font-size: 3.5rem !important;
        text-align: center;
        margin-bottom: 5px !important;
    }

    .sub-text {
        font-family: 'Roboto', sans-serif;
        color: #7f8c8d;
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Кнопка-конверт */
    div.stButton > button {
        background-color: white !important;
        border: 3px dashed #ffadad !important;
        border-radius: 25px !important;
        padding: 60px 40px !important;
        width: 320px !important; /* Фиксированная ширина для формы конверта */
        height: 220px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.15) !important;
        font-size: 1.1rem !important;
        color: #ff6b6b !important;
        font-weight: bold !important;
    }

    div.stButton > button:hover {
        transform: translateY(-10px) !important;
        box-shadow: 0 15px 45px rgba(255, 107, 107, 0.3) !important;
        border-style: solid !important;
    }

    /* Карточка поздравления */
    .wish-card {
        background: white;
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.1);
        max-width: 500px;
        text-align: left;
    }

    .wish-text {
        font-family: 'Roboto', sans-serif;
        font-size: 1.3rem;
        color: #2c3e50;
        line-height: 1.6;
        background: #fffafa;
        padding: 20px;
        border-radius: 15px;
        border-left: 6px solid #ff6b6b;
    }

    header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if 'opened' not in st.session_state:
    st.session_state.opened = False

# Центрирующий контейнер
st.markdown('<div class="main-container">', unsafe_allow_html=True)

if not st.session_state.opened:
    # Тексты над кнопкой
    st.markdown('<h1 class="main-title">С Днём Рождения, Папа!</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Нажми на конверт, чтобы открыть</p>', unsafe_allow_html=True)
    
    # Кнопка ровно по центру
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("📩\n\nОТКРЫТЬ"):
            st.session_state.opened = True
            st.rerun()

else:
    st.balloons()
    
    wishes = [
        "Дорогой папа, поздравляю тебя с днем рождения! Желаю тебе самого крепкого здоровья, долгих лет жизни и чтобы каждый день приносил только радость. Ты — лучший пример для меня!",
        "С днем рождения, папа! Пусть твоя жизнь будет наполнена светом и теплом. Желаю удачи во всех делах, бодрости духа и отличного настроения!",
        "Папа, спасибо тебе за твою мудрость и поддержку. Желаю тебе финансового благополучия, душевного спокойствия и чтобы все твои мечты обязательно сбывались!",
        "Самый лучший папа, с твоим днем! Желаю тебе побольше поводов для улыбок, приятных сюрпризов от жизни и верных друзей рядом. С праздником!"
    ]

    if 'current_wish' not in st.session_state:
        st.session_state.current_wish = random.choice(wishes)

    now = datetime.datetime.now().strftime("%d.%m.%Y")

    st.markdown(f"""
    <div class="wish-card">
        <h1 style="font-family: 'Pacifico'; color: #ff6b6b; text-align: center;">Для тебя! ❤️</h1>
        <div class="wish-text">
            {st.session_state.current_wish}
        </div>
        <div style="margin-top: 30px; font-family: 'Roboto'; border-top: 1px solid #eee; padding-top: 20px; color: #7f8c8d;">
            <p><b>От кого:</b> {NAME}</p>
            <p><b>Дата:</b> {now}</p>
            <p><b>Место:</b> Кайраккум</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("✨ ДРУГОЕ ПОЖЕЛАНИЕ"):
        st.session_state.current_wish = random.choice(wishes)
        st.rerun()

st.markdown('</div>', unsafe_allow_html=True)
