from a10sdk.common.A10BaseClass import A10BaseClass


class VlanCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param vlan: {"description": "VLAN tracking (VLAN id)", "minimum": 1, "type": "number", "maximum": 4094, "format": "number"}
    :param weight: {"description": "The failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param timeout: {"minimum": 2, "type": "number", "maximum": 600, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vlan-cfg"
        self.DeviceProxy = ""
        self.vlan = ""
        self.weight = ""
        self.timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6DestinationCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distance: {"description": "Route's administrative distance (default: match any)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param v6mask: {"description": "IPv6 Destination Prefix", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}
    :param protocol: {"enum": ["any", "static", "dynamic"], "type": "string", "description": "'any': Match any routing protocol (default); 'static': Match only static routes (added by user); 'dynamic': Match routes added by dynamic routing protocols (e.g. OSPF); ", "format": "enum"}
    :param weight: {"description": "The amount the priority will decrease if the route is missing (The amount the priority will decrease if the route is not present)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
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
        self.weight = ""
        self.ipv6_destination = ""
        self.gatewayv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpDestinationCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distance: {"description": "Route's administrative distance(default: match any)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param protocol: {"enum": ["any", "static", "dynamic"], "type": "string", "description": "'any': Match any routing protocol (default); 'static': Match only static routes (added by user); 'dynamic': Match routes added by dynamic routing protocols (e.g. OSPF); ", "format": "enum"}
    :param weight: {"description": "The amount the priority will decrease if the route is missing (The amount the priority will decrease if the route is not present)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param mask: {"type": "string", "description": "Destination prefix mask", "format": "ipv4-netmask"}
    :param ip_destination: {"type": "string", "description": "Destination prefix", "format": "ipv4-address"}
    :param gateway: {"type": "string", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-destination-cfg"
        self.DeviceProxy = ""
        self.distance = ""
        self.protocol = ""
        self.weight = ""
        self.mask = ""
        self.ip_destination = ""
        self.gateway = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Route(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6_destination_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"description": "Route's administrative distance (default: match any)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "v6mask": {"description": "IPv6 Destination Prefix", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}, "protocol": {"enum": ["any", "static", "dynamic"], "type": "string", "description": "'any': Match any routing protocol (default); 'static': Match only static routes (added by user); 'dynamic': Match routes added by dynamic routing protocols (e.g. OSPF); ", "format": "enum"}, "weight": {"description": "The amount the priority will decrease if the route is missing (The amount the priority will decrease if the route is not present)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "ipv6-destination": {"type": "string", "description": "IPv6 Destination Prefix", "format": "ipv6-address"}, "gatewayv6": {"type": "string", "description": "Match the route's gateway (next-hop) (default: match any)", "format": "ipv6-address"}, "optional": true}}]}
    :param ip_destination_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"description": "Route's administrative distance(default: match any)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "protocol": {"enum": ["any", "static", "dynamic"], "type": "string", "description": "'any': Match any routing protocol (default); 'static': Match only static routes (added by user); 'dynamic': Match routes added by dynamic routing protocols (e.g. OSPF); ", "format": "enum"}, "weight": {"description": "The amount the priority will decrease if the route is missing (The amount the priority will decrease if the route is not present)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "mask": {"type": "string", "description": "Destination prefix mask", "format": "ipv4-netmask"}, "ip-destination": {"type": "string", "description": "Destination prefix", "format": "ipv4-address"}, "optional": true, "gateway": {"type": "string", "format": "ipv4-address"}}}]}
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


class Interface(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet: {"type": "number", "description": "Ethernet Interface (Ethernet interface number)", "format": "interface"}
    :param weight: {"description": "The failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "interface"
        self.DeviceProxy = ""
        self.ethernet = ""
        self.weight = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class GwIpv4AddressCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param weight: {"description": "The failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param gw_ipv4_address: {"type": "string", "description": "IP Address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "gw-ipv4-address-cfg"
        self.DeviceProxy = ""
        self.weight = ""
        self.gw_ipv4_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class GwIpv6AddressCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param gw_ipv6_address: {"type": "string", "description": "IPV6 address", "format": "ipv6-address"}
    :param weight: {"description": "The failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "gw-ipv6-address-cfg"
        self.DeviceProxy = ""
        self.gw_ipv6_address = ""
        self.weight = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Gateway(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param gw_ipv4_address_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "weight": {"description": "The failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "gw-ipv4-address": {"type": "string", "description": "IP Address", "format": "ipv4-address"}}}]}
    :param gw_ipv6_address_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "gw-ipv6-address": {"type": "string", "description": "IPV6 address", "format": "ipv6-address"}, "weight": {"description": "The failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "gateway"
        self.DeviceProxy = ""
        self.gw_ipv4_address_cfg = []
        self.gw_ipv6_address_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TrunkCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param per_port_weight: {"description": "Per port failover weight", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}
    :param weight: {"description": "failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param trunk: {"description": "trunk tracking (trunk id)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "trunk-cfg"
        self.DeviceProxy = ""
        self.per_port_weight = ""
        self.weight = ""
        self.trunk = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FailOverPolicyTemplate(A10BaseClass):
    
    """Class Description::
    Define a VRRP-A failover policy template.

    Class fail-over-policy-template supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vlan_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"vlan": {"description": "VLAN tracking (VLAN id)", "minimum": 1, "type": "number", "maximum": 4094, "format": "number"}, "optional": true, "weight": {"description": "The failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "timeout": {"minimum": 2, "type": "number", "maximum": 600, "format": "number"}}}]}
    :param name: {"description": "VRRP-A fail over policy template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param interface: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet Interface (Ethernet interface number)", "format": "interface"}, "optional": true, "weight": {"description": "The failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}}}]}
    :param trunk_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"per-port-weight": {"description": "Per port failover weight", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}, "optional": true, "weight": {"description": "failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "trunk": {"description": "trunk tracking (trunk id)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/fail-over-policy-template/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "fail-over-policy-template"
        self.a10_url="/axapi/v3/vrrp-a/fail-over-policy-template/{name}"
        self.DeviceProxy = ""
        self.vlan_cfg = []
        self.name = ""
        self.route = {}
        self.interface = []
        self.gateway = {}
        self.trunk_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


