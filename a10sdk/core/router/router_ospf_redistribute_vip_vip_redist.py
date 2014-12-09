from a10sdk.common.A10BaseClass import A10BaseClass


class VipList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param metric_type_vip: {"default": "2", "enum": ["1", "2"], "type": "string", "description": "1: \"Set OSPF External Type 1 metrics\"; 2: \"Set OSPF External Type 2 metrics\"; ", "format": "enum"}
    :param tag_vip: {"type": "number", "description": "Set tag for routes redistributed into OSPF. help-val 32-bit tag value", "format": "number"}
    :param metric_vip: {"description": "OSPF default metric. help-val OSPF metric", "minimum": 0, "type": "number", "maximum": 16777214, "format": "number"}
    :param route_map_vip: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference. help-val Pointer to route-map entries", "format": "string"}
    :param type_vip: {"enum": ["only-flagged", "only-not-flagged"], "type": "string", "description": "only-flagged: \"Selected Virtual IP (VIP)\"; only-not-flagged: \"Only not flagged\"; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vip-list"
        self.DeviceProxy = ""
        self.metric_type_vip = ""
        self.tag_vip = ""
        self.metric_vip = ""
        self.route_map_vip = ""
        self.type_vip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VipRedist(A10BaseClass):
    
    """Class Description::
    VIP redistribution.

    Class vip-redist supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vip_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"metric-type-vip": {"default": "2", "enum": ["1", "2"], "type": "string", "description": "1: \"Set OSPF External Type 1 metrics\"; 2: \"Set OSPF External Type 2 metrics\"; ", "format": "enum"}, "tag-vip": {"type": "number", "description": "Set tag for routes redistributed into OSPF. help-val 32-bit tag value", "format": "number"}, "metric-vip": {"description": "OSPF default metric. help-val OSPF metric", "minimum": 0, "type": "number", "maximum": 16777214, "format": "number"}, "route-map-vip": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Route map reference. help-val Pointer to route-map entries", "format": "string"}, "optional": true, "type-vip": {"enum": ["only-flagged", "only-not-flagged"], "type": "string", "description": "only-flagged: \"Selected Virtual IP (VIP)\"; only-not-flagged: \"Only not flagged\"; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ospf/{process_id}/redistribute/vip/vip-redist`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vip-redist"
        self.a10_url="/axapi/v3/router/ospf/{process_id}/redistribute/vip/vip-redist"
        self.DeviceProxy = ""
        self.vip_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


