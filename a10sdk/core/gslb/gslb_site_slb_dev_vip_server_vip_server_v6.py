from a10sdk.common.A10BaseClass import A10BaseClass


class VipServerV6(A10BaseClass):
    
    """Class Description::
    Specify a VIP for the SLB device.

    Class vip-server-v6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6: {"optional": false, "type": "string", "description": "Specify IP address (IPv6 address)", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/vip-server/vip-server-v6/{ipv6}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv6"]

        self.b_key = "vip-server-v6"
        self.a10_url="/axapi/v3/gslb/site/{site_name}/slb-dev/{device_name}/vip-server/vip-server-v6/{ipv6}"
        self.DeviceProxy = ""
        self.ipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


