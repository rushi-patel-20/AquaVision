import streamlit as st

def introduction_page():
    st.subheader("Introduction")
    introduction_str=""" 
    The primary objective of this challenge is to find effective ways to monitor water quality in the Bhopal region using satellite imagery.
    The purpose of this project is to reduce the cost of the monitoring process, as the current method utilizing IoT sensors requires a 
    significant amount of maintenance, making it an expensive process. The main goal of the project is to identify parameters that can be 
    used to monitor water quality, establish a standardized way of collecting real-time data, identify any discrepancies in the current 
    monitoring process, and improve them as much as possible. To achieve these objectives, a detailed data analysis will be conducted. We 
    will examine a range of satellite imagery data and extract the relevant parameters that can be used to monitor water quality. By 
    analyzing this data, we will be able to identify patterns and trends that can be used to improve the monitoring process. Finally, we 
    will develop a visualization dashboard using either Tableau or Power BI to present the collected data in a user-friendly and visually 
    appealing manner. The dashboard will provide key metrics and insights related to water quality in the region, allowing for easy 
    monitoring and informed decision-making based on the data collected.
    
    
    The challenge, which united an international team of AI engineers over 5 weeks, was led by Vaasu Bisht and Eeman Majumder. The common 
    language for the chapter was English. Platforms such as GitHub, Notion, Asana, and a dedicated Slack channed were used to coordinate and 
    keep track of the engineer's work.
    """
    st.text(introduction_str)

    st.subheader("Our Solution")

    our_solution_str=""" 
    The team developed a user-friendly visualization dashboard that integrates the processed data from satellite imagery and GIS techniques. The dashboard 
    provides real-time updates on key water quality parameters, including temperature, pH, dissolved oxygen, and turbidity. It also allows for easy monito-
    ring of trends and patterns in the data, enabling users to quickly identify any discrepancies in water quality and take necessary corrective action. 
    The dashboard's visually appealing interface and user-friendly design make it an effective tool for decision-making and collaboration between various 
    stakeholders, including government agencies, NGOs, and local communities. Overall, the dashboard is a valuable asset in the ongoing efforts to protect 
    and improve the water quality in the Bhopal region.
    """
    st.text(our_solution_str)


    st.subheader("The Data")

    the_dat_Srt=""" 
    For our water quality monitoring project in the Bhopal region, we collected data from various lakes using satellite imagery and GIS techniques. The lakes
    we focused on include Upper Lake, Lower Lake, Kaliyasot dam, Kerwa Dam, Shahpura Lake, Sarangpani Lake, Motia talab, Hathaikheda dam/lake, Nawab Munshi 
    Hussain Khan Talab, Nawab Siddiqui Hasan Khan Talaab, Jawahar Baal Udyan Lake, Lendiya Talab, Manit lake, and bhojtal lake.

    To effectively monitor the water quality in these lakes, we collected various parameters related to water quality, including pH, salinity, turbidity, 
    temperature, chlorophyll, suspended matter, dissolved oxygen, and dissolved organic matter (DOM). These parameters were chosen based on their relevance 
    to water quality and their ability to provide insights into the health of the lakes.
    """
    st.text(the_dat_Srt)