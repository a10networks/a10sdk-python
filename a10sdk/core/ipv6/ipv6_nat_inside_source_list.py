from a10sdk.common.A10BaseClass import A10BaseClass


class List(A10BaseClass):
    
    """Class Description::
    IPv6 Access-List.

    Class list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param list_name: {"description": "IPv6 access-list name", "format": "string", "minLength": 1, "optional": false, "maxLength": 16, "type": "string", "$ref": "/axapi/v3/ipv6/access-list"}
    :param pool: {"description": "IPv6 NAT Pool (Pool Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/ipv6/nat/pool-group"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/nat/inside/source/list/{list_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "list_name"]

        self.b_key = "list"
        self.a10_url="/axapi/v3/ipv6/nat/inside/source/list/{list_name}"
        self.DeviceProxy = ""
        self.list_name = ""
        self.pool = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


