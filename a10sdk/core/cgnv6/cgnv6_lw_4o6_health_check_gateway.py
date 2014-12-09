from a10sdk.common.A10BaseClass import A10BaseClass


class HealthCheckGateway(A10BaseClass):
    
    """Class Description::
    Configure LW-4over6 health-check gateway.

    Class health-check-gateway supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv4_addr: {"optional": false, "type": "string", "description": "LW-4over6 IPv4 Gateway", "format": "ipv4-address"}
    :param ipv6_addr: {"optional": false, "type": "string", "description": "LW-4over6 IPv6 Gateway", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lw-4o6/health-check-gateway/{ipv4_addr}+{ipv6_addr}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ipv4_addr","ipv6_addr"]

        self.b_key = "health-check-gateway"
        self.a10_url="/axapi/v3/cgnv6/lw-4o6/health-check-gateway/{ipv4_addr}+{ipv6_addr}"
        self.DeviceProxy = ""
        self.ipv4_addr = ""
        self.ipv6_addr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


