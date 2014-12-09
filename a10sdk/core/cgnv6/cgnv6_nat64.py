from a10sdk.common.A10BaseClass import A10BaseClass


class Nat64(A10BaseClass):
    
    """Class Description::
    Configure NAT64.

    Class nat64 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param prefix_list: {"minItems": 1, "items": {"type": "prefix"}, "uniqueItems": true, "array": [{"required": ["prefix-val"], "properties": {"vrid": {"description": "VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}, "prefix-val": {"optional": false, "type": "string", "description": "NAT64 Prefix", "format": "ipv6-address-plen"}, "class-list": {"description": "Class-list to match for NAT64", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/nat64/prefix/{prefix-val}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat64`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "nat64"
        self.a10_url="/axapi/v3/cgnv6/nat64"
        self.DeviceProxy = ""
        self.alg = {}
        self.fragmentation = {}
        self.A10WW_global = {}
        self.prefix_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


