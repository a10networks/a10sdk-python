from a10sdk.common.A10BaseClass import A10BaseClass


class PoolGroup(A10BaseClass):
    
    """Class Description::
    IPv6 pool group name.

    Class pool-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param member_list: {"minItems": 1, "items": {"type": "member"}, "uniqueItems": true, "array": [{"required": ["pool-name"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "pool-name": {"description": "Specify NAT pool name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ipv6/nat/pool-group/{pool-group-name}/member/{pool-name}"}
    :param pool_group_name: {"description": "Specify pool group name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param vrid: {"description": "Specify VRRP-A vrid (Specify ha VRRP-A vrid)", "format": "number", "optional": true, "maximum": 31, "minimum": 1, "modify-not-allowed": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/nat/pool-group/{pool_group_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "pool_group_name"]

        self.b_key = "pool-group"
        self.a10_url="/axapi/v3/ipv6/nat/pool-group/{pool_group_name}"
        self.DeviceProxy = ""
        self.member_list = []
        self.pool_group_name = ""
        self.vrid = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


