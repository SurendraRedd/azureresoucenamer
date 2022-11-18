"""
Azure Resource Naming Application using streamlit
Author: Surendra Reddy

This application contains the code related to the
Azure Resource Namer application.
"""
# Required packages importing
import streamlit as st
from streamlit_player import st_player
import base64

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
        page_title = 'Azureresourcenaming',
        page_icon = "🅰",
        layout = "wide",
        initial_sidebar_state = "expanded"
    )

def main():
    """
    This function contains the streamlit code details
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    st.header("📘Azure Resource Naming Tool")

    with st.expander('Demo'):
        # Embed a youtube video
        #st_player("https://youtu.be/5p-z_-6T57g")
        file_ = open("streamlit-app-2022-11-17-00-11-60.gif", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" alt="name gif">',
            unsafe_allow_html=True,
        )


    st.write("A simple tool to help you name your Azure resources, based on the [Cloud Adoption Framework naming convention](https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/ready/azure-best-practices/resource-naming)")
    st.write('\n')
    col1,col2=st.columns(2)
    with col1:
        st.image('https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/_images/ready/resource-naming.png',use_column_width=True,caption="Example Resource Naming")
    with col2:
        pass
        #st.image('https://learn.microsoft.com/en-us/azure/cloud-adoption-framework/_images/ready/resource-naming-scope.png')


    final = ''
    valuewl = valueev = valueit = ""
    valuert = "default"
    valuere = "default"

    GENERAL = {"API management service instance":"apim","Management group":"mg","Managed identity":"id","Resource group":"rg","Policy definition":"policy"}
    NETWORKING = {'Application gateway':'agw','Application security group (ASG)':'asg','Bastion':'bas','CDN profile':'cdnp','CDN endpoint':'cdne',\
                    'Connections':'con','DNS':'dnsz','DNS zone':'pdnsz','Firewall':'afw','Firewall policy':'afwp','ExpressRoute circuit':'erc','Front Door instance':'fd','Front Door firewall policy':'fdfp',\
                    'Load balancer (internal)':'lbi','Load balancer (external)':'lbe','Load balancer rule':'rule','Local network gateway':'lgw','NAT gateway':'ng','Network interface (NIC)':'nic','Network security group (NSG)':'nsg',\
                    'Network security group (NSG) security rules':'nsgsr','Network Watcher':'nw','Private Link':'pl','Public IP address':'pip','Public IP address prefix':'ippre','Route filter':'rf','Route table':'rt','Service endpoint':'se',\
                    'Traffic Manager profile':'traf','User defined route (UDR)':'udr','Virtual network':'vnet','Virtual network peering':'peer','Virtual network subnet':'snet','Virtual WAN':'vwan','VPN Gateway':'vpng','VPN connection':'vcn','VPN site':'vst',\
                    'Virtual network gateway':'vgw','Web Application Firewall (WAF) policy':'waf','Web Application Firewall (WAF) policy rule group':'wafrg'}
    COMPUTE_WEB = {'App Service environment':'ase','App Service plan':'plan','Availability set':'avail','Azure Arc enabled server':'arcs','Azure Arc enabled Kubernetes cluster':'arck',\
                    'Cloud service':'cld','Disk encryption set':'des','Function app':'func','Gallery':'gal','Managed disk (OS)':'osdisk','Managed disk (data)':'disk','Notification Hubs':'ntf','Notification Hubs namespace':'ntfns',\
                    'Snapshot':'snap','Static web app':'stapp','Virtual machine':'vm','Virtual machine scale set':'vmss','VM storage account':'stvm','Web app':'app'}    
    CONTAINERS = {"AKS cluster":'aks', "Container registry":'cr',"Container instance":'ci',"Service Fabric cluster":'sf'}
    DATABASES = {"Azure Cosmos DB database":'cosmos', "Azure Cache for Redis instance":'redis',"Azure SQL Database server":'sql',"Azure SQL database":'sqldb',\
                    'Azure Synapse Analytics':'syn','Azure Synapse Analytics Workspaces':'synw','Azure Synapse Analytics SQL Dedicated Pool':'syndp','Azure Synapse Analytics Spark Pool':'synsp',\
                    'MySQL database':'mysql','PostgreSQL database':'psql','SQL Server Stretch Database':'sqlstrdb','SQL Managed Instance':'sqlmi'}
    STORAGE ={'Storage account':'st','Azure StorSimple':'ssimp'}
    AIML = {"Azure Cognitive Search":'srch', "Azure Cognitive Services":'cog',"Azure Machine Learning workspace":'mlw'}
    ANALYTICSIOT = {'Azure Analysis Services server':'as','Azure Databricks workspace':'dbw','Azure Stream Analytics':'asa','Azure Data Explorer cluster':'dec',\
                        'Azure Data Explorer cluster database':'dedb','Azure Data Factory':'adf','Data Lake Store account':'dls','Data Lake Analytics account':'dla','Event Hubs namespace':'evhns',\
                        'Event hub':'evh','Event Grid domain':'evgd','Event Grid subscriptions':'evgs','Event Grid topic':'evgt','HDInsight - Hadoop cluster':'hadoop','HDInsight - HBase cluster':'hbase',\
                        'HDInsight - Kafka cluster':'kafka','HDInsight - Spark cluster':'spark','HDInsight - Storm cluster':'storm','HDInsight - ML Services cluster':'mls','IoT hub':'iot',\
                        'Provisioning services':'provs','Provisioning services certificate':'pcert','Power BI Embedded':'pbi','Time Series Insights environment':'tsi'}
    VIRTUALDESKTOP = {'Virtual desktop host pool':'vdpool','Virtual desktop application group':'vdag','Virtual desktop workspace':'vdws'}
    DEVELOPERTOOLS = {'App Configuration store':'appcs','SignalR':'sigr'}
    INTEGRATION = {'Integration account':'ia','Logic apps':'logic','Service Bus':'sb','Service Bus queue':'sbq','Service Bus topic':'sbt'}
    MNGMTGOV={'Automation account':'aa','Application Insights':'appi','Azure Monitor action group':'ag','Azure Purview instance':'pview',\
                        'Blueprint':'bp','Blueprint assignment':'bpa','Key vault':'kv','Log Analytics workspace':'log'}
    MIGRATION={'Azure Migrate project':'migr','Database Migration Service instance':'dms','Recovery Services vault':'rsv'}
    DEPRECATED={'Azure SQL Data Warehouse':'sqldw'}                    
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        attribute = st.selectbox('Resource Type', ['Select','General', 'Networking', 'Compute and Web', 'Containers', 'Databases', 'Storage', 'AI and Machine Learning', 'Analytics and IoT', 'Azure Virtual Desktop', \
                    'Developer Tools', 'Integration', 'Management and governance', 'Migration', 'Deprecated product names'],help='Resourcetype')
        if attribute == 'General':
            valuert= st.selectbox('Choose type', options=list(GENERAL.keys()))
            valuert = GENERAL.get(valuert)
        if attribute == 'Networking':
            valuert = st.selectbox('Choose type',options=list(NETWORKING.keys()))
            valuert = NETWORKING.get(valuert)
        if attribute == 'Compute and Web':
            valuert = st.selectbox('Choose type',options=list(COMPUTE_WEB.keys()))
            valuert = COMPUTE_WEB.get(valuert)
        if attribute == 'Containers':
            valuert = st.selectbox('Choose type', options=list(CONTAINERS.keys()))
            valuert = CONTAINERS.get(valuert)
        if attribute == 'Databases':
            valuert = st.selectbox('Choose type', options=list(DATABASES.keys()))
            valuert = DATABASES.get(valuert)
        if attribute == 'Storage':
            valuert = st.selectbox('Choose type', options=list(STORAGE.keys()))
            valuert = STORAGE.get(valuert)
        if attribute == 'AI and Machine Learning':
            valuert = st.selectbox('Choose type', options=list(AIML.keys()))
            valuert = AIML.get(valuert)
        if attribute == 'Analytics and IoT':
            valuert = st.selectbox('Choose type', options=list(ANALYTICSIOT.keys()))
            valuert = ANALYTICSIOT.get(valuert)
        if attribute == 'Azure Virtual Desktop':
            valuert = st.selectbox('Choose type', options=list(VIRTUALDESKTOP.keys()))
            valuert = VIRTUALDESKTOP.get(valuert)
        if attribute == 'Developer tools':
            valuert = st.selectbox('Choose type', options=list(DEVELOPERTOOLS.keys()))
            valuert = DEVELOPERTOOLS.get(valuert)
        if attribute == 'Integration':
            valuert = st.selectbox('Choose type', options=list(INTEGRATION.keys()))
            valuert = INTEGRATION.get(valuert)
        if attribute == 'Management and governance':
            valuert = st.selectbox('Choose type', options=list(MNGMTGOV.keys()))
            valuert = MNGMTGOV.get(valuert)
        if attribute == 'Migration':
            valuert = st.selectbox('Choose type', options=list(MIGRATION.keys()))
            valuert = MIGRATION.get(valuert)
        if attribute == 'Deprecated product names':
            valuert = st.selectbox('Choose type', options=list(DEPRECATED.keys()))
            valuert = DEPRECATED.get(valuert)
    with col2:
        valuewl = st.text_input('Workload/Application','myapp',help='workload or application')
    with col3:
        valueev = st.text_input('Environment','prod',help='environment')
    with col4:
        attribute = st.selectbox('Azure Region', ['Select','Africa','Asia Pacific','Canada','Europe','Middle East','South America','US'],help='region')
        if attribute == 'Africa':
            valuere = st.selectbox('Choose region', ["South Africa North", "South Africa West"])
            valuere = valuere.replace(" ", "").lower()
        if attribute == 'Asia Pacific':
            valuere = st.selectbox('Choose region', ["Australia Central", "Australia Central 2","Australia East","Australia Southeast",\
                        "Central India","East Asia","Japan East","Japan West","Jio India Central","Jio India West","Korea Central",\
                        "Korea South","Southeast Asia","South India","West India"])
            valuere = valuere.replace(" ", "").lower()
        if attribute == 'Canada':
            valuere = st.selectbox('Choose region', ["Canada Central", "Canada East"])
            valuere = valuere.replace(" ", "").lower()
        if attribute == 'Europe':
            valuere = st.selectbox('Choose region', ["France Central", "France South", "Germany North", "Germany West Central", "North Europe",\
                        "Norway East","Norway West","Sweden Central","Switzerland North","Switzerland West","UK South","UK West","West Europe"])
            valuere = valuere.replace(" ", "").lower()
        if attribute == 'Middle East':
            valuere = st.selectbox('Choose region', ["UAE Central", "UAE North"])
            valuere = valuere.replace(" ", "").lower()
        if attribute == 'South America':
            valuere = st.selectbox('Choose region', ["Brazil South", "Brazil Southeast"])
            valuere = valuere.replace(" ", "").lower()
        if attribute == 'US':
            valuere = st.selectbox('Choose region', ["Central US", "Central US EUAP","East US","East US 2","East US 2 EUAP","North Central US",\
                        "South Central US","West Central US","West US","West US 2","West US 3"])
            valuere = valuere.replace(" ", "").lower()

    with col5:
        valueit = str(st.number_input('Instance',1,help='instance'))
        #valueit = str(st.slider('Instance',1,20,disabled=False,help='instance')) -> Slider input

    st.write('---')
    final = valuert + '-' + valuewl + '-' + valueev + '-' + valuere + '-' + valueit

    st.subheader('Resource Name')
    #st.text_area('FinalName',final,help="Final Resource Name")
    st.code(final, language="python")
    st.write('\n')                     

    URL = 'https://azureresoucenamer.streamlit.app/'
    PRJ = 'https://github.com/users/SurendraRedd/projects/4'
    DIS = 'https://github.com/SurendraRedd/azureresoucenamer/discussions'

    one,two=st.columns(2)
    with one:
        with st.expander('Share This Tool'):
            st.write(URL)
            st.markdown(f'''
                    <a href={URL}><button style="background-color:LightBlue;">AzureResourceNamingTool</button></a>
                    ''',
                    unsafe_allow_html=True)
    with two:
        with st.expander('Raise an Issue'):
            st.write(PRJ)
            st.write(DIS)
            st.markdown(f'''
                    [![Gitter](https://badges.gitter.im/discussions2021/community.svg)](https://gitter.im/discussions2021/community?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
                    ''',unsafe_allow_html=True)


# main function call
if __name__ == '__main__':
    main()
