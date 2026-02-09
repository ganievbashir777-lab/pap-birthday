import streamlit as st
import random

# Настройка страницы
st.set_page_config(page_title="Подарок для Папы", page_icon="🎁")

# Список случайных пожеланий
wishes = [
    "🚀 Чтобы каждый твой проект «взлетал» с первого запуска!",
    "💰 Желаю, чтобы кошелек был всегда в плюсе, а баги — только в старых учебниках!",
    "🦾 Крепкого здоровья, как у самого мощного процессора!",
    "🌟 Пусть каждый день приносит столько же радости, сколько приносит успешно работающий код!",
    "🏠 Уюта в доме и как можно больше времени на отдых с семьей!",
    "🚗 Желаю ровных дорог и всегда полного бака!",
    "🎮 Желаю всегда побеждать на любом уровне сложности в жизни!"
]

# Заголовок
st.title("🎁 Тебе пришла посылка!")

# Состояние «коробки» (открыта или закрыта)
if 'opened' not in st.session_state:
    st.session_state.opened = False

# Если коробка еще не открыта
if not st.session_state.opened:
    st.write("### Папа, тебе пришел подарок! Нажми на кнопку ниже, чтобы открыть его.")
    if st.button('📦 ОТКРЫТЬ ПОДАРОК'):
        st.session_state.opened = True
        st.rerun() # Перезапускаем, чтобы показать содержимое

# Если коробку открыли
else:
    st.balloons() # Запускаем шарики
    
    # Визуализация открытки
    st.markdown("""
    <style>
    .card {
        background-color: #ffffff;
        padding: 30px;
        border-radius: 15px;
        border: 5px solid #ff4b4b;
        text-align: center;
        box-shadow: 10px 10px 20px rgba(0,0,0,0.1);
    }
    .main-text {
        color: #262730;
        font-size: 24px;
        font-weight: bold;
    }
    </style>
    <div class="card">
        <p class="main-text">🎊 С ДНЕМ РОЖДЕНИЯ, ПАПА! 🎊</p>
        <p>Эта открытка создана на Python специально для тебя.</p>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")
    
    # Случайное пожелание
    current_wish = random.choice(wishes)
    st.subheader("Твое пожелание на сегодня:")
    st.info(current_wish)

    # Кнопка, чтобы получить еще одно пожелание
    if st.button('✨ Получить другое пожелание'):
        st.rerun()

    if st.button('🎁 Закрыть коробку'):
        st.session_state.opened = False
        st.rerun()
