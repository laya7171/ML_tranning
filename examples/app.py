import streamlit as st

weight = st.number_input('Weight (kg)', 0, 200)

height_format = st.radio('Height format', ('cms', 'meters', 'feet'))

height_value = st.number_input('Height', 0.0, 300.0)

button = st.button('Calculate BMI')

bmi = None

if button:
    if height_format == 'cms':
        height_in_meters = height_value / 100 
        bmi = weight / height_in_meters**2
    elif height_format == 'meters':
        bmi = weight / height_value**2
    elif height_format == 'feet':
        height_in_meters = height_value * 0.3048  
        bmi = weight / height_in_meters**2

    st.write(f'Your BMI is {bmi:.2f}')

if bmi is not None:
    if bmi < 16:
        st.write('Extremely Underweight')
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSEPLMfmOFx2MpOl-bhRJl56xTXQ8vHmdd2Gg&s")
    elif bmi >= 16 and bmi < 18.5:
        st.write('Underweight')
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzpxFt3ibO0USYqsuZIv95sfDXLGGFVqeO4g&s")
    elif bmi < 18.5 and bmi < 25:
        st.write('Healthy')
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJkr0_On6JplKHtBZR-K4SFRU1LcY5zNkXkw&s")
    elif bmi < 25 and bmi < 30:
        st.write('Overweight')
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS6mR5BNdYuG7NqUk0moO3o9DeCxV0tpt-ZRQ&s")
    else:
        st.write('Obese')
        st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAlSHYoG5OhvxUYrZI42WCK-CeTGxAgiMtag&s")
        
        
#Beautify the existing code
