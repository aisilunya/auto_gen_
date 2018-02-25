# AUTO CONFIG GENERATOR:

This script helps to automatically make config file for CPE.

# REQUIREMENTS:

* python2
* re
* json


# INSTALL:
1. Clone this repo.


# HOWTO:
1. Run RPC command 'GetParameterValues' for parameter 'I.' on the CPEManager/.
2. Save results to file 'dump_from_device.dump'.
3. Run generator:

```
python2 generator.py dump_from_device.dump support_portal_config.json
```

4. Config file will be in file 'support_portal_config.json'.
5. Add word "return" before dictionary.


# KNOWN ISSUES:

1.Config file includes standard 'changeFlows'.
2. Script does not include case when parameter is like
"InternetGatewayDevice.WANDevice.1.WANConnectionDevice._x_.WANIPConnection._y_.Name".
3.Script does not include any VENDOR parameter.
