from a10sdk.common.A10BaseClass import A10BaseClass


class AclNameList(A10BaseClass):
    
    """Class Description::
    Apply an access list.

    Class acl-name-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param msl: {"description": "Maximum Session Life Value", "format": "number", "type": "number", "maximum": 1800, "minimum": 1, "optional": true}
    :param name: {"description": "Apply an access list", "format": "string", "minLength": 1, "optional": false, "maxLength": 16, "type": "string", "$ref": "/axapi/v3/ip/access-list"}
    :param pool: {"description": "Pool or Pool Group (Pool or Pool Group Nam)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/inside/source/list/acl-name-list/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "acl-name-list"
        self.a10_url="/axapi/v3/ip/nat/inside/source/list/acl-name-list/{name}"
        self.DeviceProxy = ""
        self.msl = ""
        self.name = ""
        self.pool = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


