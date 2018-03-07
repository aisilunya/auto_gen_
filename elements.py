import params
from check_features import *


def addWlanWidget(type_wlan, widget_list):
    if type_wlan == 'wifi2_widget':
        wifi2_element = []
        for i in widget_list:
            if ".".join(i.split(".")[-2::]) == "WPS.Enable":
                if {"name": i, "pr": ".".join(i.split(".")[-2::]), "mFunction": "convert_enabled"} not in wifi2_element:
                    wifi2_element.append(
                        {"name": i, "pr": ".".join(i.split(".")[-2::]), "mFunction": "convert_enabled"})
            elif i.endswith(".Enable"):
                if {"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled"} not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled", \
                                          "changeFlow":"WLAN_Settings_Sample_for_2gh"})
            elif i.endswith(".Status"):
                if {"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"} not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"})
            elif i.endswith(".WMMEnable"):
                if {"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"} not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"})
            elif i.endswith(".TotalBytesReceived") \
                    or i.endswith(".TotalBytesSent"):
                if {"name": i, "pr": i.split(".")[-1], "mFunction": "convert_traffic"} not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_traffic"})
            elif i.endswith(".SSID"):
                if {"name": i, "pr": i.split(".")[-1], "mFunction": "bold"} not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "bold"})
            elif i.endswith('.BeaconType'):
                if ({"name": i, "pr": i.split(".")[-1], "mFunction": "encryption_type"}) \
                        not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "encryption_type"})
            else:
                if {"name": i, "pr": i.split(".")[-1]} not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1]})

        return wifi2_element

    if type_wlan == 'wifi5_widget':
        wifi2_element = []
        for i in widget_list:
            if ".".join(i.split(".")[-2::]) == "WPS.Enable":
                if {"name": i, "pr": ".".join(i.split(".")[-2::]), "mFunction": "convert_enabled"} not in wifi2_element:
                    wifi2_element.append(
                        {"name": i, "pr": ".".join(i.split(".")[-2::]), "mFunction": "convert_enabled"})
            elif i.endswith(".Enable"):
                if {"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled"} not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled",\
                                          "changeFlow":"WLAN_Settings_Sample_for_5gh"})
            elif i.endswith(".Status"):
                if {"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"} not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"})
            elif i.endswith(".WMMEnable"):
                if {"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"} not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"})
            elif i.endswith(".TotalBytesReceived") \
                    or i.endswith(".TotalBytesSent"):
                if {"name": i, "pr": i.split(".")[-1], "mFunction": "convert_traffic"} not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_traffic"})
            elif i.endswith(".SSID"):
                if {"name": i, "pr": i.split(".")[-1], "mFunction": "bold"} not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "bold"})
            elif i.endswith('.BeaconType'):
                if ({"name": i, "pr": i.split(".")[-1], "mFunction": "encryption_type"}) \
                        not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "encryption_type"})
            else:
                if {"name": i, "pr": i.split(".")[-1]} not in wifi2_element:
                    wifi2_element.append({"name": i, "pr": i.split(".")[-1]})
        return wifi2_element





def get_test(cpe_dump):
    element = []
    if isConsistPartly("InternetGatewayDevice.DownloadDiagnostics", cpe_dump):
        element.append({
            "name": "testDlWidget",
            "__type": "test-dl-widget",
            "pr": "TestDownloadWidget",
            "default_host": ["http://devel.tr069.ru:4551/1M",
                             "http://devel.tr069.ru:4551/5M",
                             "http://devel.tr069.ru:4551/10M",
                             ],

            "elements": []
        })

    if isConsistPartly("InternetGatewayDevice.UploadDiagnostics", cpe_dump):
        element.append({
            "name": "testUlWidget",
            "__type": "test-ul-widget",
            "pr": "Upload Test",
            "default_host": ["http://devel.tr069.ru:4551/"],
            "default_test_file_length": "1000000",
            "forbidView": []
        })

    if isConsistPartly("InternetGatewayDevice.IPPingDiagnostics", cpe_dump):
        element.append({
            "name": "simplePingWidget",
            "__type": "simple-ping-widget",
            "pr": "Ping Test",
            "forbidView": [],
            "defaultParams": {
                'Host': 'devel.tr069.ru',
                'NumberOfRepetitions': 10,
                'DataBlockSize': 32
            },
            "elements": []
        })

    if isConsistPartly("InternetGatewayDevice.TraceRouteDiagnostics", cpe_dump):
        element.append({
            "name": "Traceroute  Widget",
            "__type": "traceroute-widget",
            "pr": "Traceroute test",
            "default_host": "devel.tr069.ru",  # Default host name
            "elements": []
        })

    return element




