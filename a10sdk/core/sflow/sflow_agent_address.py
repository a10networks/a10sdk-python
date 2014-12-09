from a10sdk.common.A10BaseClass import A10BaseClass


class Address(A10BaseClass):
    
    """Class Description::
    Configure agent address used in sFlow datagram, default use management IP address.

    Class address supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip: {"not": "ipv6", "optional": true, "type": "string", "description": "Configure sFlow agent IP address", "format": "ipv4-address"}
    :param ipv6: {"not": "ip", "optional": true, "type": "string", "description": "Configure sFlow agent IPv6 address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sflow/agent/address`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "address"
        self.a10_url="/axapi/v3/sflow/agent/address"
        self.DeviceProxy = ""
        self.ip = ""
        self.ipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


