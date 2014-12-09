from a10sdk.common.A10BaseClass import A10BaseClass


class VrrpA(A10BaseClass):
    
    """Class Description::
    Enable VRRP-A group traps.

    Class vrrp-a supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param active: {"default": 0, "optional": true, "type": "number", "description": "Enable VRRP-A active trap", "format": "flag"}
    :param standby: {"default": 0, "optional": true, "type": "number", "description": "Enable VRRP-A standby trap", "format": "flag"}
    :param all: {"default": 0, "optional": true, "type": "number", "description": "Enable all VRRP-A group traps", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/vrrp-a`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vrrp-a"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/vrrp-a"
        self.DeviceProxy = ""
        self.active = ""
        self.standby = ""
        self.A10WW_all = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


