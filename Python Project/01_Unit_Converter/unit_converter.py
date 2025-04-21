import streamlit as st

def convert_units(value, unit_from, unit_to):

    coversions = {
        "meters_kilometers": 0.001,    # 1 meter = 0.001 kilometer
        "kilometers_meters": 1000,     # 1 kilometer = 1000 meters
        "grams_kilograms": 0.001,      # 1 gram = 0.001 kilogram
        "kilograms_grams": 1000,       # 1 kilogram = 1000 grams
        "celsius_fahrenheit": (lambda c: (c * 9/5) + 32),  # 1 celsius = 33.8 fahrenheit
        "fahrenheit_celsius": (lambda f: (f - 32) * 5/9)  # 1 fahrenheit = -17.22222222222222 celsius


 }
    
    key = f"{unit_from}_{unit_to}" # Generate key to get the conversion factor

    if key in coversions:
        convert = coversions[key]
        if callable(convert):
            return convert(value)
        else:
            return value * convert
    else:
        return "Not a valid conversion"
    
st.title("🔣 Unit Converter ")

# Adding some styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stTextInput > label {
        color: #4F8BF9;
    }
    .stNumberInput > label {
        color: #4F8BF9;
    }
    .stSelectbox > label {
        color: #4F8BF9;
    }
    .stButton > button {
        color: #ffffff;
        background-color: #4F8BF9;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
    }
    .stButton > button:hover {
        background-color: #093170;
        color:#ffffff;
    }
    </style>
    """,
    unsafe_allow_html=True
)

value = st.number_input("Enter the value you want to convert")

unit_from = st.selectbox("Convert from", ["meters", "kilometers", "grams", "kilograms", "celsius", "fahrenheit"])
                    
unit_to = st.selectbox("Convert to", ["meters", "kilometers", "grams", "kilograms", "celsius", "fahrenheit"]) 

if st.button("Convert"):
    result = convert_units(value, unit_from, unit_to)
    st.success(f"Conversion result: {result} {unit_to}")
