import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="С Днем Рождения, Папа!", page_icon="❤️", layout="centered")

# CSS для исправления видимости и работы кнопки
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;700&display=swap');

    /* Мягкий праздничный фон */
    .stApp {
        background: linear-gradient(135deg, #fff5f5 0%, #f0f4ff 100%);
    }

    /* Контейнер для центрирования */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 20px;
    }

    /* Заголовок (теперь темный и четкий) */
    .main-title {
        font-family: 'Pacifico', cursive;
        color: #ff6b6b !important;
        font-size: 3.5rem !important;
        margin-bottom: 10px !important;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }

    .sub-text {
        font-family: 'Roboto', sans-serif;
        color: #7f8c8d;
        font-size: 1.2rem;
        margin-bottom: 30px;
    }

    /* Стилизация КНОПКИ под конверт */
    div.stButton > button {
        background-color: white !important;
        border: 3px dashed #ffadad !important;
        border-radius: 25px !important;
        padding: 60px 40px !important;
        width: 100% !important;
        max-width: 450px;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.15) !important;
    }

    div.stButton > button:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 15px 40px rgba(255, 107, 107, 0.3) !important;
        border-style: solid !important;
        background-color: #fffafa !important;
    }

    /* Внутренний текст кнопки (эмодзи и подпись) */
    .envelope-content {
        pointer-events: none; /* Чтобы клик пролетал сквозь текст на кнопку */
    }

    /* Карточка поздравления */
    .wish-card {
        background: white;
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        text-align: left;
        border: none;
    }

    .wish-text {
        font-family: 'Roboto', sans-serif;
        font-size: 1.4rem;
        color: #2c3e50;
        line-height: 1.6;
        background: #fff9f9;
        padding: 20px;
        border-left: 6px solid #ff6b6b;
        border-radius: 10px;
    }

    header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if 'opened' not in st.session_state:
    st.session_state.opened = False

# --- ЭТАП 1: ГЛАВНЫЙ ЭКРАН С КОНВЕРТОМ ---
if not st.session_state.opened:
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.markdown('<h1 class="main-title">С Днём Рождения, Папа!</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Тебе пришло личное сообщение</p>', unsafe_allow_html=True)
    
    # Кнопка-конверт
    # Используем HTML внутри кнопки для отображения эмодзи
    if st.button("📩\n\nНАЖМИ, ЧТОБЫ ОТКРЫТЬ"):
        st.session_state.opened = True
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# --- ЭТАП 2: ОТКРЫТАЯ ОТКРЫТКА ---
else:
    # Эффект вылетающих шаров (Streamlit запускает их с боков и снизу)
    st.balloons()
    
    wishes = [
        "Дорогой папа, поздравляю тебя с днем рождения! Желаю тебе самого крепкого здоровья, долгих лет жизни и чтобы каждый день приносил только радость. Ты — лучший пример для меня!",
        "С днем рождения, папа! Пусть твоя жизнь будет наполнена светом и теплом. Желаю удачи во всех делах, бодрости духа и отличного настроения в нашем любимом Кайраккуме!",
        "Папа, спасибо тебе за твою мудрость и поддержку. Желаю тебе финансового благополучия, душевного спокойствия и чтобы все твои мечты обязательно сбывались!",
        "Поздравляю! Желаю тебе всегда оставаться таким же сильным и добрым. Пусть здоровье никогда не подводит, а дом всегда будет полной чашей. Мы тебя любим!",
        "Самый лучший папа, с твоим днем! Желаю тебе побольше поводов для улыбок, приятных сюрпризов от жизни и верных друзей рядом. С праздником!"
    ]

    if 'current_wish' not in st.session_state:
        st.session_state.current_wish = random.choice(wishes)

    now = datetime.datetime.now().strftime("%d.%m.%Y")

    st.markdown(f"""
    <div class="wish-card">
        <h1 style="font-family: 'Pacifico'; color: #ff6b6b; text-align: center; font-size: 2.5rem;">Для тебя! ❤️</h1>
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
    if st.button("✨ ПРОЧИТАТЬ ДРУГОЕ ПОЖЕЛАНИЕ"):
        st.session_state.current_wish = random.choice(wishes)
        st.rerun()
