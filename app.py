import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="PAPA_OS: Hack Edition", page_icon="📟", layout="centered")

# Функция создания матрицы (фон)
def get_matrix_bg():
    cols = 50
    svg_txt = ""
    celebration_elements = ["0", "1", "🎂", "🎁", "🎉", "🔥"]
    for i in range(cols):
        x = i * (100 / cols)
        dur = random.uniform(3, 7)
        dly = random.uniform(0, 5)
        chars = "".join(random.choice(celebration_elements) for _ in range(15))
        svg_txt += f"""
        <text x="{x}%" y="-10%" fill="%2300ff41" font-family="monospace" font-size="25" opacity="0.3" style="writing-mode: tb; glyph-orientation-vertical: 0;">
            {chars}
            <animate attributeName="y" from="-50%" to="110%" dur="{dur}s" begin="-{dly}s" repeatCount="indefinite" />
        </text>
        """
    svg = f'<svg width="100%" height="100%" xmlns="http://www.w3.org/2000/svg">{svg_txt}</svg>'
    return svg.replace('"', "'").replace("\n", "")

matrix_data = get_matrix_bg()

# CSS для хакерского стиля и кнопок
st.markdown(f"""
<style>
    .stApp {{
        background-color: #000000;
        background-image: url("data:image/svg+xml;utf8,{matrix_data}");
        background-size: cover;
    }}

    /* Центрирование */
    [data-testid="stVerticalBlock"] {{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 85vh;
    }}

    /* Карточки */
    .wish-card, .login-card {{
        position: relative;
        z-index: 100;
        border: 2px solid #00ff41;
        padding: 40px;
        border-radius: 20px;
        background-color: rgba(0, 0, 0, 0.9);
        box-shadow: 0 0 40px rgba(0, 255, 65, 0.3);
        max-width: 550px;
        width: 100%;
    }}

    .terminal-text {{
        color: #00ff41;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 10px #00ff41;
    }}

    /* СТИЛЬ КНОПОК (Хакерский неон) */
    .stButton > button {{
        background-color: transparent !important;
        border: 2px solid #00ff41 !important;
        border-radius: 10px !important;
        padding: 15px 30px !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 0 15px rgba(0, 255, 65, 0.2) !important;
    }}

    .stButton > button p {{
        color: #00ff41 !important;
        font-family: 'Courier New', monospace !important;
        font-weight: bold !important;
        font-size: 1.1rem !important;
    }}

    .stButton > button:hover {{
        background-color: #00ff41 !important;
        box-shadow: 0 0 40px #00ff41 !important;
        transform: scale(1.05) !important;
    }}

    .stButton > button:hover p {{
        color: black !important;
    }}

    /* Выравнивание нижней кнопки влево */
    .left-btn {{
        display: flex;
        justify-content: flex-start;
        width: 100%;
        max-width: 550px;
        margin-top: 20px;
    }}

    header, footer {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

if 'step' not in st.session_state:
    st.session_state.step = 'start'

# --- ЭТАП 1: КНОПКА ВХОДА (ОТКРЫТКА) ---
if st.session_state.step == 'start':
    st.markdown("""
    <div class="login-card">
        <h1 class="terminal-text" style="text-align:center;">СИСТЕМА ЗАБЛОКИРОВАНА</h1>
        <p class="terminal-text" style="font-size: 1.1em; text-align:center;">Обнаружен праздничный протокол для:</p>
        <h2 class="terminal-text" style="font-size: 2em; text-align:center;">ЛУЧШЕГО ПАПЫ</h2>
        <p class="terminal-text" style="text-align:center; margin-top:20px; opacity:0.7;">[ Требуется авторизация ]</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("🔓 ДЕШИФРОВАТЬ ПИСЬМО"):
        st.session_state.step = 'loading'
        st.rerun()

# --- ЭТАП 2: ЗАГРУЗКА ---
elif st.session_state.step == 'loading':
    st.markdown("<div class='login-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='terminal-text' style='text-align:center;'>ВЗЛОМ ЗАЩИТЫ...</h2>", unsafe_allow_html=True)
    bar = st.progress(0)
    status = st.empty()
    logs = ["Bypassing firewalls...", "Loading cake.dll...", "Decrypting wishes...", "ACCESS GRANTED!"]
    for i, log in enumerate(logs):
        status.markdown(f"<p class='terminal-text'>[SYS]: {log}</p>", unsafe_allow_html=True)
        bar.progress((i + 1) * 25)
        time.sleep(0.6)
    st.session_state.step = 'final'
    st.rerun()

# --- ЭТАП 3: ФИНАЛ ---
elif st.session_state.step == 'final':
    # Вместо шариков оставляем снег (как частицы кода)
    st.snow() 
    
    wishes = [
        "Дорогой папа, поздравляю тебя! Желаю стального здоровья и чтобы твоя личная система всегда работала без багов. Ты — лучший пример силы и мудрости!",
        "С днем рождения! Пусть каждый твой день в Кайраккуме будет наполнен радостью. Желаю удачи во всех делах и бесконечного запаса энергии!",
        "Папа, спасибо за поддержку. Желаю тебе финансового благополучия, спокойствия и чтобы все твои мечты исполнялись мгновенно!",
        "Самый крутой папа, с праздником! Пусть этот год принесет только радостные события и много поводов для улыбки. Мы тебя любим!"
    ]

    if 'msg' not in st.session_state:
        st.session_state.msg = random.choice(wishes)

    now = datetime.datetime.now().strftime("%d.%m.%Y")

    st.markdown(f"""
    <div class="wish-card">
        <div class="terminal-text">
            <p style="font-size: 1.4em; text-align: center; border-bottom: 1px solid #00ff41; padding-bottom: 10px;">📊 ОТЧЕТ: BIRTHDAY_2026 📊</p>
            <p style="margin-top:15px;"><b>ОБЪЕКТ:</b> ЛЮБИМЫЙ ПАПА</p>
            <p><b>ЛОКАЦИЯ:</b> КАЙРАККУМ</p>
            <p><b>СТАТУС:</b> САМЫЙ КРУТОЙ</p>
            <p><b>ДАТА:</b> {now}</p>
            <p style="border-top: 1px dashed #00ff41; margin-top:15px; padding-top:15px; font-size: 1.2em; line-height: 1.5;">
                {st.session_state.msg}
            </p>
            <p style="border-top: 1px dashed #00ff41; margin-top:15px; padding-top:15px; opacity:0.8;"><b>ОТ КОГО:</b> {NAME}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Кнопка слева
    st.markdown('<div class="left-btn">', unsafe_allow_html=True)
    if st.button("🔄 ДРУГОЙ ЛОГ"):
        st.session_state.msg = random.choice(wishes)
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
