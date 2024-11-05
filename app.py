import streamlit as st

st.title('🐻My First Streamlit App🐻')

st.header('이게 된다고?🤔⚾')

multi_select = st.multiselect(
    label = '좋아하는 과일을 입력하세요.',
    options = ['사과', '바나나', '파인애플', '키위', '아보카도']
)
st.write(f'당신이 좋아하는 과일은 :blue[**{multi_select}**]입니다.')

