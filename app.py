import streamlit as st
import time

# Настройка страницы в стиле консоли
st.set_page_config(page_title="Terminal: Access Granted", page_icon="💻")

# Применяем CSS для создания черного фона и зеленого шрифта (как в старых компьютерах)
st.markdown("""
<style>
    /* Весь фон делаем черным */
    .stApp {
        background-color: #000000;
    }
    /* Текст делаем ярко-зеленым */
    p, h1, h2, h3, span, div {
        color: #00ff00 !important;
        font-family: 'Courier New', Courier, monospace !important;
    }
    /* Стилизация кнопок под терминал */
    .stButton>button {
        color: #00ff00 !important;
        border: 2px solid #00ff00 !important;
        background-color: #111111 !important;
        width: 100%;
        border-radius: 0px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #00ff00 !important;
        color: #000000 !important;
    }
    /* Скрываем лишние элементы интерфейса Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Инициализация состояния программы
if 'stage' not in st.session_state:
    st.session_state.stage = 'start'

# СТРАНИЦА 1: Вход в систему
if st.session_state.stage == 'start':
    st.title("> SYSTEM LOGIN")
    st.write("---")
    st.write("WARNING: RESTRICTED ACCESS")
    st.write("ENCRYPTION: AES-256")
    if st.button("RUN SYSTEM DIAGNOSTIC"):
        st.session_state.stage = 'loading'
        st.rerun()

# СТРАНИЦА 2: Процесс "загрузки"
elif st.session_state.stage == 'loading':
    st.title("> LOADING DATA...")
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Имитация логов загрузки
    logs = [
        "Initializing core modules...",
        "Bypassing security layers...",
        "Accessing personal_records.db...",
        "Analyzing family_history...",
        "Filtering results: 'Best Father'...",
        "MATCH FOUND: [ID_PAPA_001]",
        "Decrypting message..."
    ]
    
    for i, log in enumerate(logs):
        status_text.text(f"PROCESSED: {log}")
        progress_bar.progress((i + 1) * 100 // len(logs))
        time.sleep(0.8) # Скорость "загрузки"
    
    st.session_state.stage = 'result'
    st.rerun()

# СТРАНИЦА 3: Финальный результат
elif st.session_state.stage == 'result':
    st.title("> ACCESS GRANTED")
    st.write("---")
    
    st.subheader("DATA REPORT: 09.02.2026")
    
    st.markdown("""
    **ОБЪЕКТ:** Папа  
    **СТАТУС:** Главный человек в системе  
    **ВЕРДИКТ:** С Днем Рождения!
    
    ---
    **КОММЕНТАРИЙ РАЗРАБОТЧИКА:** Папа, этот скрипт — мой способ сказать тебе спасибо.  
    Ты — мой главный сервер стабильности и надежности.  
    Желаю тебе 100% аптайма, крепкого здоровья  
    и чтобы в твоей жизни никогда не было критических ошибок!
    ---
    """)
    
    if st.button("LOGOUT"):
        st.session_state.stage = 'start'
        st.rerun()
