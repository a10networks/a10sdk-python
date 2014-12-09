from a10sdk.common.A10BaseClass import A10BaseClass


class IpNatListCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip_nat_list: {"default": 0, "type": "number", "description": "IP NAT list", "format": "flag"}
    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-nat-list-cfg"
        self.DeviceProxy = ""
        self.ip_nat_list = ""
        self.route_map = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Lw4O6Cfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param lw4o6: {"default": 0, "type": "number", "description": "LW4O6 Prefix", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "lw4o6-cfg"
        self.DeviceProxy = ""
        self.route_map = ""
        self.lw4o6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Nat64Cfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param nat64: {"default": 0, "type": "number", "description": "NAT64 Prefix", "format": "flag"}
    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "nat64-cfg"
        self.DeviceProxy = ""
        self.nat64 = ""
        self.route_map = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ConnectedCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param connected: {"default": 0, "type": "number", "description": "Connected", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "connected-cfg"
        self.DeviceProxy = ""
        self.route_map = ""
        self.connected = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpNatCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param ip_nat: {"default": 0, "type": "number", "description": "IP NAT", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-nat-cfg"
        self.DeviceProxy = ""
        self.route_map = ""
        self.ip_nat = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FloatingIpCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param floating_ip: {"default": 0, "type": "number", "description": "Floating IP", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "floating-ip-cfg"
        self.DeviceProxy = ""
        self.route_map = ""
        self.floating_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IsisCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param isis: {"default": 0, "type": "number", "description": "ISO IS-IS", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "isis-cfg"
        self.DeviceProxy = ""
        self.route_map = ""
        self.isis = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class OnlyNotFlaggedCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param only_not_flagged: {"default": 0, "type": "number", "description": "Only not flagged", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "only-not-flagged-cfg"
        self.DeviceProxy = ""
        self.route_map = ""
        self.only_not_flagged = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class OnlyFlaggedCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param only_flagged: {"default": 0, "type": "number", "description": "Selected Virtual IP (VIP)", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "only-flagged-cfg"
        self.DeviceProxy = ""
        self.route_map = ""
        self.only_flagged = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Vip(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vip"
        self.DeviceProxy = ""
        self.only_not_flagged_cfg = {}
        self.only_flagged_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RipCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param rip: {"default": 0, "type": "number", "description": "Routing Information Protocol (RIP)", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "rip-cfg"
        self.DeviceProxy = ""
        self.route_map = ""
        self.rip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class OspfCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param ospf: {"default": 0, "type": "number", "description": "Open Shortest Path First (OSPF)", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ospf-cfg"
        self.DeviceProxy = ""
        self.route_map = ""
        self.ospf = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class StaticCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference (Pointer to route-map entries)", "format": "string"}
    :param static: {"default": 0, "type": "number", "description": "Static routes", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "static-cfg"
        self.DeviceProxy = ""
        self.route_map = ""
        self.static = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Redistribute(A10BaseClass):
    
    """Class Description::
    Redistribute information from another routing protocol.

    Class redistribute supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}/address-family/ipv6/redistribute`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "redistribute"
        self.a10_url="/axapi/v3/router/bgp/{as_number}/address-family/ipv6/redistribute"
        self.DeviceProxy = ""
        self.ip_nat_list_cfg = {}
        self.lw4o6_cfg = {}
        self.nat64_cfg = {}
        self.connected_cfg = {}
        self.ip_nat_cfg = {}
        self.floating_ip_cfg = {}
        self.isis_cfg = {}
        self.vip = {}
        self.rip_cfg = {}
        self.ospf_cfg = {}
        self.static_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


