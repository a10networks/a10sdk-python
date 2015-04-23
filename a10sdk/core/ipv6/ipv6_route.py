from a10sdk.common.A10BaseClass import A10BaseClass


class Route(A10BaseClass):
    
    """Class Description::
    Establish static routes.

    Class route supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param rib_list: {"minItems": 1, "items": {"type": "rib"}, "uniqueItems": true, "array": [{"required": ["ipv6-address"], "properties": {"ipv6-address": {"optional": false, "type": "string", "description": "IPV6 address", "format": "ipv6-address-plen"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv6-nexthop-ipv6": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"description": "Distance value for this route", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}, "ipv6-nexthop": {"type": "string", "description": "Forwarding router's address", "format": "ipv6-address"}, "description": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "ethernet": {"type": "number", "description": "Ethernet interface (Ethernet interface number)", "format": "interface"}, "optional": true, "ve": {"type": "number", "description": "Virtual Ethernet interface (Virtual Ethernet interface number)", "format": "interface"}}}]}}}], "type": "array", "$ref": "/axapi/v3/ipv6/route/rib/{ipv6-address}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/route`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "route"
        self.a10_url="/axapi/v3/ipv6/route"
        self.DeviceProxy = ""
        self.rib_list = []
        self.static = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


