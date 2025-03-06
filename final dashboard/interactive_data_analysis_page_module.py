import streamlit as st
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import folium_static
import re

# Read the CSV file
df = pd.read_csv(r"lake_data.csv")

# Function to parse the coordinate string into a list of [lat, lon] pairs
def parse_coordinates(coord_str):
    if not isinstance(coord_str, str) or not coord_str:
        return None
    
    try:
        # Extract all coordinate pairs using regex pattern that matches your specific data format
        # This pattern looks for number pairs separated by comma and enclosed in square brackets
        pairs = re.findall(r'\[([\d\.]+),([\d\.]+)\]', coord_str)
        
        if not pairs:
            return None
            
        # Convert to list of [lat, lon] pairs
        return [[float(lat), float(lon)] for lon, lat in pairs]
    except Exception as e:
        print(f"Error parsing coordinates: {e}")
        return None

# Apply the parsing function
df["Coordinates"] = df["Coordinates"].apply(parse_coordinates)

# Filter out rows with invalid coordinates
valid_df = df.dropna(subset=["Coordinates"])

if valid_df.empty:
    print("No valid coordinates found in the dataset")
else:
    # Create a map centered around the average of all coordinates
    all_coords = []
    for coords in valid_df["Coordinates"]:
        if coords:
            all_coords.extend(coords)

    if all_coords:
        avg_lat = sum(coord[0] for coord in all_coords) / len(all_coords)
        avg_lon = sum(coord[1] for coord in all_coords) / len(all_coords)
        lake_map = folium.Map(location=[avg_lat, avg_lon], zoom_start=14)
        
        # Add polygons for each lake
        for index, row in valid_df.iterrows():
            if row["Coordinates"]:
                name = row["Name"]
                size = row["Size"] if not pd.isna(row["Size"]) else "Unknown"
                
                # Add lake polygon
                folium.Polygon(
                    locations=row["Coordinates"],
                    popup=f"Name: {name}<br>Size: {size}",
                    color='blue',
                    fill=True,
                    fill_color='blue',
                    fill_opacity=0.4
                ).add_to(lake_map)
        
        # Save the map
        lake_map.save("lake_visualization.html")
        print("Map saved as lake_visualization.html")

# Create a dictionary mapping lake names to their coordinates
lake_dict = dict(zip(df["Name"], df["Coordinates"]))
lake_names = df["Name"].tolist()

def interactive_data_analysis_page():
    st.sidebar.subheader("Visualization Settings")

    # Lake selection
    selected_lake = st.sidebar.selectbox("Select the Lake", lake_names)

    if selected_lake:
        st.subheader(selected_lake)
        coordinates = lake_dict.get(selected_lake, [])

        if coordinates:
            # Calculate center of the polygon
            if len(coordinates) > 0:
                center_lat = sum(coord[0] for coord in coordinates) / len(coordinates)
                center_lon = sum(coord[1] for coord in coordinates) / len(coordinates)
                
                # Create a Folium map centered at the calculated center
                m = folium.Map(location=[center_lat, center_lon], zoom_start=15)
                folium.Polygon(locations=coordinates, color='blue', fill_opacity=0.3).add_to(m)
                folium_static(m)
            else:
                st.error("Invalid coordinate format for this lake.")
        else:
            st.error("No coordinates available for this lake.")

    # Dataset visibility toggle
    # if st.sidebar.checkbox("Show Dataset"):
    #     st.write(df)

    # # Determine numeric columns (excluding coordinates)
    # try:
    #     # Filter out the Coordinates column and find numeric columns
    #     numeric_df = df.drop(columns=['Coordinates'], errors='ignore')
    #     numeric_columns = list(numeric_df.select_dtypes(['float', 'int']).columns)
        
    #     if not numeric_columns:
    #         st.warning("No numeric columns found for visualization.")
    #         return
    # except Exception as e:
    #     st.error(f"Error determining numeric columns: {e}")
    #     return
    show_data = st.sidebar.checkbox("Show dataset")
    df = pd.read_csv('merged_data_lowerlake.csv')
    if show_data:
        st.write(df)

    global numeric_columns
    try:
        numeric_columns  = list(df.select_dtypes(['float','int' ]).columns)
    except Exception as e:
        print(e)

    # Chart type selection
    chart_select = st.sidebar.selectbox(
        label = "Select the Chart Type",
        options = ['Scatterplots', 'Lineplots', 'Histogram', 'Boxplot']
    )

    if chart_select == 'Scatterplots':
        st.sidebar.subheader('Scatterplot Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
            plot = px.scatter(data_frame = df, x = x_values, y = y_values)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Lineplots':
        st.sidebar.subheader('Lineplots Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
            plot = px.area(data_frame = df, x = x_values, y = y_values)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Boxplot':
        st.sidebar.subheader('Boxplot Settings')
        try:
            x_values = st.sidebar.selectbox('X axis', options = numeric_columns)
            y_values = st.sidebar.selectbox('Y axis', options = numeric_columns)
            plot = px.box(data_frame = df, x = x_values, y = y_values)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

    if chart_select == 'Histogram':
        st.sidebar.subheader('Histogram Settings')
        try:
            x_values = st.sidebar.selectbox('Select the variable to plot histogram', options = numeric_columns)
            bins = st.sidebar.slider("Select the number of bins", min_value=5, max_value=50, value=20, step=1)
            plot = px.histogram(data_frame = df, x = x_values, nbins=bins)
            st.plotly_chart(plot)
        except Exception as e:
            print(e)

# Run the function
if __name__ == "__main__":
    interactive_data_analysis_page()