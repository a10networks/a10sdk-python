from a10sdk.common.A10BaseClass import A10BaseClass


class Bfd(A10BaseClass):
    
    """Class Description::
    Bidirectional Forwarding Detection.

    Class bfd supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param local_ip: {"optional": false, "type": "string", "description": "Local IP address", "format": "ipv4-address"}
    :param nexthop_ip: {"optional": false, "type": "string", "description": "Nexthop IP address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/route/static/bfd/{local_ip}+{nexthop_ip}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "local_ip","nexthop_ip"]

        self.b_key = "bfd"
        self.a10_url="/axapi/v3/ip/route/static/bfd/{local_ip}+{nexthop_ip}"
        self.DeviceProxy = ""
        self.local_ip = ""
        self.nexthop_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


