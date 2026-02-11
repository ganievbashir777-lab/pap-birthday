import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Твое Имя" 
# ---------------------------

st.set_page_config(page_title="PAPA_OS: Party Edition", page_icon="🎂", layout="centered")

# Функция создания матрицы с добавлением тортов и подарков
def get_matrix_bg():
    cols = 50
    svg_txt = ""
    # Праздничные элементы, которые будут лететь в потоке
    celebration_elements = ["0", "1", "🎂", "🎁", "🎉", "🔥"]
    
    for i in range(cols):
        x = i * (100 / cols)
        dur = random.uniform(3, 7)
        dly = random.uniform(0, 5)
        # Смешиваем цифры и праздничные эмодзи
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

# CSS Стили с праздничными акцентами
st.markdown(f"""
<style>
    .stApp {{
        background-color: #000000;
        background-image: url("data:image/svg+xml;utf8,{matrix_data}");
        background-size: cover;
    }}
    .wish-card, .login-card {{
        position: relative;
        z-index: 100;
        border: 3px solid #00ff41;
        padding: 40px;
        border-radius: 20px;
        background-color: rgba(0, 0, 0, 0.92);
        box-shadow: 0 0 60px rgba(0, 255, 65, 0.5);
        margin-top: 80px;
        text-align: center;
    }}
    .terminal-text {{
        color: #00ff41;
        font-family: 'Courier New', monospace;
        text-shadow: 0 0 10px #00ff41;
    }}
    .birthday-header {{
        color: #ffffff;
        text-shadow: 0 0 20px #00ff41, 0 0 30px #00ff41;
        font-size: 2.5em;
        margin-bottom: 20px;
    }}
    .stButton>button {{
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        background-color: transparent !important;
        box-shadow: 0 0 15px #00ff41;
        padding: 10px 30px !important;
        font-size: 20px !important;
        font-weight: bold;
        border-radius: 10px;
    }}
    .stButton>button:hover {{
        background-color: #00ff41 !important;
        color: black !important;
        box-shadow: 0 0 50px #00ff41;
        transform: scale(1.05);
    }}
    header, footer {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

# Управление этапами
if 'step' not in st.session_state:
    st.session_state.step = 'start'

# --- ЭТАП 1: КНОПКА ВХОДА ---
if st.session_state.step == 'start':
    st.markdown("""
    <div class="login-card">
        <h1 class="terminal-text">СИСТЕМА ЗАБЛОКИРОВАНА</h1>
        <p class="terminal-text" style="font-size: 1.2em;">Обнаружен праздничный протокол для:</p>
        <h2 class="terminal-text" style="font-size: 2em;">ЛУЧШЕГО ПАПЫ</h2>
        <p class="terminal-text">Нажмите кнопку для дешифровки...</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("РАСПАКОВАТЬ ПОЗДРАВЛЕНИЕ"):
        st.session_state.step = 'loading'
        st.rerun()

# --- ЭТАП 2: ЗАГРУЗКА ---
elif st.session_state.step == 'loading':
    st.markdown("<div class='login-card'>", unsafe_allow_html=True)
    st.markdown("<h2 class='terminal-text'>ЗАГРУЗКА ПРАЗДНИКА...</h2>", unsafe_allow_html=True)
    bar = st.progress(0)
    status = st.empty()
    logs = [
        "Поиск тортов в базе данных...", 
        "Сборка конфетти-модуля...", 
        "Генерация искренних пожеланий...", 
        "ДОСТУП ОТКРЫТ!"
    ]
    
    for i, log in enumerate(logs):
        status.markdown(f"<p class='terminal-text'>[LOG]: {log}</p>", unsafe_allow_html=True)
        bar.progress((i + 1) * 25)
        time.sleep(0.7)
    
    st.session_state.step = 'final'
    st.rerun()

# --- ЭТАП 3: ФИНАЛ (КОНФЕТТИ И ТОРТ) ---
elif st.session_state.step == 'final':
    # ЭФФЕКТ КОНФЕТТИ
    st.balloons() 
    
    st.markdown("<h1 class='birthday-header' style='text-align:center;'>С ДНЕМ РОЖДЕНИЯ! 🎂</h1>", unsafe_allow_html=True)
    
    wishes = [
        "Дорогой папа, желаю тебе стального здоровья и бесконечного счастья! Пусть в твоей жизни всегда всё работает как часы, а каждый день в Кайраккуме будет наполнен радостью и теплом!",
        "Желаю тебе всегда оставаться таким же мудрым и сильным. Пусть твои планы всегда сбываются, а удача преследует тебя по пятам. Ты — наш герой!",
        "С праздником! Пусть этот год принесет тебе много новых побед, крепких нервов и побольше поводов для улыбки. Мы тебя очень сильно любим!",
        "Самый лучший папа на свете! Желаю тебе благополучия, энергии и чтобы сердце всегда было спокойно. Пусть в доме всегда будет уют и смех!",
        "Желаю тебе здоровья на сто лет вперед! Пусть каждый твой день будет ярким, как этот праздник. Спасибо за твою поддержку и любовь!"
    ]

    if 'msg' not in st.session_state:
        st.session_state.msg = random.choice(wishes)

    tz = datetime.timezone(datetime.timedelta(hours=5))
    now = datetime.datetime.now(tz).strftime("%d.%m.%Y")

    st.markdown(f"""
    <div class="wish-card">
        <div class="terminal-text" style="text-align: left;">
            <p style="font-size: 1.5em; text-align: center; color: #ffffff;">📊 ОТЧЕТ СИСТЕМЫ 📊</p>
            <p><b>ОБЪЕКТ:</b> ЛЮБИМЫЙ ПАПА</p>
            <p><b>ЛОКАЦИЯ:</b> КАЙРАККУМ</p>
            <p><b>СТАТУС:</b> САМЫЙ КРУТОЙ</p>
            <p><b>ДАТА:</b> {now}</p>
            <p>-------------------------------------------</p>
            <p style="font-size: 1.2em; line-height: 1.6; color: #ffffff; text-shadow: none;">{st.session_state.msg}</p>
            <p>-------------------------------------------</p>
            <p><b>АВТОР:</b> {NAME}</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("ПОЛУЧИТЬ ЕЩЕ ОДНО ПОЖЕЛАНИЕ 🎁"):
        st.session_state.msg = random.choice(wishes)
        st.rerun()
