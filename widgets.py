from elements import get_widget_element
import params
import check_features

"""
Configure widgets with elements for tabs
"""


def get_widget(widget_name, cpe_dump):
    """
    Get widgets from cpe_dump by widget name
    :param widget_name:
    :param cpe_dump:
    :return:
    """
    widgets = {
        'device_info_widget_front': {
            "pr": "Device Information",
            "elements": get_widget_element('full_device_info_widget', cpe_dump),
            "name": "DeviceInfos",
            "__type": "section-widget",
            "width": 4
        },

        'user_interface_widget_front': {
            "width": 4,
            "pr": "User Interface",
            "__type": "section-widget",
            "name": "UserInterface",
            "elements": get_widget_element('user_interface_widget', cpe_dump)
        },

        'wan_ip_widget_front': {
            "pr": "WAN IP Connections",
            "__type": "multi-section-table",
            "selector": "",
            # "__flow": "SmartGPVTwo",
            "parent_width": 12,
            "name": "IP WAN interfaces",
            "elements": get_widget_element('wan_ip_widget', cpe_dump)
        },


        'wan_ppp_widget_front': {
            "name": "PPP WAN interfaces",
            "pr": "WAN PPP Connections",
            "selector": '',
            # "__flow": 'SmartGPV',
            "__type": "multi-section-widget",
            "parent_width": 12,
            "child_width": 6,
            "elements": get_widget_element('wan_ppp_widget', cpe_dump)
        },

        'wan_pots_widget_front': {
            "pr": "WAN POTS Link Config",
            "parent_width": 12,
            "elements": get_widget_element('wan_pots_widget', cpe_dump),
            "name": "WANPOTSLinkConfig",
            "selector": '',
            # "__flow": 'SmartGPV',
            "__type": "multi-section-table"
        },

        'wan_dsl_link_widget_front': {
            "name": "WAN DSL Link Config",
            "pr": "WAN DSL Link Config",
            "selector": '',
            # "__flow": 'SmartGPV',
            "__type": "multi-section-widget",
            "parent_width": 12,
            "child_width": 3,
            "elements": get_widget_element('wan_dsl_link_widget', cpe_dump)

        },

        'wan_ip_stats_widget_front': {
            "pr": "WAN IP Statistics",
            "elements": get_widget_element('wan_ip_stats_widget', cpe_dump),
            "__type": "multi-section-widget",
            "selector": '',
            # "__flow": "SmartIndexGPV",
            "name": "WANIPStats",
            "parent_width": 6,
            "columns": 1,
            "child_width": 12,
        },

        'wan_ppp_stats_widget_front': {
            "pr": "WAN PPP Statistics",
            "elements": get_widget_element('wan_ppp_stats_widget', cpe_dump),
            "__type": "multi-section-widget",
            "selector": '',
            # "__flow": "SmartIndexGPV",
            "name": "WANPPPStats",
            "parent_width": 6,
            "columns": 1,
            "child_width": 12,
        },

        'wan_common_stats_widget_front': {
            "pr": "WAN Common Statistics",
            "elements": get_widget_element('wan_common_stats_widget', cpe_dump),
            "__type": "multi-section-widget",
            "selector": '',
            # "__flow": "SmartIndexGPV",
            "name": "WANCommonStats",
            "parent_width": 6,
            "child_width": 12,
        },

        'wan_ethernet_stats_widget_front': {
            "pr": "WAN Ethernet Interface Statistics",
            "elements": get_widget_element('wan_ethernet_stats_widget', cpe_dump),
            "__type": "multi-section-widget",
            "selector": '',
            # "__flow": "SmartIndexGPV",
            "name": "WANEhernetInterfaceStats",
            "parent_width": 6,
            "child_width": 12,
        },

        'nat_info_widget_front': {
            "name": "LAN",
            "__type": "section-widget",
            "flow": "LANFlow",
            "pr": "LAN Config",
            "elements": get_widget_element('nat_info_widget', cpe_dump)
        },

        'dhcp_widget_front': {
            "name": "DHCPLAN",
            "__type": "multi-section-widget",
            "__flow": 'SmartGPV',
            "selector": '',
            "pr": "DHCP Serving Pool",
            "parent_width": 12,
            "child_width": 3,
            "elements": get_widget_element('serving_pool_widget', cpe_dump)
        },

        'wadsl_widget_front': {
            "name": "WAN_DSL_Info_Smart",
            "__type": "multi-section-widget",
            "pr": "WAN DSL Information",
            "flow": "MainDiagFlow",
            "forbidView": [],
            "parent_width": 12,
            "child_width": 6,
            "selector": '',
            "elements": get_widget_element('wadsl_widget', cpe_dump)
        },

        'dsl_stats_widget_front': {
            "name": "DSL_ST_Stats",
            "__type": "multi-section-widget",
            "pr": "DSL Show time Statistics",
            "flow": "MainDiagFlow",
            "forbidView": [],
            "parent_width": 12,
            "child_width": 6,
            "selector": "",
            "elements": get_widget_element('dsl_stats_widget', cpe_dump)
        },

        'DSL_CD_Stats_widget_front': {
            "name": "DSL_CD_Stats",
            "__type": "multi-section-widget",
            "pr": "DSL Current Day Statistics",
            "flow": "MainDiagFlow",
            "forbidView": [],
            "parent_width": 12,
            "child_width": 6,
            "selector": "",
            "elements": get_widget_element('DSL_CD_Stats_widget', cpe_dump)
        },

        'ontop_image_widget': {
            "pr": "Name of Your device",
            "name": "Image",
            "height": "150",
            "link": "",
            "width": 12,
            "__type": "image-action-buttons-widget",
            "__onhead": "True",
            "elements": [
                {
                    "pr": "Reboot",
                    "lockMsg": "CPE is rebooting",
                    "lock": "True",
                    "confirmation": "Reboot CPE?",
                    "rpc": "RebootAndWait",
                    "params": "Reboot by Axess Server",
                    "timeout": 600
                },
                {
                    "pr": "FactoryReset",
                    "confirmation": "Reset CPE?",
                    "rpc": "FactoryReset",
                },

            ],
            "images": [
                {
                    "url": "",
                    "descr": "front view",
                },

                {
                    "url": "",
                    "descr": "back view",
                }
            ]

        },

        'ontop_devices_widget': {
            "__type": "support-portal-column-layout",
            "name": "Service Overview",
            'width': 6,
            "elements": [
                {
                    "pr": "Service Overview",
                    "name": "Services",
                    "flow": "MainDiagFlow",
                    "__onhead": "True",
                    "__type": "section-widget",
                    "columns": 2,
                    "width": 12,
                    "elements": get_widget_element('device_info_widget', cpe_dump)
                }
            ]
        },

        'ontop_wifi_lan_ports_widget': {
            "__type": "support-portal-column-layout",
            "width": 12,
            "elements": [
                {
                    "__type": "section-table-widget",
                    "__flow": "SmartIndexGPV",
                    "name": "LAN STATUS",
                    "pr": "WIFI/LAN Status",
                    "width": 12,
                    "elements": [

                    ]}]}

    }
    if len([item for item in params.wan_ip if check_features.isPart(item, cpe_dump)]) != 0:
        widgets['wan_ip_widget_front']['selector'] = \
        [item for item in params.wan_ip if check_features.isPart(item, cpe_dump)][0]

    if len([item for item in params.wan_ppp if check_features.isPart(item, cpe_dump)]) != 0:
        widgets['wan_ppp_widget_front']['selector'] = \
        [item for item in params.wan_ppp if check_features.isPart(item, cpe_dump)][0]

    if len([item for item in params.wan_pots if check_features.isPart(item, cpe_dump)]) != 0:
        widgets['wan_pots_widget_front']['selector'] = \
            [item for item in params.wan_pots if check_features.isPart(item, cpe_dump)][0]

    if len([item for item in params.wadsl if check_features.isPart(item, cpe_dump) or check_features.isPartSmartIndex(item, cpe_dump)]) != 0:
        widgets['wan_dsl_link_widget_front']['selector'] = \
            [item for item in params.wadsl if
             check_features.isPart(item, cpe_dump) or check_features.isPartSmartIndex(item, cpe_dump)][0]

    if len([item for item in params.wan_ip_stats if check_features.isPart(item, cpe_dump)]) != 0:
        widgets['wan_ip_stats_widget_front']['selector'] = \
            [item for item in params.wan_ip_stats if check_features.isPart(item, cpe_dump)][0]

    if len([item for item in params.wan_ppp_stats if check_features.isPart(item, cpe_dump)]) != 0:
        widgets['wan_ppp_stats_widget_front']['selector'] = \
            [item for item in params.wan_ppp_stats if check_features.isPart(item, cpe_dump)][0]

    if len([item for item in params.wan_common_stats if check_features.isPart(item, cpe_dump)]) != 0:
        widgets['wan_common_stats_widget_front']['selector'] = \
            [item for item in params.wan_common_stats if check_features.isPart(item, cpe_dump)][0]

    if len([item for item in params.wan_eth_stats if check_features.isPart(item, cpe_dump)]) != 0:
        widgets['wan_ethernet_stats_widget_front']['selector'] = \
            [item for item in params.wan_eth_stats if check_features.isPart(item, cpe_dump)][0]


    if len([item for item in params.serving_pool if check_features.isPart(item, cpe_dump)]) != 0:
        widgets['dhcp_widget_front']['selector'] = \
            [item for item in params.serving_pool if check_features.isPart(item, cpe_dump)][0]

    if len([item for item in params.wadsl if check_features.isPart(item, cpe_dump) or check_features.isPartSmartIndex(item, cpe_dump)]) != 0:
        widgets['WAN_DSL_Info_Smart']['selector'] = \
            [item for item in params.wadsl if
             check_features.isPart(item, cpe_dump) or check_features.isPartSmartIndex(item, cpe_dump)][0]

    if len([item for item in params.wadsl if check_features.isPart(item, cpe_dump) or check_features.isPartSmartIndex(item, cpe_dump)]) != 0:
        widgets['WAN_DSL_Info_Smart']['selector'] = \
            [item for item in params.wadsl if
             check_features.isPart(item, cpe_dump) or check_features.isPartSmartIndex(item, cpe_dump)][0]


    widget = widgets[widget_name]


    return widget
