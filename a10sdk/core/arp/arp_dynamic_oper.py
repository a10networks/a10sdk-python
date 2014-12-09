from a10sdk.common.A10BaseClass import A10BaseClass


class ArpList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Age: {"minimum": 60, "type": "number", "maximum": 86400, "format": "number"}
    :param Vlan: {"minimum": 1, "type": "number", "maximum": 4094, "format": "number"}
    :param IP_Address: {"type": "string", "format": "ipv4-address"}
    :param Interface: {"enum": ["Management", "ethernet", "trunk"], "type": "string", "format": "enum"}
    :param Type: {"enum": ["Incomplete", "Dynamic", "Static"], "type": "string", "format": "enum"}
    :param MAC_Address: {"minLength": 11, "maxLength": 17, "type": "string", "format": "mac-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "arp-list"
        self.DeviceProxy = ""
        self.Age = ""
        self.Vlan = ""
        self.IP_Address = ""
        self.Interface = ""
        self.Type = ""
        self.MAC_Address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param arp_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "Age": {"minimum": 60, "type": "number", "maximum": 86400, "format": "number"}, "Vlan": {"minimum": 1, "type": "number", "maximum": 4094, "format": "number"}, "IP-Address": {"type": "string", "format": "ipv4-address"}, "Interface": {"enum": ["Management", "ethernet", "trunk"], "type": "string", "format": "enum"}, "Type": {"enum": ["Incomplete", "Dynamic", "Static"], "type": "string", "format": "enum"}, "MAC-Address": {"minLength": 11, "maxLength": 17, "type": "string", "format": "mac-address"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.arp_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dynamic(A10BaseClass):
    
    """Class Description::
    Operational Status for the object dynamic.

    Class dynamic supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/arp/dynamic/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dynamic"
        self.a10_url="/axapi/v3/arp/dynamic/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


