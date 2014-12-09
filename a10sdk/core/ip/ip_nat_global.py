from a10sdk.common.A10BaseClass import A10BaseClass


class NatGlobal(A10BaseClass):
    
    """Class Description::
    IP NAT global settings.

    Class nat-global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param reset_idle_tcp_conn: {"description": "Reset Idle TCP Connections", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat-global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "nat-global"
        self.a10_url="/axapi/v3/ip/nat-global"
        self.DeviceProxy = ""
        self.reset_idle_tcp_conn = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


