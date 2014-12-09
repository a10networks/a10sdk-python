from a10sdk.common.A10BaseClass import A10BaseClass


class DefaultGateway(A10BaseClass):
    
    """Class Description::
    Transparent mode gateway.

    Class default-gateway supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param gateway_ip: {"optional": true, "$ref": "/axapi/v3/ip/address", "type": "string", "description": "Default gateway address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/default-gateway`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "default-gateway"
        self.a10_url="/axapi/v3/ip/default-gateway"
        self.DeviceProxy = ""
        self.gateway_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


