from a10sdk.common.A10BaseClass import A10BaseClass


class Neighbor(A10BaseClass):
    
    """Class Description::
    Specify a neighbor router.

    Class neighbor supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param peer_group_neighbor_list: {"minItems": 1, "items": {"type": "peer-group-neighbor"}, "uniqueItems": true, "array": [{"required": ["peer-group"], "properties": {"maximum-prefix": {"description": "Maximum number of prefix accept from this peer (maximum no. of prefix limit (various depends on model))", "format": "number", "type": "number", "maximum": 65536, "minimum": 1, "optional": true}, "neighbor-prefix-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-prefix-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-prefix-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (Name of a prefix list)", "format": "string"}}}]}, "activate": {"default": 0, "optional": true, "type": "number", "description": "Enable the Address Family for this Neighbor", "format": "flag"}, "weight": {"description": "Set default weight for routes from this neighbor", "format": "number", "default": 0, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}, "send-community-val": {"description": "'both': Send Standard and Extended Community attributes; 'none': Disable Sending Community attributes; 'standard': Send Standard Community attributes; 'extended': Send Extended Community attributes; ", "format": "enum", "default": "both", "type": "string", "enum": ["both", "none", "standard", "extended"], "optional": true}, "inbound": {"default": 0, "optional": true, "type": "number", "description": "Allow inbound soft reconfiguration for this neighbor", "format": "flag"}, "next-hop-self": {"default": 0, "optional": true, "type": "number", "description": "Disable the next hop calculation for this neighbor", "format": "flag"}, "maximum-prefix-thres": {"description": "threshold-value, 1 to 100 percent", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}, "allowas-in-count": {"description": "Number of occurrences of AS number", "format": "number", "default": 3, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}, "peer-group": {"description": "Neighbor tag", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}, "remove-private-as": {"default": 0, "optional": true, "type": "number", "description": "Remove private AS number from outbound updates", "format": "flag"}, "default-originate": {"default": 0, "optional": true, "type": "number", "description": "Originate default route to this neighbor", "format": "flag"}, "allowas-in": {"default": 0, "optional": true, "type": "number", "description": "Accept as-path with my AS present in it", "format": "flag"}, "distribute-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distribute-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "distribute-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (IP standard/extended/named access list)", "format": "string"}}}]}, "prefix-list-direction": {"optional": true, "enum": ["both", "receive", "send"], "type": "string", "description": "'both': both; 'receive': receive; 'send': send; ", "format": "enum"}, "unsuppress-map": {"description": "Route-map to selectively unsuppress suppressed routes (Name of route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "route-map": {"description": "Route-map to specify criteria to originate default (route-map name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "neighbor-route-map-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-rmap-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Apply route map to neighbor (Name of route map)", "format": "string"}}}]}, "neighbor-filter-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"filter-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Establish BGP filters (AS path access-list name)", "format": "string"}, "filter-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true}}]}}}], "type": "array", "$ref": "/axapi/v3/router/bgp/{as-number}/address-family/ipv6/neighbor/peer-group-neighbor/{peer-group}"}
    :param ipv6_neighbor_list: {"minItems": 1, "items": {"type": "ipv6-neighbor"}, "uniqueItems": true, "array": [{"required": ["neighbor-ipv6"], "properties": {"maximum-prefix": {"description": "Maximum number of prefix accept from this peer (maximum no. of prefix limit (various depends on model))", "format": "number", "type": "number", "maximum": 65536, "minimum": 1, "optional": true}, "neighbor-prefix-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-prefix-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-prefix-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (Name of a prefix list)", "format": "string"}}}]}, "allowas-in-count": {"description": "Number of occurrences of AS number", "format": "number", "default": 3, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}, "weight": {"description": "Set default weight for routes from this neighbor", "format": "number", "default": 0, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}, "neighbor-ipv6": {"optional": false, "type": "string", "description": "Neighbor IPv6 address", "format": "ipv6-address"}, "send-community-val": {"description": "'both': Send Standard and Extended Community attributes; 'none': Disable Sending Community attributes; 'standard': Send Standard Community attributes; 'extended': Send Extended Community attributes; ", "format": "enum", "default": "both", "type": "string", "enum": ["both", "none", "standard", "extended"], "optional": true}, "inbound": {"default": 0, "optional": true, "type": "number", "description": "Allow inbound soft reconfiguration for this neighbor", "format": "flag"}, "next-hop-self": {"default": 0, "optional": true, "type": "number", "description": "Disable the next hop calculation for this neighbor", "format": "flag"}, "maximum-prefix-thres": {"description": "threshold-value, 1 to 100 percent", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}, "route-map": {"description": "Route-map to specify criteria to originate default (route-map name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "default-originate": {"default": 0, "optional": true, "type": "number", "description": "Originate default route to this neighbor", "format": "flag"}, "remove-private-as": {"default": 0, "optional": true, "type": "number", "description": "Remove private AS number from outbound updates", "format": "flag"}, "unsuppress-map": {"description": "Route-map to selectively unsuppress suppressed routes (Name of route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "allowas-in": {"default": 0, "optional": true, "type": "number", "description": "Accept as-path with my AS present in it", "format": "flag"}, "activate": {"default": 0, "optional": true, "type": "number", "description": "Enable the Address Family for this Neighbor", "format": "flag"}, "distribute-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distribute-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "distribute-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (IP standard/extended/named access list)", "format": "string"}}}]}, "prefix-list-direction": {"optional": true, "enum": ["both", "receive", "send"], "type": "string", "description": "'both': both; 'receive': receive; 'send': send; ", "format": "enum"}, "neighbor-route-map-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-rmap-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Apply route map to neighbor (Name of route map)", "format": "string"}}}]}, "neighbor-filter-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"filter-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Establish BGP filters (AS path access-list name)", "format": "string"}, "filter-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true}}]}, "peer-group-name": {"description": "Configure peer-group (peer-group name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/router/bgp/{as-number}/address-family/ipv6/neighbor/ipv6-neighbor/{neighbor-ipv6}"}
    :param ipv4_neighbor_list: {"minItems": 1, "items": {"type": "ipv4-neighbor"}, "uniqueItems": true, "array": [{"required": ["neighbor-ipv4"], "properties": {"maximum-prefix": {"description": "Maximum number of prefix accept from this peer (maximum no. of prefix limit (various depends on model))", "format": "number", "type": "number", "maximum": 65536, "minimum": 1, "optional": true}, "neighbor-prefix-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-prefix-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-prefix-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (Name of a prefix list)", "format": "string"}}}]}, "allowas-in-count": {"description": "Number of occurrences of AS number", "format": "number", "default": 3, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}, "weight": {"description": "Set default weight for routes from this neighbor", "format": "number", "default": 0, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}, "peer-group-name": {"description": "Configure peer-group (peer-group name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "send-community-val": {"description": "'both': Send Standard and Extended Community attributes; 'none': Disable Sending Community attributes; 'standard': Send Standard Community attributes; 'extended': Send Extended Community attributes; ", "format": "enum", "default": "both", "type": "string", "enum": ["both", "none", "standard", "extended"], "optional": true}, "neighbor-ipv4": {"optional": false, "type": "string", "description": "Neighbor address", "format": "ipv4-address"}, "inbound": {"default": 0, "optional": true, "type": "number", "description": "Allow inbound soft reconfiguration for this neighbor", "format": "flag"}, "next-hop-self": {"default": 0, "optional": true, "type": "number", "description": "Disable the next hop calculation for this neighbor", "format": "flag"}, "maximum-prefix-thres": {"description": "threshold-value, 1 to 100 percent", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}, "route-map": {"description": "Route-map to specify criteria to originate default (route-map name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "default-originate": {"default": 0, "optional": true, "type": "number", "description": "Originate default route to this neighbor", "format": "flag"}, "remove-private-as": {"default": 0, "optional": true, "type": "number", "description": "Remove private AS number from outbound updates", "format": "flag"}, "unsuppress-map": {"description": "Route-map to selectively unsuppress suppressed routes (Name of route map)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "allowas-in": {"default": 0, "optional": true, "type": "number", "description": "Accept as-path with my AS present in it", "format": "flag"}, "activate": {"default": 0, "optional": true, "type": "number", "description": "Enable the Address Family for this Neighbor", "format": "flag"}, "distribute-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distribute-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "distribute-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Filter updates to/from this neighbor (IP standard/extended/named access list)", "format": "string"}}}]}, "prefix-list-direction": {"optional": true, "enum": ["both", "receive", "send"], "type": "string", "description": "'both': both; 'receive': receive; 'send': send; ", "format": "enum"}, "neighbor-route-map-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"nbr-rmap-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true, "nbr-route-map": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Apply route map to neighbor (Name of route map)", "format": "string"}}}]}, "neighbor-filter-lists": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"filter-list": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Establish BGP filters (AS path access-list name)", "format": "string"}, "filter-list-direction": {"enum": ["in", "out"], "type": "string", "description": "'in': in; 'out': out; ", "format": "enum"}, "optional": true}}]}}}], "type": "array", "$ref": "/axapi/v3/router/bgp/{as-number}/address-family/ipv6/neighbor/ipv4-neighbor/{neighbor-ipv4}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}/address-family/ipv6/neighbor`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "neighbor"
        self.a10_url="/axapi/v3/router/bgp/{as_number}/address-family/ipv6/neighbor"
        self.DeviceProxy = ""
        self.peer_group_neighbor_list = []
        self.ipv6_neighbor_list = []
        self.ipv4_neighbor_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


