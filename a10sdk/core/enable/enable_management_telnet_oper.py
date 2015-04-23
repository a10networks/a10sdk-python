from a10sdk.common.A10BaseClass import A10BaseClass


class PortList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param management: {"type": "number", "format": "number"}
    :param ve: {"type": "number", "format": "number"}
    :param ipv6_acl: {"type": "string", "format": "string"}
    :param ipv4_acl: {"type": "string", "format": "string"}
    :param action: {"type": "string", "format": "string"}
    :param ethernet: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "port-list"
        self.DeviceProxy = ""
        self.management = ""
        self.ve = ""
        self.ipv6_acl = ""
        self.ipv4_acl = ""
        self.action = ""
        self.ethernet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"management": {"type": "number", "format": "number"}, "ve": {"type": "number", "format": "number"}, "ipv6-acl": {"type": "string", "format": "string"}, "ipv4-acl": {"type": "string", "format": "string"}, "action": {"type": "string", "format": "string"}, "ethernet": {"type": "number", "format": "number"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.port_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Telnet(A10BaseClass):
    
    """Class Description::
    Operational Status for the object telnet.

    Class telnet supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/enable-management/telnet/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "telnet"
        self.a10_url="/axapi/v3/enable-management/telnet/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


