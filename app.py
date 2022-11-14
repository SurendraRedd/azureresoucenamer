"""
This application contains the code related to the
Azure Resource Namer application.
"""
# Required packages importing
import streamlit as st

# Header template
html_temp = """
    <body style="background-color:red;">
    <div style="background-color:tomato;padding:10px">
    <h3 style="color:white;text-align:center;"> Azure Resource Naming tool</h3>
    </div>
    </body>
"""
# Hide Styles
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
# Page Config details
st.set_page_config(
        page_title = 'azureresourcenaming',
        page_icon = "📝",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )

def main():
    """
    This function contains the streamlit code details
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.header("Azure Resource Namer")
    st.write("A simple tool to help you name your Azure resources, based on the [Cloud Adoption Framework naming convention](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)")

    st.write('---')
    final = ''

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        #st.write('Resource type')
        #Host_Country1 = st.selectbox('Resource type',('Resource group', '', ''))
        # attribute is a string
        attribute = st.selectbox('Resource type', ['Select','General', 'Networking', 'Compute and Web', 'Containers', 'Databases', 'Storage', 'AI and Machine Learning', 'Analytics and IoT', 'Azure Virtual Desktop', \
                    'Developer Tools', 'Integration', 'Management and governance', 'Migration', 'Deprecated product names'],help='Resourcetype')
        #st.write('You selected:', Host_Country)
        if attribute == 'General':
            valuert = st.selectbox('Choose type', ["API management service instance", "Management group","Managed identity","Resource group","Policy definition"])
    with col2:
        #st.write('Workload')
        valuewl = st.text_input('Workload','myapp',help='workload')
    with col3:
        #st.write('Environment')
        valueev = st.text_input('Environment','prod',help='environment')
    with col4:
        #st.write('Region')
        #Host_Country4 = st.selectbox('Region',('West US', '', ''))
        attribute = st.selectbox('Region', ['Select','Africa','Asia Pacific','Canada','Europe','Middle East','South America','US'],help='region')
        if attribute == 'Africa':
            valuere = st.selectbox('Choose region', ["South Africa North", "South Africa West"])
        if attribute == 'Asia Pacific':
            valuere = st.selectbox('Choose region', ["Australia Central", "Australia Central 2","Australia East","Australia Southeast",\
                        "Central India","East Asia","Japan East","Japan West","Jio India Central","Jio India West","Korea Central",\
                        "Korea South","Southeast Asia","South India","West India"])
        if attribute == 'Canada':
            valuere = st.selectbox('Choose region', ["Canada Central", "Canada East"])
        if attribute == 'Europe':
            valuere = st.selectbox('Choose region', ["France Central", "France South", "Germany North", "Germany West Central", "North Europe",\
                        "Norway East","Norway West","Sweden Central","Switzerland North","Switzerland West","UK South","UK West","West Europe"])
        if attribute == 'Middle East':
            valuere = st.selectbox('Choose region', ["UAE Central", "UAE North"])
        if attribute == 'South America':
            valuere = st.selectbox('Choose region', ["Brazil South", "Brazil Southeast"])
        if attribute == 'US':
            valuere = st.selectbox('Choose region', ["Central US", "Central US EUAP","East US","East US 2","East US 2 EUAP","North Central US",\
                        "South Central US","West Central US","West US","West US 2","West US 3"])

    with col5:
        #st.write('Instance')
        #Host_Country5 = st.selectbox('Instance',('1', '', ''))
        valueit = st.number_input('Instance',1,help='instance')   

    st.write('---')
    final = "valuert" + '-' + valuewl + '-' + valueev + '-' + valuere + '-' + valueit

    st.subheader('Resource Name')
    st.text_area('',final,help="Final Resource Name")                     

# main function call
if __name__ == '__main__':
    main()