import streamlit as st
import time

# Настройка страницы
st.set_page_config(page_title="PAPA_OS v2.0", page_icon="📟", layout="centered")

# Продвинутый CSS для атмосферы "Матрицы"
st.markdown("""
<style>
    .stApp {
        background-color: #050505;
    }
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
        text-transform: uppercase;
        letter-spacing: 2px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #00ff41 !important;
        color: #000000 !important;
        box-shadow: 0 0 20px #00ff41;
    }
    /* Анимация мигающего курсора */
    .cursor {
        display: inline-block;
        width: 10px;
        height: 20px;
        background-color: #00ff41;
        animation: blink 1s infinite;
    }
    @keyframes blink {
        0% { opacity: 0; }
        50% { opacity: 1; }
        100% { opacity: 0; }
    }
</style>
""", unsafe_allow_html=True)

def type_text(text, delay=0.05):
    """Функция для имитации печати текста"""
    placeholder = st.empty()
    displayed_text = ""
    for char in text:
        displayed_text += char
        placeholder.markdown(f"<p class='terminal-text'>{displayed_text}<span class='cursor'></span></p>", unsafe_allow_html=True)
        time.sleep(delay)

if 'stage' not in st.session_state:
    st.session_state.stage = 'boot'

# 1. Загрузка системы (BOOT)
if st.session_state.stage == 'boot':
    st.markdown("<h1 class='terminal-text' style='text-align:center;'>CORE_SYSTEM_V2.0</h1>", unsafe_allow_html=True)
    st.write("")
    if st.button("INITIALIZE BOOT SEQUENCE"):
        st.session_state.stage = 'loading'
        st.rerun()

# 2. Имитация взлома
elif st.session_state.stage == 'loading':
    st.markdown("<p class='terminal-text'>[LOG]: Remote connection established...</p>", unsafe_allow_html=True)
    time.sleep(0.5)
    st.markdown("<p class='terminal-text'>[LOG]: Scanning for high-level authority...</p>", unsafe_allow_html=True)
    
    progress_bar = st.progress(0)
    for i in range(100):
        time.sleep(0.03)
        progress_bar.progress(i + 1)
        if i == 20: st.write("`[OK] Firewall bypassed`")
        if i == 50: st.write("`[OK] Root privileges obtained`")
        if i == 80: st.write("`[OK] Decrypting Birthday_Wishes.exe`")
    
    time.sleep(1)
    st.session_state.stage = 'final'
    st.rerun()

# 3. Финальный экран
elif st.session_state.stage == 'final':
    st.markdown("<h1 class='terminal-text' style='color:#00ff41;'>[ ACCESS GRANTED ]</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # Сначала печатаем поздравление красиво
    type_text("Поздравление загружено...")
    time.sleep(0.5)
    
    st.markdown(f"""
    <div style="border: 2px solid #00ff41; padding: 20px; border-radius: 5px;">
        <h2 style="color:#00ff41; font-family:Courier New;">REPORT FOR: PAPA_ID</h2>
        <p style="color:#00ff41; font-family:Courier New;">
        <b>STATUS:</b> THE_BEST_FATHER_IN_WORLD <br>
        <b>LOCATION:</b> FAMILY_CORE <br>
        <b>DATE:</b> {time.strftime("%d.%m.%Y")} <br><br>
        <b>MESSAGE:</b> <br>
        Папа, система проанализировала все данные и пришла к выводу:<br>
        Ты — самый надежный код в моей жизни. <br>
        Желаю тебе здоровья, которое никогда не выдаст "Error", <br>
        и счастья, которое будет копироваться бесконечным циклом!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("TERMINATE SESSION (EXIT)"):
        st.session_state.stage = 'boot'
        st.rerun()
