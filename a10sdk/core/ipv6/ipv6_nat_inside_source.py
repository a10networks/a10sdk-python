from a10sdk.common.A10BaseClass import A10BaseClass


class Source(A10BaseClass):
    
    """Class Description::
    Source Association.

    Class source supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param list_list: {"minItems": 1, "items": {"type": "list"}, "uniqueItems": true, "array": [{"required": ["list-name"], "properties": {"list-name": {"description": "IPv6 access-list name", "format": "string", "minLength": 1, "optional": false, "maxLength": 16, "type": "string", "$ref": "/axapi/v3/ipv6/access-list"}, "pool": {"description": "IPv6 NAT Pool (Pool Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/ipv6/nat/pool-group"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ipv6/nat/inside/source/list/{list-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/nat/inside/source`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "source"
        self.a10_url="/axapi/v3/ipv6/nat/inside/source"
        self.DeviceProxy = ""
        self.list_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


