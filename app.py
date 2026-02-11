import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="С Днем Рождения, Папа!", page_icon="❤️", layout="centered")

# ПОЛНЫЙ CSS: Кнопки, Центрирование и Тексты
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@400;700&display=swap');

    /* Фон всей страницы */
    .stApp {
        background: linear-gradient(135deg, #fff5f5 0%, #f0f4ff 100%);
    }

    /* Центрируем всё содержимое */
    [data-testid="stAppViewContainer"] > .main {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        min-height: 100vh;
    }

    /* ЕДИНЫЙ СТИЛЬ ДЛЯ ВСЕХ КНОПОК (как конверт на 1-м скрине) */
    div.stButton > button {
        background-color: white !important;
        border: 3px dashed #ffadad !important;
        border-radius: 25px !important;
        padding: 40px 20px !important;
        width: 100% !important;
        max-width: 400px !important;
        min-height: 150px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 10px 30px rgba(255, 107, 107, 0.15) !important;
        color: #ff6b6b !important;
        font-family: 'Roboto', sans-serif !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        margin: 20px auto !important;
        display: block !important;
    }

    div.stButton > button:hover {
        transform: translateY(-5px) !important;
        box-shadow: 0 15px 45px rgba(255, 107, 107, 0.3) !important;
        border-style: solid !important;
        background-color: #fffafa !important;
    }

    /* Заголовки */
    .main-title {
        font-family: 'Pacifico', cursive;
        color: #ff6b6b;
        font-size: 3rem;
        text-align: center;
        margin-bottom: 0px;
    }

    .sub-text {
        font-family: 'Roboto', sans-serif;
        color: #7f8c8d;
        font-size: 1.1rem;
        text-align: center;
    }

    /* Карточка поздравления */
    .wish-card {
        background: white;
        padding: 30px;
        border-radius: 30px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.08);
        max-width: 500px;
        width: 100%;
        text-align: left;
        margin-bottom: 20px;
    }

    .wish-header {
        font-family: 'Pacifico', cursive;
        color: #ff6b6b;
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 15px;
    }

    .wish-text {
        font-family: 'Roboto', sans-serif;
        font-size: 1.3rem;
        color: #2c3e50;
        line-height: 1.5;
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

# --- ЛОГИКА ЭКРАНОВ ---

if not st.session_state.opened:
    # ЭКРАН 1: ЗАКРЫТЫЙ КОНВЕРТ
    st.markdown('<h1 class="main-title">С Днём Рождения, Папа!</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-text">Нажми на конверт, чтобы открыть</p>', unsafe_allow_html=True)
    
    # Кнопка-конверт
    if st.button("📩\n\nОТКРЫТЬ ПИСЬМО"):
        st.session_state.opened = True
        st.rerun()

else:
    # ЭКРАН 2: ОТКРЫТОЕ ПОЗДРАВЛЕНИЕ
    # Эффекты праздника (двойной выстрел)
    st.balloons() # Шары
    st.snow()     # Конфетти (снежинки/частицы)
    
    wishes = [
        "Дорогой папа, поздравляю тебя с днем рождения! Желаю тебе самого крепкого здоровья, долгих лет жизни и чтобы каждый день приносил только радость. Ты — лучший пример для меня!",
        "С днем рождения, папа! Пусть твоя жизнь будет наполнена светом и теплом. Желаю удачи во всех делах, бодрости духа и отличного настроения!",
        "Папа, спасибо тебе за твою мудрость и поддержку. Желаю тебе финансового благополучия, душевного спокойствия и чтобы все твои мечты обязательно сбывались!",
        "Самый лучший папа, с твоим днем! Желаю тебе побольше поводов для улыбок, приятных сюрпризов от жизни и верных друзей рядом. С праздником!"
    ]

    if 'current_wish' not in st.session_state:
        st.session_state.current_wish = random.choice(wishes)

    now = datetime.datetime.now().strftime("%d.%m.%Y")

    # Сама карточка
    st.markdown(f"""
    <div class="wish-card">
        <div class="wish-header">Для тебя! ❤️</div>
        <div class="wish-text">
            {st.session_state.current_wish}
        </div>
        <div style="margin-top: 20px; font-family: 'Roboto'; border-top: 1px solid #eee; padding-top: 15px; color: #7f8c8d; font-size: 0.9rem;">
            <p><b>От кого:</b> {NAME}</p>
            <p><b>Дата:</b> {now}</p>
            <p><b>Место:</b> Кайраккум</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Кнопка "Другое пожелание" — теперь она выглядит ТОЧНО ТАК ЖЕ, как конверт
    if st.button("✨ ДРУГОЕ ПОЖЕЛАНИЕ"):
        st.session_state.current_wish = random.choice(wishes)
        st.rerun()
