import streamlit as st
import time
import datetime
import random

# Настройка страницы
st.set_page_config(page_title="PAPA_OS ULTRA", page_icon="👑", layout="centered")

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
        font-family: 'Courier New', Courier, monospace;
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

# Список поздравлений
random_wishes = [
    "Дорогой папа, желаю тебе прежде всего крепкого и несокрушимого здоровья! Пусть энергии хватает на все твои идеи, а каждый день начинается с бодрости. Ты для нас — пример силы!",
    "Желаю большого успеха в делах! Пусть любая работа спорится, а трудности отступают перед твоим опытом и мудростью. Финансового благополучия и стабильности тебе!",
    "Пусть наш дом всегда будет для тебя местом силы и уюта. Мы тебя очень любим и всегда поддержим. Желаю тебе душевного спокойствия и побольше времени на отдых!",
    "Желаю только добрых новостей! Пусть рядом всегда будут верные друзья, а жизнь наполняется приятными сюрпризами. Мы очень гордимся тобой и твоими успехами!",
    "С днем рождения, лучший отец! Желаю сохранять твою крутую выдержку и уверенность. Пусть каждый год приносит новые интересные цели и силы для их достижения!"
]

if 'stage' not in st.session_state:
    st.session_state.stage = 'security'

# --- ШАГ 1: ПРОВЕРКА ЛИЧНОСТИ ---
if st.session_state.stage == 'security':
    st.markdown("<h2 class='terminal-text'>[SECURITY CHECK]</h2>", unsafe_allow_html=True)
    st.write("---")
    st.markdown("<p class='terminal-text'>СИСТЕМА ТРЕБУЕТ ПОДТВЕРЖДЕНИЯ:</p>", unsafe_allow_html=True)
    answer = st.radio("КТО ЯВЛЯЕТСЯ ЛУЧШИМ ОТЦОМ В МИРЕ?", ["Не знаю", "Кто-то другой", "МОЙ ПАПА"])
    
    if st.button("ПОДТВЕРДИТЬ ДОСТУП"):
        if answer == "МОЙ ПАПА":
            st.success("ЛИЧНОСТЬ ПОДТВЕРЖДЕНА. ДОСТУП РАЗРЕШЕН.")
            time.sleep(1)
            st.session_state.stage = 'mood'
            st.rerun()
        else:
            st.error("ОШИБКА: НЕВЕРНЫЙ ВЫБОР. ПОПРОБУЙТЕ СНОВА.")

# --- ШАГ 2: НАСТРОЙКА ПАРАМЕТРОВ ---
elif st.session_state.stage == 'mood':
    st.markdown("<h2 class='terminal-text'>[SYSTEM CALIBRATION]</h2>", unsafe_allow_html=True)
    st.write("Папа, настрой уровень счастья на сегодня (в процентах):")
    happiness = st.slider("", 0, 100, 80)
    
    if st.button("ЗАПУСТИТЬ ПРОГРАММУ ПОЗДРАВЛЕНИЯ"):
        if happiness > 90:
            st.balloons() # Шарики, если папа очень счастлив
        st.session_state.stage = 'loading'
        st.rerun()

# --- ШАГ 3: ЗАГРУЗКА ---
elif st.session_state.stage == 'loading':
    st.markdown("<p class='terminal-text'>[INIT]: Расшифровка секретных данных...</p>", unsafe_allow_html=True)
    bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        bar.progress(i+1)
    st.session_state.stage = 'final'
    st.rerun()

# --- ШАГ 4: ФИНАЛ ---
elif st.session_state.stage == 'final':
    st.snow() # Эффект «падающих звезд»
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>🎉 ACCESS GRANTED 🎉</h1>", unsafe_allow_html=True)
    
    tz = datetime.timezone(datetime.timedelta(hours=5))
    date_str = datetime.datetime.now(tz).strftime("%d.%m.%Y")
    
    # Выбираем случайное поздравление
    if 'display_wish' not in st.session_state:
        st.session_state.display_wish = random.choice(random_wishes)

    st.markdown(f"""
    <div class="wish-card">
        <h2 style="color:#00ff41; text-align:center; font-family: Courier New;">ОТЧЕТ: С ДНЕМ РОЖДЕНИЯ!</h2>
        <p style="color:#00ff41; font-family:Courier New; font-size: 16px;">
        <b>ОБЪЕКТ:</b> ЛУЧШИЙ ПАПА <br>
        <b>ЛОКАЦИЯ:</b> КАЙРАККУМ <br>
        <b>ДАТА:</b> {date_str} <br>
        -------------------------------------------<br>
        <b>СООБЩЕНИЕ:</b><br>
        {st.session_state.display_wish}<br>
        -------------------------------------------<br><br>
        <b>ОТ КОГО:</b> Твой сын. <br>
        <i>Я написал этот код специально для тебя!</i>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("ПОЛУЧИТЬ ДРУГОЕ ПОЗДРАВЛЕНИЕ"):
        st.session_state.display_wish = random.choice(random_wishes)
        st.session_state.stage = 'loading'
        st.rerun()
