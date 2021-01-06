#!/usr/bin/env python3
from multiprocessing.pool import ThreadPool
from time import time as timer
from urllib.request import urlopen
import mmh3
import codecs
import sys
import ssl
import argparse
import os
import errno
from os import path



def main():
    urls = []
    c = 0
    a = {}
    for line in sys.stdin:
        if line.strip()[-1] == "/":
            urls.append(line.strip() + "favicon.ico")
        else:
            urls.append(line.strip() + "/favicon.ico")
    
    def fetch_url(url):
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            response = urlopen(url, timeout=5,context=ctx)
            favicon = codecs.encode(response.read(),"base64")
            hash = mmh3.hash(favicon)
            key = hash
            a.setdefault(key, [])
            a[key].append(url)

            return url, hash, None
        except Exception as e:
            return url, None, e

    start = timer()
    results = ThreadPool(20).imap_unordered(fetch_url, urls)
    for url, hash, error in results:
        if error is None:
            print("\u001b[32m[INFO]\u001b[0mFetched %r" % ( url[:-12]))
        else:
            print("\u001b[31m[ERR]\u001b[0m Not Fetched %r " % (url[:-12]))
    print("\n")
    print("-------------------------------------------------------------------")
    print("\u001b[32m[Favicon Hash Results] - \u001b[0m\n")
    for i,j in a.items():
        if len(j)>1:
            print("\u001b[33m[Hash]\u001b[0m " + "\u001b[32;1m" + str(i)+"\u001b[0m")
            for k in j:
                print("     " + k[:-12])
        else:
            print("\u001b[33m[Hash]\u001b[0m " + "\u001b[32;1m" + str(i)+"\u001b[0m")
            for k in j:
                print("     " + k[:-12])
        
        

    return a,urls

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description='FavFreak - a Favicon Hash based asset mapper')
        parser.add_argument('-o','--output' , help = 'Output file name')
        parser.add_argument('--shodan' , help = 'Prints Shodan Dorks', action='store_true')
        args = parser.parse_args()
        if os.name == 'nt':
            os.system('cls')
        banner = """\u001b[32m

    \u001b[31m_______ _______ \u001b[0m\u001b[32m_    _ _______  ______ _______ _______ _     _
    |______ |_____|  \  /  |______ |_____/ |______ |_____| |____/ 
    |       |     |   \/   |       |    \u001b[31m\_ |______\u001b[0m\u001b[32m |     | |    \_

                                \u001b[35m- Coded with \u001b[31m<3\u001b[0m\u001b[35m by Devansh Batham               
                                                        
           \u001b[0m 
        """
        print(banner)
        a,urls= main()

        # add your fingerprints here :
        
        fingerprint = {

            99395752:"slack-instance",
            116323821:"spring-boot",
            81586312:"Jenkins",
            -235701012:"Cnservers LLC",
            743365239:"Atlassian",
            2128230701:"Chainpoint",
            -1277814690:"LaCie",
            246145559:"Parse",
            628535358:"Atlassian",
            855273746:"JIRA",
            1318124267:"Avigilon",
            -305179312:"Atlassian – Confluence",
            786533217:"OpenStack",
            432733105:"Pi Star",
            705143395:"Atlassian",
            -1255347784:"Angular IO (AngularJS)",
            -1275226814:"XAMPP",
            -2009722838:"React",
            981867722:"Atlassian – JIRA",
            -923088984:"OpenStack",
            494866796:"Aplikasi",
            2110041688:"ระบบจองห้องประชุม",
            -493051473:"hxxp://www[.k2ie.net",
            1249285083:"Ubiquiti Aircube",
            -1379982221:"Atlassian – Bamboo",
            420473080:"Exostar – Managed Access Gateway",
            -1642532491:"Atlassian – Confluence",
            163842882:"Cisco Meraki",
            -1378182799:"Archivematica",
            -702384832:"TCN",
            -532394952:"CX",
            -183163807:"Ace",
            552727997:"Atlassian – JIRA",
            1302486561:"NetData",
            -609520537:"OpenGeo Suite",
            -1961046099:"Dgraph Ratel",
            -1581907337:"Atlassian – JIRA",
            1913538826:"Material Dashboard",
            1319699698:"Form.io",
            -1203021870:"Kubeflow",
            -182423204:"netdata dashboard",
            988422585:"CapRover",
            2113497004:"WiJungle",
            1234311970:"Onera",
            430582574:"SmartPing",
            1232596212:"OpenStack",
            1585145626:"netdata dashboard",
            -219752612:"FRITZ!Box",
            -697231354:"Ubiquiti – AirOS",
            945408572:"Fortinet – Forticlient",
            1768726119:"Outlook Web Application",
            2109473187:"Huawei – Claro",
            552592949:"ASUS AiCloud",
            631108382:"SonicWALL",
            708578229:"Google",
            -134375033:"Plesk",
            2019488876:"Dahua Storm (IP Camera)",
            -1395400951:"Huawei – ADSL/Router",
            1601194732:"Sophos Cyberoam (appliance)",
            -325082670:"LANCOM Systems",
            -1050786453:"Plesk",
            -1346447358:"TilginAB (HomeGateway)",
            1410610129:"Supermicro Intelligent Management (IPMI)",
            -440644339:"Zyxel ZyWALL",
            363324987:"Dell SonicWALL",
            -1446794564:"Ubiquiti Login Portals",
            1045696447:"Sophos User Portal/VPN Portal",
            -297069493:"Apache Tomcat",
            396533629:"OpenVPN",
            1462981117:"Cyberoam",
            1772087922:"ASP.net favicon",
            1594377337:"Technicolor",
            165976831:"Vodafone (Technicolor)",
            -1677255344:"UBNT Router UI",
            -359621743:"Intelbras Wireless",
            -677167908:"Kerio Connect (Webmail)",
            878647854:"BIG-IP",
            442749392:"Microsoft OWA",
            1405460984:"pfSense",
            -271448102:"iKuai Networks",
            31972968:"Dlink Webcam",
            970132176:"3CX Phone System",
            -1119613926:"Bluehost",
            123821839:"Sangfor",
            459900502:"ZTE Corporation (Gateway/Appliance)",
            -2069844696:"Ruckus Wireless",
            -1607644090:"Bitnami",
            2141724739:"Juniper Device Manager",
            1835479497:"Technicolor Gateway",
            1278323681:"Gitlab",
            -1929912510:"NETASQ - Secure / Stormshield",
            -1255992602:"VMware Horizon",
            1895360511:"VMware Horizon",
            -991123252:"VMware Horizon",
            1642701741:"Vmware Secure File Transfer",
            -266008933:"SAP Netweaver",
            -1967743928:"SAP ID Service: Log On",
            1347937389:"SAP Conversational AI",
            602431586:"Palo Alto Login Portal",
            -318947884:"Palo Alto Networks",
            1356662359:"Outlook Web Application",
            1453890729:"Webmin",
            -1814887000:"Docker",
            1937209448:"Docker",
            -1544605732:"Amazon",
            716989053:"Amazon",
            -1010568750:"phpMyAdmin",
            -1240222446:"Zhejiang Uniview Technologies Co.",
            -986678507:"ISP Manager",
            -1616143106:"AXIS (network cameras)",
            -976235259:"Roundcube Webmail",
            768816037:"UniFi Video Controller (airVision)",
            1015545776:"pfSense",
            1838417872:"Freebox OS",
            1188645141:"hxxps://www.hws[.com/?host",
            547282364:"Keenetic",
            -1571472432:"Sierra Wireless Ace Manager (Airlink)",
            149371702:"Synology DiskStation",
            -1169314298:"INSTAR IP Cameras",
            -1038557304:"Webmin",
            1307375944:"Octoprint (3D printer)",
            1280907310:"Webmin",
            1954835352:"Vesta Hosting Control Panel",
            509789953:"Farming Simulator Dedicated Server",
            -1933493443:"Residential Gateway",
            1993518473:"cPanel Login",
            -1477563858:"Arris",
            -895890586:"PLEX Server",
            -1354933624:"Dlink Webcam",
            944969688:"Deluge",
            479413330:"Webmin",
            -359621743:"Intelbras Wireless",
            -435817905:"Cambium Networks",
            -981606721:"Plesk",
            833190513:"Dahua Storm (IP Camera)",
            -1314864135:10,
            -652508439:"Parallels Plesk Panel",
            -569941107:"Fireware Watchguard",
            1326164945:"Shock&Innovation!! netis setup",
            -1738184811:"cacaoweb",
            904434662:"Loxone (Automation)",
            905744673:"HP Printer / Server",
            902521196:"Netflix",
            -2063036701:"Linksys Smart Wi-Fi",
            -1205024243:"lwIP (A Lightweight TCP/IP stack)",
            607846949:"Hitron Technologies",
            1281253102:"Dahua Storm (DVR)",
            661332347:"MOBOTIX Camera",
            -520888198:"Blue Iris (Webcam)",
            104189364:"Vigor Router",
            1227052603:"Alibaba Cloud (Block Page)",
            252728887:"DD WRT (DD-WRT milli_httpd)",
            -1922044295:"Mitel Networks (MiCollab End User Portal)",
            1221759509:"Dlink Webcam",
            1037387972:"Dlink Router",
            -655683626:"PRTG Network Monitor",
            1611729805:"Elastic (Database)",
            1144925962:"Dlink Webcam",
            -1666561833:"Wildfly",
            804949239:"Cisco Meraki Dashboard",
            -459291760:"Workday",
            1734609466:"JustHost",
            -1507567067:"Baidu (IP error page)",
            2006716043:"Intelbras SA",
            -1298108480:"Yii PHP Framework (Default Favicon)",
            1782271534:"truVision NVR (interlogix)",
            603314:"Redmine",
            -476231906:"phpMyAdmin",
            -646322113:"Cisco (eg:Conference Room Login Page)",
            -629047854:"Jetty 404",
            -1351901211:"Luma Surveillance",
            -519765377:"Parallels Plesk Panel",
            -2144363468:"HP Printer / Server",
            -127886975:"Metasploit",
            1139788073:"Metasploit",
            -1235192469:"Metasploit",
            1876585825:"ALIBI NVR",
            -1810847295:"Sangfor",
            -291579889:"Websockets test page (eg: port 5900)",
            1629518721:"macOS Server (Apple)",
            -986816620:"OpenRG",
            -299287097:"Cisco Router",
            -1926484046:"Sangfor",
            -873627015:"HeroSpeed Digital Technology Co. (NVR/IPC/XVR)",
            2071993228:"Nomadix Access Gateway",
            516963061:"Gitlab",
            -38580010:"Magento",
            1490343308:"MK-AUTH",
            -632583950:"Shoutcast Server",
            95271369:"FireEye",
            1476335317:"FireEye",
            -842192932:"FireEye",
            105083909:"FireEye",
            240606739:"FireEye",
            2121539357:"FireEye",
            -333791179:"Adobe Campaign Classic",
            -1437701105:"XAMPP",
            -676077969:"Niagara Web Server",
            -2138771289:"Technicolor",
            711742418:"Hitron Technologies Inc.",
            728788645:"IBM Notes",
            1436966696:"Barracuda",
            86919334:"ServiceNow",
            1211608009:"Openfire Admin Console",
            2059618623:"HP iLO",
            1975413433:"Sunny WebBox",
            943925975:"ZyXEL",
            281559989:"Huawei",
            -2145085239:"Tenda Web Master",
            -1399433489:"Prometheus Time Series Collection and Processing Server",
            1786752597:"wdCP cloud host management system",
            90680708:"Domoticz (Home Automation)",
            -1441956789:"Tableau",
            -675839242:"openWRT Luci",
            1020814938:"Ubiquiti – AirOS",
            -766957661:"MDaemon Webmail",
            119741608:"Teltonika",
            1973665246:"Entrolink",
            74935566:"WindRiver-WebServer",
            -1723752240:"Microhard Systems",
            -1807411396:"Skype",
            -1612496354:"Teltonika",
            1877797890:"Eltex (Router)",
            -375623619:"bintec elmeg",
            1483097076:"SyncThru Web Service (Printers)",
            1169183049:"BoaServer",
            1051648103:"Securepoint",
            -438482901:"Moodle",
            -1492966240:"RADIX",
            1466912879:"CradlePoint Technology (Router)",
            -167656799:"Drupal",
            -1593651747:"Blackboard",
            -895963602:"Jupyter Notebook",
            -972810761:"HostMonster - Web hosting",
            1703788174:"D-Link (router/network)",
            225632504:"Rocket Chat",
            -1702393021:"mofinetwork",
            892542951:"Zabbix",
            547474373:"TOTOLINK (network)",
            -374235895:"Ossia (Provision SR) | Webcam/IP Camera",
            1544230796:"cPanel Login",
            517158172:"D-Link (router/network)",
            462223993:"Jeedom (home automation)",
            937999361:"JBoss Application Server 7",
            1991562061:"Niagara Web Server / Tridium",
            812385209:"Solarwinds Serv-U FTP Server",
            1142227528:"Aruba (Virtual Controller)",
            -1153950306:"Dell",
            72005642:"RemObjects SDK / Remoting SDK for .NET HTTP Server Microsoft",
            -484708885:"Zyxel ZyWALL",
            706602230:"VisualSVN Server",
            -656811182:"Jboss",
            -332324409:"STARFACE VoIP Software",
            -594256627:"Netis (network devices)",
            -649378830:"WHM",
            97604680:"Tandberg",
            -1015932800:"Ghost (CMS)",
            -194439630:"Avtech IP Surveillance (Camera)",
            129457226:"Liferay Portal",
            -771764544:"Parallels Plesk Panel",
            -617743584:"Odoo",
            77044418:"Polycom",
            980692677:"Cake PHP",
            476213314:"Exacq",
            794809961:"CheckPoint",
            1157789622:"Ubiquiti UNMS",
            1244636413:"cPanel Login",
            1985721423:"WorldClient for Mdaemon",
            -1124868062:"Netport Software (DSL)",
            -335242539:"f5 Big IP",
            2146763496:"Mailcow",
            -1041180225:"QNAP NAS Virtualization Station",
            -1319025408:"Netgear",
            917966895:"Gogs",
            512590457:"Trendnet IP camera",
            1678170702:"Asustor",
            -1466785234:"Dahua",
            -505448917:"Discuz!",
            255892555:"wdCP cloud host management system",
            1627330242:"Joomla",
            -1935525788:"SmarterMail",
            -12700016:"Seafile",
            1770799630:"bintec elmeg",
            -137295400:"NETGEAR ReadyNAS",
            -195508437:"iPECS",
            -2116540786:"bet365",
            -38705358:"Reolink",
            -450254253:"idera",
            -1630354993:"Proofpoint",
            -1678298769:"Kerio Connect WebMail",
            -35107086:"WorldClient for Mdaemon",
            2055322029:"Realtek",
            -692947551:"Ruijie Networks (Login)",
            -1710631084:"Askey Cable Modem",
            89321398:"Askey Cable Modem",
            90066852:"JAWS Web Server (IP Camera)",
            768231242:"JAWS Web Server (IP Camera)",
            -421986013:"Homegrown Website Hosting",
            156312019:"Technicolor / Thomson Speedtouch (Network / ADSL)",
            -560297467:"DVR (Korean)",
            -1950415971:"Joomla",
            1842351293:"TP-LINK (Network Device)",
            1433417005:"Salesforce",
            -632070065:"Apache Haus",
            1103599349:"Untangle",
            224536051:"Shenzhen coship electronics co.",
            1038500535:"D-Link (router/network)",
            -355305208:"D-Link (camera)",
            -267431135:"Kibana",
            -759754862:"Kibana",
            -1200737715:"Kibana",
            75230260:"Kibana",
            1668183286:"Kibana",
            283740897:"Intelbras SA",
            1424295654:"Icecast Streaming Media Server",
            1922032523:"NEC WebPro",
            -1654229048:"Vivotek (Camera)",
            -1414475558:"Microsoft IIS",
            -1697334194:"Univention Portal",
            -1424036600:"Portainer (Docker Management)",
            -831826827:"NOS Router",
            -759108386:"Tongda",
            -1022206565:"CrushFTP",
            -1225484776:"Endian Firewall",
            -631002664:"Kerio Control Firewall",
            2072198544:"Ferozo Panel",
            -466504476:"Kerio Control Firewall",
            1251810433:"Cafe24 (Korea)",
            1273982002:"Mautic (Open Source Marketing Automation)",
            -978656757:"NETIASPOT (Network)",
            916642917:"Multilaser",
            575613323:"Canvas LMS (Learning Management)",
            1726027799:"IBM Server",
            -587741716:"ADB Broadband S.p.A. (Network)",
            -360566773:"ARRIS (Network)",
            -884776764:"Huawei (Network)",
            929825723:"WAMPSERVER",
            240136437:"Seagate Technology (NAS)",
            1911253822:"UPC Ceska Republica (Network)",
            -393788031:"Flussonic (Video Streaming)",
            366524387:"Joomla",
            443944613:"WAMPSERVER",
            1953726032:"Metabase",
            -2031183903:"D-Link (Network)",
            545827989:"MobileIron",
            967636089:"MobileIron",
            362091310:"MobileIron",
            2086228042:"MobileIron",
            -1588746893:"CommuniGate",
            1427976651:"ZTE (Network)",
            1648531157:"InfiNet Wireless | WANFleX (Network)",
            938616453:"Mersive Solstice",
            1632780968:"Université Toulouse 1 Capitole",
            2068154487:"Digium (Switchvox)",
            -1788112745:"PowerMTA monitoring",
            -644617577:"SmartLAN/G",
            -1822098181:"Checkpoint (Gaia)",
            -1131689409:"УТМ (Federal Service for Alcohol Market Regulation | Russia)",
            2127152956:"MailWizz",
            1064742722:"RabbitMQ",
            -693082538:"openmediavault (NAS)",
            1941381095:"openWRT Luci",
            903086190:"Honeywell",
            829321644:"BOMGAR Support Portal",
            -1442789563:"Nuxt JS",
            -2140379067:"RoundCube Webmail",
            -1897829998:"D-Link (camera)",
            1047213685:"Netgear (Network)",
            1485257654:"SonarQube",
            -299324825:"Lupus Electronics XT",
            -1162730477:"Vanderbilt SPC",
            -1268095485:"VZPP Plesk",
            1118684072:"Baidu",
            -1616115760:"ownCloud",
            -2054889066:"Sentora",
            1333537166:"Alfresco",
            -373674173:"Digital Keystone (DK)",
            -106646451:"WISPR (Airlan)",
            1235070469:"Synology VPN Plus",
            2063428236:"Sentry",
            15831193:"WatchGuard",
            -956471263:"Web Client Pro",
            -1452159623:"Tecvoz",
            99432374:"MDaemon Remote Administration",
            727253975:"Paradox IP Module",
            -630493013:"DokuWiki",
            552597979:"Sails",
            774252049:"FastPanel Hosting",
            -329747115:"C-Lodop",
            1262005940:"Jamf Pro Login",
            979634648:"StruxureWare (Schneider Electric)",
            475379699:"Axcient Replibit Management Server",
            -878891718:"Twonky Server (Media Streaming)",
            -2125083197:"Windows Azure",
            -1151675028:"ISP Manager (Web Hosting Panel)",
            1248917303:"JupyterHub",
            -1908556829:"CenturyLink Modem GUI Login (eg: Technicolor)",
            1059329877:"Tecvoz",
            -1148190371:"OPNsense",
            1467395679:"Ligowave (network)",
            -1528414776:"Rumpus",
            -2117390767:"Spiceworks (panel)",
            -1944119648:"TeamCity",
            -1748763891:"INSTAR Full-HD IP-Camera",
            251106693:"GPON Home Gateway",
            -1779611449:"Alienvault",
            -1745552996:"Arbor Networks",
            -1275148624:"Accrisoft",
            -178685903:"Yasni",
            -43161126:"Slack",
            671221099:"innovaphone",
            -10974981:"Shinobi (CCTV)",
            1274078387:"TP-LINK (Network Device)",
            -336242473:"Siemens OZW772",
            882208493:"Lantronix (Spider)",
            -687783882:"ClaimTime (Ramsell Public Health & Safety)",
            -590892202:"Surfilter SSL VPN Portal",
            -50306417:"Kyocera (Printer)",
            784872924:"Lucee!",
            1135165421:"Ricoh",
            926501571:"Handle Proxy",
            579239725:"Metasploit",
            -689902428:"iomega NAS",
            -600508822:"iomega NAS",
            656868270:"iomega NAS",
            -2056503929:"iomega NAS",
            -1656695885:"iomega NAS",
            331870709:"iomega NAS",
            1241049726:"iomega NAS",
            998138196:"iomega NAS",
            322531336:"iomega NAS",
            -401934945:"iomega NAS",
            -613216179:"iomega NAS",
            -276759139:"Chef Automate",
            1862132268:"Gargoyle Router Management Utility",
            -1738727418:"KeepItSafe Management Console",
            -368490461:"Entronix Energy Management Platform",
            1836828108:"OpenProject",
            -1775553655:"Unified Management Console (Polycom)",
            381100274:"Moxapass ioLogik Remote Ethernet I/O Server ",
            2124459909:"HFS (HTTP File Server)",
            731374291:"HFS (HTTP File Server)",
            -335153896:"Traccar GPS tracking",
            896412703:"IW",
            191654058:"Wordpress Under Construction Icon",
            -342262483:"Combivox",
            5542029:"NetComWireless (Network)",
            1552860581:"Elastic (Database)",
            1174841451:"Drupal",
            -1093172228:"truVision (NVR)",
            -1688698891:"SpamExperts",
            -1546574541:"Sonatype Nexus Repository Manager",
            -256828986:"iDirect Canada (Network Management)",
            1966198264:"OpenERP (now known as Odoo)",
            2099342476:"PKP (OpenJournalSystems) Public Knowledge Project",
            541087742:"LiquidFiles",
            -882760066:"ZyXEL (Network)",
            16202868:"Universal Devices (UD)",
            987967490:"Huawei (Network)",
            -647318973:"gm77[.]com",
            -1583478052:"Okazik[.]pl",
            1969970750:"Gitea",
            -1734573358:"TC-Group",
            -1589842876:"Deluge Web UI",
            1822002133:"登录 – AMH",
            -2006308185:"OTRS (Open Ticket Request System)",
            -1702769256:"Bosch Security Systems (Camera)",
            321591353:"Node-RED",
            -923693877:"motionEye (camera)",
            -1547576879:"Saia Burgess Controls – PCD",
            1479202414:"Arcadyan o2 box (Network)",
            1081719753:"D-Link (Network)",
            -166151761:"Abilis (Network/Automation)",
            -1231681737:"Ghost (CMS)",
            321909464:"Airwatch",
            -1153873472:"Airwatch",
            1095915848:"Airwatch",
            788771792:"Airwatch",
            -1863663974:"Airwatch",
            -1267819858:"KeyHelp (Keyweb AG)",
            726817668:"KeyHelp (Keyweb AG)",
            -1474875778:"GLPI",
            5471989:"Netcom Technology",
            -1457536113:"CradlePoint",
            -736276076:"MyASP",
            -1343070146:"Intelbras SA",
            538585915:"Lenel",
            -625364318:"OkoFEN Pellematic",
            1117165781:"SimpleHelp (Remote Support)",
            -1067420240:"GraphQL",
            -1465479343:"DNN (CMS)",
            1232159009:"Apple",
            1382324298:"Apple",
            -1498185948:"Apple",
            483383992:"ISPConfig",
            -1249852061:"Microsoft Outlook",
            999357577:"? (Possibly DVR)",
            492290497:"? (Possible IP Camera)",
            400100893:"? (DVR)",
            -1252041730:"Vue.js",
            180732787:"Apache Flink"
            }





        print("\n")
        print("-------------------------------------------------------------------")
        print("\u001b[32m[FingerPrint Based Detection Results] - \u001b[0m\n")
        for i in a.keys():
            if i in fingerprint.keys():
                print("\u001b[31m["+fingerprint[i]+"] \u001b[0m" + str(i) + " - count : " + str(len(a[i])))
               # print('\n'.join(a[i][:-12]))
                if len(a[i]) > 0:
                    for k in a[i]:
                        print("     " + k[:-12])
        
                

        print("\n")
        if args.shodan:
            print("-------------------------------------------------------------------")
            print("\u001b[32m[Shodan Dorks] - \u001b[0m\n")
            for i in a.keys():
                if i != 0:
                    print("\u001b[34m[DORK]\u001b[0m org:\"Target-Name\" http.favicon.hash:"+str(i))

        if args.output:
            for i in a.keys():
                filename = args.output + "/" + str(i) + ".txt"
                if path.exists(filename):
                    os.remove(filename)
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.makedirs(os.path.dirname(filename))
                    except OSError as exc: 
                        if exc.errno != errno.EEXIST:
                            raise
            
                with open(filename, "a") as f:
                    f.write('\n'.join(a[i]))
                    f.write("\n")
        print("-------------------------------------------------------------------")
        print("\u001b[32m[Summary]\u001b[0m\n")
        print(" \u001b[36mcount      \u001b[35mHash\u001b[0m         ")
        for i in a.keys():
            print(f"~ \u001b[36m[{len(a[i])}]  : \u001b[35m[{i}]\u001b[0m ")
        if args.output:
            print(f"\n\u001b[32m[+] Output saved here : {args.output}\u001b[0m")
    except KeyboardInterrupt:
        print("\n\u001b[31m[EXIT]KeyBoard Interrucpt Encountered \u001b[0m")
