import streamlit as st
from countryinfo import CountryInfo
import pycountry

st.set_page_config(page_title="Country Capital Finder", layout="centered")

# -----------------------------------
# SOUNDARYA LIGHT THEME
# -----------------------------------

st.markdown("""
<style>

/* Light Background */
.stApp{
background-color:#f5f5f5;
}

/* Developer text */
.dev{
text-align:center;
font-size:20px;
font-weight:bold;
color:black;
}

/* Title */
.title{
text-align:center;
color:black;
font-size:38px;
font-weight:bold;
}

/* Card UI */
.card{
background:white;
padding:30px;
border-radius:12px;
box-shadow:0px 5px 15px rgba(0,0,0,0.15);
}

/* All text black */
label, .stMarkdown, .stSelectbox{
color:black;
}

/* Button Style */
.stButton>button{
background-color:#ff69b4;
color:white;
border-radius:8px;
height:40px;
width:100%;
font-size:16px;
border:none;
}

.stButton>button:hover{
background-color:#ff1493;
color:white;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------

st.markdown("<div class='dev'>Developed by TRUERIZE </div>", unsafe_allow_html=True)

st.markdown("<div class='title'>🌍 Country Capital Finder</div>", unsafe_allow_html=True)



# -----------------------------------
# CARD
# -----------------------------------

st.markdown('<div class="card">', unsafe_allow_html=True)

countries = [country.name for country in pycountry.countries]

country = st.selectbox("🔍 Select Country", countries)

# -----------------------------------
# FIND CAPITAL
# -----------------------------------

if st.button("Find Capital"):

    try:
        info = CountryInfo(country)
        capital = info.capital()

        country_code = pycountry.countries.get(name=country).alpha_2
        flag_url = f"https://flagsapi.com/{country_code}/flat/64.png"

        st.image(flag_url)

        st.success(f"🏛 Capital of {country} is {capital}")

    except:
        st.error("Country not found")

st.markdown('</div>', unsafe_allow_html=True)