import streamlit as st

def data_collection_page():
    st.title("Data Collection")
    introduction_string = """
    Collecting data using the Google Earth Engine API can be a complex and daunting task. Our team found that one of the major challenges in the process was 
    the lack of a standardized approach to data collection. Without a standardized methodology, the data collected from different sources can vary greatly, 
    making analysis and comparison difficult. This is where our team stepped in, developing a standardized function and classes to improve the data collection 
    process.

    Our standardized function and classes not only made data collection more efficient, but also helped to maintain consistency across multiple data sources. 
    With our solution, we were able to collect data from various sources in a streamlined manner, ensuring that the collected data was consistent and accurate. 
    We believe that our contribution will be valuable to researchers and scientists working in the field, and we are proud to have developed a solution that 
    improves the quality and reliability of data collected using the Google Earth Engine API.
    """
    st.text(introduction_string)

    st.title("Get Salanity")

    code = """
def get_Salanity(start_date, end_date):

# Selecting the satellite and AOI  
# Sentinel 2A
# copernicus/s2_sr 
sentinel = ee.ImageCollection("COPERNICUS/S2_SR").
            filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',20)).
            filterDate(start_date, end_date)
AOI = geometry

sentinel_AOI = sentinel.filterBounds(AOI)

#calculate NDSI
def calculate_NDSI(image):
    ndsi = image.normalizedDifference(['B11', 'B12']).rename('NDSI')
    return image.addBands(ndsi)
ndsi = sentinel_AOI.map(calculate_NDSI)

# Mean NDSI
def calculate_mean_NDSI(image):
    image = ee.Image(image)
    mean = image.reduceRegion(reducer = ee.Reducer.mean().setOutputs(['NDSI']),
                            geometry = AOI,
                            scale = image.projection().nominalScale().getInfo(),
                            maxPixels = 100000,
                            bestEffort = True);
    return mean.get('NDSI').getInfo()
    
# NDSI Mean Collection
Images_ndsi = ndsi.select('NDSI').toList(ndsi.size())
ndsi_coll = []
for i in range(Images_ndsi.length().getInfo()):
    image = ee.Image(Images_ndsi.get(i-1))
    temp_ndsi = calculate_mean_NDSI(image)
    ndsi_coll.append(temp_ndsi)

# Dates Collection
dates = np.array(ndsi.aggregate_array("system:time_start").getInfo())
day = [datetime.datetime.fromtimestamp(i/1000).strftime('%Y-%m-%d') for i in (dates)]

# Dataframe for Salinity

df = pd.DataFrame(ndsi_coll, index = day, columns = ['Salinity'])
df.index = pd.to_datetime(df.index, format="%Y/%m/%d")
df.sort_index(ascending = True, inplace = True)

return df
"""

    st.code(code, language='python')



    st.title("Get Chlorophyll")

    code = """
def get_chlorophyll(start_date, end_date):

    # Selecting the satellite and AOI  
    # Sentinel 2A
    # copernicus/s2_sr 
    sentinel = ee.ImageCollection("COPERNICUS/S2_SR").
            filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',20)).
            filterDate(start_date, end_date)
    AOI = geometry

    sentinel_AOI = sentinel.filterBounds(AOI)
    # NDCI calculation
    def calculate_NDCI(image):
        ndci = image.normalizedDifference(['B5', 'B4']).rename('NDCI')
        return image.addBands(ndci)
    ndci = sentinel_AOI.map(calculate_NDCI)  

    # NDCI mean
    def calculate_mean_NDCI(image):
        image = ee.Image(image)
        mean = image.reduceRegion(reducer = ee.Reducer.mean().setOutputs(['NDCI']),
                        geometry = AOI,
                        scale = image.projection().nominalScale().getInfo(),
                        maxPixels = 100000,
                        bestEffort = True);
        return mean.get('NDCI').getInfo()    
    
    # NDCI mean collection    
    Images_ndci = ndci.select('NDCI').toList(ndci.size())
    ndci_coll = []
    for i in range(Images_ndci.length().getInfo()):
        image = ee.Image(Images_ndci.get(i-1))
        temp_ndci = calculate_mean_NDCI(image)
        ndci_coll.append(temp_ndci)
    # Dates collection
    dates = np.array(ndci.aggregate_array("system:time_start").getInfo())
    day = [datetime.datetime.fromtimestamp(i/1000).strftime('%Y-%m-%d') for i in (dates)]

    # Dataframe for chlorophyll
    df = pd.DataFrame(ndci_coll, index = day, columns = ['Chlorophyll'])
    df.index = pd.to_datetime(df.index, format="%Y/%m/%d")
    df.sort_index(ascending = True, inplace = True)

    return df
    """

    st.code(code, language='python')


    st.title("Get Turbidity")

    code = """
def get_turbidity(start_date, end_date):

    # Selecting the satellite and AOI  
    # Sentinel 2A
    # copernicus/s2_sr 
    sentinel = ee.ImageCollection("COPERNICUS/S2_SR").
            filter(ee.Filter.lt('CLOUDY_PIXEL_PERCENTAGE',20)).
            filterDate(start_date, end_date)
    AOI = geometry

    sentinel_AOI = sentinel.filterBounds(AOI)

    #calculate NDTI
    def calculate_NDTI(image):
        ndti = image.normalizedDifference(['B4', 'B3']).rename('NDTI')
        return image.addBands(ndti)
    ndti = sentinel_AOI.map(calculate_NDTI)

    # Mean NDTI
    def calculate_mean_NDTI(image):
        image = ee.Image(image)
        mean = image.reduceRegion(reducer = ee.Reducer.mean().setOutputs(['NDTI']),
                                geometry = AOI,
                                scale = image.projection().nominalScale().getInfo(),
                                maxPixels = 100000,
                                bestEffort = True);
        return mean.get('NDTI').getInfo()
    
    # NDTI mean collection 
    Images_ndti = ndti.select('NDTI').toList(ndti.size())
    ndti_coll = []
    for i in range(Images_ndti.length().getInfo()):
        image = ee.Image(Images_ndti.get(i-1))
        temp_ndti = calculate_mean_NDTI(image)
        ndti_coll.append(temp_ndti)

    # Dates Collection
    dates = np.array(ndti.aggregate_array("system:time_start").getInfo())
    day = [datetime.datetime.fromtimestamp(i/1000).strftime('%Y-%m-%d') for i in (dates)]

    # Dataframe for Turtbidity

    df = pd.DataFrame(ndti_coll, index = day, columns = ['Turbidity'])
    df.index = pd.to_datetime(df.index, format="%Y/%m/%d")
    df.sort_index(ascending = True, inplace = True)

return df
"""

    st.code(code, language='python')



    st.write("You can find other functions here -  [link](https://github.com/OmdenaAI/omdena-bhopal-water-quality-monitoring/blob/main/Standard_function.ipynb)")




    st.video(r"datcollection_dashboard.mp4", format="video/mp4")
#         st.text(
#             """ In the first week of the project, we conducted research on different types of APIs for 
# collecting water quality data in Bhopal. After careful consideration, we chose the 
# Google Earth Engine API for our data collection. \n    streamlit run main.py
# In the second week, we started collecting data using the Google Earth Engine API, 
# using Sentinel 2A and Landsat 8 satellite imagery to collect data on various water 
# quality parameters, including chlorophyll, turbidity, salinity, pH, dissolved oxygen, 
# dissolved organic matter, and suspended matter."""
#         )