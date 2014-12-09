from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6Routes(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Distance: {"type": "number", "format": "number"}
    :param Interface: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param Metric: {"type": "number", "format": "number"}
    :param Nexthop: {"type": "string", "format": "ipv6-address"}
    :param Subtype: {"enum": ["inter-area", "nssa-type-1", "nssa-type-2", "external-type-1", "external-type-2", "level-1", "level-2"], "type": "string", "format": "enum"}
    :param Prefix: {"type": "string", "format": "ipv6-address"}
    :param PrefixLen: {"type": "number", "format": "number"}
    :param Type: {"enum": ["kernel", "connected", "static", "rip", "ospf", "bgp", "isis", "vip", "selected-vip", "ip-nat-list", "ip-nat", "floating-ip", "a10"], "type": "string", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "IPv6-routes"
        self.DeviceProxy = ""
        self.Distance = ""
        self.Interface = ""
        self.Metric = ""
        self.Nexthop = ""
        self.Subtype = ""
        self.Prefix = ""
        self.PrefixLen = ""
        self.Type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param IPv6_routes: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"Distance": {"type": "number", "format": "number"}, "Interface": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "optional": true, "Metric": {"type": "number", "format": "number"}, "Nexthop": {"type": "string", "format": "ipv6-address"}, "Subtype": {"enum": ["inter-area", "nssa-type-1", "nssa-type-2", "external-type-1", "external-type-2", "level-1", "level-2"], "type": "string", "format": "enum"}, "Prefix": {"type": "string", "format": "ipv6-address"}, "PrefixLen": {"type": "number", "format": "number"}, "Type": {"enum": ["kernel", "connected", "static", "rip", "ospf", "bgp", "isis", "vip", "selected-vip", "ip-nat-list", "ip-nat", "floating-ip", "a10"], "type": "string", "format": "enum"}}}]}
    :param Total: {"type": "number", "format": "number"}
    :param Limit: {"type": "number", "format": "number"}
    :param Description: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.IPv6_routes = []
        self.Total = ""
        self.Limit = ""
        self.Description = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rib(A10BaseClass):
    
    """Class Description::
    Operational Status for the object rib.

    Class rib supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/rib/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rib"
        self.a10_url="/axapi/v3/ipv6/rib/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


