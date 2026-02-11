import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твоего сына" 
# ---------------------------

st.set_page_config(page_title="С Днем Рождения, Папа!", page_icon="❤️", layout="centered")

# CSS для анимации и стилизации
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Roboto:wght@300;700&display=swap');

    .stApp {
        background: linear-gradient(135deg, #fff5f5 0%, #f0f4ff 100%);
    }

    /* Стиль конверта-кнопки */
    .envelope-btn {
        background: #ffffff;
        padding: 50px 20px;
        border-radius: 25px;
        box-shadow: 0 15px 45px rgba(255, 107, 107, 0.2);
        text-align: center;
        border: 3px dashed #ffadad;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        cursor: pointer;
        margin: 50px auto;
        max-width: 500px;
    }

    .envelope-btn:hover {
        transform: translateY(-10px) scale(1.03);
        box-shadow: 0 25px 50px rgba(255, 107, 107, 0.3);
        border-style: solid;
        background: #fffafa;
    }

    .main-title {
        font-family: 'Pacifico', cursive;
        color: #ff6b6b;
        font-size: 3rem;
        margin: 20px 0;
    }

    .instruction {
        font-family: 'Roboto', sans-serif;
        color: #aaa;
        font-size: 1rem;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* Финальная карточка */
    .wish-card {
        background: white;
        padding: 40px;
        border-radius: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.08);
        border: none;
        animation: fadeIn 1s ease-in;
    }

    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .wish-text {
        font-family: 'Roboto', sans-serif;
        font-size: 1.4rem;
        color: #444;
        line-height: 1.6;
        padding: 25px;
        background: #fff9f9;
        border-radius: 15px;
        border-left: 6px solid #ff6b6b;
    }

    /* Скрываем стандартную кнопку Streamlit, делая её прозрачной поверх конверта */
    .stButton>button {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0;
        z-index: 10;
        cursor: pointer;
    }

    .button-container {
        position: relative;
        width: 100%;
        display: flex;
        justify-content: center;
    }

    header, footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

if 'opened' not in st.session_state:
    st.session_state.opened = False

# --- ЭТАП 1: КОНВЕРТ (КНОПКА) ---
if not st.session_state.opened:
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Обертка, которая превращает всё внутри в визуальный конверт
    st.markdown("""
    <div class="button-container">
        <div class="envelope-btn">
            <div style="font-size: 100px; margin-bottom: 10px;">📩</div>
            <h1 class="main-title">С Днём Рождения, Папа!</h1>
            <p class="instruction">Нажми на конверт, чтобы открыть</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Невидимая кнопка поверх всего контейнера
    if st.button("Открыть"):
        st.session_state.opened = True
        st.rerun()

# --- ЭТАП 2: ОТКРЫТОЕ ПОЗДРАВЛЕНИЕ ---
else:
    # Выстрел конфетти и шаров с двух сторон
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
        <h1 style="font-family: 'Pacifico'; color: #ff6b6b; text-align: center; font-size: 3rem;">Для тебя! ❤️</h1>
        <div class="wish-text">
            {st.session_state.current_wish}
        </div>
        <div style="margin-top: 30px; font-family: 'Roboto'; border-top: 1px solid #eee; padding-top: 20px;">
            <p><b>От кого:</b> {NAME}</p>
            <p><b>Дата:</b> {now}</p>
            <p><b>Место:</b> Кайраккум</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Кнопка для смены пожелания (уже обычная, внизу)
    if st.button("Прочитать другое пожелание ✨"):
        st.session_state.current_wish = random.choice(wishes)
        st.rerun()
