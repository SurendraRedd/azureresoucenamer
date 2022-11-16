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
        page_title = 'AzureNamingTool',
        page_icon = "🅰",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )

def main():
    """
    This function contains the streamlit code details
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.header("⛈Azure Resource Naming Tool")
    st.write("A simple tool to help you name your Azure resources, based on the [Cloud Adoption Framework naming convention](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)")

    st.write('---')
    final = ''
    valuewl = valueev = valueit = ""
    valuert = "rg"
    valuere = "westus"

    GENERAL = {"API management service instance":"apim","Management group":"mg","Managed identity":"id","Resource group":"rg","Policy definition":"policy"}
    NETWORKING = {'Application gateway':'agw','Application security group (ASG)':'asg','Bastion':'bas','CDN profile':'cdnp','CDN endpoint':'cdne',\
                    'Connections':'con','DNS':'dnsz','DNS zone':'pdnsz','Firewall':'afw','Firewall policy':'afwp','ExpressRoute circuit':'erc','Front Door instance':'fd','Front Door firewall policy':'fdfp',\
                    'Load balancer (internal)':'lbi','Load balancer (external)':'lbe','Load balancer rule':'rule','Local network gateway':'lgw','NAT gateway':'ng','Network interface (NIC)':'nic','Network security group (NSG)':'nsg',\
                    'Network security group (NSG) security rules':'nsgsr','Network Watcher':'nw','Private Link':'pl','Public IP address':'pip','Public IP address prefix':'ippre','Route filter':'rf','Route table':'rt','Service endpoint':'se',\
                    'Traffic Manager profile':'traf','User defined route (UDR)':'udr','Virtual network':'vnet','Virtual network peering':'peer','Virtual network subnet':'snet','Virtual WAN':'vwan','VPN Gateway':'vpng','VPN connection':'vcn','VPN site':'vst',\
                    'Virtual network gateway':'vgw','Web Application Firewall (WAF) policy':'waf','Web Application Firewall (WAF) policy rule group':'wafrg'}
    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        attribute = st.selectbox('Resource type', ['Select','General', 'Networking', 'Compute and Web', 'Containers', 'Databases', 'Storage', 'AI and Machine Learning', 'Analytics and IoT', 'Azure Virtual Desktop', \
                    'Developer Tools', 'Integration', 'Management and governance', 'Migration', 'Deprecated product names'],help='Resourcetype')
        if attribute == 'General':
            valuert= st.selectbox('Choose type', options=list(GENERAL.keys()))
            valuert = GENERAL.get(valuert)
        if attribute == 'Networking':
            valuert = st.selectbox('Choose type',options=list(NETWORKING.keys()))
            valuert = NETWORKING.get(valuert)
        if attribute == 'Compute and Web':
            valuert = st.selectbox('Choose type',['App Service environment','App Service plan','Availability set','Azure Arc enabled server','Azure Arc enabled Kubernetes cluster',\
                    'Cloud service','Disk encryption set','Function app','Gallery','Managed disk (OS)','Managed disk (data)','Notification Hubs','Notification Hubs namespace',\
                    'Snapshot','Static web app','Virtual machine','Virtual machine scale set','VM storage account','Web app'])
        if attribute == 'Containers':
            valuert = st.selectbox('Choose type', ["AKS cluster", "Container registry","Container instance","Service Fabric cluster"])
        if attribute == 'Databases':
            valuert = st.selectbox('Choose type', ["Azure Cosmos DB database", "Azure Cache for Redis instance","Azure SQL Database server","Azure SQL database",\
                    'Azure Synapse Analytics','Azure Synapse Analytics Workspaces','Azure Synapse Analytics SQL Dedicated Pool','Azure Synapse Analytics Spark Pool',\
                    'MySQL database','PostgreSQL database','SQL Server Stretch Database','SQL Managed Instance'])
        if attribute == 'Storage':
            valuert = st.selectbox('Choose type', ['Storage account','Azure StorSimple'])
        if attribute == 'AI and Machine Learning':
            valuert = st.selectbox('Choose type', ["Azure Cognitive Search", "Azure Cognitive Services","Azure Machine Learning workspace"])
        if attribute == 'Analytics and IoT':
            valuert = st.selectbox('Choose type', ['Azure Analysis Services server','Azure Databricks workspace','Azure Stream Analytics','Azure Data Explorer cluster',\
                        'Azure Data Explorer cluster database','Azure Data Factory','Data Lake Store account','Data Lake Analytics account','Event Hubs namespace',\
                        'Event hub','Event Grid domain','Event Grid subscriptions','Event Grid topic','HDInsight - Hadoop cluster','HDInsight - HBase cluster',\
                        'HDInsight - Kafka cluster','HDInsight - Spark cluster','HDInsight - Storm cluster','HDInsight - ML Services cluster','IoT hub',\
                        'Provisioning services','Provisioning services certificate','Power BI Embedded','Time Series Insights environment'])
        if attribute == 'Azure Virtual Desktop':
            valuert = st.selectbox('Choose type', ['Virtual desktop host pool','Virtual desktop application group','Virtual desktop workspace'])
        if attribute == 'Developer tools':
            valuert = st.selectbox('Choose type', ['App Configuration store','SignalR'])
        if attribute == 'Integration':
            valuert = st.selectbox('Choose type', ['Integration account','Logic apps','Service Bus','Service Bus queue','Service Bus topic'])
        if attribute == 'Management and governance':
            valuert = st.selectbox('Choose type', ['Automation account','Application Insights','Azure Monitor action group','Azure Purview instance',\
                        'Blueprint','Blueprint assignment','Key vault','Log Analytics workspace'])
        if attribute == 'Migration':
            valuert = st.selectbox('Choose type', ['Azure Migrate project','Database Migration Service instance','Recovery Services vault'])
        if attribute == 'Deprecated product names':
            valuert = st.selectbox('Choose type', ['Azure SQL Data Warehouse'])
    with col2:
        valuewl = st.text_input('Workload','myapp',help='workload')
    with col3:
        valueev = st.text_input('Environment','prod',help='environment')
    with col4:
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
        valueit = str(st.number_input('Instance',1,help='instance'))
        #valueit = str(st.slider('Instance',1,20,disabled=False,help='instance')) -> Slider input

    st.write('---')
    final = valuert + '-' + valuewl + '-' + valueev + '-' + valuere + '-' + valueit

    st.subheader('Resource Name')
    #st.text_area('FinalName',final,help="Final Resource Name")
    st.code(final, language="python")                     

# main function call
if __name__ == '__main__':
    main()