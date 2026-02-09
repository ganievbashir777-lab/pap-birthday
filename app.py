import streamlit as st
import time
import datetime
import random

# --- ВПИШИ СВОЕ ИМЯ ЗДЕСЬ ---
NAME = "Алишер" # Замени Алишер на свое имя
# ---------------------------

# Настройка страницы
st.set_page_config(page_title="PAPA_OS: Security Login", page_icon="🔐", layout="centered")

# Дизайн терминала
st.markdown("""
<style>
    .stApp { background-color: #050505; }
    .terminal-text {
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 8px #00ff41;
    }
    .stButton>button {
        color: #00ff41 !important;
        border: 2px solid #00ff41 !important;
        background-color: transparent !important;
        box-shadow: 0 0 10px #00ff41;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00ff41 !important;
        color: black !important;
        box-shadow: 0 0 30px #00ff41;
    }
    .wish-card {
        border: 2px solid #00ff41;
        padding: 25px;
        border-radius: 15px;
        background: linear-gradient(145deg, #0a0a0a, #111111);
        box-shadow: 0 0 25px rgba(0, 255, 65, 0.3);
    }
</style>
""", unsafe_allow_html=True)

# Список длинных поздравлений
random_wishes = [
    "Дорогой папа, желаю тебе крепкого и несокрушимого здоровья! Пусть энергии хватает на все идеи, а каждый день начинается с бодрости. Ты для нас — пример силы!",
    "Желаю большого успеха в делах! Пусть любая работа спорится, а трудности отступают перед твоим опытом и мудростью. Благополучия и стабильности тебе!",
    "Пусть наш дом всегда будет для тебя местом силы и уюта. Мы тебя очень любим и всегда поддержим. Желаю тебе душевного спокойствия и побольше отдыха!",
    "Желаю только добрых новостей! Пусть рядом всегда будут верные друзья, а жизнь наполняется приятными сюрпризами. Гордимся тобой!",
    "С днем рождения, лучший отец! Желаю сохранять твою крутую выдержку и уверенность. Пусть каждый год приносит новые цели и силы для их достижения!"
]

if 'stage' not in st.session_state:
    st.session_state.stage = 'security_1'

# --- ШАГ 1: ВОПРОС ПРО ИМЯ СЫНА ---
if st.session_state.stage == 'security_1':
    st.markdown("<h2 class='terminal-text'>[SECURITY LEVEL 1]</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown(f"<p class='terminal-text'>ВВЕДИТЕ ИМЯ СЫНА ДЛЯ ПОДТВЕРЖДЕНИЯ ДОСТУПА:</p>", unsafe_allow_html=True)
    ans1 = st.text_input("Username:", key="name_input")
    
    if st.button("LOGIN"):
        # Проверяем имя (переводим в нижний регистр, чтобы не было ошибки из-за больших букв)
        if ans1.lower().strip() == NAME.lower().strip():
            st.success("ЛИЧНОСТЬ АВТОРА ПОДТВЕРЖДЕНА...")
            time.sleep(1)
            st.session_state.stage = 'security_2'
            st.rerun()
        else:
            st.error("ОШИБКА: НЕВЕРНОЕ ИМЯ ПОЛЬЗОВАТЕЛЯ.")

# --- ШАГ 2: ВОПРОС ПРО СТАТУС ---
elif st.session_state.stage == 'security_2':
    st.markdown("<h2 class='terminal-text'>[SECURITY LEVEL 2]</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='terminal-text'>ПОДТВЕРДИТЕ ВАШ СТАТУС В ЭТОЙ СИСТЕМЕ:</p>", unsafe_allow_html=True)
    ans2 = st.radio("", ["Посторонний", "Гость", "ЛУЧШИЙ ОТЕЦ В МИРЕ"])
    
    if st.button("CONFIRM"):
        if ans2 == "ЛУЧШИЙ ОТЕЦ В МИРЕ":
            st.success("ДОСТУП ПОЛНОСТЬЮ РАЗРЕШЕН.")
            time.sleep(1)
            st.session_state.stage = 'mood'
            st.rerun()
        else:
            st.warning("ДОСТУП ЗАБЛОКИРОВАН. ВЫБЕРИТЕ ВЕРНЫЙ СТАТУС.")

# --- ШАГ 3: КАЛИБРОВКА СЧАСТЬЯ ---
elif st.session_state.stage == 'mood':
    st.markdown("<h2 class='terminal-text'>[SYSTEM CALIBRATION]</h2>", unsafe_allow_html=True)
    st.write("Настройте уровень праздничного настроения (0-100%):")
    happiness = st.slider("", 0, 100, 100)
    
    if st.button("РАСШИФРОВАТЬ ПОЗДРАВЛЕНИЕ"):
        if happiness > 50:
            st.balloons()
        st.session_state.stage = 'final'
        st.rerun()

# --- ШАГ 4: ФИНАЛ ---
elif st.session_state.stage == 'final':
    st.snow()
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>🎉 ACCESS GRANTED 🎉</h1>", unsafe_allow_html=True)
    
    tz = datetime.timezone(datetime.timedelta(hours=5))
    date_str = datetime.datetime.now(tz).strftime("%d.%m.%Y")
    
    if 'display_wish' not in st.session_state:
        st.session_state.display_wish = random.choice(random_wishes)

    st.markdown(f"""
    <div class="wish-card">
        <h2 style="color:#00ff41; text-align:center; font-family: Courier New;">ОТЧЕТ: ДЕНЬ РОЖДЕНИЯ</h2>
        <p style="color:#00ff41; font-family:Courier New; font-size: 16px;">
        <b>ПОЛУЧАТЕЛЬ:</b> ПАПА <br>
        <b>ГОРОД:</b> КАЙРАККУМ <br>
        <b>ДАТА:</b> {date_str} <br>
        -------------------------------------------<br>
        <b>ПОЗДРАВЛЕНИЕ:</b><br>
        {st.session_state.display_wish}<br>
        -------------------------------------------<br><br>
        <b>АВТОР КОДА:</b> {NAME} <br>
        <i>Сделано с любовью на Python специально для тебя!</i>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ЕЩЕ ОДНО ПОЖЕЛАНИЕ"):
        st.session_state.display_wish = random.choice(random_wishes)
        st.rerun()
