"""
Load dump from CPE into dictionary
"""

def is_valid(cpe_dump):
    if "InternetGatewayDevice.DeviceInfo.ModelName" in cpe_dump.keys():
        return True
    else:
        return False

def load_dump(dump_path='example.dump'):
    parameters = []
    with open(dump_path) as myfile:
        read_data = myfile.read()
        info = read_data.split('\n')
        for i in info:
            parameters.append(i)

    parameters_from_dump = {}
    for item in parameters:
        if len(item.split(':')) > 1:
            parameters_from_dump[item.split(':')[0].strip()] = item.split(':')[1]

    cpe_dump = parameters_from_dump
    if is_valid(cpe_dump):
         return cpe_dump
    else:
         raise KeyError("Wrong dump file")

