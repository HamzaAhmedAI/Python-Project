import streamlit as st
import requests

def fetch_countries_data(country):
    url = f'https://restcountries.com/v3.1/name/{country}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        country_data = data[0] # Assuming the first result is the most relevant
        name = country_data["name"]["common"]  
        capital = country_data["capital"][0]
        population = country_data["population"]
        area = country_data["area"]
        currency = country_data["currencies"]
        region = country_data["region"]
        return name, capital, population, area, currency, region
    else:
        return None, None, None, None, None, None

def main():
    st.title("Country Information App")
    
    country = st.text_input("Enter a country name:")

    if country:
        country_info = fetch_countries_data(country)
        if country_info[0]:
            name, capital, population, area, currency, region = country_info

            st.subheader("Country Information")
            st.write(f"Name: {name}")  
            st.write(f"Capital: {capital}")  
            st.write(f"Population: {population}")  
            st.write(f"Area: {area}")  
            st.write(f"Currency: {currency}")  
            st.write(f"region: {region}")  
        else:
            st.error("Error: Country data not found!")
    

if __name__ == "__main__":
        main()
