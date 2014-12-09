from a10sdk.common.A10BaseClass import A10BaseClass


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
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "offset-list"
        self.DeviceProxy = ""
        self.acl_cfg = []

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


class RouteCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param route: {"type": "string", "description": "Static route advertisement (debugging purpose) (IP prefix)", "format": "ipv6-address-plen"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "route-cfg"
        self.DeviceProxy = ""
        self.route = ""

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


class AggregateAddressCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param aggregate_address: {"type": "string", "description": "Set aggregate RIP route announcement (Aggregate network)", "format": "ipv6-address-plen"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "aggregate-address-cfg"
        self.DeviceProxy = ""
        self.aggregate_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RipngNeighborCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve: {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}
    :param loopback: {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}
    :param neighbor_link_local_addr: {"type": "string", "description": "IPv6 link-local address", "format": "ipv6-address"}
    :param trunk: {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}
    :param ethernet: {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ripng-neighbor-cfg"
        self.DeviceProxy = ""
        self.ve = ""
        self.loopback = ""
        self.neighbor_link_local_addr = ""
        self.trunk = ""
        self.ethernet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RipngNeighbor(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ripng_neighbor_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}, "neighbor-link-local-addr": {"type": "string", "description": "IPv6 link-local address", "format": "ipv6-address"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ripng-neighbor"
        self.DeviceProxy = ""
        self.ripng_neighbor_cfg = []

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

    :param prefix_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}, "prefix-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter prefixes in routing updates (Name of a prefix list)", "format": "string"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "prefix-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': Filter incoming routing updates; 'out': Filter outgoing routing updates; ", "format": "enum"}, "ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "prefix"
        self.DeviceProxy = ""
        self.prefix_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DistributeList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param acl_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"acl-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': Filter incoming routing updates; 'out': Filter outgoing routing updates; ", "format": "enum"}, "ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}, "acl": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access-list name", "format": "string"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "distribute-list"
        self.DeviceProxy = ""
        self.acl_cfg = []
        self.prefix = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rip(A10BaseClass):
    
    """Class Description::
    Routing Information Protocol (RIPng).

    Class rip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param default_metric: {"description": "Set a metric of redistribute routes (Default metric)", "format": "number", "default": 1, "optional": true, "maximum": 16, "minimum": 1, "type": "number"}
    :param recv_buffer_size: {"description": "Set the RIPNG UDP receive buffer size (the RIPNG UDP receive buffer size value)", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 8192, "optional": true}
    :param cisco_metric_behavior: {"optional": true, "enum": ["enable", "disable"], "type": "string", "description": "'enable': Enables updating metric consistent with Cisco; 'disable': Disables updating metric consistent with Cisco;  (Enable/Disable updating metric consistent with Cisco)", "format": "enum"}
    :param passive_interface_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "optional": true, "ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}}}]}
    :param route_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"route": {"type": "string", "description": "Static route advertisement (debugging purpose) (IP prefix)", "format": "ipv6-address-plen"}, "optional": true}}]}
    :param aggregate_address_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "aggregate-address": {"type": "string", "description": "Set aggregate RIP route announcement (Aggregate network)", "format": "ipv6-address-plen"}}}]}
    :param default_information: {"optional": true, "enum": ["originate"], "type": "string", "description": "'originate': originate;  (Distribute default route)", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ipv6/rip`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "rip"
        self.a10_url="/axapi/v3/router/ipv6/rip"
        self.DeviceProxy = ""
        self.default_metric = ""
        self.recv_buffer_size = ""
        self.cisco_metric_behavior = ""
        self.offset_list = {}
        self.route_map = {}
        self.passive_interface_list = []
        self.redistribute = {}
        self.route_cfg = []
        self.timers = {}
        self.aggregate_address_cfg = []
        self.ripng_neighbor = {}
        self.default_information = ""
        self.distribute_list = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


