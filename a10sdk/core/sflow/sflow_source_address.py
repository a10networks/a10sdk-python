from a10sdk.common.A10BaseClass import A10BaseClass


class SourceAddress(A10BaseClass):
    
    """Class Description::
    Specify source address of sFlow packet.

    Class source-address supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip: {"optional": true, "type": "string", "description": "Source IPv4 address", "format": "ipv4-address"}
    :param ipv6: {"optional": true, "type": "string", "description": "Source IPv6 address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sflow/source-address`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "source-address"
        self.a10_url="/axapi/v3/sflow/source-address"
        self.DeviceProxy = ""
        self.ip = ""
        self.ipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


