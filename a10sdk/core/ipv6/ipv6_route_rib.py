from a10sdk.common.A10BaseClass import A10BaseClass


class Ipv6NexthopIpv6(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param distance: {"description": "Distance value for this route", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}
    :param ipv6_nexthop: {"type": "string", "description": "Forwarding router's address", "format": "ipv6-address"}
    :param description: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}
    :param trunk: {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}
    :param ethernet: {"type": "number", "description": "Ethernet interface (Ethernet interface number)", "format": "interface"}
    :param ve: {"type": "number", "description": "Virtual Ethernet interface (Virtual Ethernet interface number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-nexthop-ipv6"
        self.DeviceProxy = ""
        self.distance = ""
        self.ipv6_nexthop = ""
        self.description = ""
        self.trunk = ""
        self.ethernet = ""
        self.ve = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Rib(A10BaseClass):
    
    """Class Description::
    Establish static routes.

    Class rib supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_address: {"optional": false, "type": "string", "description": "IPV6 address", "format": "ipv6-address-plen"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ipv6_nexthop_ipv6: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"description": "Distance value for this route", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}, "ipv6-nexthop": {"type": "string", "description": "Forwarding router's address", "format": "ipv6-address"}, "description": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Description for static route", "format": "string-rlx"}, "trunk": {"type": "number", "description": "Trunk interface (Trunk interface number)", "format": "interface"}, "ethernet": {"type": "number", "description": "Ethernet interface (Ethernet interface number)", "format": "interface"}, "optional": true, "ve": {"type": "number", "description": "Virtual Ethernet interface (Virtual Ethernet interface number)", "format": "interface"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/route/rib/{ipv6_address}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv6_address"]

        self.b_key = "rib"
        self.a10_url="/axapi/v3/ipv6/route/rib/{ipv6_address}"
        self.DeviceProxy = ""
        self.ipv6_address = ""
        self.uuid = ""
        self.ipv6_nexthop_ipv6 = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


