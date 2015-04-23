from a10sdk.common.A10BaseClass import A10BaseClass


class Nat46Stateless(A10BaseClass):
    
    """    :param static_dest_mapping_list: {"minItems": 1, "items": {"type": "static-dest-mapping"}, "uniqueItems": true, "array": [{"required": ["v4-address", "v6-address"], "properties": {"count": {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Set number of consecutive mappings (Number of mappings)", "format": "number", "optional": true, "modify-not-allowed": 1, "type": "number"}, "v6-address": {"optional": false, "type": "string", "description": "IPv6 address", "format": "ipv6-address"}, "v4-address": {"optional": false, "type": "string", "description": "IPv4 address", "format": "ipv4-address"}, "vrid": {"description": "VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/nat46-stateless/static-dest-mapping/{v4-address}+{v6-address}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure Stateless NAT46.

    Class nat46-stateless supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat46-stateless`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "nat46-stateless"
        self.a10_url="/axapi/v3/cgnv6/nat46-stateless"
        self.DeviceProxy = ""
        self.static_dest_mapping_list = []
        self.fragmentation = {}
        self.A10WW_global = {}
        self.prefix = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