def getDeviceInfo(cpe_dump):
    element = []

    for i in [item for item in params.device_info if isConsist(item, cpe_dump)]:
        if i == "InternetGatewayDevice.DeviceInfo.UpTime":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_uptime"})
        elif i == "InternetGatewayDevice.DeviceInfo.ModelName":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "bold"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    for i in params.device_info_props:
        if i == "cpe.ip" or i == "cpe.cpeid":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "bold"})
        elif i == "cpe.firstMsg" or i == "cpe.lastMsg":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_timestamp"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})

    return element



def get_full_device_info(cpe_dump):
    element = []

    full_device_info_gen = [item for item in params.full_device_info if isConsist(item, cpe_dump)]

    for i in full_device_info_gen:

        if i.endswith('.EnableCWMP') or i.endswith('.PeriodicInformEnable') or i.endswith(
                '.UpgradesManaged') or i.endswith(
                '.STUNEnable'):
                element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})

    return element


def get_time(cpe_dump):
    element = []

    for i in [item for item in params.time if isConsist(item, cpe_dump)]:
        if {"pr": 'Settings', "changeFlow": "TIME_SETTINGS_SET_Sample"} not in element:
            element.append({"pr": 'Settings', "changeFlow": "TIME_SETTINGS_SET_Sample"})
        elif i == "InternetGatewayDevice.Time.Enable":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled"})
        elif i == "InternetGatewayDevice.Time.CurrentLocalTime":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_datetime"})
        elif i == "InternetGatewayDevice.Time.Status":
            element.append({"name": i, "pr": i.split(".")[-1]})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_wan_ip(cpe_dump):
    element = []
    wan_ip_gen = [item for item in params.wan_ip if isPart(item, cpe_dump)]
    for i in wan_ip_gen:
        if i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Name":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "bold_dlink_dir300"})
        elif i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.DNSEnabled":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled", "changeFlow": "ENABLE_DNS_IP_Sample"})
        elif i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Enable":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled"})
        elif i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.NATEnabled":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled", "changeFlow": "ENABLE_IP_NAT_Sample"})
        elif i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Uptime":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_uptime"})
        elif i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.DNSServers":
            element.append({"name": i, "pr": i.split(".")[-1], "changeFlow": "DNS_SERVERS_IP_Sample"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})

    return element


def get_wan_ppp(cpe_dump):
    element = []
    wan_ppp_gen = [item for item in params.wan_ppp if isPart(item, cpe_dump)]

    for i in wan_ppp_gen:
        if i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Status":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"})
        elif i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.DNSEnabled":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled",\
                            "changeFlow": "ENABLE_PPPoE_DNS_Sample"})
        elif i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Enable":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled"})
        elif i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.NATEnabled":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled",\
                            "changeFlow": "ENABLE_PPPoE_NAT_Sample"})
        elif i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Uptime":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_uptime"})

        elif i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.DNSServers":
            element.append({"name": i, "pr": i.split(".")[-1], "changeFlow": "DNS_SERVERS_PPP_Sample"})

        else:
            element.append({"name": i, "pr": i.split(".")[-1]})

    return element


