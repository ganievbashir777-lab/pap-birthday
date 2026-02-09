import streamlit as st
import time
import datetime
import random

# Настройка страницы
st.set_page_config(page_title="Для папы", page_icon="❤️", layout="centered")

# Дизайн терминала
st.markdown("""
<style>
    .stApp { background-color: #050505; }
    .terminal-text {
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
        text-shadow: 0 0 5px #00ff41;
        line-height: 1.6;
    }
    .stButton>button {
        color: #00ff41 !important;
        border: 1px solid #00ff41 !important;
        background-color: transparent !important;
        font-family: 'Courier New', Courier, monospace !important;
        width: 100%;
        border-radius: 0px;
    }
    .stButton>button:hover {
        background-color: #00ff41 !important;
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# Список длинных, человеческих поздравлений
random_wishes = [
    """Дорогой папа, от всей души желаю тебе прежде всего крепкого и несокрушимого здоровья. 
    Пусть каждый твой день начинается с бодрости и хорошего настроения, а энергии хватает на 
    все важные дела и любимые хобби. Ты для нас — пример силы, и я хочу, чтобы ты всегда 
    оставался таким же активным и жизнерадостным!""",
    
    """В этот особенный день хочу пожелать тебе большого успеха во всех твоих начинаниях. 
    Пусть любая работа спорится, а все трудности отступают перед твоим опытом и мудростью. 
    Я желаю тебе финансового благополучия и стабильности, чтобы ты мог воплощать в жизнь 
    даже самые смелые свои мечты и планы!""",
    
    """Папа, пусть наш дом всегда будет для тебя самым уютным и спокойным местом на земле, 
    где тебя всегда ждут, любят и поддерживают. Я очень ценю всё, что ты делаешь для нашей 
    семьи, твою заботу и надежное плечо. Желаю тебе душевного спокойствия, радости от 
    каждого прожитого момента и побольше времени на отдых в кругу близких.""",
    
    """Желаю тебе, чтобы жизнь была наполнена только добрыми новостями и приятными событиями. 
    Пусть рядом всегда будут верные друзья и люди, на которых можно положиться. 
    Я желаю тебе как можно больше поводов для гордости за себя и за нас, а мы в свою очередь 
    будем стараться только радовать тебя своими успехами!""",
    
    """С днем рождения, самый лучший отец! Желаю тебе всегда сохранять ту удивительную 
    выдержку и уверенность, которые в тебе есть. Пусть каждый новый год жизни приносит 
    тебе только интересные открытия, новые цели и силы для их достижения. Знай, что твои 
    советы для меня очень важны, и я всегда равняюсь на тебя!"""
]

def type_text(text, delay=0.03):
    placeholder = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f"<p class='terminal-text'>{displayed_text}</p>", unsafe_allow_html=True)
        time.sleep(delay)

if 'stage' not in st.session_state:
    st.session_state.stage = 'boot'
if 'current_wish' not in st.session_state:
    st.session_state.current_wish = random.choice(random_wishes)

# 1. Начало
if st.session_state.stage == 'boot':
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>SYSTEM_BOOT_INIT...</h1>", unsafe_allow_html=True)
    if st.button("ОТКРЫТЬ ЛИЧНОЕ ПОСЛАНИЕ"):
        st.session_state.current_wish = random.choice(random_wishes)
        st.session_state.stage = 'loading'
        st.rerun()

# 2. Загрузка
elif st.session_state.stage == 'loading':
    st.markdown("<p class='terminal-text'>[ЗАГРУЗКА]: Подбор самого искреннего пожелания...</p>", unsafe_allow_html=True)
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01) # Ускорил загрузку, чтобы не ждать долго
        progress_bar.progress(i + 1)
    st.session_state.stage = 'final'
    st.rerun()

# 3. Финал
elif st.session_state.stage == 'final':
    st.markdown("<h1 class='terminal-text' style='color:#00ff41;'>[ ДОСТУП РАЗРЕШЕН ]</h1>", unsafe_allow_html=True)
    
    tz_tajikistan = datetime.timezone(datetime.timedelta(hours=5))
    date_string = datetime.datetime.now(tz_tajikistan).strftime("%d.%m.%Y")
    
    st.markdown(f"""
    <div style="border: 2px solid #00ff41; padding: 25px; border-radius: 10px; background-color: #0a0a0a; box-shadow: 0 0 15px #00ff41;">
        <h2 style="color:#00ff41; font-family:Courier New; text-align:center;">С ДНЕМ РОЖДЕНИЯ, ПАПА! 🎉</h2>
        <p style="color:#00ff41; font-family:Courier New; font-size: 16px;">
        <b>ОТ КОГО:</b> Твой сын <br>
        <b>ЛОКАЦИЯ:</b> Кайраккум <br>
        <b>ДАТА:</b> {date_string} <br><br>
        <b>ПОСЛАНИЕ:</b> <br>
        {st.session_state.current_wish} <br><br>
        --- <br>
        <i style="font-size: 14px;">Я горжусь тем, что ты мой отец. Спасибо тебе за всё!</i>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ПРОЧИТАТЬ ДРУГОЕ ПОЖЕЛАНИЕ"):
        st.session_state.stage = 'boot'
        st.rerun()

# 3. Финал
elif st.session_state.stage == 'final':
    st.markdown("<h1 class='terminal-text' style='color:#00ff41;'>[ ДОСТУП РАЗРЕШЕН ]</h1>", unsafe_allow_html=True)
    
    tz_tajikistan = datetime.timezone(datetime.timedelta(hours=5))
    date_string = datetime.datetime.now(tz_tajikistan).strftime("%d.%m.%Y")
    
    st.markdown(f"""
    <div style="border: 2px solid #00ff41; padding: 25px; border-radius: 10px; background-color: #0a0a0a;">
        <h2 style="color:#00ff41; font-family:Courier New; text-align:center;">С ДНЕМ РОЖДЕНИЯ, ПАПА!</h2>
        <p style="color:#00ff41; font-family:Courier New;">
        <b>ОТ КОГО:</b> Твой сын <br>
        <b>ЛОКАЦИЯ:</b> Кайраккум <br>
        <b>ДАТА:</b> {date_string} <br><br>
        <b>ЛИЧНОЕ ПОЖЕЛАНИЕ:</b> <br>
        {st.session_state.current_wish} <br><br>
        --- <br>
        Дорогой папа, я тебя очень люблю и горжусь тобой. Оставайся всегда таким же сильным и мудрым!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("ПОЛУЧИТЬ ЕЩЕ ОДНО ПОЖЕЛАНИЕ"):
        st.session_state.stage = 'boot'
        st.rerun()
