from a10sdk.common.A10BaseClass import A10BaseClass


class Gslb(A10BaseClass):
    
    """Class Description::
    Enable GSLB group traps.

    Class gslb supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param all: {"default": 0, "optional": true, "type": "number", "description": "Enable all GSLB traps", "format": "flag"}
    :param service_ip: {"default": 0, "optional": true, "type": "number", "description": "Enable GSLB service-ip related traps", "format": "flag"}
    :param group: {"default": 0, "optional": true, "type": "number", "description": "Enable GSLB group related traps", "format": "flag"}
    :param site: {"default": 0, "optional": true, "type": "number", "description": "Enable GSLB site related traps", "format": "flag"}
    :param zone: {"default": 0, "optional": true, "type": "number", "description": "Enable GSLB zone related traps", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/gslb`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "gslb"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/gslb"
        self.DeviceProxy = ""
        self.A10WW_all = ""
        self.service_ip = ""
        self.group = ""
        self.site = ""
        self.zone = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


