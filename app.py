import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="С Днем Рождения, Папа!", page_icon="🎂", layout="centered")

# CSS для красивого праздничного оформления и центрирования
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;700&display=swap');

    /* Мягкий праздничный фон */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }

    /* Магия центрирования содержимого */
    [data-testid="stVerticalBlock"] {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 80vh;
    }

    /* Стиль основной белой карточки */
    .main-card {
        background-color: white;
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        text-align: left;
        max-width: 550px;
        width: 100%;
        border: none;
    }

    /* Заголовок внутри карточки */
    .card-title {
        font-family: 'Pacifico', cursive;
        color: #6a11cb;
        font-size: 2.8rem;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Текст пожелания */
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

    /* Та самая маленькая аккуратная кнопка */
    div.stButton > button {
        background: linear-gradient(to right, #6a11cb 0%, #2575fc 100%) !important;
        color: white !important;
        border: none !important;
        padding: 10px 25px !important;
        border-radius: 50px !important;
        font-weight: bold !important;
        font-size: 0.9rem !important;
        transition: all 0.3s ease !important;
        display: block !important;
        margin: 20px auto !important;
        width: auto !important;
    }

    div.stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 20px rgba(37, 117, 252, 0.3);
    }

    header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Эффекты праздника при загрузке страницы
st.balloons()

# Список пожеланий
wishes = [
    "Дорогой папа, поздравляю тебя с днем рождения! Желаю тебе самого крепкого здоровья, долгих лет жизни и чтобы каждый день приносил только радость. Ты — лучший пример для меня!",
    "С днем рождения, папа! Пусть твоя жизнь будет наполнена светом и теплом. Желаю удачи во всех делах, бодрости духа и отличного настроения!",
    "Папа, спасибо тебе за твою мудрость и поддержку. Желаю тебе финансового благополучия, душевного спокойствия и чтобы все твои мечты обязательно сбывались!",
    "Самый лучший папа, с праздником! Пусть этот год принесет тебе много радости и новых успехов. Мы тебя очень любим!",
    "Желаю здоровья на сто лет вперед, чтобы каждый день в Кайраккуме был солнечным и добрым. С днем рождения!"
]

# Хранение текущего сообщения
if 'msg' not in st.session_state:
    st.session_state.msg = random.choice(wishes)

now = datetime.datetime.now().strftime("%d.%m.%Y")

# Вывод основной карточки
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

# Кнопка обновления (маленькая и под карточкой)
if st.button("Прочитать другое пожелание ✨"):
    st.session_state.msg = random.choice(wishes)
    st.rerun()
