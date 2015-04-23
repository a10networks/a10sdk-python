from a10sdk.common.A10BaseClass import A10BaseClass


class Source(A10BaseClass):
    
    """Class Description::
    Source.

    Class source supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param static_list: {"minItems": 1, "items": {"type": "static"}, "uniqueItems": true, "array": [{"required": ["src-address", "nat-address"], "properties": {"nat-address": {"optional": false, "type": "string", "description": "NAT Address", "format": "ipv4-address"}, "vrid": {"description": "VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "src-address": {"optional": false, "type": "string", "description": "Original Source Address", "format": "ipv4-address"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/nat/inside/source/static/{src-address}+{nat-address}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat/inside/source`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "source"
        self.a10_url="/axapi/v3/cgnv6/nat/inside/source"
        self.DeviceProxy = ""
        self.static_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


