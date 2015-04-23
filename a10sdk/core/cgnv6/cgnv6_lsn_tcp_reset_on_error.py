from a10sdk.common.A10BaseClass import A10BaseClass


class ResetOnError(A10BaseClass):
    
    """Class Description::
    Send TCP resets for invalid sessions (Default: enabled).

    Class reset-on-error supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param outbound: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': Disable send TCP reset on error; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/tcp/reset-on-error`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "reset-on-error"
        self.a10_url="/axapi/v3/cgnv6/lsn/tcp/reset-on-error"
        self.DeviceProxy = ""
        self.outbound = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


