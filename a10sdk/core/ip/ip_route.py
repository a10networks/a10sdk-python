from a10sdk.common.A10BaseClass import A10BaseClass


class Route(A10BaseClass):
    
    """Class Description::
    Establish static routes.

    Class route supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rib_list: {"minItems": 1, "items": {"type": "rib"}, "uniqueItems": true, "array": [{"required": ["ip-dest-addr", "ip-mask"], "properties": {"ip-nexthop-lif": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cpu-process-1": {"default": 0, "type": "number", "description": "CPU rather than HW handle this entity", "plat-neg-list": ["non-fpga", "soft-ax"], "format": "flag"}, "lif": {"description": "LIF Interface (Logical tunnel interface number)", "minimum": 1, "type": "number", "maximum": 128, "format": "number"}, "description-nexthop-lif": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}, "distance-nexthop-lif": {"description": "Distance value for this route", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}, "optional": true}}]}, "ip-nexthop-ipv4": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "cpu-process-3": {"default": 0, "type": "number", "description": "CPU rather than HW handle this entity", "plat-neg-list": ["non-fpga", "soft-ax"], "format": "flag"}, "description-nexthop-ip": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}, "ip-next-hop": {"type": "string", "description": "Forwarding router's address", "format": "ipv4-address"}, "distance-nexthop-ip": {"description": "Distance value for this route", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}}}]}, "ip-dest-addr": {"optional": false, "type": "string", "description": "Destination prefix", "format": "ipv4-address"}, "ip-nexthop-tunnel": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"description-nexthop-tunnel": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}, "tunnel": {"description": "Tunnel interface (Tunnel interface number)", "minimum": 1, "type": "number", "maximum": 128, "format": "number"}, "ip-next-hop-tunnel": {"type": "string", "description": "Forwarding router's address", "format": "ipv4-address"}, "distance-nexthop-tunnel": {"description": "Distance value for this route", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}, "optional": true, "cpu-process-2": {"default": 0, "type": "number", "description": "CPU rather than HW handle this entity", "plat-neg-list": ["non-fpga", "soft-ax"], "format": "flag"}}}]}, "ip-nexthop-partition": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"partition-name": {"minLength": 1, "maxLength": 14, "type": "string", "description": "Name of network partition", "format": "string"}, "vrid-num-in-partition": {"description": "Specify ha VRRP-A vrid", "minimum": 0, "type": "number", "maximum": 31, "format": "number"}, "optional": true, "description-partition-vrid": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}, "description-nexthop-partition": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}}}]}, "ip-mask": {"optional": false, "type": "string", "description": "Destination prefix mask", "format": "ipv4-netmask-brief"}}}], "type": "array", "$ref": "/axapi/v3/ip/route/rib/{ip-dest-addr}+{ip-mask}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/route`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "route"
        self.a10_url="/axapi/v3/ip/route"
        self.DeviceProxy = ""
        self.rib_list = []
        self.static = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


