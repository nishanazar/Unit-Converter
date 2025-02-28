import streamlit as st
import time

# Custom Page Config
st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="wide")

# Custom Styling
st.markdown(
    """
    <style>
        .big-font { font-size:24px !important; font-weight: bold; color: #4CAF50; }
        .stButton>button { background-color: #4CAF50; color: white; font-size: 18px; padding: 10px; }
        .stSelectbox, .stNumber_input { border-radius: 10px; }
        .result-box { font-size: 22px; font-weight: bold; color: #4CAF50; text-align: center; }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title with Emoji
st.title("🔄 Google Unit Converter - Streamlit")

# Unit Categories (Google Style)
categories = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
    "Weight & Mass": {"Gram": 1, "Kilogram": 0.001, "Milligram": 1000, "Pound": 0.00220462, "Ounce": 0.035274, "Ton": 0.000001},
    "Temperature": {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"},
    "Time": {"Second": 1, "Minute": 1/60, "Hour": 1/3600, "Day": 1/86400, "Week": 1/604800, "Month": 1/2.628e+6, "Year": 1/3.154e+7},
    "Speed": {"Meter per second": 1, "Kilometer per hour": 3.6, "Mile per hour": 2.23694, "Knot": 1.94384},
    "Area": {"Square Meter": 1, "Square Kilometer": 0.000001, "Hectare": 0.0001, "Acre": 0.000247105, "Square Foot": 10.7639, "Square Inch": 1550},
    "Volume": {"Liter": 1, "Milliliter": 1000, "Cubic Meter": 0.001, "Cubic Centimeter": 1000, "Gallon": 0.264172, "Pint": 2.11338},
    "Energy": {"Joule": 1, "Kilojoule": 0.001, "Calorie": 0.239006, "Kilocalorie": 0.000239006, "Kilowatt-hour": 2.7778e-7},
    "Power": {"Watt": 1, "Kilowatt": 0.001, "Megawatt": 1e-6, "Horsepower": 0.00134102},
    "Pressure": {"Pascal": 1, "Bar": 1e-5, "PSI": 0.000145038},
    "Data Storage": {"Bit": 1, "Byte": 0.125, "Kilobyte": 0.000125, "Megabyte": 1.25e-7, "Gigabyte": 1.25e-10, "Terabyte": 1.25e-13},
    "Fuel Efficiency": {"Kilometers per liter": 1, "Miles per gallon": 2.35215}
}

# Layout
col1, col2 = st.columns([1, 2])

with col2:
    st.markdown('<p class="big-font">Convert Length, Weight, Time, Speed, Temperature & More!</p>', unsafe_allow_html=True)

# Select Category
category = st.selectbox("🔍 Select a category:", list(categories.keys()))

# Select Units
from_unit = st.selectbox("🎯 Convert from:", list(categories[category].keys()))
to_unit = st.selectbox("🎯 Convert to:", list(categories[category].keys()))

# Input Value
value = st.number_input("📝 Enter value:", min_value=0.0, format="%.2f")

# Conversion Logic
def convert(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value * categories[category][to_unit] / categories[category][from_unit]

# Convert and Display Result with Spinner
if st.button("🚀 Convert"):
    with st.spinner("Converting... Please wait..."):
        time.sleep(2)
    result = convert(value, from_unit, to_unit, category)
    st.markdown(f'<p class="result-box">{value} {from_unit} = {result:.4f} {to_unit} ✅</p>', unsafe_allow_html=True)
