from a10sdk.common.A10BaseClass import A10BaseClass


class PortList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param action: {"type": "string", "format": "string"}
    :param ethernet: {"type": "number", "format": "number"}
    :param management: {"type": "number", "format": "number"}
    :param ve: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "port-list"
        self.DeviceProxy = ""
        self.action = ""
        self.ethernet = ""
        self.management = ""
        self.ve = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param port_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"action": {"type": "string", "format": "string"}, "ethernet": {"type": "number", "format": "number"}, "management": {"type": "number", "format": "number"}, "optional": true, "ve": {"type": "number", "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.port_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AclIpv4(A10BaseClass):
    
    """Class Description::
    Operational Status for the object acl-ipv4.

    Class acl-ipv4 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/enable-management/acl-ipv4/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "acl-ipv4"
        self.a10_url="/axapi/v3/enable-management/acl-ipv4/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


