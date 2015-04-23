from a10sdk.common.A10BaseClass import A10BaseClass


class Traps(A10BaseClass):
    
    """Class Description::
    Enable SNMP traps.

    Class traps supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param lldp: {"default": 0, "optional": true, "type": "number", "description": "Enable lldp traps", "format": "flag"}
    :param all: {"default": 0, "optional": true, "type": "number", "description": "Enable all SNMP traps", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/enable/traps`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "traps"
        self.a10_url="/axapi/v3/snmp-server/enable/traps"
        self.DeviceProxy = ""
        self.lldp = ""
        self.A10WW_all = ""
        self.slb_change = {}
        self.uuid = ""
        self.lsn = {}
        self.vrrp_a = {}
        self.snmp = {}
        self.system = {}
        self.routing = {}
        self.gslb = {}
        self.slb = {}
        self.network = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


