import streamlit as st
import pandas as pd


st.title(':zap: Communicate Dashboard')
st.header('Hi buddy 👋. Welcome to my dashboard ❤️')
st.text('''
Here i want to share my future plans on my social media pages.
•  Sharing my github activities
•  Add new educating videos on my YouTube channel
•  Communicating in Telegram
''')

with st.expander('Github'):
    df = pd.DataFrame(
        [
            {'Repositories': 'fun-with-python', 'Fork': True, 'Info': 'funny projects like Authentication User Logger'},
            {'Repositories': 'python-challenge', 'Fork': False, 'Info': 'Some python challenges and mini projects'},
            {'Repositories': 'streamlit-dashboard', 'Fork': False, 'Info': 'A dashboard to know me better and communicate with me'},
        ]
)
    st.dataframe(df, use_container_width=True)

    button = st.link_button('Click Here', url='https://github.com/martybin')

with st.expander('Telegram'):
    st.text(
        'You can message me from here if you have any question'
    )

    button = st.link_button('Click Here', url='https://t.me/its_matinn')


with st.expander('YouTube'):
    df = pd.DataFrame(
        [
            {'Short Videos': 'Match Case Statement', 'TODO-Shorts': True, 'Videos': 'Wordle with python', 'TODO-Videos': False},
            {'Short Videos': '', 'TODO-Shorts': False, 'Videos': 'Tic Tac Toe with python', 'TODO-Videos': False},
            {'Short Videos': '', 'TODO-Shorts': False, 'Videos': 'YouTube Downloader with python', 'TODO-Videos': False},
            {'Short Videos': '', 'TODO-Shorts': False, 'Videos': '', 'TODO-Videos': False},
        ]
    )

    st.dataframe(df, use_container_width=True)

    button = st.link_button('Click Here', url='https://www.youtube.com/@PyLearn_ai')

with st.expander('Email'):
    st.text(
        'If you do not have Telegram you can also message me from Email'
    )

    button = st.link_button('Click Here', url='mailto:m.hosseini9998@gmail.com')
