import streamlit as st
import joblib
import numpy as np

# 헤드라인
st.write("# 보험료 계산기 ")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSYL203CqnnOR5ppBj09N1pYxB3Y6afCDgOBA&usqp=CAU")

# 첫번째 행
r1_col1, r1_col2, r1_col3 = st.columns(3)

age = r1_col1.number_input("나이", step=1, value=23)

bmi = r1_col2.number_input("체질량지수", value=34.40)

children = r1_col3.number_input("자녀", step=1, value=0)

# 두번째 행
r2_col1, r2_col2, r2_col3 = st.columns(3)

r2_col1.write("흡연유무")
smoker = r2_col1.checkbox("")

sex_option = ("남성", "여성")
sex = r2_col2.selectbox("성별", sex_option)
is_male = sex_option[0] == sex

region_option = ('남서쪽', '남동쪽', '북서쪽', '북동쪽')
region = r2_col3.selectbox("지역", region_option)
is_southwest = region_option[0] == region
is_southeast = region_option[1] == region
is_northwest = region_option[2] == region

# 예측 버튼
predict_button = st.button("예측하기")

st.write("---")

# 예측 결과
if predict_button:
    model = joblib.load('first_model.pkl')

    pred = model.predict(np.array([[age, bmi, children, smoker * 1,
        is_male * 1, is_northwest * 1, is_southeast * 1, is_southwest * 1]]))
    

    st.metric("예측 보험료", int(pred[0]))