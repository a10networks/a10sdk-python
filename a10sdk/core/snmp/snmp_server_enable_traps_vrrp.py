from a10sdk.common.A10BaseClass import A10BaseClass


class Vrrp(A10BaseClass):
    
    """Class Description::
    Enable HA group traps.

    Class vrrp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param active: {"default": 0, "optional": true, "type": "number", "description": "Enable vrrp active trap", "format": "flag"}
    :param standby: {"default": 0, "optional": true, "type": "number", "description": "Enable vrrp standby trap", "format": "flag"}
    :param all: {"default": 0, "optional": true, "type": "number", "description": "Enable all vrrp group traps", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/vrrp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vrrp"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/vrrp"
        self.DeviceProxy = ""
        self.active = ""
        self.standby = ""
        self.A10WW_all = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


