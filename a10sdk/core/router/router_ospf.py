from a10sdk.common.A10BaseClass import A10BaseClass


class DistributeInternalList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param di_cost: {"description": "Cost of route", "format": "number", "default": 1, "maximum": 65535, "minimum": 1, "type": "number"}
    :param di_area_num: {"description": "OSPF area ID as a decimal value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param di_type: {"enum": ["lw4o6", "floating-ip", "ip-nat", "ip-nat-list", "vip", "vip-only-flagged"], "type": "string", "description": "'lw4o6': LW4O6 Prefix; 'floating-ip': Floating IP; 'ip-nat': IP NAT; 'ip-nat-list': IP NAT list; 'vip': Virtual IP (VIP); 'vip-only-flagged': Selected Virtual IP (VIP); ", "format": "enum"}
    :param di_area_ipv4: {"type": "string", "description": "OSPF area ID as a IP address format", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "distribute-internal-list"
        self.DeviceProxy = ""
        self.di_cost = ""
        self.di_area_num = ""
        self.di_type = ""
        self.di_area_ipv4 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DistributeLists(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param direction: {"enum": ["in", "out"], "type": "string", "description": "'in': Filter incoming routing updates; 'out': Filter outgoing routing updates; ", "format": "enum"}
    :param protocol: {"enum": ["bgp", "connected", "floating-ip", "lw4o6", "ip-nat", "ip-nat-list", "isis", "ospf", "rip", "static"], "type": "string", "description": "'bgp': Border Gateway Protocol (BGP); 'connected': Connected; 'floating-ip': Floating IP; 'lw4o6': LW4O6 Prefix; 'ip-nat': IP NAT; 'ip-nat-list': IP NAT list; 'isis': ISO IS-IS; 'ospf': Open Shortest Path First (OSPF); 'rip': Routing Information Protocol (RIP); 'static': Static routes; ", "format": "enum"}
    :param option: {"enum": ["only-flagged", "only-not-flagged"], "type": "string", "description": "'only-flagged': Selected Virtual IP (VIP); 'only-not-flagged': Only not flagged; ", "format": "enum"}
    :param value: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access-list name", "format": "string"}
    :param ospf_id: {"description": "OSPF process ID", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "distribute-lists"
        self.DeviceProxy = ""
        self.direction = ""
        self.protocol = ""
        self.option = ""
        self.value = ""
        self.ospf_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RouterId(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param value: {"type": "string", "description": "OSPF router-id in IPv4 address format", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "router-id"
        self.DeviceProxy = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NeighborList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param priority: {"description": "OSPF priority of non-broadcast neighbor", "minimum": 0, "type": "number", "maximum": 255, "format": "number"}
    :param cost: {"description": "OSPF cost for point-to-multipoint neighbor (Metric)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param poll_interval: {"description": "OSPF dead-router polling interval (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param address: {"type": "string", "description": "Neighbor address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "neighbor-list"
        self.DeviceProxy = ""
        self.priority = ""
        self.cost = ""
        self.poll_interval = ""
        self.address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AbrType(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param option: {"default": "cisco", "enum": ["cisco", "ibm", "shortcut", "standard"], "type": "string", "description": "'cisco': Alternative ABR, Cisco implementation (RFC3509); 'ibm': Alternative ABR, IBM implementation (RFC3509); 'shortcut': Shortcut ABR; 'standard': Standard behavior (RFC2328); ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "abr-type"
        self.DeviceProxy = ""
        self.option = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ospf1(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ospf-1"
        self.DeviceProxy = ""
        self.abr_type = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AreaCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param area_num: {"description": "OSPF area ID as a decimal value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param cost: {"description": "Cost of host", "format": "number", "default": 0, "maximum": 65535, "minimum": 0, "type": "number"}
    :param area_ipv4: {"type": "string", "description": "OSPF area ID in IP address format", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "area-cfg"
        self.DeviceProxy = ""
        self.area_num = ""
        self.cost = ""
        self.area_ipv4 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HostList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param host_address: {"type": "string", "description": "Host address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "host-list"
        self.DeviceProxy = ""
        self.host_address = ""
        self.area_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LogAdjacencyChangesCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param state: {"enum": ["detail", "disable"], "type": "string", "description": "'detail': Log changes in adjacency state; 'disable': Disable logging; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "log-adjacency-changes-cfg"
        self.DeviceProxy = ""
        self.state = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SummaryAddressList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param summary_address: {"type": "string", "description": "Configure IP address summaries (Summary prefix)", "format": "ipv4-cidr"}
    :param not_advertise: {"default": 0, "type": "number", "description": "Suppress routes that match the prefix", "format": "flag"}
    :param tag: {"description": "Set tag (32-bit tag value)", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "summary-address-list"
        self.DeviceProxy = ""
        self.summary_address = ""
        self.not_advertise = ""
        self.tag = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EthCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet: {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}
    :param eth_address: {"type": "string", "description": "Address of Interface", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "eth-cfg"
        self.DeviceProxy = ""
        self.ethernet = ""
        self.eth_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VeCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ve_address: {"type": "string", "description": "Address of Interface", "format": "ipv4-address"}
    :param ve: {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ve-cfg"
        self.DeviceProxy = ""
        self.ve_address = ""
        self.ve = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TrunkCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param trunk_address: {"type": "string", "description": "Address of Interface", "format": "ipv4-address"}
    :param trunk: {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "trunk-cfg"
        self.DeviceProxy = ""
        self.trunk_address = ""
        self.trunk = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LoopbackCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param loopback_address: {"type": "string", "description": "Address of Interface", "format": "ipv4-address"}
    :param loopback: {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "loopback-cfg"
        self.DeviceProxy = ""
        self.loopback_address = ""
        self.loopback = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LifCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param lif: {"type": "number", "description": "Logical interface (Lif interface number)", "format": "interface"}
    :param lif_address: {"type": "string", "description": "Address of Interface", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "lif-cfg"
        self.DeviceProxy = ""
        self.lif = ""
        self.lif_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PassiveInterface(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param eth_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet interface (Port number)", "format": "interface"}, "optional": true, "eth-address": {"type": "string", "description": "Address of Interface", "format": "ipv4-address"}}}]}
    :param ve_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ve-address": {"type": "string", "description": "Address of Interface", "format": "ipv4-address"}, "optional": true, "ve": {"type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "format": "interface"}}}]}
    :param trunk_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"trunk-address": {"type": "string", "description": "Address of Interface", "format": "ipv4-address"}, "optional": true, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}}}]}
    :param loopback_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"loopback-address": {"type": "string", "description": "Address of Interface", "format": "ipv4-address"}, "optional": true, "loopback": {"type": "number", "description": "Loopback interface (Port number)", "format": "interface"}}}]}
    :param lif_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"lif": {"type": "number", "description": "Logical interface (Lif interface number)", "format": "interface"}, "optional": true, "lif-address": {"type": "string", "description": "Address of Interface", "format": "ipv4-address"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "passive-interface"
        self.DeviceProxy = ""
        self.eth_cfg = []
        self.ve_cfg = []
        self.trunk_cfg = []
        self.loopback_cfg = []
        self.lif_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Database(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param count: {"description": "Maximum number of LSAs", "format": "number", "default": 4294967294, "maximum": 4294967294, "minimum": 0, "type": "number"}
    :param recovery_time: {"description": "Time to recover (0 not recover)", "format": "number", "default": 0, "maximum": 65535, "minimum": 0, "type": "number"}
    :param limit: {"default": "hard", "enum": ["hard", "soft"], "type": "string", "description": "'hard': Hard limit: Instance will be shutdown if exceeded; 'soft': Soft limit: Warning will be given if exceeded; ", "format": "enum"}
    :param db_external: {"description": "Maximum number of LSAs", "format": "number", "default": 2147483647, "maximum": 2147483647, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "database"
        self.DeviceProxy = ""
        self.count = ""
        self.recovery_time = ""
        self.limit = ""
        self.db_external = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Overflow(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "overflow"
        self.DeviceProxy = ""
        self.database = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DistanceOspf(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distance_external: {"description": "External routes (Distance for external routes)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param distance_intra_area: {"description": "Intra-area routes (Distance for intra-area routes)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param distance_inter_area: {"description": "Inter-area routes (Distance for inter-area routes)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "distance-ospf"
        self.DeviceProxy = ""
        self.distance_external = ""
        self.distance_intra_area = ""
        self.distance_inter_area = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Distance(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distance_value: {"description": "OSPF Administrative distance", "format": "number", "default": 110, "maximum": 255, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "distance"
        self.DeviceProxy = ""
        self.distance_ospf = {}
        self.distance_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NetworkArea(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param instance_value: {"description": "Instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}
    :param network_area_ipv4: {"type": "string", "description": "OSPF area ID in IP address format", "format": "ipv4-address"}
    :param network_area_num: {"description": "OSPF area ID as a decimal value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "network-area"
        self.DeviceProxy = ""
        self.instance_value = ""
        self.network_area_ipv4 = ""
        self.network_area_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NetworkList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param network_ipv4: {"type": "string", "description": "Network number", "format": "ipv4-address"}
    :param network_ipv4_cidr: {"type": "string", "description": "OSPF network prefix", "format": "ipv4-cidr"}
    :param network_ipv4_mask: {"type": "string", "description": "OSPF wild card bits", "format": "ipv4-rev-netmask"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "network-list"
        self.DeviceProxy = ""
        self.network_area = {}
        self.network_ipv4 = ""
        self.network_ipv4_cidr = ""
        self.network_ipv4_mask = ""

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
    Open Shortest Path First (OSPF).

    Class ospf supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param distribute_internal_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"di-cost": {"description": "Cost of route", "format": "number", "default": 1, "maximum": 65535, "minimum": 1, "type": "number"}, "di-area-num": {"description": "OSPF area ID as a decimal value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}, "optional": true, "di-type": {"enum": ["lw4o6", "floating-ip", "ip-nat", "ip-nat-list", "vip", "vip-only-flagged"], "type": "string", "description": "'lw4o6': LW4O6 Prefix; 'floating-ip': Floating IP; 'ip-nat': IP NAT; 'ip-nat-list': IP NAT list; 'vip': Virtual IP (VIP); 'vip-only-flagged': Selected Virtual IP (VIP); ", "format": "enum"}, "di-area-ipv4": {"type": "string", "description": "OSPF area ID as a IP address format", "format": "ipv4-address"}}}]}
    :param distribute_lists: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"direction": {"enum": ["in", "out"], "type": "string", "description": "'in': Filter incoming routing updates; 'out': Filter outgoing routing updates; ", "format": "enum"}, "protocol": {"enum": ["bgp", "connected", "floating-ip", "lw4o6", "ip-nat", "ip-nat-list", "isis", "ospf", "rip", "static"], "type": "string", "description": "'bgp': Border Gateway Protocol (BGP); 'connected': Connected; 'floating-ip': Floating IP; 'lw4o6': LW4O6 Prefix; 'ip-nat': IP NAT; 'ip-nat-list': IP NAT list; 'isis': ISO IS-IS; 'ospf': Open Shortest Path First (OSPF); 'rip': Routing Information Protocol (RIP); 'static': Static routes; ", "format": "enum"}, "option": {"enum": ["only-flagged", "only-not-flagged"], "type": "string", "description": "'only-flagged': Selected Virtual IP (VIP); 'only-not-flagged': Only not flagged; ", "format": "enum"}, "value": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access-list name", "format": "string"}, "ospf-id": {"description": "OSPF process ID", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "optional": true}}]}
    :param default_metric: {"description": "Set metric of redistributed routes (Default metric)", "format": "number", "default": 20, "optional": true, "maximum": 16777214, "minimum": 1, "type": "number"}
    :param auto_cost_reference_bandwidth: {"description": "Use reference bandwidth method to assign OSPF cost (The reference bandwidth in terms of Mbits per second)", "format": "number", "default": 10000, "optional": true, "maximum": 4294967, "minimum": 1, "type": "number"}
    :param neighbor_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"priority": {"description": "OSPF priority of non-broadcast neighbor", "minimum": 0, "type": "number", "maximum": 255, "format": "number"}, "cost": {"description": "OSPF cost for point-to-multipoint neighbor (Metric)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "optional": true, "poll-interval": {"description": "OSPF dead-router polling interval (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "address": {"type": "string", "description": "Neighbor address", "format": "ipv4-address"}}}]}
    :param host_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "host-address": {"type": "string", "description": "Host address", "format": "ipv4-address"}, "area-cfg": {"type": "object", "properties": {"area-num": {"description": "OSPF area ID as a decimal value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}, "cost": {"description": "Cost of host", "format": "number", "default": 0, "maximum": 65535, "minimum": 0, "type": "number"}, "area-ipv4": {"type": "string", "description": "OSPF area ID in IP address format", "format": "ipv4-address"}}}}}]}
    :param area_list: {"minItems": 1, "items": {"type": "area"}, "uniqueItems": true, "array": [{"required": ["area-ipv4", "area-num"], "properties": {"nssa-cfg": {"type": "object", "properties": {"no-redistribution": {"default": 0, "type": "number", "description": "No redistribution into this NSSA area", "format": "flag"}, "translator-role": {"default": "candidate", "enum": ["always", "candidate", "never"], "type": "string", "description": "'always': Translate always; 'candidate': Candidate for translator (default); 'never': Do not translate; ", "format": "enum"}, "metric": {"description": "OSPF default metric (OSPF metric)", "format": "number", "default": 1, "maximum": 16777214, "minimum": 0, "type": "number"}, "nssa": {"default": 0, "type": "number", "description": "Specify a NSSA area", "format": "flag"}, "default-information-originate": {"default": 0, "type": "number", "description": "Originate Type 7 default into NSSA area", "format": "flag"}, "no-summary": {"default": 0, "type": "number", "description": "Do not send summary LSA into NSSA", "format": "flag"}, "metric-type": {"description": "OSPF metric type (OSPF metric type for default routes)", "format": "number", "default": 2, "maximum": 2, "minimum": 1, "type": "number"}}}, "filter-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"acl-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': Filter networks sent to this area; 'out': Filter networks sent from this area; ", "format": "enum"}, "plist-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': Filter networks sent to this area; 'out': Filter networks sent from this area; ", "format": "enum"}, "acl-name": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter networks by access-list (Name of an access-list)", "format": "string"}, "plist-name": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter networks by prefix-list (Name of an IP prefix-list)", "format": "string"}, "filter-list": {"default": 0, "type": "number", "description": "Filter networks between OSPF areas", "format": "flag"}, "optional": true}}]}, "area-ipv4": {"optional": false, "type": "string", "description": "OSPF area ID in IP address format", "format": "ipv4-address"}, "virtual-link-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dead-interval": {"description": "Dead router detection time (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "message-digest-key": {"description": "Set message digest key (Key ID)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "hello-interval": {"description": "Hello packet interval (Seconds)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "bfd": {"default": 0, "type": "number", "description": "Bidirectional Forwarding Detection (BFD)", "format": "flag"}, "transmit-delay": {"description": "LSA transmission delay (Seconds)", "format": "number", "default": 1, "maximum": 3600, "minimum": 1, "type": "number"}, "virtual-link-authentication": {"default": 0, "type": "number", "description": "Enable authentication", "format": "flag"}, "virtual-link-ip-addr": {"type": "string", "description": "ID (IP addr) associated with virtual link neighbor", "format": "ipv4-address"}, "virtual-link-auth-type": {"enum": ["message-digest", "null"], "type": "string", "description": "'message-digest': Use message-digest authentication; 'null': Use null authentication; ", "format": "enum"}, "authentication-key": {"minLength": 1, "maxLength": 8, "type": "string", "description": "Set authentication key (Authentication key (8 chars))", "format": "string-rlx"}, "retransmit-interval": {"description": "LSA retransmit interval (Seconds)", "minimum": 1, "type": "number", "maximum": 3600, "format": "number"}, "optional": true, "md5": {"minLength": 1, "maxLength": 16, "type": "string", "description": "Use MD5 algorithm (Authentication key (16 chars))", "format": "string-rlx"}}}]}, "stub-cfg": {"type": "object", "properties": {"stub": {"default": 0, "type": "number", "description": "Configure OSPF area as stub", "format": "flag"}, "no-summary": {"default": 0, "type": "number", "description": "Do not inject inter-area routes into area", "format": "flag"}}}, "shortcut": {"description": "'default': Set default shortcutting behavior; 'disable': Disable shortcutting through the area; 'enable': Enable shortcutting through the area; ", "format": "enum", "default": "default", "type": "string", "enum": ["default", "disable", "enable"], "optional": true}, "auth-cfg": {"type": "object", "properties": {"authentication": {"default": 0, "type": "number", "description": "Enable authentication", "format": "flag"}, "message-digest": {"default": 0, "type": "number", "description": "Use message-digest authentication", "format": "flag"}}}, "range-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"area-range-prefix": {"type": "string", "description": "Area range for IPv4 prefix", "format": "ipv4-cidr"}, "optional": true, "option": {"default": "advertise", "enum": ["advertise", "not-advertise"], "type": "string", "description": "'advertise': Advertise this range (default); 'not-advertise': DoNotAdvertise this range; ", "format": "enum"}}}]}, "default-cost": {"description": "Set the summary-default cost of a NSSA or stub area (Stub's advertised default summary cost)", "format": "number", "default": 1, "optional": true, "maximum": 16777215, "minimum": 0, "type": "number"}, "area-num": {"description": "OSPF area ID as a decimal value", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 0, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/router/ospf/{process-id}/area/{area-ipv4}+{area-num}"}
    :param maximum_area: {"description": "Maximum number of OSPF area (OSPF area limit)", "format": "number", "type": "number", "maximum": 4294967294, "minimum": 1, "optional": true}
    :param summary_address_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"summary-address": {"type": "string", "description": "Configure IP address summaries (Summary prefix)", "format": "ipv4-cidr"}, "not-advertise": {"default": 0, "type": "number", "description": "Suppress routes that match the prefix", "format": "flag"}, "tag": {"description": "Set tag (32-bit tag value)", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}, "optional": true}}]}
    :param rfc1583_compatible: {"default": 0, "optional": true, "type": "number", "description": "Compatible with RFC 1583", "format": "flag"}
    :param max_concurrent_dd: {"description": "Maximum number allowed to process DD concurrently (Number of DD process)", "format": "number", "default": 5, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param process_id: {"description": "OSPF process ID", "format": "number", "default": 0, "optional": false, "maximum": 65535, "minimum": 0, "type": "number"}
    :param bfd_all_interfaces: {"default": 0, "optional": true, "type": "number", "description": "Enable BFD on all interfaces", "format": "flag"}
    :param network_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"network-area": {"type": "object", "properties": {"instance-value": {"description": "Instance ID", "format": "number", "default": 0, "maximum": 255, "minimum": 0, "type": "number"}, "network-area-ipv4": {"type": "string", "description": "OSPF area ID in IP address format", "format": "ipv4-address"}, "network-area-num": {"description": "OSPF area ID as a decimal value", "minimum": 0, "type": "number", "maximum": 4294967295, "format": "number"}}}, "network-ipv4": {"type": "string", "description": "Network number", "format": "ipv4-address"}, "network-ipv4-cidr": {"type": "string", "description": "OSPF network prefix", "format": "ipv4-cidr"}, "network-ipv4-mask": {"type": "string", "description": "OSPF wild card bits", "format": "ipv4-rev-netmask"}, "optional": true}}]}
    :param ha_standby_extra_cost: {"description": "Extra ospf cost when there is any standby HA group (The extra cost value)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ospf/{process_id}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "process_id"]

        self.b_key = "ospf"
        self.a10_url="/axapi/v3/router/ospf/{process_id}"
        self.DeviceProxy = ""
        self.distribute_internal_list = []
        self.distribute_lists = []
        self.default_metric = ""
        self.auto_cost_reference_bandwidth = ""
        self.router_id = {}
        self.neighbor_list = []
        self.ospf_1 = {}
        self.host_list = []
        self.log_adjacency_changes_cfg = {}
        self.area_list = []
        self.maximum_area = ""
        self.summary_address_list = []
        self.rfc1583_compatible = ""
        self.max_concurrent_dd = ""
        self.process_id = ""
        self.passive_interface = {}
        self.default_information = {}
        self.overflow = {}
        self.bfd_all_interfaces = ""
        self.distance = {}
        self.redistribute = {}
        self.network_list = []
        self.timers = {}
        self.ha_standby_extra_cost = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