def get_wan_pots(cpe_dump):
    element = []
    wan_pots_gen = [item for item in params.wan_pots if isPart(item, cpe_dump)]
    for i in wan_pots_gen:
        if i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.Enable":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled"})
        elif i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANPOTSLinkConfig.LinkStatus":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_wan_dsl(cpe_dump):
    element = []
    wan_dsl_gen = [item for item in params.wan_dsl_link if isPart(item, cpe_dump)]
    for i in wan_dsl_gen:
        if i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANDSLLinkConfig.Enable":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled"})
        elif i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANDSLLinkConfig.LinkStatus":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_wan_ip_stats(cpe_dump):
    element = []
    wan_ip_stats_gen = [item for item in params.wan_ip_stats if isPart(item, cpe_dump)]
    for i in wan_ip_stats_gen:
        if i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetBytesReceived" \
                or i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection._x_.Stats.EthernetBytesSent":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_traffic"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_wan_ppp_stats(cpe_dump):
    element = []
    wan_ppp_stats_gen = [item for item in params.wan_ppp_stats if isPart(item, cpe_dump)]
    for i in wan_ppp_stats_gen:
        if i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetBytesReceived" \
                or i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.Stats.EthernetBytesSent":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_traffic"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_wan_common_stats(cpe_dump):
    element = []
    wan_common_stats_gen = [item for item in params.wan_common_stats if isPart(item, cpe_dump)]

    for i in wan_common_stats_gen:
        if i == "InternetGatewayDevice.WANDevice._x_.WANCommonInterfaceConfig.TotalBytesReceived" \
                or i == "InternetGatewayDevice.WANDevice._x_.WANCommonInterfaceConfig.TotalBytesSent":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_traffic"})
        elif i == 'InternetGatewayDevice.WANDevice._x_.WANCommonInterfaceConfig.EnabledForInternet':
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled"})
        elif i.endswith('.PhysicalLinkStatus'):
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_wan_eth_stats(cpe_dump):
    element = []
    wan_eth_stats_gen = [item for item in params.wan_eth_stats if isPart(item, cpe_dump)]

    for i in wan_eth_stats_gen:
        if i == "InternetGatewayDevice.WANDevice._x_.WANEthernetInterfaceConfig.Stats.BytesReceived" \
                or i == "InternetGatewayDevice.WANDevice._x_.WANEthernetInterfaceConfig.Stats.BytesSent":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_traffic"})
        elif i == "InternetGatewayDevice.WANDevice._x_.WANEthernetInterfaceConfig.Status":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_port_map(cpe_dump):
    element = []
    if len([item for item in params.port_mapPPP if isPart(item, cpe_dump)]) != 0:
        for i in [item for item in params.port_mapPPP if isPart(item, cpe_dump)]:
            if i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.PortMapping._x_.PortMappingEnabled":
                element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled",\
                            "changeFlow": "Port_Mapping_PPPoe_Sample", "deleteFlow": "PortForward_del_IPoE_Sample"})
            else:
                element.append({"name": i, "pr": i.split(".")[-1]})
    if len([item for item in params.port_mapPPP_y if isPart(item, cpe_dump)]) != 0:
        for i in [item for item in params.port_mapPPP_y if isPart(item, cpe_dump)]:
            if i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection._x_.PortMapping.1.PortMappingEnabled":
                element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled",\
                            "changeFlow": "Port_Mapping_PPPoe_Sample", "deleteFlow": "PortForward_del_IPoE_Sample"})
            else:
                element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_port_map_ip(cpe_dump):
    element = []
    port_mapIP_gen = [item for item in params.port_mapIP if isPart(item, cpe_dump)]
    for i in port_mapIP_gen:
        if i == "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection.1.PortMapping._x_.PortMappingEnabled":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled",\
                            "changeFlow": "Port_Mapping_IPoE_Sample", "deleteFlow": "PortForward_del_IPoE_Sample"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_nat_info(cpe_dump):
    element = []
    for i in [item for item in params.nat_info if isConsist(item, cpe_dump)]:
        if i == "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPServerEnable":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled", "changeFlow": "DHCP_Sample"})
        elif i == "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPLeaseTime":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_uptime"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_serving_pool(cpe_dump):
    element = []
    serving_pool_gen = [item for item in params.serving_pool if isPart(item, cpe_dump)]
    for i in serving_pool_gen:
        if i == "InternetGatewayDevice.LANDevice.1.LANHostConfigManagement.DHCPConditionalServingPool._x_.Enable":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled", "changeFlow": "SERVING_POOL_Sample"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_lan_ports(cpe_dump):
    element = []

    for i in [item for item in params.lan_ports if isPart(item, cpe_dump)]:
        if i == "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Status":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"})
        elif i == "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Enable":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled", "changeFlow": "LAN_Settings_Sample"})
        elif i == "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Stats.BytesReceived" \
                or i == "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Stats.BytesSent":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_traffic"})
        elif i == "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.DuplexMode" \
                or i == "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.DuplexMode":
            element.append({"name": i, "pr": i.split(".")[-1], "changeFlow": "CHANGE_DUPLEX_MODE_Sample"})
        elif i == "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.MaxBitRate" \
                or i == "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.MaxBitRate":
            element.append({"name": i, "pr": i.split(".")[-1], "changeFlow": "CHANGE_LAN_SPEED_Sample"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_wlan(type_wlan, cpe_dump):
    wifi_list = [item for item in params.wifi if isPart(item, cpe_dump)]
    wifi5_widget = []
    wifi2_widget = []

    for k, v in cpe_dump.items():
        if k.endswith('PossibleChannels'):
            if v == ' 1,2,3,4,5,6,7,8,9,10,11,12,13' or v == ' 1-13':
                new_list = []
                if len(getListWLAN('2.4', cpe_dump)) == 1:
                    for i in [item for item in params.wifi if isPart(item, cpe_dump)]:
                        i = i.replace("_x_", getListWLAN('2.4', cpe_dump)[0])
                        new_list.append(i)
                    wifi2_widget = addWlanWidget('wifi2_widget', new_list)

                else:
                    wifi2_widget = addWlanWidget('wifi2_widget', wifi_list)
            else:
                new_list = []

                if len(getListWLAN('5', cpe_dump)) == 1:
                    for i in [item for item in params.wifi if isPart(item, cpe_dump)]:
                        i = i.replace("_x_", getListWLAN('5', cpe_dump)[0])
                        new_list.append(i)
                    wifi5_widget = addWlanWidget('wifi5_widget', new_list)

                else:
                    wifi5_widget = addWlanWidget('wifi5_widget', wifi_list)
        elif k.endswith('.Channel'):
            if v in [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10', ' 11', ' 12', ' 13'] \
                    or v in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
                new_list = []
                if len(getListWLAN('2.4', cpe_dump)) == 1:
                    for i in [item for item in params.wifi if isPart(item, cpe_dump)]:
                        i = i.replace("_x_", getListWLAN('2.4', cpe_dump)[0])
                        new_list.append(i)
                    wifi2_widget = addWlanWidget('wifi2_widget', new_list)

                else:
                    wifi2_widget = addWlanWidget('wifi2_widget', wifi_list)
            else:
                new_list = []
                if len(getListWLAN('5', cpe_dump)) == 1:
                    for i in [item for item in params.wifi if isPart(item, cpe_dump)]:
                        i = i.replace("_x_", getListWLAN('5', cpe_dump)[0])
                        new_list.append(i)
                    wifi5_widget = addWlanWidget('wifi5_widget', new_list)

                else:
                    wifi5_widget = addWlanWidget('wifi5_widget', new_list)

    if type_wlan == '2':
        return wifi2_widget
    elif type_wlan == '5':
        return wifi5_widget


def get_wlan5(cpe_dump):
    element = get_wlan('5', cpe_dump)
    return element

def get_wlan2(cpe_dump):
    element = get_wlan('2', cpe_dump)
    return element

def get_dsl(cpe_dump):
    element = []
    for i in [item for item in params.wadsl if isPart(item, cpe_dump) or isPartSmartIndex(item, cpe_dump)]:
        if i == "smartIndex.InternetGatewayDevice.WANDevice.smartIndex1.WANDSLInterfaceConfig.Status":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_dsl_stats(cpe_dump):
    element = []

    for i in [item for item in params.dsl_stats if isPart(item, cpe_dump) or isPartSmartIndex(item, cpe_dump)]:
        element.append({"name": i, "pr": i.split(".")[-1]})

    for i in [item for item in params.DSL_CD_Stats if isPart(item, cpe_dump) or isPartSmartIndex(item, cpe_dump)]:
        element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_trace_roat(cpe_dump):
    element = []

    for i in [item for item in params.trace_roat if isPart(item, cpe_dump)]:
        if i == "InternetGatewayDevice.Layer3Forwarding.Forwarding._x_.Status":
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_status",\
                            "changeFlow": "ROUTINGTABLE_SET_Sample", "deleteFlow": "ROUTINGTABLE_DEL_Sample"})
        else:
            element.append({"name": i, "pr": i.split(".")[-1]})
    return element


def get_user_interface(cpe_dump):
    element = []
    for i in [item for item in params.user_interface if isConsist(item, cpe_dump)]:
        if i.endswith('.Enable'):
            element.append({"name": i, "pr": i.split(".")[-1], "mFunction": "convert_enabled"})
        else:

            element.append({"name": i, "pr": i.split(".")[-1]})

    return element




def get_widget_element(element_name, cpe_dump):
    elements = {
        'device_info_widget': getDeviceInfo,
        'full_device_info_widget': get_full_device_info,
        'managment_server_widget': get_user_interface,
        'time_widget': get_time,
        'wan_ip_widget': get_wan_ip,
        'wan_ppp_widget': get_wan_ppp,
        'wan_pots_widget': get_wan_pots,
        'wan_dsl_link_widget': get_dsl,
        'wan_ip_stats_widget': get_wan_ip_stats,
        'wan_ppp_stats_widget': get_wan_ppp_stats,
        'wan_common_stats_widget': get_wan_common_stats,
        'wan_ethernet_stats_widget': get_wan_eth_stats,
        'port_map_widget_PPP': get_port_map,
        'port_map_widget_IP': get_port_map_ip,
        'nat_info_widget': get_nat_info,
        'serving_pool_widget': get_serving_pool,
        'lan_ports_widget': get_lan_ports,
        'wifi2_widget': get_wlan2,
        'wifi5_widget': get_wlan5,
        'wadsl_widget': get_dsl,
        'dsl_stats_widget': get_dsl_stats,
        'DSL_CD_Stats_widget': get_wan_dsl,
        'trace_roat_widget': get_trace_roat,
        'user_interface_widget': get_user_interface,
        'test': get_test
    }
    element = elements[element_name](cpe_dump)

    return element

