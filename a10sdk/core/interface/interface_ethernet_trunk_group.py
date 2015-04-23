from a10sdk.common.A10BaseClass import A10BaseClass


class UdldTimeoutCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param slow: {"description": "slow timeout in unit of seconds", "format": "number", "default": 1, "maximum": 60, "minimum": 1, "not": "fast", "type": "number"}
    :param fast: {"description": "fast timeout in unit of milli-seconds", "format": "number", "default": 1000, "maximum": 1000, "minimum": 100, "not": "slow", "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "udld-timeout-cfg"
        self.DeviceProxy = ""
        self.slow = ""
        self.fast = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TrunkGroup(A10BaseClass):
    
    """Class Description::
    Trunk Group Settings.

    Class trunk-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param trunk_number: {"description": "Trunk Number", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": false}
    :param mode: {"description": "'active': enable initiation of LACP negotiation on a port(default); 'passive': disable initiation of LACP negotiation on a port; ", "format": "enum", "default": "active", "type": "string", "enum": ["active", "passive"], "optional": true}
    :param timeout: {"description": "'long': Set LACP long timeout (default); 'short': Set LACP short timeout; ", "format": "enum", "default": "long", "type": "string", "enum": ["long", "short"], "optional": true}
    :param type: {"description": "'static': Static (default); 'lacp': lacp; 'lacp-udld': lacp-udld; ", "format": "enum", "default": "static", "optional": true, "enum": ["static", "lacp", "lacp-udld"], "modify-not-allowed": 1, "type": "string"}
    :param admin_key: {"description": "LACP admin key (Admin key value)", "format": "number", "type": "number", "maximum": 65535, "minimum": 10000, "optional": true}
    :param port_priority: {"description": "Set LACP priority for a port (LACP port priority)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ethernet/{ifnum}/trunk-group/{trunk_number}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "trunk_number"]

        self.b_key = "trunk-group"
        self.a10_url="/axapi/v3/interface/ethernet/{ifnum}/trunk-group/{trunk_number}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.trunk_number = ""
        self.udld_timeout_cfg = {}
        self.mode = ""
        self.timeout = ""
        self.A10WW_type = ""
        self.admin_key = ""
        self.port_priority = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


