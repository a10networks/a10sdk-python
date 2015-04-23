from a10sdk.common.A10BaseClass import A10BaseClass


class AggregateAddressList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param as_set: {"default": 0, "type": "number", "description": "Generate AS set path information", "format": "flag"}
    :param summary_only: {"default": 0, "type": "number", "description": "Filter more specific routes from updates", "format": "flag"}
    :param aggregate_address: {"type": "string", "description": "Configure BGP aggregate entries (Aggregate prefix)", "format": "ipv4-cidr"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "aggregate-address-list"
        self.DeviceProxy = ""
        self.as_set = ""
        self.summary_only = ""
        self.aggregate_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DampeningCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dampening_max_supress: {"description": "Maximum duration to suppress a stable route(minutes)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param dampening: {"default": 0, "type": "number", "description": "Enable route-flap dampening", "format": "flag"}
    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route-map to specify criteria for dampening (Route-map name)", "format": "string"}
    :param dampening_penalty: {"description": "Un-reachability Half-life time for the penalty(minutes)", "minimum": 1, "type": "number", "maximum": 45, "format": "number"}
    :param dampening_half_time: {"description": "Reachability Half-life time for the penalty(minutes)", "minimum": 1, "type": "number", "maximum": 45, "format": "number"}
    :param dampening_supress: {"description": "Value to start suppressing a route", "minimum": 1, "type": "number", "maximum": 20000, "format": "number"}
    :param dampening_reuse: {"description": "Value to start reusing a route", "minimum": 1, "type": "number", "maximum": 20000, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dampening-cfg"
        self.DeviceProxy = ""
        self.dampening_max_supress = ""
        self.dampening = ""
        self.route_map = ""
        self.dampening_penalty = ""
        self.dampening_half_time = ""
        self.dampening_supress = ""
        self.dampening_reuse = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class BestpathCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ignore: {"default": 0, "type": "number", "description": "Ignore as-path length in selecting a route", "format": "flag"}
    :param remove_send_med: {"default": 0, "type": "number", "description": "To remove send MED attribute", "format": "flag"}
    :param remove_recv_med: {"default": 0, "type": "number", "description": "To remove rcvd MED attribute", "format": "flag"}
    :param compare_routerid: {"default": 0, "type": "number", "description": "Compare router-id for identical EBGP paths", "format": "flag"}
    :param missing_as_worst: {"default": 0, "type": "number", "description": "Treat missing MED as the least preferred one", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "bestpath-cfg"
        self.DeviceProxy = ""
        self.ignore = ""
        self.remove_send_med = ""
        self.remove_recv_med = ""
        self.compare_routerid = ""
        self.missing_as_worst = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Bgp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param enforce_first_as: {"default": 0, "type": "number", "description": "Enforce the first AS for EBGP routes", "format": "flag"}
    :param scan_time: {"description": "Configure background scan interval (Scan interval (sec) [Default:60 Disable:0])", "format": "number", "default": 60, "maximum": 60, "minimum": 0, "type": "number"}
    :param router_id: {"type": "string", "description": "Override current router identifier (peers will reset) (Manually configured router identifier)", "format": "ipv4-address"}
    :param log_neighbor_changes: {"default": 0, "type": "number", "description": "Log neighbor up/down and reset reason", "format": "flag"}
    :param deterministic_med: {"default": 0, "type": "number", "description": "Pick the best-MED path among paths advertised from the neighboring AS", "format": "flag"}
    :param fast_external_failover: {"default": 1, "type": "number", "description": "Immediately reset session if a link to a directly connected external peer goes down", "format": "flag"}
    :param local_preference_value: {"description": "Configure default local preference value", "format": "number", "default": 100, "maximum": 4294967295, "minimum": 0, "type": "number"}
    :param nexthop_trigger_count: {"description": "BGP nexthop-tracking status (count)", "format": "number", "default": 0, "maximum": 127, "minimum": 0, "type": "number"}
    :param always_compare_med: {"default": 0, "type": "number", "description": "Allow comparing MED from different neighbors", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "bgp"
        self.DeviceProxy = ""
        self.enforce_first_as = ""
        self.scan_time = ""
        self.router_id = ""
        self.log_neighbor_changes = ""
        self.deterministic_med = ""
        self.fast_external_failover = ""
        self.local_preference_value = ""
        self.nexthop_trigger_count = ""
        self.dampening_cfg = {}
        self.always_compare_med = ""
        self.bestpath_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Timers(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param bgp_holdtime: {"description": "Holdtime", "format": "number", "default": 90, "maximum": 65535, "minimum": 0, "type": "number"}
    :param bgp_keepalive: {"description": "Keepalive interval", "format": "number", "default": 30, "maximum": 65535, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "timers"
        self.DeviceProxy = ""
        self.bgp_holdtime = ""
        self.bgp_keepalive = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DistanceList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ext_routes_dist: {"description": "Distance for routes external to the AS", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param src_prefix: {"type": "string", "description": "IP source prefix", "format": "ipv4-cidr"}
    :param int_routes_dist: {"description": "Distance for routes internal to the AS", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param acl_str: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access list name", "format": "string"}
    :param admin_distance: {"description": "Define an administrative distance", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param local_routes_dist: {"description": "Distance for local routes", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "distance-list"
        self.DeviceProxy = ""
        self.ext_routes_dist = ""
        self.src_prefix = ""
        self.int_routes_dist = ""
        self.acl_str = ""
        self.admin_distance = ""
        self.local_routes_dist = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Bgp(A10BaseClass):
    
    """Class Description::
    Border Gateway Protocol (BGP).

    Class bgp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param as_number: {"description": "AS number", "format": "number", "type": "number", "maximum": 4294967295, "minimum": 1, "optional": false}
    :param aggregate_address_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"as-set": {"default": 0, "type": "number", "description": "Generate AS set path information", "format": "flag"}, "summary-only": {"default": 0, "type": "number", "description": "Filter more specific routes from updates", "format": "flag"}, "optional": true, "aggregate-address": {"type": "string", "description": "Configure BGP aggregate entries (Aggregate prefix)", "format": "ipv4-cidr"}}}]}
    :param originate: {"default": 0, "optional": true, "type": "number", "description": "Distribute a default route", "format": "flag"}
    :param auto_summary: {"default": 0, "optional": true, "type": "number", "description": "Enable automatic network number summarization", "format": "flag"}
    :param maximum_paths_value: {"description": "Supported BGP multipath numbers", "format": "number", "default": 1, "optional": true, "maximum": 64, "minimum": 1, "type": "number"}
    :param synchronization: {"default": 0, "optional": true, "type": "number", "description": "Perform IGP synchronization", "format": "flag"}
    :param distance_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ext-routes-dist": {"description": "Distance for routes external to the AS", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "src-prefix": {"type": "string", "description": "IP source prefix", "format": "ipv4-cidr"}, "int-routes-dist": {"description": "Distance for routes internal to the AS", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "acl-str": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Access list name", "format": "string"}, "admin-distance": {"description": "Define an administrative distance", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "local-routes-dist": {"description": "Distance for local routes", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "as_number"]

        self.b_key = "bgp"
        self.a10_url="/axapi/v3/router/bgp/{as_number}"
        self.DeviceProxy = ""
        self.redistribute = {}
        self.as_number = ""
        self.aggregate_address_list = []
        self.originate = ""
        self.auto_summary = ""
        self.bgp = {}
        self.network = {}
        self.maximum_paths_value = ""
        self.synchronization = ""
        self.timers = {}
        self.neighbor = {}
        self.distance_list = []
        self.address_family = {}
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


