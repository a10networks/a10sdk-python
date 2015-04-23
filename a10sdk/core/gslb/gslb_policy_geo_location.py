from a10sdk.common.A10BaseClass import A10BaseClass


class IpMultipleFields(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip_addr2_sub: {"type": "string", "description": "Specify IP address range", "format": "ipv4-address"}
    :param ip_sub: {"type": "string", "description": "Specify IP information", "format": "ipv4-address"}
    :param ip_mask_sub: {"type": "string", "description": "Specify IP/mask format (Specify IP address mask)", "format": "ipv4-netmask-brief"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-multiple-fields"
        self.DeviceProxy = ""
        self.ip_addr2_sub = ""
        self.ip_sub = ""
        self.ip_mask_sub = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv6MultipleFields(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ipv6_mask_sub: {"description": "Specify IPv6/mask format (Specify IP address mask)", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}
    :param ipv6_sub: {"type": "string", "description": "Specify IPv6 information", "format": "ipv6-address"}
    :param ipv6_addr2_sub: {"type": "string", "description": "Specify IPv6 address range", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv6-multiple-fields"
        self.DeviceProxy = ""
        self.ipv6_mask_sub = ""
        self.ipv6_sub = ""
        self.ipv6_addr2_sub = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class GeoLocation(A10BaseClass):
    
    """Class Description::
    Specify geo-location.

    Class geo-location supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_multiple_fields: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ip-addr2-sub": {"type": "string", "description": "Specify IP address range", "format": "ipv4-address"}, "optional": true, "ip-sub": {"type": "string", "description": "Specify IP information", "format": "ipv4-address"}, "ip-mask-sub": {"type": "string", "description": "Specify IP/mask format (Specify IP address mask)", "format": "ipv4-netmask-brief"}}}]}
    :param name: {"description": "Specify geo-location name, section range is (1-15)", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param ipv6_multiple_fields: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv6-mask-sub": {"description": "Specify IPv6/mask format (Specify IP address mask)", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}, "ipv6-sub": {"type": "string", "description": "Specify IPv6 information", "format": "ipv6-address"}, "optional": true, "ipv6-addr2-sub": {"type": "string", "description": "Specify IPv6 address range", "format": "ipv6-address"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/policy/{name}/geo-location/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "geo-location"
        self.a10_url="/axapi/v3/gslb/policy/{name}/geo-location/{name}"
        self.DeviceProxy = ""
        self.ip_multiple_fields = []
        self.name = ""
        self.ipv6_multiple_fields = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


