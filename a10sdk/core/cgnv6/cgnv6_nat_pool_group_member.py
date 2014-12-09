from a10sdk.common.A10BaseClass import A10BaseClass


class Member(A10BaseClass):
    
    """Class Description::
    Add a CGNv6 NAT pool to this pool-group.

    Class member supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param pool_name: {"description": "Specify CGNv6 NAT pool name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/nat/pool-group/{pool_group_name}/member/{pool_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "pool_name"]

        self.b_key = "member"
        self.a10_url="/axapi/v3/cgnv6/nat/pool-group/{pool_group_name}/member/{pool_name}"
        self.DeviceProxy = ""
        self.pool_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


