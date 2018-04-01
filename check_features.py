import re


"""
#Functions to identify there is our parameter in device's dump
"""


def isConsist(parameter, data):
    if parameter in data:
        return True
    else:
        return False


def isConsistPartly(parameter, cpe_dump):
    new_data = []
    for item in cpe_dump:
        new_item = ".".join(item.split(".")[0:2])
        new_data.append(new_item)
    if parameter in new_data:
        return True
    else:
        return False


def isConsistPartly3(parameter, cpe_dump):
    new_data = []
    for item in cpe_dump:
        new_item = ".".join(item.split(".")[0:3])
        new_data.append(new_item)
    if parameter in new_data:
        return True
    else:
        return False


def isConsistPartly4(parameter, cpe_dump):
    new_data = []
    for item in cpe_dump:
        new_item = ".".join(item.split(".")[0:4])
        new_data.append(new_item)
    if parameter in new_data:
        return True
    else:
        return False


def isConsistPartly8(parameter, cpe_dump):
    new_data = []
    for item in cpe_dump:
        new_item = ".".join(item.split(".")[0:8])
        new_data.append(new_item)
    if parameter in new_data:
        return True
    else:
        return False


def isPart(parameter, cpe_dump):
    new_param_start = parameter.split("_x_")[0]
    if len(parameter.split("_x_")) > 1:
        new_param_end = parameter.split("_x_")[1]
    new_item = re.sub("\.[0-9]+\.", "._x_.", parameter)
    temp_data = []
    temp_indexes = []
    for k in cpe_dump:
        if k.startswith(new_param_start) and k.endswith(new_param_end):
            temp_key = k.split(new_param_start)[1][0]
            new_b = re.sub("\.[0-9]+\.", "._x_.", k)
            if new_item == new_b:
                if temp_key not in temp_data:
                    temp_data.append(temp_key)
        if k.startswith(new_param_start):
            temp_index = k.split(new_param_start)[1][0]
            if temp_index not in temp_indexes:
                temp_indexes.append(temp_index)
    if len(temp_data) == len(temp_indexes) and len(temp_data) != 0:
        return True
    return False


def isPartTwo(parameter, cpe_dump):
    new_param_start = parameter.split("_x_")[0]
    if len(parameter.split("_y_")) > 1:
        new_param_end = parameter.split("_y_")[1]
    new_item = re.sub("\.[0-9]+\.", "._x_.", parameter)
    new_item = new_item.replace('_y_', '_x_')
    temp_data1 = []
    temp_data2 = []
    temp_indexes = []
    for k in cpe_dump:
        if k.startswith(new_param_start) and k.endswith(new_param_end):
            temp_key_1 = k.split(new_param_start)[1].split('.')[0]
            temp_key_2 = k.split(new_param_end)[0][-1]
            new_b = re.sub("\.[0-9]+\.", "._x_.", k)
            if new_item == new_b:
                if temp_key_1 not in temp_data1:
                    temp_data1.append(temp_key_1)
                if temp_key_2 not in temp_data2:
                    temp_data2.append(temp_key_2)

        if k.startswith(new_param_start):
            temp_index = k.split(new_param_start)[1][0]
            if temp_index not in temp_indexes:
                temp_indexes.append(temp_index)
    if len(temp_data1) == len(temp_indexes) and len(temp_data1) != 0:
        return True
    return False


def isPartSmartIndex(parameter, cpe_dump):
    new_parameter = ".".join(parameter.split(".")[1::])
    new_p = new_parameter.replace("smartIndex1", "_x_")
    new_param = re.sub("\.[0-9]+\.", "._x_.", new_p)
    for k in cpe_dump:
        new_k = re.sub("\.[0-9]+\.", "._x_.", k)
        if new_param == new_k:
            return True
    return False


def getListWLAN(type, cpe_dump):
    wlan2_4 = []
    wlan5 = []
    for k, v in cpe_dump.items():
        if k.endswith('PossibleChannels'):
            if v == ' 1,2,3,4,5,6,7,8,9,10,11,12,13' or v == ' 1-13':
                index2 = k.split('.')[-2]
                if index2 not in wlan2_4:
                    wlan2_4.append(index2)
            else:
                index5 = k.split('.')[-2]
                if index5 not in wlan5:
                    wlan5.append(index5)
        elif k.endswith('Channel'):
            if v in [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', ' 10', ' 11', ' 12', ' 13'] \
                    or v in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]:
                index2 = k.split('.')[-2]
                if index2 not in wlan2_4:
                    wlan2_4.append(index2)
            else:
                index5 = k.split('.')[-2]
                if index5 not in wlan5:
                    wlan5.append(index5)

    if type == '2.4':
        return wlan2_4
    elif type == '5':
        return wlan5

def isMaxBitRateInLEIC(found_list):
    flag = False
    for i in found_list:
        for k,v in i.items():
            if 'LANEthernetInterfaceConfig' in v:
                flag = True
    return flag



