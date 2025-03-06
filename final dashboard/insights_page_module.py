import streamlit as st
from PIL import Image

def insights_page():
    st.header("Water Quality Index and Parameters Identification")
        
    str_text_body = """ 
        There are several water quality parameters available, but the team has chosen the following 8 important 
    parameters to monitor water quality.\n

    1-pH:One of the most crucial indicators of water quality is pH. The pH scale determines how basic or acidic a 
    solution is. \n
    2- Salinity: The quantity of dissolved salts in water is known as salinity.
    Water that is cloudy or hazy due to numerous tiny particles that are often unseen to the unaided eye is said to 
    be turbid. Water quality is typically impacted by suspended sediments, such as clay, dirt, and silt particles, 
    which frequently enter the water from disturbed locations.\n

    3- Temperature: The aquatic system is significantly influenced by water temperature, which also affects the habitat's 
    suitability for supporting aquatic life. Lower oxygen solubility in warmer water restricts the amount of oxygen
    available.\n

    4- Chlorophyll: A popular indicator of water quality and eutrophication level is chlorophyll-a.
    The concentration of phytoplankton is determined by the amount of chlorophyll present in a water sample. 
    Greater concentrations, which often occur when high algal production is sustained, indicate poorer water quality.\n


    5- Suspended matter: Fine particles make up suspended matter, which is in suspension. Plankton, tiny pieces of plant matter,
    and minerals are among those that naturally occur in river water, whilst others are a result of human activity
    (organic and inorganic matter). Water can become more turbid due to suspended materials, harming the ecology 
    of rivers and streams.\n

    6- Dissolved oxygen (DO) is a gaseous form of molecular oxygen (O2) that comes from the environment. 
    The concentrations of dissolved oxygen in water are influenced by salinity and temperature. 
    Temperature and salinity have an opposite relationship with oxygen solubility in water;
    as these two variables rise, so does DO.\n
    7- The organic matter percentage in solution that passes through a 0.45 m filter is referred to as
    "dissolved organic matter" (DOM). The mass of other elements, such as nitrogen, oxygen, and hydrogen,
    that are present in organic material is also included in DOM. The total mass of the dissolved organic matter
    is referred to here as DOM. \n

    This figure shows paramters values for safe and danger zone. \n
    """
    st.text(str_text_body)
    image = Image.open(r'Parameter-Thresholds.png')
    st.image(image)
    st.header("Findings")
    st.subheader('Per-year Findins')
    str_findings= """
    1- pH level had outlier in 2019, 2022. However it could be concluded that each year the distribution ranges changes
    2- Turbidity had outliers values since 2019, however the disrtibution didn't change across the years
    3- Temperautre had outliersin every-year. However we have no information in 2022.
    In covid year the disribution of temperatures varies. However before and  after 2020 the temperatures variation across years is not large
    4- Salinty had large number of outliers in 2019. However distribution and ranges across year varies.
    5- Disssolved oxygen matter is the most consisent features across years. There are small number of outliers
    6- Dissolved oxygen had outliers since 2019. However the disrtibution across years are quit similar.
    """
    st.text(str_findings)
    st.subheader('Per-Month Findins')
    str_findings= """
    1- Chrolophyll values across year pe-month ar not so good except for 2022 fisrt month has bad zone values. 
    2- Dissloved oxygen for 20220 values where in bad zone and begging of2021. Hoever the rest are in good zone values
    3- Dissolved oxygen matters for 2019,2018 the values where in bad zone ranges. However, 
    for 2020,2021,2022 for first 2 months andlast 3 months the values where in good zone range however
    from month 3-9 the values are too high
    4- Salinty values are between 0-1 for most year hence, lies whithin bad zone values
    5- Trubidity values are less than 0 for all months hence lies within good zone 
    6- pH values are in good zone ranges for all years and months
    """
    st.text(str_findings)
    st.subheader('Overall Conclusion')
    str_findings="""
    Our data collection efforts yielded a rich dataset of water quality parameters for Lendyia lake in the Bhopal region.
    We found that chlorophyll levels varied widely showing high levels of chlorophyll, indicating high levels of algae and other aquatic plants. 
    Turbidity levels were generally within the acceptable range.
    pH levels were generally within the acceptable range.
    Dissolved oxygen levels were generally within the acceptable range as well, however there were some outliers.
    For the dissolved oxygen matters: Mmre than **50%** of the values lie in **need treatment zone**.
    Overall, the data provides a comprehensive view of water quality in the Bhopal region and can be
    used to inform future efforts to monitor and manage water resources in the area.


    """
    st.text(str_findings)
    st.subheader('Conclusion')
        
    conlsution = """
    In conclusion, monitoring water quality using satellite imagery, GIS techniques, and 
    machine learning is crucial to ensure safe water consumption and protect the 
    environment. These technologies provide a broad and detailed view of the region, 
    which is essential for developing appropriate strategies to address water quality 
    issues. The project's findings and recommendations can inform stakeholders to 
    implement effective and sustainable monitoring programs to ensure the long-term 
    """

    st.text(conlsution)