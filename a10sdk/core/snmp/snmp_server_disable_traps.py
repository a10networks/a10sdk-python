from a10sdk.common.A10BaseClass import A10BaseClass


class Traps(A10BaseClass):
    
    """Class Description::
    Disable l3v partition SNMP traps.

    Class traps supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param all: {"default": 0, "optional": true, "type": "number", "description": "Disable all traps on this partition", "format": "flag"}
    :param slb_change: {"default": 0, "optional": true, "type": "number", "description": "Disable all slb-change traps on this partition", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param snmp: {"default": 0, "optional": true, "type": "number", "description": "Disable all snmp traps on this partition", "format": "flag"}
    :param gslb: {"default": 0, "optional": true, "type": "number", "description": "Disable all gslb traps on this partition", "format": "flag"}
    :param slb: {"default": 0, "optional": true, "type": "number", "description": "Disable all slb traps on this partition", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/disable/traps`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "traps"
        self.a10_url="/axapi/v3/snmp-server/disable/traps"
        self.DeviceProxy = ""
        self.A10WW_all = ""
        self.slb_change = ""
        self.uuid = ""
        self.snmp = ""
        self.gslb = ""
        self.slb = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


