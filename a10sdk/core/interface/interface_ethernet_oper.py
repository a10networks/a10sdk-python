from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param line_protocol: {"enum": ["UP", "DOWN"], "type": "string", "format": "enum"}
    :param config_speed: {"enum": ["10Mbit", "100Mbit", "1Gbit", "10Gbit", "40Gbit", "auto"], "type": "string", "format": "enum"}
    :param ipv4_netmask: {"type": "string", "description": "IP subnet mask", "format": "ipv4-netmask"}
    :param mac: {"minLength": 11, "maxLength": 17, "type": "string", "format": "mac-address"}
    :param actual_speed: {"enum": ["10Mbit", "100Mbit", "1Gbit", "10Gbit", "40Gbit", "unknown"], "type": "string", "format": "enum"}
    :param state: {"enum": ["UP", "DISABLED", "DOWN"], "type": "string", "format": "enum"}
    :param actual_duplexity: {"enum": ["Full", "fdx", "Half", "hdx", "auto"], "type": "string", "format": "enum"}
    :param media_type: {"enum": ["Copper", "Fiber"], "type": "string", "format": "enum"}
    :param ipv4_address: {"type": "string", "description": "IP address", "format": "ipv4-address"}
    :param config_duplexity: {"enum": ["Full", "fdx", "Half", "hdx", "auto"], "type": "string", "format": "enum"}
    :param link_type: {"enum": ["GigabitEthernet", "10Gig", "40Gig"], "type": "string", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.line_protocol = ""
        self.config_speed = ""
        self.ipv4_netmask = ""
        self.mac = ""
        self.actual_speed = ""
        self.state = ""
        self.actual_duplexity = ""
        self.media_type = ""
        self.ipv4_address = ""
        self.config_duplexity = ""
        self.link_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ethernet(A10BaseClass):
    
    """Class Description::
    Operational Status for the object ethernet.

    Class ethernet supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ifnum: {"optional": false, "oid": "1001", "type": "number", "description": "Ethernet interface number", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ethernet/{ifnum}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ethernet"
        self.a10_url="/axapi/v3/interface/ethernet/{ifnum}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.ifnum = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


