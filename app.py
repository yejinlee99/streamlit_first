import streamlit as st

st.title('🐻My First Streamlit App🐻')

st.header('이게 된다고?🤔⚾')

multi_select = st.multiselect(
    label = '좋아하는 두산베어스 선수를 입력하세요.',
    options = ['김택연','곽빈','정수빈','허경민','김재호','양의지','최승용','이병헌','최지강','이영하']
)
st.write(f'당신이 좋아하는 두산베어스 선수는 :blue[**{multi_select}**]입니다.')

