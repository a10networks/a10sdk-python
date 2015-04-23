from a10sdk.common.A10BaseClass import A10BaseClass


class RipMaximumPrefixCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param maximum_prefix: {"description": "Set the maximum number of RIP routes", "minimum": 1, "type": "number", "maximum": 2048, "format": "number"}
    :param maximum_prefix_thres: {"description": "Percentage of maximum routes to generate a warning (Default 75%)", "format": "number", "default": 75, "maximum": 100, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rip-maximum-prefix-cfg"
        self.DeviceProxy = ""
        self.maximum_prefix = ""
        self.maximum_prefix_thres = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RouteCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param route: {"type": "string", "description": "Static route advertisement (debugging purpose) (IP prefix network/length)", "format": "ipv4-cidr"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "route-cfg"
        self.DeviceProxy = ""
        self.route = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PassiveInterfaceList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet: {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}
    :param trunk: {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}
    :param ve: {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}
    :param loopback: {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "passive-interface-list"
        self.DeviceProxy = ""
        self.ethernet = ""
        self.trunk = ""
        self.ve = ""
        self.loopback = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NetworkInterfaceListCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet: {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}
    :param trunk: {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}
    :param ve: {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}
    :param loopback: {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "network-interface-list-cfg"
        self.DeviceProxy = ""
        self.ethernet = ""
        self.trunk = ""
        self.ve = ""
        self.loopback = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TimersCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param val_3: {"description": "Garbage collection timer. Default is 120", "minimum": 5, "type": "number", "maximum": 2147483647, "format": "number"}
    :param val_2: {"description": "Routing information timeout timer. Default is 180", "minimum": 5, "type": "number", "maximum": 2147483647, "format": "number"}
    :param basic: {"description": "Basic routing protocol update timers (Routing table update timer value in second. Default is 30)", "minimum": 5, "type": "number", "maximum": 2147483647, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "timers-cfg"
        self.DeviceProxy = ""
        self.val_3 = ""
        self.val_2 = ""
        self.basic = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Timers(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "timers"
        self.DeviceProxy = ""
        self.timers_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Neighbor(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param value: {"type": "string", "description": "Neighbor address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "neighbor"
        self.DeviceProxy = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AclCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve: {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}
    :param loopback: {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}
    :param metric: {"description": "Metric value", "minimum": 0, "type": "number", "maximum": 16, "format": "number"}
    :param trunk: {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}
    :param acl: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access-list name", "format": "string"}
    :param offset_list_direction: {"enum": ["in", "out"], "type": "string", "description": "'in': Filter incoming updates; 'out': Filter outgoing updates; ", "format": "enum"}
    :param ethernet: {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "acl-cfg"
        self.DeviceProxy = ""
        self.ve = ""
        self.loopback = ""
        self.metric = ""
        self.trunk = ""
        self.acl = ""
        self.offset_list_direction = ""
        self.ethernet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class OffsetList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}, "metric": {"description": "Metric value", "minimum": 0, "type": "number", "maximum": 16, "format": "number"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "acl": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access-list name", "format": "string"}, "offset-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': Filter incoming updates; 'out': Filter outgoing updates; ", "format": "enum"}, "ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "optional": true}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "offset-list"
        self.DeviceProxy = ""
        self.acl_cfg = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AclCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl_direction: {"enum": ["in", "out"], "type": "string", "description": "'in': Filter incoming routing updates; 'out': Filter outgoing routing updates; ", "format": "enum"}
    :param ve: {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}
    :param loopback: {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}
    :param acl: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access-list name", "format": "string"}
    :param trunk: {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}
    :param ethernet: {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "acl-cfg"
        self.DeviceProxy = ""
        self.acl_direction = ""
        self.ve = ""
        self.loopback = ""
        self.acl = ""
        self.trunk = ""
        self.ethernet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PrefixCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve: {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}
    :param loopback: {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}
    :param prefix_list: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter prefixes in routing updates (Name of a prefix list)", "format": "string"}
    :param trunk: {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}
    :param prefix_list_direction: {"enum": ["in", "out"], "type": "string", "description": "'in': Filter incoming routing updates; 'out': Filter outgoing routing updates; ", "format": "enum"}
    :param ethernet: {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "prefix-cfg"
        self.DeviceProxy = ""
        self.ve = ""
        self.loopback = ""
        self.prefix_list = ""
        self.trunk = ""
        self.prefix_list_direction = ""
        self.ethernet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Prefix(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "maxLength": 64, "type": "string"}
    :param prefix_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}, "prefix-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter prefixes in routing updates (Name of a prefix list)", "format": "string"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "prefix-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': Filter incoming routing updates; 'out': Filter outgoing routing updates; ", "format": "enum"}, "ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "prefix"
        self.DeviceProxy = ""
        self.uuid = ""
        self.prefix_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DistributeList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"acl-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': Filter incoming routing updates; 'out': Filter outgoing routing updates; ", "format": "enum"}, "ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}, "acl": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access-list name", "format": "string"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "optional": true}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "distribute-list"
        self.DeviceProxy = ""
        self.acl_cfg = []
        self.prefix = {}
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DistanceListCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distance: {"description": "Administrative distance (Distance value)", "format": "number", "default": 120, "maximum": 255, "minimum": 1, "type": "number"}
    :param distance_acl: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access list name", "format": "string"}
    :param distance_ipv4_mask: {"type": "string", "description": "IP source prefix", "format": "ipv4-cidr"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "distance-list-cfg"
        self.DeviceProxy = ""
        self.distance = ""
        self.distance_acl = ""
        self.distance_ipv4_mask = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NetworkAddresses(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param network_ipv4_mask: {"type": "string", "description": "IP prefix network/length, e.g., 35.0.0.0/8", "format": "ipv4-cidr"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "network-addresses"
        self.DeviceProxy = ""
        self.network_ipv4_mask = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rip(A10BaseClass):
    
    """Class Description::
    Routing Information Protocol (RIP).

    Class rip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param default_metric: {"description": "Set a metric of redistribute routes (Default metric)", "format": "number", "default": 1, "optional": true, "maximum": 16, "minimum": 1, "type": "number"}
    :param recv_buffer_size: {"description": "Set the RIP UDP receive buffer size (the RIP UDP receive buffer size value)", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 8192, "optional": true}
    :param cisco_metric_behavior: {"description": "'enable': Enables updating metric consistent with Cisco; 'disable': Disables updating metric consistent with Cisco;  (Enable/Disable updating metric consistent with Cisco)", "format": "enum", "default": "disable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param route_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"route": {"type": "string", "description": "Static route advertisement (debugging purpose) (IP prefix network/length)", "format": "ipv4-cidr"}, "optional": true}}]}
    :param passive_interface_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "optional": true, "ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}}}]}
    :param network_interface_list_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "optional": true, "ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}}}]}
    :param version: {"description": "Set routing protocol version (RIP version)", "format": "number", "default": 2, "optional": true, "maximum": 2, "minimum": 1, "type": "number"}
    :param neighbor: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "value": {"type": "string", "description": "Neighbor address", "format": "ipv4-address"}}}]}
    :param default_information: {"optional": true, "enum": ["originate"], "type": "string", "description": "'originate': originate;  (Distribute default route)", "format": "enum"}
    :param distance_list_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"description": "Administrative distance (Distance value)", "format": "number", "default": 120, "maximum": 255, "minimum": 1, "type": "number"}, "optional": true, "distance-acl": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access list name", "format": "string"}, "distance-ipv4-mask": {"type": "string", "description": "IP source prefix", "format": "ipv4-cidr"}}}]}
    :param network_addresses: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"network-ipv4-mask": {"type": "string", "description": "IP prefix network/length, e.g., 35.0.0.0/8", "format": "ipv4-cidr"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/rip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rip"
        self.a10_url="/axapi/v3/router/rip"
        self.DeviceProxy = ""
        self.default_metric = ""
        self.recv_buffer_size = ""
        self.cisco_metric_behavior = ""
        self.uuid = ""
        self.rip_maximum_prefix_cfg = {}
        self.route_cfg = []
        self.passive_interface_list = []
        self.redistribute = {}
        self.network_interface_list_cfg = []
        self.version = ""
        self.timers = {}
        self.neighbor = []
        self.offset_list = {}
        self.default_information = ""
        self.distribute_list = {}
        self.distance_list_cfg = []
        self.network_addresses = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


