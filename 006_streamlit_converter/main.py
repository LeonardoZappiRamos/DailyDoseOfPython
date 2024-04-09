import streamlit as st


if __name__ == "__main__":
    st.title("Kilometer :repeat: Miles Converter")
    
    tab1, tab2 = st.tabs(["Kilometer to Miles", "Miles to Kilometer"])
    
    with tab1:
        input_kilometer = st.number_input("Kilometer")
        st.button("Converter", key="kilometer_converter")
        miles = input_kilometer * 0.6214
        st.subheader(f"Miles Converted: {round(miles, 2)}")
    with tab2:
        input_miles = st.number_input("Miles")
        st.button("Converter", key="miles_converter")
        kilometer = input_miles * 1.6093
        st.subheader(f"Kilometers Converted: {round(kilometer, 2)}")