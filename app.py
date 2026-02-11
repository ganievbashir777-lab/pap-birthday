import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="С Днем Рождения, Папа!", page_icon="💌", layout="centered")

# CSS для праздничного оформления
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@300;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #fceeb5 0%, #f9dede 100%);
    }

    /* Стиль открытки на первом экране */
    .envelope {
        background: #ffffff;
        padding: 60px 40px;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        text-align: center;
        border: 4px double #ffadad;
        cursor: pointer;
        transition: transform 0.3s ease;
        margin-top: 50px;
    }

    .envelope:hover {
        transform: scale(1.02);
    }

    .main-title {
        font-family: 'Pacifico', cursive;
        color: #ff6b6b;
        font-size: 3.5rem;
        margin-bottom: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.05);
    }

    /* Стиль финальной карточки */
    .wish-card {
        background: white;
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
        border: none;
        margin-top: 30px;
    }

    .wish-text {
        font-family: 'Roboto', sans-serif;
        font-size: 1.4rem;
        color: #444;
        line-height: 1.6;
        padding: 20px;
        border-left: 5px solid #ffadad;
        background: #fffafa;
        border-radius: 10px;
    }

    .stButton>button {
        background: #ff6b6b !important;
        color: white !important;
        border: none !important;
        padding: 12px 25px !important;
        border-radius: 25px !important;
        font-size: 18px !important;
        width: 100%;
        margin-top: 20px;
    }

    header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if 'opened' not in st.session_state:
    st.session_state.opened = False

# --- ЭТАП 1: ЗАКРЫТАЯ ОТКРЫТКА ---
if not st.session_state.opened:
    st.markdown(f"""
    <div class="envelope">
        <div style="font-size: 80px;">✉️</div>
        <h1 class="main-title">С Днём Рождения, Папа!</h1>
        <p style="color: #888; font-family: 'Roboto'; font-size: 1.1rem;">
            Тебе пришло персональное поздравление.<br>Нажми на кнопку ниже, чтобы открыть его.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("ОТКРЫТЬ ОТКРЫТКУ 🔓"):
        with st.spinner('Открываем...'):
            time.sleep(1)
            st.session_state.opened = True
            st.rerun()

# --- ЭТАП 2: РАСКРЫТАЯ ОТКРЫТКА ---
else:
    # Праздничные эффекты
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
        <h1 style="font-family: 'Pacifico'; color: #ff6b6b; text-align: center;">Для тебя, папа! ❤️</h1>
        <div class="wish-text">
            {st.session_state.current_wish}
        </div>
        <div style="margin-top: 30px; font-family: 'Roboto'; border-top: 1px solid #eee; pt-3">
            <p style="margin-top: 15px;"><b>От кого:</b> {NAME}</p>
            <p><b>Дата:</b> {now}</p>
            <p><b>Место:</b> Кайраккум</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ПРОЧИТАТЬ ДРУГОЕ ПОЖЕЛАНИЕ ✨"):
        st.session_state.current_wish = random.choice(wishes)
        st.rerun()
