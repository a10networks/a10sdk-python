from a10sdk.common.A10BaseClass import A10BaseClass


class Distance(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distance_local: {"description": "Distance for local routes", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param distance_int: {"description": "Distance for routes internal to the AS", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param distance_ext: {"description": "Distance for routes external to the AS", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "distance"
        self.DeviceProxy = ""
        self.distance_local = ""
        self.distance_int = ""
        self.distance_ext = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AggregateAddressList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param as_set: {"default": 0, "type": "number", "description": "Generate AS set path information", "format": "flag"}
    :param summary_only: {"default": 0, "type": "number", "description": "Filter more specific routes from updates", "format": "flag"}
    :param aggregate_address: {"type": "string", "description": "Configure BGP aggregate entries (Aggregate IPv6 prefix)", "format": "ipv6-address-plen"}
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


class Bgp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dampening_max_supress: {"description": "Maximum duration to suppress a stable route(minutes)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param dampening: {"default": 0, "type": "number", "description": "Enable route-flap dampening", "format": "flag"}
    :param dampening_half: {"description": "Reachability Half-life time for the penalty(minutes)", "minimum": 1, "type": "number", "maximum": 45, "format": "number"}
    :param dampening_start_reuse: {"description": "Value to start reusing a route", "minimum": 1, "type": "number", "maximum": 20000, "format": "number"}
    :param route_map: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route-map to specify criteria for dampening (Route-map name)", "format": "string"}
    :param dampening_start_supress: {"description": "Value to start suppressing a route", "minimum": 1, "type": "number", "maximum": 20000, "format": "number"}
    :param dampening_unreachability: {"description": "Un-reachability Half-life time for the penalty(minutes)", "minimum": 1, "type": "number", "maximum": 45, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "bgp"
        self.DeviceProxy = ""
        self.dampening_max_supress = ""
        self.dampening = ""
        self.dampening_half = ""
        self.dampening_start_reuse = ""
        self.route_map = ""
        self.dampening_start_supress = ""
        self.dampening_unreachability = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6(A10BaseClass):
    
    """Class Description::
    ipv6 Address family.

    Class ipv6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param aggregate_address_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"as-set": {"default": 0, "type": "number", "description": "Generate AS set path information", "format": "flag"}, "summary-only": {"default": 0, "type": "number", "description": "Filter more specific routes from updates", "format": "flag"}, "optional": true, "aggregate-address": {"type": "string", "description": "Configure BGP aggregate entries (Aggregate IPv6 prefix)", "format": "ipv6-address-plen"}}}]}
    :param originate: {"default": 0, "optional": true, "type": "number", "description": "Distribute an IPv6 default route", "format": "flag"}
    :param auto_summary: {"default": 0, "optional": true, "type": "number", "description": "Enable automatic network number summarization", "format": "flag"}
    :param maximum_paths_value: {"description": "Supported BGP multipath numbers", "format": "number", "default": 1, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}
    :param synchronization: {"default": 0, "optional": true, "type": "number", "description": "Perform IGP synchronization", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/bgp/{as_number}/address-family/ipv6`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ipv6"
        self.a10_url="/axapi/v3/router/bgp/{as_number}/address-family/ipv6"
        self.DeviceProxy = ""
        self.distance = {}
        self.redistribute = {}
        self.aggregate_address_list = []
        self.originate = ""
        self.auto_summary = ""
        self.bgp = {}
        self.network = {}
        self.maximum_paths_value = ""
        self.synchronization = ""
        self.neighbor = {}
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


