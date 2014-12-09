from a10sdk.common.A10BaseClass import A10BaseClass


class AclIdList(A10BaseClass):
    
    """Class Description::
    Acl id.

    Class acl-id-list supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param msl: {"description": "Maximum Session Life Value", "format": "number", "type": "number", "maximum": 1800, "minimum": 1, "optional": true}
    :param acl_id: {"description": "Acl id", "format": "number", "optional": false, "maximum": 199, "minimum": 1, "type": "number", "$ref": "/axapi/v3/access-list/standard"}
    :param pool: {"description": "Pool or Pool Group (Pool or Pool Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/inside/source/list/acl-id-list/{acl_id}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "acl_id"]

        self.b_key = "acl-id-list"
        self.a10_url="/axapi/v3/ip/nat/inside/source/list/acl-id-list/{acl_id}"
        self.DeviceProxy = ""
        self.msl = ""
        self.acl_id = ""
        self.pool = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


