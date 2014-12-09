from a10sdk.common.A10BaseClass import A10BaseClass


class Network(A10BaseClass):
    
    """Class Description::
    Enable network group traps.

    Class network supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param trunk_port_threshold: {"default": 0, "optional": true, "type": "number", "description": "Enable network trunk-port-threshold trap", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/network`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "network"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/network"
        self.DeviceProxy = ""
        self.trunk_port_threshold = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


