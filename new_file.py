import pandas as pd
import numpy as np
import folium
from folium import plugins

# Create a base map centered at a specific location
def create_flood_map(center_lat=0, center_lon=0, zoom_start=10):
    flood_map = folium.Map(location=[center_lat, center_lon], 
                          zoom_start=zoom_start,
                          tiles='CartoDB positron')
    
    # Add a fullscreen option
    plugins.Fullscreen().add_to(flood_map)
    
    return flood_map

# Example usage
if __name__ == "__main__":
    print("Hello, world!")
    # Example coordinates (replace with your area of interest)
    latitude = 27.7128
    longitude = -81.0060
    
    # Create the map
    my_map = create_flood_map(latitude, longitude)
    
    # Save the map
    my_map.save('flood_map.html')

