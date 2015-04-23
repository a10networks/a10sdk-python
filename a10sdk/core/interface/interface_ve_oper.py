from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param line_protocol: {"enum": ["UP", "DOWN"], "type": "string", "format": "enum"}
    :param ipv4_netmask: {"type": "string", "description": "IP subnet mask", "format": "ipv4-netmask"}
    :param mac: {"minLength": 11, "maxLength": 17, "type": "string", "format": "mac-address"}
    :param state: {"enum": ["UP", "DISABLED", "DOWN"], "type": "string", "format": "enum"}
    :param ipv4_address: {"type": "string", "description": "IP address", "format": "ipv4-address"}
    :param link_type: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.line_protocol = ""
        self.ipv4_netmask = ""
        self.mac = ""
        self.state = ""
        self.ipv4_address = ""
        self.link_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ve(A10BaseClass):
    
    """Class Description::
    Operational Status for the object ve.

    Class ve supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ifnum: {"optional": false, "oid": "1001", "type": "number", "description": "Virtual ethernet interface number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ve/{ifnum}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ve"
        self.a10_url="/axapi/v3/interface/ve/{ifnum}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.ifnum = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


