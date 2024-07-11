import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Sample data
data = pd.DataFrame({
    'latitude': [37.7749, 34.0522, 40.7128],
    'longitude': [-122.4194, -118.2437, -74.0060],
    'city': ['San Francisco', 'Los Angeles', 'New York']
})

# Streamlit sidebar for filtering
st.sidebar.title("Filter Data")
city_filter = st.sidebar.multiselect("Select City", data['city'].unique(), default=data['city'].unique())

# Filter data based on user selection
filtered_data = data[data['city'].isin(city_filter)]

# Display data
st.write("## Filtered Data")
st.write(filtered_data)

# Create a Folium map
m = folium.Map(location=[filtered_data['latitude'].mean(), filtered_data['longitude'].mean()], zoom_start=4)

# Add points to the map
for idx, row in filtered_data.iterrows():
    folium.Marker([row['latitude'], row['longitude']], popup=row['city']).add_to(m)

# Display the map in Streamlit
st_folium(m, width=700, height=500)
