from a10sdk.common.A10BaseClass import A10BaseClass


class GeoLocnMultipleAddresses(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param first_ip_address: {"type": "string", "description": "Specify IP information (Specify IP address)", "format": "ipv4-address"}
    :param first_ipv6_address: {"type": "string", "description": "Specify IPv6 address", "format": "ipv6-address"}
    :param geol_ipv4_mask: {"not": "ip-addr2", "type": "string", "description": "Specify IPv4 mask", "format": "ipv4-netmask"}
    :param ip_addr2: {"not": "geol-ipv4-mask", "type": "string", "description": "Specify IP address range", "format": "ipv4-address"}
    :param ipv6_addr2: {"not": "geol-ipv6-mask", "type": "string", "description": "Specify IPv6 address range", "format": "ipv6-address"}
    :param geol_ipv6_mask: {"description": "Specify IPv6 mask", "format": "number", "maximum": 128, "minimum": 0, "not": "ipv6-addr2", "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "geo-locn-multiple-addresses"
        self.DeviceProxy = ""
        self.first_ip_address = ""
        self.first_ipv6_address = ""
        self.geol_ipv4_mask = ""
        self.ip_addr2 = ""
        self.ipv6_addr2 = ""
        self.geol_ipv6_mask = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class GeoLocation(A10BaseClass):
    
    """Class Description::
    Configure a GSLB global geo-location object.

    Class geo-location supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param geo_locn_obj_name: {"description": "Specify geo-location name, section range is (1-15)", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param geo_locn_multiple_addresses: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"first-ip-address": {"type": "string", "description": "Specify IP information (Specify IP address)", "format": "ipv4-address"}, "first-ipv6-address": {"type": "string", "description": "Specify IPv6 address", "format": "ipv6-address"}, "geol-ipv4-mask": {"not": "ip-addr2", "type": "string", "description": "Specify IPv4 mask", "format": "ipv4-netmask"}, "ip-addr2": {"not": "geol-ipv4-mask", "type": "string", "description": "Specify IP address range", "format": "ipv4-address"}, "ipv6-addr2": {"not": "geol-ipv6-mask", "type": "string", "description": "Specify IPv6 address range", "format": "ipv6-address"}, "geol-ipv6-mask": {"description": "Specify IPv6 mask", "format": "number", "maximum": 128, "minimum": 0, "not": "ipv6-addr2", "type": "number"}, "optional": true}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/geo-location/{geo_locn_obj_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "geo_locn_obj_name"]

        self.b_key = "geo-location"
        self.a10_url="/axapi/v3/gslb/geo-location/{geo_locn_obj_name}"
        self.DeviceProxy = ""
        self.geo_locn_obj_name = ""
        self.geo_locn_multiple_addresses = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


