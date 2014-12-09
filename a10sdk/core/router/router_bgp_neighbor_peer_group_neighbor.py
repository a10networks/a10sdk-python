from a10sdk.common.A10BaseClass import A10BaseClass


class DistributeLists(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distribute_list_direction: {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}
    :param distribute_list: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (IP standard/extended/named access list)", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "distribute-lists"
        self.DeviceProxy = ""
        self.distribute_list_direction = ""
        self.distribute_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NeighborRouteMapLists(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param nbr_rmap_direction: {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}
    :param nbr_route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Apply route map to neighbor (Name of route map)", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "neighbor-route-map-lists"
        self.DeviceProxy = ""
        self.nbr_rmap_direction = ""
        self.nbr_route_map = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NeighborPrefixLists(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param nbr_prefix_list_direction: {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}
    :param nbr_prefix_list: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (Name of a prefix list)", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "neighbor-prefix-lists"
        self.DeviceProxy = ""
        self.nbr_prefix_list_direction = ""
        self.nbr_prefix_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NeighborFilterLists(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param filter_list: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Establish BGP filters (AS path access-list name)", "format": "string"}
    :param filter_list_direction: {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "neighbor-filter-lists"
        self.DeviceProxy = ""
        self.filter_list = ""
        self.filter_list_direction = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PeerGroupNeighbor(A10BaseClass):
    
    """Class Description::
    Specify a peer-group neighbor router.

    Class peer-group-neighbor supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param timers_holdtime: {"description": "Holdtime", "format": "number", "default": 90, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param activate: {"default": 1, "optional": true, "type": "number", "description": "Enable the Address Family for this Neighbor", "format": "flag"}
    :param route_refresh: {"default": 1, "optional": true, "type": "number", "description": "Advertise route-refresh capability to this neighbor", "format": "flag"}
    :param ve: {"not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "loopback", "trunk"], "type": "number", "description": "Virtual ethernet interface (Virtual ethernet interface number)", "optional": true, "format": "interface"}
    :param weight: {"description": "Set default weight for routes from this neighbor", "format": "number", "default": 0, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param timers_keepalive: {"description": "Keepalive interval", "format": "number", "default": 30, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param dynamic: {"default": 0, "optional": true, "type": "number", "description": "Advertise dynamic capability to this neighbor", "format": "flag"}
    :param loopback: {"not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "ve", "trunk"], "type": "number", "description": "Loopback interface (Port number)", "optional": true, "format": "interface"}
    :param default_originate: {"default": 0, "optional": true, "type": "number", "description": "Originate default route to this neighbor", "format": "flag"}
    :param distribute_lists: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distribute-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "distribute-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (IP standard/extended/named access list)", "format": "string"}}}]}
    :param shutdown: {"default": 0, "optional": true, "type": "number", "description": "Administratively shut down this neighbor", "format": "flag"}
    :param prefix_list_direction: {"optional": true, "enum": ["both", "receive", "send"], "type": "string", "description": "'both': both; 'receive': receive; 'send': send; ", "format": "enum"}
    :param neighbor_route_map_lists: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-rmap-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Apply route map to neighbor (Name of route map)", "format": "string"}}}]}
    :param advertisement_interval: {"description": "Minimum interval between sending BGP routing updates (time in seconds)", "format": "number", "type": "number", "maximum": 600, "minimum": 1, "optional": true}
    :param lif: {"description": "Logical interface (Lif interface number)", "format": "number", "optional": true, "not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "loopback", "ve"], "maximum": 128, "minimum": 1, "type": "number"}
    :param send_community_val: {"description": "'both': Send Standard and Extended Community attributes; 'none': Disable Sending Community attributes; 'standard': Send Standard Community attributes; 'extended': Send Extended Community attributes; ", "format": "enum", "default": "both", "type": "string", "enum": ["both", "none", "standard", "extended"], "optional": true}
    :param update_source_ip: {"not-list": ["update-source-ipv6", "ethernet", "loopback", "ve", "trunk"], "type": "string", "description": "IP address", "optional": true, "format": "ipv4-address"}
    :param collide_established: {"default": 0, "optional": true, "type": "number", "description": "Include Neighbor in Established State for Collision Detection", "format": "flag"}
    :param next_hop_self: {"default": 0, "optional": true, "type": "number", "description": "Disable the next hop calculation for this neighbor", "format": "flag"}
    :param pass_encrypted: {"optional": true, "type": "encrypted", "format": "encrypted"}
    :param peer_group: {"description": "Neighbor tag", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param dont_capability_negotiate: {"default": 0, "optional": true, "type": "number", "description": "Do not perform capability negotiation", "format": "flag"}
    :param unsuppress_map: {"description": "Route-map to selectively unsuppress suppressed routes (Name of route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param passive: {"default": 0, "optional": true, "type": "number", "description": "Don't send open messages to this neighbor", "format": "flag"}
    :param ebgp_multihop_hop_count: {"description": "maximum hop count", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}
    :param allowas_in: {"default": 0, "optional": true, "type": "number", "description": "Accept as-path with my AS present in it", "format": "flag"}
    :param pass_value: {"description": "Key String", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param connection_retry_time: {"description": "BGP per neighbor timers (BGP connect timer)", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param description: {"optional": true, "type": "string", "description": "Neighbor specific description (Up to 80 characters describing this neighbor)", "format": "string-rlx"}
    :param inbound: {"default": 0, "optional": true, "type": "number", "description": "Allow inbound soft reconfiguration for this neighbor", "format": "flag"}
    :param maximum_prefix_thres: {"description": "threshold-value, 1 to 100 percent", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}
    :param neighbor_prefix_lists: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-prefix-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-prefix-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (Name of a prefix list)", "format": "string"}}}]}
    :param peer_group_remote_as: {"description": "Specify AS number of BGP neighbor", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 1, "optional": true}
    :param disallow_infinite_holdtime: {"default": 0, "optional": true, "type": "number", "description": "BGP per neighbor disallow-infinite-holdtime", "format": "flag"}
    :param route_map: {"description": "Route-map to specify criteria to originate default (route-map name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param trunk: {"not-list": ["update-source-ip", "update-source-ipv6", "ethernet", "loopback", "ve"], "type": "number", "description": "Trunk interface (Trunk interface number)", "optional": true, "format": "interface"}
    :param remove_private_as: {"default": 0, "optional": true, "type": "number", "description": "Remove private AS number from outbound updates", "format": "flag"}
    :param neighbor_filter_lists: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"filter-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Establish BGP filters (AS path access-list name)", "format": "string"}, "filter-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true}}]}
    :param update_source_ipv6: {"not-list": ["update-source-ip", "ethernet", "loopback", "ve", "trunk"], "type": "string", "description": "IPv6 address", "optional": true, "format": "ipv6-address"}
    :param maximum_prefix: {"description": "Maximum number of prefix accept from this peer (maximum no. of prefix limit (various depends on model))", "format": "number", "type": "number", "maximum": 65536, "minimum": 1, "optional": true}
    :param peer_group_key: {"default": 0, "optional": true, "type": "number", "description": "Configure peer-group", "format": "flag"}
    :param allowas_in_count: {"description": "Number of occurrences of AS number", "format": "number", "default": 3, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}
    :param as_origination_interval: {"description": "Minimum interval between sending AS-origination routing updates (time in seconds)", "format": "number", "type": "number", "maximum": 600, "minimum": 1, "optional": true}
    :param override_capability: {"default": 0, "optional": true, "type": "number", "description": "Override capability negotiation result", "format": "flag"}
    :param enforce_multihop: {"default": 0, "optional": true, "type": "number", "description": "Enforce EBGP neighbors to perform multihop", "format": "flag"}
    :param strict_capability_match: {"default": 0, "optional": true, "type": "number", "description": "Strict capability negotiation match", "format": "flag"}
    :param ebgp_multihop: {"default": 0, "optional": true, "type": "number", "description": "Allow EBGP neighbors not on directly connected networks", "format": "flag"}
    :param ethernet: {"not-list": ["update-source-ip", "update-source-ipv6", "loopback", "ve", "trunk"], "type": "number", "description": "Ethernet interface (Port number)", "optional": true, "format": "interface"}
    :param connect: {"description": "BGP connect timer", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}/neighbor/peer-group-neighbor/{peer_group}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "peer_group"]

        self.b_key = "peer-group-neighbor"
        self.a10_url="/axapi/v3/router/bgp/{as_number}/neighbor/peer-group-neighbor/{peer_group}"
        self.DeviceProxy = ""
        self.timers_holdtime = ""
        self.activate = ""
        self.route_refresh = ""
        self.ve = ""
        self.weight = ""
        self.timers_keepalive = ""
        self.dynamic = ""
        self.loopback = ""
        self.default_originate = ""
        self.distribute_lists = []
        self.shutdown = ""
        self.prefix_list_direction = ""
        self.neighbor_route_map_lists = []
        self.advertisement_interval = ""
        self.lif = ""
        self.send_community_val = ""
        self.update_source_ip = ""
        self.collide_established = ""
        self.next_hop_self = ""
        self.pass_encrypted = ""
        self.peer_group = ""
        self.dont_capability_negotiate = ""
        self.unsuppress_map = ""
        self.passive = ""
        self.ebgp_multihop_hop_count = ""
        self.allowas_in = ""
        self.pass_value = ""
        self.connection_retry_time = ""
        self.description = ""
        self.inbound = ""
        self.maximum_prefix_thres = ""
        self.neighbor_prefix_lists = []
        self.peer_group_remote_as = ""
        self.disallow_infinite_holdtime = ""
        self.route_map = ""
        self.trunk = ""
        self.remove_private_as = ""
        self.neighbor_filter_lists = []
        self.update_source_ipv6 = ""
        self.maximum_prefix = ""
        self.peer_group_key = ""
        self.allowas_in_count = ""
        self.as_origination_interval = ""
        self.override_capability = ""
        self.enforce_multihop = ""
        self.strict_capability_match = ""
        self.ebgp_multihop = ""
        self.ethernet = ""
        self.connect = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


