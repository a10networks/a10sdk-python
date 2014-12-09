from a10sdk.common.A10BaseClass import A10BaseClass


class IpNat(A10BaseClass):
    
    """Class Description::
    IP NAT.

    Class ip-nat supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/router/ospf/{process_id}/redistribute/ip-nat`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ip-nat"
        self.a10_url="/axapi/v3/router/ospf/{process_id}/redistribute/ip-nat"
        self.DeviceProxy = ""
        self.ip_nat_redist = {}
        self.ip_nat_map = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


