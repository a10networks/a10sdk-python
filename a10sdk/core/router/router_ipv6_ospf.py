from a10sdk.common.A10BaseClass import A10BaseClass


class DistributeInternalList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param area_num: {"description": "OSPF area ID as a decimal value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param area_ipv4: {"default": "255.255.255.255", "type": "string", "description": "OSPF area ID in IP address format", "format": "ipv4-address"}
    :param cost: {"description": "Cost", "format": "number", "default": 1, "maximum": 65535, "minimum": 1, "type": "number"}
    :param type: {"enum": ["lw4o6", "nat64", "floating-ip", "ip-nat", "ip-nat-list", "vip", "vip-only-flagged"], "type": "string", "description": "'lw4o6': LW4O6 Prefix; 'nat64': NAT64 Prefix; 'floating-ip': Floating IP; 'ip-nat': IP NAT; 'ip-nat-list': IP NAT list; 'vip': Virtual IP (VIP); 'vip-only-flagged': Selected Virtual IP (VIP); ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "distribute-internal-list"
        self.DeviceProxy = ""
        self.area_num = ""
        self.area_ipv4 = ""
        self.cost = ""
        self.A10WW_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VeCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve: {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ve-cfg"
        self.DeviceProxy = ""
        self.ve = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TrunkCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param trunk: {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "trunk-cfg"
        self.DeviceProxy = ""
        self.trunk = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LoopbackCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param loopback: {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "loopback-cfg"
        self.DeviceProxy = ""
        self.loopback = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EthCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet: {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "eth-cfg"
        self.DeviceProxy = ""
        self.ethernet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PassiveInterface(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}}}]}
    :param trunk_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}}}]}
    :param loopback_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}}}]}
    :param eth_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "passive-interface"
        self.DeviceProxy = ""
        self.ve_cfg = []
        self.trunk_cfg = []
        self.loopback_cfg = []
        self.eth_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Exp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param max_delay: {"description": "Maximum delay between receiving a change to SPF calculation in milliseconds", "format": "number", "default": 50000, "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param min_delay: {"description": "Minimum delay between receiving a change to SPF calculation in milliseconds", "format": "number", "default": 500, "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "exp"
        self.DeviceProxy = ""
        self.max_delay = ""
        self.min_delay = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Spf(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "spf"
        self.DeviceProxy = ""
        self.exp = {}

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
        self.spf = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ospf(A10BaseClass):
    
    """Class Description::
    Open Shortest Path First (OSPFv3).

    Class ospf supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param default_metric: {"description": "Set metric of redistributed routes (Default metric)", "format": "number", "default": 20, "optional": true, "maximum": 16777214, "minimum": 1, "type": "number"}
    :param abr_type_option: {"description": "'cisco': Alternative ABR, Cisco implementation (RFC3509); 'ibm': Alternative ABR, IBM implementation (RFC3509); 'standard': Standard behavior (RFC2328); ", "format": "enum", "default": "cisco", "type": "string", "enum": ["cisco", "ibm", "standard"], "optional": true}
    :param auto_cost_reference_bandwidth: {"description": "Use reference bandwidth method to assign OSPF cost (The reference bandwidth in terms of Mbits per second)", "format": "number", "default": 10000, "optional": true, "maximum": 4294967, "minimum": 1, "type": "number"}
    :param router_id: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "router-id for the OSPF process (OSPFv3 router-id in IPv4 address format)", "format": "ipv4-address"}
    :param distribute_internal_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"area-num": {"description": "OSPF area ID as a decimal value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}, "area-ipv4": {"default": "255.255.255.255", "type": "string", "description": "OSPF area ID in IP address format", "format": "ipv4-address"}, "cost": {"description": "Cost", "format": "number", "default": 1, "maximum": 65535, "minimum": 1, "type": "number"}, "type": {"enum": ["lw4o6", "nat64", "floating-ip", "ip-nat", "ip-nat-list", "vip", "vip-only-flagged"], "type": "string", "description": "'lw4o6': LW4O6 Prefix; 'nat64': NAT64 Prefix; 'floating-ip': Floating IP; 'ip-nat': IP NAT; 'ip-nat-list': IP NAT list; 'vip': Virtual IP (VIP); 'vip-only-flagged': Selected Virtual IP (VIP); ", "format": "enum"}, "optional": true}}]}
    :param max_concurrent_dd: {"description": "Maximum number allowed to process DD concurrently (Number of DD process)", "format": "number", "default": 5, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param process_id: {"description": "OSPFv3 process tag", "format": "string", "default": "0", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param ha_standby_extra_cost: {"description": "Extra ospf cost when there is any standby HA group (The extra cost value)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param bfd_all_interfaces: {"default": 0, "optional": true, "type": "number", "description": "Enable BFD on all interfaces", "format": "flag"}
    :param area_list: {"minItems": 1, "items": {"type": "area"}, "uniqueItems": true, "array": [{"required": ["area-ipv4", "area-num"], "properties": {"area-ipv4": {"optional": false, "type": "string", "description": "OSPFv3 area ID in IP address format", "format": "ipv4-address"}, "virtual-link-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dead-interval": {"description": "Dead router detection time (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "hello-interval": {"description": "Hello packet interval (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "bfd": {"default": 0, "type": "number", "description": "Bidirectional Forwarding Detection (BFD)", "format": "flag"}, "transmit-delay": {"description": "LSA transmission delay (Seconds)", "format": "number", "default": 1, "maximum": 3600, "minimum": 1, "type": "number"}, "value": {"type": "string", "description": "ID (IP addr) associated with virtual link neighbor", "format": "ipv4-address"}, "retransmit-interval": {"description": "LSA retransmit interval (Seconds)", "minimum": 1, "type": "number", "maximum": 3600, "format": "number"}, "optional": true, "instance-id": {"description": "OSPFv3 instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}}}]}, "no-summary": {"default": 0, "optional": true, "type": "number", "description": "Do not inject inter-area routes into area", "format": "flag"}, "stub": {"default": 0, "optional": true, "type": "number", "description": "Configure OSPFv3 area as stub", "format": "flag"}, "range-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "option": {"enum": ["advertise", "not-advertise"], "type": "string", "description": "'advertise': Advertise this range (default); 'not-advertise': DoNotAdvertise this range; ", "format": "enum"}, "value": {"type": "string", "description": "Area range for IPv6 prefix", "format": "ipv6-address-plen"}}}]}, "default-cost": {"description": "Set the summary-default cost of a NSSA or stub area (Stub's advertised default summary cost)", "format": "number", "default": 1, "optional": true, "maximum": 16777215, "minimum": 0, "type": "number"}, "area-num": {"description": "OSPFv3 area ID as a decimal value", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 0, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/router/ipv6/ospf/{process-id}/area/{area-ipv4}+{area-num}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ipv6/ospf/{process_id}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "process_id"]

        self.b_key = "ospf"
        self.a10_url="/axapi/v3/router/ipv6/ospf/{process_id}"
        self.DeviceProxy = ""
        self.default_metric = ""
        self.abr_type_option = ""
        self.auto_cost_reference_bandwidth = ""
        self.router_id = ""
        self.distribute_internal_list = []
        self.redistribute = {}
        self.max_concurrent_dd = ""
        self.process_id = ""
        self.passive_interface = {}
        self.timers = {}
        self.ha_standby_extra_cost = ""
        self.bfd_all_interfaces = ""
        self.area_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


