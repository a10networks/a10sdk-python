from a10sdk.common.A10BaseClass import A10BaseClass


class DefaultGateway(A10BaseClass):
    
    """Class Description::
    Default gateway address.

    Class default-gateway supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_default_gateway: {"optional": true, "$ref": "/axapi/v3/ipv6/address", "type": "string", "description": "Default gateway address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ipv6/default-gateway`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "default-gateway"
        self.a10_url="/axapi/v3/ipv6/default-gateway"
        self.DeviceProxy = ""
        self.ipv6_default_gateway = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


