from a10sdk.common.A10BaseClass import A10BaseClass


class Snmp(A10BaseClass):
    
    """Class Description::
    Enable SNMP group traps.

    Class snmp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param linkup: {"default": 0, "optional": true, "type": "number", "description": "Enable SNMP link-up trap", "format": "flag"}
    :param all: {"default": 0, "optional": true, "type": "number", "description": "Enable all SNMP group traps", "format": "flag"}
    :param linkdown: {"default": 0, "optional": true, "type": "number", "description": "Enable SNMP link-down trap", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps/snmp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "snmp"
        self.a10_url="/axapi/v3/snmp-server/enable/traps/snmp"
        self.DeviceProxy = ""
        self.linkup = ""
        self.A10WW_all = ""
        self.linkdown = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


