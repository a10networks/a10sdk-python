from a10sdk.common.A10BaseClass import A10BaseClass


class Interface(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet: {"type": "number", "description": "Ethernet Interface (Ethernet interface number)", "format": "interface"}
    :param priority_cost: {"description": "The amount the priority will decrease", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "interface"
        self.DeviceProxy = ""
        self.ethernet = ""
        self.priority_cost = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6DestinationCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distance: {"description": "Route's administrative distance (default: match any)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param v6mask: {"description": "IPv6 Destination Prefix", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}
    :param protocol: {"enum": ["any", "static", "dynamic"], "type": "string", "description": "'any': Match any routing protocol (default); 'static': Match only static routes (added by user); 'dynamic': Match routes added by dynamic routing protocols (e.g. OSPF); ", "format": "enum"}
    :param priority_cost: {"description": "The amount the priority will decrease if the route is missing (The amount the priority will decrease if the route is not present)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param ipv6_destination: {"type": "string", "description": "IPv6 Destination Prefix", "format": "ipv6-address"}
    :param gatewayv6: {"type": "string", "description": "Match the route's gateway (next-hop) (default: match any)", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-destination-cfg"
        self.DeviceProxy = ""
        self.distance = ""
        self.v6mask = ""
        self.protocol = ""
        self.priority_cost = ""
        self.ipv6_destination = ""
        self.gatewayv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpDestinationCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distance: {"description": "Route's administrative distance (default: match any)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param protocol: {"enum": ["any", "static", "dynamic"], "type": "string", "description": "'any': Match any routing protocol (default); 'static': Match only static routes (added by user); 'dynamic': Match routes added by dynamic routing protocols (e.g. OSPF); ", "format": "enum"}
    :param mask: {"type": "string", "description": "Destination prefix mask", "format": "ipv4-netmask"}
    :param priority_cost: {"description": "The amount the priority will decrease if the route is missing (The amount the priority will decrease if the route is not present)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param ip_destination: {"type": "string", "description": "Destination prefix", "format": "ipv4-address"}
    :param gateway: {"type": "string", "description": "Match the route's gateway (next-hop) (default: match any)", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-destination-cfg"
        self.DeviceProxy = ""
        self.distance = ""
        self.protocol = ""
        self.mask = ""
        self.priority_cost = ""
        self.ip_destination = ""
        self.gateway = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Route(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6_destination_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"description": "Route's administrative distance (default: match any)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "v6mask": {"description": "IPv6 Destination Prefix", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}, "protocol": {"enum": ["any", "static", "dynamic"], "type": "string", "description": "'any': Match any routing protocol (default); 'static': Match only static routes (added by user); 'dynamic': Match routes added by dynamic routing protocols (e.g. OSPF); ", "format": "enum"}, "priority-cost": {"description": "The amount the priority will decrease if the route is missing (The amount the priority will decrease if the route is not present)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "ipv6-destination": {"type": "string", "description": "IPv6 Destination Prefix", "format": "ipv6-address"}, "gatewayv6": {"type": "string", "description": "Match the route's gateway (next-hop) (default: match any)", "format": "ipv6-address"}, "optional": true}}]}
    :param ip_destination_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"description": "Route's administrative distance (default: match any)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "protocol": {"enum": ["any", "static", "dynamic"], "type": "string", "description": "'any': Match any routing protocol (default); 'static': Match only static routes (added by user); 'dynamic': Match routes added by dynamic routing protocols (e.g. OSPF); ", "format": "enum"}, "mask": {"type": "string", "description": "Destination prefix mask", "format": "ipv4-netmask"}, "priority-cost": {"description": "The amount the priority will decrease if the route is missing (The amount the priority will decrease if the route is not present)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "ip-destination": {"type": "string", "description": "Destination prefix", "format": "ipv4-address"}, "optional": true, "gateway": {"type": "string", "description": "Match the route's gateway (next-hop) (default: match any)", "format": "ipv4-address"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "route"
        self.DeviceProxy = ""
        self.ipv6_destination_cfg = []
        self.ip_destination_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VlanCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param vlan: {"description": "VLAN tracking (VLAN id)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}
    :param timeout: {"minimum": 2, "type": "number", "maximum": 600, "format": "number"}
    :param priority_cost: {"description": "The amount the priority will decrease", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vlan-cfg"
        self.DeviceProxy = ""
        self.vlan = ""
        self.timeout = ""
        self.priority_cost = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TrunkCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param per_port_pri: {"description": "per port priority", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}
    :param priority_cost: {"description": "The amount the priority will decrease", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param trunk: {"description": "trunk tracking (Trunk Number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "trunk-cfg"
        self.DeviceProxy = ""
        self.per_port_pri = ""
        self.priority_cost = ""
        self.trunk = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TrackingOptions(A10BaseClass):
    
    """Class Description::
    VRRP-A tracking.

    Class tracking-options supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param interface: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet Interface (Ethernet interface number)", "format": "interface"}, "optional": true, "priority-cost": {"description": "The amount the priority will decrease", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}}}]}
    :param vlan_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"vlan": {"description": "VLAN tracking (VLAN id)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}, "optional": true, "timeout": {"minimum": 2, "type": "number", "maximum": 600, "format": "number"}, "priority-cost": {"description": "The amount the priority will decrease", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}}}]}
    :param trunk_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"per-port-pri": {"description": "per port priority", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}, "priority-cost": {"description": "The amount the priority will decrease", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "optional": true, "trunk": {"description": "trunk tracking (Trunk Number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/vrid/{vrid_val}/blade-parameters/tracking-options`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "tracking-options"
        self.a10_url="/axapi/v3/vrrp-a/vrid/{vrid_val}/blade-parameters/tracking-options"
        self.DeviceProxy = ""
        self.interface = []
        self.route = {}
        self.vlan_cfg = []
        self.trunk_cfg = []
        self.gateway = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


