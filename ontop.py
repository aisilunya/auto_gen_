import check_features
from widgets import get_widget


def getOntop(cpe_dump):
    ontop_dict = {
        "elements": [
            {
                "__type": "support-portal-column-layout",
                "width": "6",
                "elements": []},

        ],
        "__type": "support-portal-tab"
    }

    countWLAN = 0
    for param in cpe_dump:
        if param.startswith("InternetGatewayDevice.LANDevice.1.WLANConfiguration.") and param.endswith("BSSID"):
            countWLAN += 1

    countLAN = 0
    for param in cpe_dump:
        if param.startswith("InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig.") and \
                param.endswith("Status"):
            countLAN += 1

    port_numbers = {"pr": "Port Number",
                    "elements": []
                    }

    for i in range(1, countWLAN + 1):
        port_numbers["elements"].append(
            {"name": "external.text.WiFi 2,4" + " " + str(i), "mFunction": "bold"})

    for i in range(1, countLAN + 1):
        port_numbers["elements"].append({"name": "external.text.LAN" + " " + str(i), "mFunction": "bold"})

    interface_names = {"pr": "Interface Name",
                       "elements": [

                       ]}

    enable = {
        "pr": "Enable",
        "changeFlow": "LanWifi_SET_Sample",
        "elements": []
    }

    port_status = {
        "pr": "Port Status",
        "elements": []}

    duplex_mode = {
        "pr": "Duplex Mode",
        "changeFlow": "DUPLEX_MODE_SET_Sample",
        "elements": []
    }

    port_speeds = {
        "pr": "Port Speed",
        "elements": [],
        "changeFlow": ""
    }

    ssid = {
        "pr": "SSID",
        'elements': []
    }

    bytes_recieved = {
        "pr": "Bytes received",
        "elements": []
    }

    bytes_sent = {
        "pr": "Bytes sent",
        "elements": [
        ]
    }

    """
    Function for add ontop widget to "ontop"
    """


    def fillParameter(myList, param):
        if check_features.isConsistPartly4("InternetGatewayDevice.LANDevice.1.WLANConfiguration", cpe_dump):
            for i in range(1, countWLAN + 1):
                if check_features.isConsist("InternetGatewayDevice.LANDevice.1.WLANConfiguration." + str(i) + param, cpe_dump):
                    if param == '.Enable':
                        if {"name": "InternetGatewayDevice.LANDevice.1.WLANConfiguration." + str(i) +
                                param, "mFunction": "convert_enabled"} not in myList:
                            myList.append({
                                "name": "InternetGatewayDevice.LANDevice.1.WLANConfiguration." + str(i) + param,
                                "mFunction": "convert_enabled"
                            })
                    elif param == '.Status':
                        if {"name": "InternetGatewayDevice.LANDevice.1.WLANConfiguration." + str(i) +
                                param, "mFunction": "convert_status"} not in myList:
                            myList.append({
                                "name": "InternetGatewayDevice.LANDevice.1.WLANConfiguration." + str(i) + param,
                                "mFunction": "convert_status"
                            })
                    else:
                        if {"name": "InternetGatewayDevice.LANDevice.1.WLANConfiguration." + str(i) + param} not \
                                in myList:
                            myList.append({
                                "name": "InternetGatewayDevice.LANDevice.1.WLANConfiguration." + str(i) + param
                            })
                else:
                    myList.append({
                        "name": "external.text. "
                    })

        if check_features.isConsistPartly4("InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig", cpe_dump):
            for i in range(1, countLAN + 1):
                if check_features.isConsist("InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig." + str(i) +
                                                    param, cpe_dump):
                    if param == '.Enable':
                        if {"name": "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig." + str(i) +
                                param, "mFunction": "convert_enabled"} not in myList:
                            myList.append({
                                "name": "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig." + str(i) +
                                        param, "mFunction": "convert_enabled"})
                    elif param == ".Status":
                        if {"name": "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig." + str(i) +
                                param, "mFunction": "convert_status"} not in myList:
                            myList.append({
                                "name": "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig." + str(i) +
                                        param, "mFunction": "convert_status"})
                    else:
                        if {"name": "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig." + str(i) +
                                param} not in myList:
                            myList.append({
                                "name": "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig." + str(i) +
                                        param})

                else:
                    myList.append({
                        "name": "external.text. "
                    })
            if myList.count({"name": "external.text. "}) == countLAN + countWLAN:
                for i in range(0, countWLAN + countLAN):
                    myList.remove({"name": "external.text. "})

        return myList

    fillParameter(interface_names["elements"], ".Name")
    fillParameter(enable["elements"], ".Enable")
    fillParameter(port_status["elements"], ".Status")
    fillParameter(duplex_mode["elements"], ".DuplexMode")
    fillParameter(port_speeds["elements"], ".MaxBitRate")
    fillParameter(ssid['elements'], ".SSID")

    if check_features.isMaxBitRateInLEIC(fillParameter(port_speeds["elements"], ".MaxBitRate")):
        port_speeds["changeFlow"] = 'PORT_SPEED_SET_Sample'


    if check_features.isConsistPartly4("InternetGatewayDevice.LANDevice.1.WLANConfiguration", cpe_dump):
        for item in cpe_dump:
            if item.endswith(".TotalBytesReceived"):

                for i in range(1, countWLAN + 1):
                    if {"name": "InternetGatewayDevice.LANDevice.1.WLANConfiguration." + str(i) +
                            ".TotalBytesReceived", "mFunction": "convert_traffic"} not in bytes_recieved["elements"]:
                        bytes_recieved["elements"].append({
                            "name": "InternetGatewayDevice.LANDevice.1.WLANConfiguration." + str(i) +
                                    ".TotalBytesReceived",
                            "mFunction": "convert_traffic"
                        })
    if check_features.isConsistPartly4("InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig", cpe_dump):
        for i in range(1, countLAN + 1):
            if {"name": "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig." + str(
                    i) + ".Stats.BytesReceived", "mFunction": "convert_traffic"} not in bytes_recieved["elements"]:
                bytes_recieved["elements"].append({
                    "name": "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig." + str(i) +
                            ".Stats.BytesReceived",
                    "mFunction": "convert_traffic"
                })

    if check_features.isConsistPartly4("InternetGatewayDevice.LANDevice.1.WLANConfiguration", cpe_dump):
        for item in cpe_dump:
            if item.endswith(".TotalBytesSent"):

                for i in range(1, countWLAN + 1):
                    if {"name": "InternetGatewayDevice.LANDevice.1.WLANConfiguration." + str(
                            i) + ".TotalBytesSent", "mFunction": "convert_traffic"} not in bytes_sent["elements"]:
                        bytes_sent["elements"].append({
                            "name": "InternetGatewayDevice.LANDevice.1.WLANConfiguration." + str(
                                i) + ".TotalBytesSent",
                            "mFunction": "convert_traffic"
                        })
    if check_features.isConsistPartly4("InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig", cpe_dump):
        for i in range(1, countLAN + 1):
            if {"name": "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig." + str(
                    i) + ".Stats.BytesSent", "mFunction": "convert_traffic"} not in bytes_sent["elements"]:
                bytes_sent["elements"].append({
                    "name": "InternetGatewayDevice.LANDevice.1.LANEthernetInterfaceConfig."
                            + str(
                        i) + ".Stats.BytesSent",
                    "mFunction": "convert_traffic"
                })
    wifi_lan_ports = get_widget('ontop_wifi_lan_ports_widget', cpe_dump)
    image_widget = get_widget('ontop_image_widget', cpe_dump)
    devices = get_widget('ontop_devices_widget', cpe_dump)
    info_elements = [port_numbers, interface_names, enable, port_status, duplex_mode, port_speeds, ssid,
                     bytes_recieved, bytes_sent]

    ontop_dict["elements"][0]["elements"].append(image_widget)
    ontop_dict["elements"].append(devices)

    for item in info_elements:
        if item["elements"] != []:
            wifi_lan_ports["elements"][0]["elements"].append(item)
    ontop_dict["elements"][0]["elements"].append(wifi_lan_ports)


    return ontop_dict