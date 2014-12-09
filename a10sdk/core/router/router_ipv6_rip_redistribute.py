from a10sdk.common.A10BaseClass import A10BaseClass


class VipList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param metric: {"description": "Metric for redistributed routes (metric value)", "minimum": 0, "type": "number", "maximum": 16, "format": "number"}
    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param type: {"enum": ["only-flagged", "only-not-flagged"], "type": "string", "description": "'only-flagged': Selected Virtual IP (VIP); 'only-not-flagged': Only not flagged; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vip-list"
        self.DeviceProxy = ""
        self.metric = ""
        self.route_map = ""
        self.A10WW_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RedistList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param metric: {"description": "Metric for redistributed routes (metric value)", "minimum": 0, "type": "number", "maximum": 16, "format": "number"}
    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param type: {"enum": ["bgp", "connected", "floating-ip", "ip-nat-list", "ip-nat", "isis", "lw4o6", "nat64", "ospf", "static"], "type": "string", "description": "'bgp': Border Gateway Protocol (BGP); 'connected': Connected; 'floating-ip': Floating IP; 'ip-nat-list': IP NAT list; 'ip-nat': IP NAT; 'isis': ISO IS-IS; 'lw4o6': LW4O6 Prefix; 'nat64': NAT64 Prefix; 'ospf': Open Shortest Path First (OSPF); 'static': Static routes; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "redist-list"
        self.DeviceProxy = ""
        self.metric = ""
        self.route_map = ""
        self.A10WW_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Redistribute(A10BaseClass):
    
    """Class Description::
    Redistribute information from another routing protocol.

    Class redistribute supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vip_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "metric": {"description": "Metric for redistributed routes (metric value)", "minimum": 0, "type": "number", "maximum": 16, "format": "number"}, "route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}, "type": {"enum": ["only-flagged", "only-not-flagged"], "type": "string", "description": "'only-flagged': Selected Virtual IP (VIP); 'only-not-flagged': Only not flagged; ", "format": "enum"}}}]}
    :param redist_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "metric": {"description": "Metric for redistributed routes (metric value)", "minimum": 0, "type": "number", "maximum": 16, "format": "number"}, "route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}, "type": {"enum": ["bgp", "connected", "floating-ip", "ip-nat-list", "ip-nat", "isis", "lw4o6", "nat64", "ospf", "static"], "type": "string", "description": "'bgp': Border Gateway Protocol (BGP); 'connected': Connected; 'floating-ip': Floating IP; 'ip-nat-list': IP NAT list; 'ip-nat': IP NAT; 'isis': ISO IS-IS; 'lw4o6': LW4O6 Prefix; 'nat64': NAT64 Prefix; 'ospf': Open Shortest Path First (OSPF); 'static': Static routes; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ipv6/rip/redistribute`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "redistribute"
        self.a10_url="/axapi/v3/router/ipv6/rip/redistribute"
        self.DeviceProxy = ""
        self.vip_list = []
        self.redist_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


