from a10sdk.common.A10BaseClass import A10BaseClass


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

    :param maximum_prefix: {"description": "Maximum number of prefix accept from this peer (maximum no. of prefix limit (various depends on model))", "format": "number", "type": "number", "maximum": 65536, "minimum": 1, "optional": true}
    :param neighbor_prefix_lists: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-prefix-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-prefix-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (Name of a prefix list)", "format": "string"}}}]}
    :param activate: {"default": 0, "optional": true, "type": "number", "description": "Enable the Address Family for this Neighbor", "format": "flag"}
    :param weight: {"description": "Set default weight for routes from this neighbor", "format": "number", "default": 0, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param send_community_val: {"description": "'both': Send Standard and Extended Community attributes; 'none': Disable Sending Community attributes; 'standard': Send Standard Community attributes; 'extended': Send Extended Community attributes; ", "format": "enum", "default": "both", "type": "string", "enum": ["both", "none", "standard", "extended"], "optional": true}
    :param inbound: {"default": 0, "optional": true, "type": "number", "description": "Allow inbound soft reconfiguration for this neighbor", "format": "flag"}
    :param next_hop_self: {"default": 0, "optional": true, "type": "number", "description": "Disable the next hop calculation for this neighbor", "format": "flag"}
    :param maximum_prefix_thres: {"description": "threshold-value, 1 to 100 percent", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}
    :param allowas_in_count: {"description": "Number of occurrences of AS number", "format": "number", "default": 3, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}
    :param peer_group: {"description": "Neighbor tag", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param remove_private_as: {"default": 0, "optional": true, "type": "number", "description": "Remove private AS number from outbound updates", "format": "flag"}
    :param default_originate: {"default": 0, "optional": true, "type": "number", "description": "Originate default route to this neighbor", "format": "flag"}
    :param allowas_in: {"default": 0, "optional": true, "type": "number", "description": "Accept as-path with my AS present in it", "format": "flag"}
    :param distribute_lists: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distribute-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "distribute-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (IP standard/extended/named access list)", "format": "string"}}}]}
    :param prefix_list_direction: {"optional": true, "enum": ["both", "receive", "send"], "type": "string", "description": "'both': both; 'receive': receive; 'send': send; ", "format": "enum"}
    :param unsuppress_map: {"description": "Route-map to selectively unsuppress suppressed routes (Name of route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param route_map: {"description": "Route-map to specify criteria to originate default (route-map name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param neighbor_route_map_lists: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-rmap-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Apply route map to neighbor (Name of route map)", "format": "string"}}}]}
    :param neighbor_filter_lists: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"filter-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Establish BGP filters (AS path access-list name)", "format": "string"}, "filter-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}/address-family/ipv6/neighbor/peer-group-neighbor/{peer_group}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "peer_group"]

        self.b_key = "peer-group-neighbor"
        self.a10_url="/axapi/v3/router/bgp/{as_number}/address-family/ipv6/neighbor/peer-group-neighbor/{peer_group}"
        self.DeviceProxy = ""
        self.maximum_prefix = ""
        self.neighbor_prefix_lists = []
        self.activate = ""
        self.weight = ""
        self.send_community_val = ""
        self.inbound = ""
        self.next_hop_self = ""
        self.maximum_prefix_thres = ""
        self.allowas_in_count = ""
        self.peer_group = ""
        self.remove_private_as = ""
        self.default_originate = ""
        self.allowas_in = ""
        self.distribute_lists = []
        self.prefix_list_direction = ""
        self.unsuppress_map = ""
        self.route_map = ""
        self.neighbor_route_map_lists = []
        self.neighbor_filter_lists = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


