from elements import get_widget_element, getListWLAN
from widgets import get_widget
import check_features


def getTabs(cpe_dump):
    """
    Generate tabs from cpe_dump
    :param cpe_dump:
    :return:
    """

    tabs_list = []
    device_information = {
        "pr": "Device Information",
        "__type": "support-portal-tab",
        "name": "MainDiag",
        "elements": []
    }

    time_settings = {
        "pr": "Time Settings",
        "__type": "support-portal-tab",
        "name": "Time",
        "elements": [
            {
                "pr": "Local Time",
                "__type": "section-widget",
                "name": "Time",
                "elements": get_widget_element('time_widget', cpe_dump)
            }
        ]
    }

    network_map = {
        "__type": "network-map-tree",
        "name": "NetworkMap",
        "pr": "Network Map",
        "__priority": -1,
        "selector": "I.LD.1.H.H._x_.A",
        "classifiers": {
            '_active': {
                'key': 'I.LD.1.H.H._x_.A',
                'values': [
                    {
                        'match': '1',
                        'value': 1,
                    }
                ],
                'default': 1,
            },
            '_group': {
                'key': 'I.LD.1.H.H._x_.IT',
                'default': 'N/A',
                'show_empty_default': "False",
                'values': [
                    {
                        'match': '802.11',
                        'replace': 'WiFi'
                    }
                ]
            },
        },
        'rootname': 'Model name of Your device',
        "elements": [
            {'name': 'I.LD.1.H.H._x_.A', 'pr': 'Active', 'hide': "True"},
            {'name': 'I.LD.1.H.H._x_.HN', 'pr': 'HostName', 'key': 'id', 'hide': "True"},
            {'name': 'I.LD.1.H.H._x_.IA', 'pr': 'IP Address'},
            {'name': 'I.LD.1.H.H._x_.MA', 'pr': 'MAC address', 'mFunction': 'eval_vendor'},
            {'name': 'I.LD.1.H.H._x_.IT', 'pr': 'IP Address Type'},
            {'name': 'I.LD.1.H.H._x_.LTR', 'pr': 'Lease Time'}
        ]
    }

    wan_information = {
        "pr": "WAN Information",
        "__type": "support-portal-tab",
        "name": "WANDiag",
        "elements": []
    }
    nat_port_mapping = {
        "name": "NATPortmap",
        "pr": "NAT Port mapping",
        "__type": "multi-section-table",
        "parent_width": 12,
        "elements": [],
        # "createFlow": "CreatePortMap_DLINK_DIR300a",
        # "__exploration_flow": "multi_section_exploration_two",
        "__flow": "SmartGPV",

    }
    if len(get_widget_element('port_map_widget_PPP', cpe_dump)) != 0:
        nat_port_mapping["elements"] = get_widget_element('port_map_widget_PPP', cpe_dump)
        nat_port_mapping["selector"] = "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANPPPConnection.1.PortMapping._x_.PortMappingDescription"
    if len(get_widget_element('port_map_widget_IP', cpe_dump)) != 0:
        nat_port_mapping["elements"] = get_widget_element('port_map_widget_IP', cpe_dump)
        nat_port_mapping["selector"] = "InternetGatewayDevice.WANDevice.1.WANConnectionDevice.1.WANIPConnection.1.PortMapping._x_.PortMappingDescription"



    nat_information = {
        "name": "NATDiag",
        "pr": "NAT Information",
        "__type": "support-portal-tab",
        "elements": []
    }

    lan_ports_information = {
        "pr": "LAN Information",
        "__type": "support-portal-tab",
        "name": "LANDiag",
        "elements": [
            {

                "__type": "multi-section-widget",
                "__flow": 'SmartGPV',
                "name": "LANPorts",
                "flow": "MainDiagFlow",
                "pr": "LAN port status",
                "parent_width": 12,
                "child_width": 3,
                "selector": "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig._x_.Name",
                "elements": get_widget_element('lan_ports_widget', cpe_dump)
            }

        ]
    }

    wifi_information = {
        "name": "WiFiDiag",
        "pr": "WiFi Information",
        "__type": "support-portal-tab",
        "elements": []
    }

    dsl_statist = {
        "name": "WANDSL",
        "pr": "DSL Information",
        "__type": "support-portal-tab",
        "forbidView": [],
        "elements": []
    }

    port_forwarding = {
        "name": "Layer3Forwarding",
        "pr": "Routing Table",
        "__type": "support-portal-tab",
        "elements": [
            {
                "__type": "multi-section-table",
                "name": "Forwarding Infos",
                "pr": "Forwarding Info",
                "forbidView": [],
                "__priority": -1,
                "selector": "InternetGatewayDevice.Layer3Forwarding.Forwarding._x_.Enable",
                "parent_width": 12,
                "elements": get_widget_element('trace_roat_widget', cpe_dump)
            }
        ]
    }

    userinterface = {
        "pr": "UserInterface",
        "__type": "support-portal-tab",
        "name": "User Interface",
        "elements": [
            {
                "pr": "User Interface",
                "__type": "section-widget",
                "name": "UserInterface",
                "elements": get_widget_element('user_interface_widget', cpe_dump)
            }
        ]
    }

    tests = {
        "name": "Diagnose",
        "__type": "support-portal-tab",
        "pr": "Diagnose",
        "forbidView": [],
        "elements": [
            {
                "name": "DiagnoseSubtabs",
                "__type": "support-portal-tab-layout",
                "pr": "",
                "forbidView": [],
                "elements": get_widget_element('test', cpe_dump)
            }
        ]
    }

    cpe_logs = {
        "name": "Log",
        "__type": "cpe-log-widget",
        "pr": "Device Log",
        "forbidView": []
    }

    server_logs = {
        "name": "SrvLog",
        "__type": "ax-sp-server-log",
        "pr": "Server Log",
        "roles": ['Level1', 'Level2', 'Level3', 'Manager'],
        "hide": ["Opening Support Portal"],
        "forbidView": [],
        "elements": []
    }

    action_log = {
        "name": "ActionLog",
        "pr": "Action Log",
        "forbidView": [],
        "__type": "actionlog-new"
    }

    cpe_config = {
        "name": "CPEConfig",
        "__type": "support-portal-tab",
        "pr": "CPE Config files",
        "forbidView": ["Level1"],
        "elements": [
            {
                "name": "CPE Configs",
                "actions": ['backup', 'diff', 'download', 'restore', 'change'],
                "__type": "cpe-config-files-widget",
                "download_link": "/live/CPEManager/{0}/get_cfg?cfgid={1}",
                "forbidView": [],
                "port": 1,
                "storage_id": "AXConfigStorage"
            }
        ]
    }

    rpc = {
        "name": "RPC",
        "__type": "get-rpc",
        "pr": "RPC",
        "forbidView": ['Anonymous', 'Level1', 'Level2'],
        "elements": []
    }

    """
    Add widgets in the tabs
    """


    if get_widget('device_info_widget_front', cpe_dump)["elements"] != []:
        device_information["elements"].append(get_widget('device_info_widget_front', cpe_dump))

    if get_widget('device_info_widget_front', cpe_dump)["elements"] != []:
        device_information["elements"].append(get_widget('user_interface_widget_front', cpe_dump))

    # if managment_server_widget_front["elements"] != []:
    #     device_information["elements"][0]["elements"].append(managment_server_widget_front)

    if get_widget('wan_ip_widget_front', cpe_dump)["elements"] != []:
        wan_information["elements"].append(get_widget('wan_ip_widget_front', cpe_dump))

    if get_widget('wan_ppp_widget_front', cpe_dump)["elements"] != []:
        wan_information["elements"].append(get_widget('wan_ppp_widget_front', cpe_dump))

    if get_widget('wan_pots_widget_front', cpe_dump)["elements"] != []:
        wan_information["elements"].append(get_widget('wan_pots_widget_front', cpe_dump))

    if get_widget('wan_dsl_link_widget_front', cpe_dump)["elements"] != []:
        wan_information["elements"].append(get_widget('wan_dsl_link_widget_front', cpe_dump))

    if get_widget('wan_ip_stats_widget_front', cpe_dump)["elements"] != []:
        wan_information["elements"].append(get_widget('wan_ip_stats_widget_front', cpe_dump))

    if get_widget('wan_ppp_stats_widget_front', cpe_dump)["elements"] != []:
        wan_information["elements"].append(get_widget('wan_ppp_stats_widget_front', cpe_dump))

    if get_widget('wan_common_stats_widget_front', cpe_dump)["elements"] != []:
        wan_information["elements"].append(get_widget('wan_common_stats_widget_front', cpe_dump))

    if get_widget('wan_ethernet_stats_widget_front', cpe_dump)["elements"] != []:
        wan_information["elements"].append(get_widget('wan_ethernet_stats_widget_front', cpe_dump))

    for item in wan_information["elements"]:
        if "selector" in item:
            if '_x_' and '_y_' in item["selector"]:
                item["__flow"] = "SmartGPVTwo"
                item["__exploration_flow"] = "multi_section_exploration_two"
            elif '_y_' not in item["selector"]:
                item["__flow"] = "SmartGPV"

    if get_widget('nat_info_widget_front', cpe_dump)["elements"] != []:
        nat_information["elements"].append(get_widget('nat_info_widget_front', cpe_dump))
    if get_widget('dhcp_widget_front', cpe_dump)["elements"] != []:
        nat_information["elements"].append(get_widget('dhcp_widget_front', cpe_dump))



    if get_widget('wadsl_widget_front', cpe_dump)["elements"] != []:
        dsl_statist["elements"].append(get_widget('wadsl_widget_front', cpe_dump))
    if get_widget('dsl_stats_widget_front', cpe_dump)["elements"] != []:
        dsl_statist["elements"].append(get_widget('dsl_stats_widget_front', cpe_dump))
    if get_widget('DSL_CD_Stats_widget_front', cpe_dump)["elements"] != []:
        dsl_statist["elements"].append(get_widget('DSL_CD_Stats_widget_front', cpe_dump))

    """
    Function to check tabs
    """

    def appendIntoConfig(param, tab):
        if check_features.isConsistPartly(param, cpe_dump) or check_features.isConsistPartly4(param, cpe_dump) or \
                check_features.isConsistPartly8(param, cpe_dump) or check_features.isConsistPartly3(param, cpe_dump):
            if tab not in tabs_list:
                tabs_list.append(tab)
        return tabs_list

    """
    Add tabs into config
    """


    appendIntoConfig("InternetGatewayDevice.DeviceInfo", device_information)
    appendIntoConfig("InternetGatewayDevice.Time", time_settings)
    if network_map not in tabs_list:
        tabs_list.append(network_map)
    appendIntoConfig("InternetGatewayDevice.WANDevice.1.WANConnectionDevice", wan_information)

    if nat_port_mapping["elements"] != [] and nat_port_mapping not in tabs_list:
        tabs_list.append(nat_port_mapping)

    appendIntoConfig("InternetGatewayDevice.LANDevice.1.LANHostConfigManagement", nat_information)
    appendIntoConfig("InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig", lan_ports_information)

    if get_widget_element('wifi2_widget', cpe_dump) != []:

        if len(check_features.getListWLAN('2.4', cpe_dump)) == 1:
            if {
                "__type": "section-widget",
                "name": "WiFiSSIDs2.4",
                "flow": "MainDiagFlow",
                "pr": "SSID 2,4Ghz",
                "__priority": -1,
                "parent_width": 12,
                "child_width": 3,

                "elements": get_widget_element('wifi2_widget', cpe_dump)} not in wifi_information["elements"]:
                wifi_information["elements"].append({
                    "__type": "section-widget",
                    "name": "WiFiSSIDs2.4",
                    "flow": "MainDiagFlow",
                    "pr": "SSID 2,4Ghz",
                    "__priority": -1,
                    "parent_width": 12,
                    "child_width": 3,

                    "elements": get_widget_element('wifi2_widget', cpe_dump)
                })
        elif len(check_features.getListWLAN('2.4', cpe_dump)) > 1:
            if {
                "__type": "multi-section-widget",
                "name": "WiFiSSIDs2.4",
                "flow": "MainDiagFlow",
                "pr": "SSID 2,4Ghz",
                "__priority": -1,
                "parent_width": 12,
                "child_width": 3,
                "selector": "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Status",
                "elements": get_widget_element('wifi2_widget', cpe_dump)} not in wifi_information["elements"]:
                wifi_information["elements"].append({
                    "__type": "multi-section-widget",
                    "name": "WiFiSSIDs2.4",
                    "flow": "MainDiagFlow",
                    "pr": "SSID 2,4Ghz",
                    "__priority": -1,
                    "parent_width": 12,
                    "child_width": 3,
                    "selector": "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Status",
                    "elements": get_widget_element('wifi2_widget', cpe_dump)
                })

    if get_widget_element('wifi5_widget', cpe_dump) != []:
        if len(check_features.getListWLAN('5')) == 1:
            if {
                "__type": "section-widget",
                "name": "WiFiSSIDs5",
                "flow": "MainDiagFlow",
                "pr": "SSID 5Ghz",
                "__priority": -1,
                "parent_width": 12,
                "child_width": 3,

                "elements": get_widget_element('wifi5_widget', cpe_dump)} not in wifi_information["elements"]:
                wifi_information["elements"].append(
                    {
                        "__type": "section-widget",
                        "name": "WiFiSSIDs5",
                        "flow": "MainDiagFlow",
                        "pr": "SSID 5Ghz",
                        "__priority": -1,
                        "parent_width": 12,
                        "child_width": 3,

                        "elements": get_widget_element('wifi5_widget', cpe_dump)
                    }
                )
        elif len(check_features.getListWLAN('5', cpe_dump)) > 1:
            if {
                "__type": "multi-section-widget",
                "name": "WiFiSSIDs5",
                "flow": "MainDiagFlow",
                "pr": "SSID 5Ghz",
                "__priority": -1,
                "parent_width": 12,
                "child_width": 3,
                "selector": "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Status",
                "elements": get_widget_element('wifi5_widget', cpe_dump)} not in wifi_information["elements"]:
                wifi_information["elements"].append(
                    {
                        "__type": "multi-section-widget",
                        "name": "WiFiSSIDs5",
                        "flow": "MainDiagFlow",
                        "pr": "SSID 5Ghz",
                        "__priority": -1,
                        "parent_width": 12,
                        "child_width": 3,
                        "selector": "InternetGatewayDevice.LANDevice.1.WLANConfiguration._x_.Status",
                        "elements": get_widget_element('wifi5_widget', cpe_dump)
                    })

    appendIntoConfig("InternetGatewayDevice.LANDevice.1.WLANConfiguration", wifi_information)
    appendIntoConfig("InternetGatewayDevice.WANDevice.1.WANDSLInterfaceConfig", dsl_statist)
    if len(get_widget_element('trace_roat_widget', cpe_dump)) != 0:
        appendIntoConfig("InternetGatewayDevice.Layer3Forwarding", port_forwarding)

    if tests not in tabs_list:
        tabs_list.append(tests)

    if check_features.isConsistPartly3("InternetGatewayDevice.DeviceInfo.DeviceLog", cpe_dump):
        if cpe_dump["InternetGatewayDevice.DeviceInfo.DeviceLog"] != ' ' or cpe_dump[
            "InternetGatewayDevice.DeviceInfo.DeviceLog"] != '':
            if cpe_logs not in tabs_list:
                tabs_list.append(cpe_logs)

    if server_logs not in tabs_list:
        tabs_list.append(server_logs)
    if action_log not in tabs_list:
        tabs_list.append(action_log)
    if cpe_config not in tabs_list:
        tabs_list.append(cpe_config)
    if rpc not in tabs_list:
        tabs_list.append(rpc)

    return tabs_list
