from a10sdk.common.A10BaseClass import A10BaseClass


class VipList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param level: {"default": "level-2", "enum": ["level-1", "level-1-2", "level-2"], "type": "string", "description": "'level-1': IS-IS level-1 routes only; 'level-1-2': IS-IS level-1 and level-2 routes; 'level-2': IS-IS level-2 routes only; ", "format": "enum"}
    :param type: {"enum": ["only-flagged", "only-not-flagged"], "type": "string", "description": "'only-flagged': Selected Virtual IP (VIP); 'only-not-flagged': Only not flagged; ", "format": "enum"}
    :param metric: {"description": "Metric for redistributed routes (IS-IS default metric)", "format": "number", "default": 0, "maximum": 4261412864, "minimum": 0, "type": "number"}
    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param metric_type: {"default": "internal", "enum": ["external", "internal"], "type": "string", "description": "'external': Set IS-IS External metric type; 'internal': Set IS-IS Internal metric type; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vip-list"
        self.DeviceProxy = ""
        self.level = ""
        self.A10WW_type = ""
        self.metric = ""
        self.route_map = ""
        self.metric_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RedistList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param level: {"default": "level-2", "enum": ["level-1", "level-1-2", "level-2"], "type": "string", "description": "'level-1': IS-IS level-1 routes only; 'level-1-2': IS-IS level-1 and level-2 routes; 'level-2': IS-IS level-2 routes only; ", "format": "enum"}
    :param type: {"enum": ["bgp", "connected", "floating-ip", "ip-nat-list", "ip-nat", "lw4o6", "nat64", "ospf", "rip", "static"], "type": "string", "description": "'bgp': Border Gateway Protocol (BGP); 'connected': Connected; 'floating-ip': Floating IP; 'ip-nat-list': IP NAT list; 'ip-nat': IP NAT; 'lw4o6': LW4O6 Prefix; 'nat64': NAT64 Prefix; 'ospf': Open Shortest Path First (OSPF); 'rip': Routing Information Protocol (RIP); 'static': Static routes; ", "format": "enum"}
    :param metric: {"description": "Metric for redistributed routes (IS-IS default metric)", "format": "number", "default": 0, "maximum": 4261412864, "minimum": 0, "type": "number"}
    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param metric_type: {"default": "internal", "enum": ["external", "internal"], "type": "string", "description": "'external': Set IS-IS External metric type; 'internal': Set IS-IS Internal metric type; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "redist-list"
        self.DeviceProxy = ""
        self.level = ""
        self.A10WW_type = ""
        self.metric = ""
        self.route_map = ""
        self.metric_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Into2(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distribute_list: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Select routes (Access-list name)", "format": "string"}
    :param level_1: {"default": 0, "type": "number", "description": "Inter-area routes into level-2", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "into-2"
        self.DeviceProxy = ""
        self.distribute_list = ""
        self.level_1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Level2From(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "level-2-from"
        self.DeviceProxy = ""
        self.into_2 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Into1(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param level_2: {"default": 0, "type": "number", "description": "Inter-area routes into level-2", "format": "flag"}
    :param distribute_list: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Select routes (Access-list name)", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "into-1"
        self.DeviceProxy = ""
        self.level_2 = ""
        self.distribute_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Level1From(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "level-1-from"
        self.DeviceProxy = ""
        self.into_1 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Isis(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "isis"
        self.DeviceProxy = ""
        self.level_2_from = {}
        self.level_1_from = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Redistribute(A10BaseClass):
    
    """Class Description::
    Redistribute information from another routing protocol.

    Class redistribute supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vip_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"level": {"default": "level-2", "enum": ["level-1", "level-1-2", "level-2"], "type": "string", "description": "'level-1': IS-IS level-1 routes only; 'level-1-2': IS-IS level-1 and level-2 routes; 'level-2': IS-IS level-2 routes only; ", "format": "enum"}, "type": {"enum": ["only-flagged", "only-not-flagged"], "type": "string", "description": "'only-flagged': Selected Virtual IP (VIP); 'only-not-flagged': Only not flagged; ", "format": "enum"}, "metric": {"description": "Metric for redistributed routes (IS-IS default metric)", "format": "number", "default": 0, "maximum": 4261412864, "minimum": 0, "type": "number"}, "route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}, "optional": true, "metric-type": {"default": "internal", "enum": ["external", "internal"], "type": "string", "description": "'external': Set IS-IS External metric type; 'internal': Set IS-IS Internal metric type; ", "format": "enum"}}}]}
    :param redist_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"level": {"default": "level-2", "enum": ["level-1", "level-1-2", "level-2"], "type": "string", "description": "'level-1': IS-IS level-1 routes only; 'level-1-2': IS-IS level-1 and level-2 routes; 'level-2': IS-IS level-2 routes only; ", "format": "enum"}, "type": {"enum": ["bgp", "connected", "floating-ip", "ip-nat-list", "ip-nat", "lw4o6", "nat64", "ospf", "rip", "static"], "type": "string", "description": "'bgp': Border Gateway Protocol (BGP); 'connected': Connected; 'floating-ip': Floating IP; 'ip-nat-list': IP NAT list; 'ip-nat': IP NAT; 'lw4o6': LW4O6 Prefix; 'nat64': NAT64 Prefix; 'ospf': Open Shortest Path First (OSPF); 'rip': Routing Information Protocol (RIP); 'static': Static routes; ", "format": "enum"}, "metric": {"description": "Metric for redistributed routes (IS-IS default metric)", "format": "number", "default": 0, "maximum": 4261412864, "minimum": 0, "type": "number"}, "route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}, "optional": true, "metric-type": {"default": "internal", "enum": ["external", "internal"], "type": "string", "description": "'external': Set IS-IS External metric type; 'internal': Set IS-IS Internal metric type; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/isis/{tag}/address-family/ipv6/redistribute`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "redistribute"
        self.a10_url="/axapi/v3/router/isis/{tag}/address-family/ipv6/redistribute"
        self.DeviceProxy = ""
        self.vip_list = []
        self.redist_list = []
        self.isis = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


