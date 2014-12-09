from a10sdk.common.A10BaseClass import A10BaseClass


class Rt(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param value: {"type": "string", "description": "VPN extended community", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rt"
        self.DeviceProxy = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Soo(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param value: {"type": "string", "description": "VPN extended community", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "soo"
        self.DeviceProxy = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Extcommunity(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "extcommunity"
        self.DeviceProxy = ""
        self.rt = {}
        self.soo = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Origin(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param egp: {"default": 0, "not-list": ["igp", "incomplete"], "type": "number", "description": "remote EGP", "format": "flag"}
    :param incomplete: {"default": 0, "not-list": ["egp", "igp"], "type": "number", "description": "unknown heritage", "format": "flag"}
    :param igp: {"default": 0, "not-list": ["egp", "incomplete"], "type": "number", "description": "local IGP", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "origin"
        self.DeviceProxy = ""
        self.egp = ""
        self.incomplete = ""
        self.igp = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AggregatorAs(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip: {"type": "string", "description": "IP address of aggregator", "format": "ipv4-address"}
    :param asn: {"description": "AS number", "minimum": 1, "type": "number", "maximum": 4294967295, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "aggregator-as"
        self.DeviceProxy = ""
        self.ip = ""
        self.asn = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Aggregator(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "aggregator"
        self.DeviceProxy = ""
        self.aggregator_as = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Weight(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param weight_val: {"description": "Weight value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "weight"
        self.DeviceProxy = ""
        self.weight_val = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Level(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param value: {"enum": ["level-1", "level-1-2", "level-2"], "type": "string", "description": "'level-1': Export into a level-1 area; 'level-1-2': Export into level-1 and level-2; 'level-2': Export into level-2 sub-domain; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "level"
        self.DeviceProxy = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NextHop(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param address: {"type": "string", "description": "IP address of next hop", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "next-hop"
        self.DeviceProxy = ""
        self.address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ip(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip"
        self.DeviceProxy = ""
        self.next_hop = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Metric(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param value: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Metric value", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "metric"
        self.DeviceProxy = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AsPath(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param num: {"description": "AS number", "minimum": 1, "type": "number", "maximum": 4294967295, "format": "number"}
    :param num2: {"description": "AS number", "minimum": 1, "type": "number", "maximum": 4294967295, "format": "number"}
    :param prepend: {"type": "string", "description": "Prepend to the as-path (AS number)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "as-path"
        self.DeviceProxy = ""
        self.num = ""
        self.num2 = ""
        self.prepend = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CommList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param name: {"description": "Community-list name", "format": "string", "minLength": 1, "not-list": ["v-std", "v-exp"], "maxLength": 128, "type": "string"}
    :param v_std: {"description": "Community-list number (standard)", "format": "number", "not-list": ["v-exp", "name"], "maximum": 99, "minimum": 1, "type": "number"}
    :param v_exp_delete: {"default": 0, "type": "number", "description": "Delete matching communities", "format": "flag"}
    :param v_exp: {"description": "Community-list number (expanded)", "format": "number", "not-list": ["v-std", "name"], "maximum": 199, "minimum": 100, "type": "number"}
    :param name_delete: {"default": 0, "type": "number", "description": "Delete matching communities", "format": "flag"}
    :param delete: {"default": 0, "type": "number", "description": "Delete matching communities", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "comm-list"
        self.DeviceProxy = ""
        self.name = ""
        self.v_std = ""
        self.v_exp_delete = ""
        self.v_exp = ""
        self.name_delete = ""
        self.delete = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LocalPreference(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param val: {"description": "Preference value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "local-preference"
        self.DeviceProxy = ""
        self.val = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Tag(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param value: {"description": "Tag value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "tag"
        self.DeviceProxy = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Local(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param address: {"type": "string", "description": "IPv6 address of next hop", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "local"
        self.DeviceProxy = ""
        self.address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NextHop1(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param address: {"type": "string", "description": "global address of next hop", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "next-hop-1"
        self.DeviceProxy = ""
        self.local = {}
        self.address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6"
        self.DeviceProxy = ""
        self.next_hop_1 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DampeningCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dampening_max_supress: {"description": "Maximum duration to suppress a stable route(minutes)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param dampening: {"default": 0, "type": "number", "description": "Enable route-flap dampening", "format": "flag"}
    :param dampening_penalty: {"description": "Un-reachability Half-life time for the penalty(minutes)", "minimum": 1, "type": "number", "maximum": 45, "format": "number"}
    :param dampening_half_time: {"description": "Reachability Half-life time for the penalty(minutes)", "minimum": 1, "type": "number", "maximum": 45, "format": "number"}
    :param dampening_supress: {"description": "Value to start suppressing a route", "minimum": 1, "type": "number", "maximum": 20000, "format": "number"}
    :param dampening_reuse: {"description": "Value to start reusing a route", "minimum": 1, "type": "number", "maximum": 20000, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dampening-cfg"
        self.DeviceProxy = ""
        self.dampening_max_supress = ""
        self.dampening = ""
        self.dampening_penalty = ""
        self.dampening_half_time = ""
        self.dampening_supress = ""
        self.dampening_reuse = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class OriginatorId(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param originator_ip: {"type": "string", "description": "IP address of originator", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "originator-id"
        self.DeviceProxy = ""
        self.originator_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MetricType(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param value: {"enum": ["external", "internal", "type-1", "type-2"], "type": "string", "description": "'external': IS-IS external metric type; 'internal': IS-IS internal metric type; 'type-1': OSPF external type 1 metric; 'type-2': OSPF external type 2 metric; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "metric-type"
        self.DeviceProxy = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Set(A10BaseClass):
    
    """Class Description::
    Set values in destination routing protocol.

    Class set supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param atomic_aggregate: {"default": 0, "optional": true, "type": "number", "description": "BGP atomic aggregate attribute", "format": "flag"}
    :param community: {"optional": true, "type": "string", "description": "BGP community attribute", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/route-map/{tag}+{action}+{sequence}/set`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "set"
        self.a10_url="/axapi/v3/route-map/{tag}+{action}+{sequence}/set"
        self.DeviceProxy = ""
        self.extcommunity = {}
        self.origin = {}
        self.aggregator = {}
        self.weight = {}
        self.level = {}
        self.ip = {}
        self.metric = {}
        self.as_path = {}
        self.comm_list = {}
        self.atomic_aggregate = ""
        self.community = ""
        self.local_preference = {}
        self.tag = {}
        self.ipv6 = {}
        self.dampening_cfg = {}
        self.originator_id = {}
        self.metric_type = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


