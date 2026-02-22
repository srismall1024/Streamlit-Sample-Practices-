import streamlit as st

st.title("🌡 Temperature Converter")
st.header("Welcome to Temperature Converting Page")


conversion = st.selectbox(
    "Select Conversion Type",
    [
        "Celsius → Fahrenheit",
        "Fahrenheit → Celsius",
        "Celsius → Kelvin",
        "Kelvin → Celsius",
        "Fahrenheit → Kelvin",
        "Kelvin → Fahrenheit"
    ]
)


value = st.number_input("Enter the temperature value")


convert = st.button("Convert")

if convert:

    if conversion == "Celsius → Fahrenheit":
        result = (value * 9/5) + 32
        st.success(f"Result: {result} °F")

    elif conversion == "Fahrenheit → Celsius":
        result = (value - 32) * 5/9
        st.success(f"Result: {result} °C")

    elif conversion == "Celsius → Kelvin":
        result = value + 273.15
        st.success(f"Result: {result} K")

    elif conversion == "Kelvin → Celsius":
        result = value - 273.15
        st.success(f"Result: {result} °C")

    elif conversion == "Fahrenheit → Kelvin":
        result = ((value - 32) * 5/9) + 273.15
        st.success(f"Result: {result} K")

    elif conversion == "Kelvin → Fahrenheit":
        result = ((value - 273.15) * 9/5) + 32
        st.success(f"Result: {result} °F")
