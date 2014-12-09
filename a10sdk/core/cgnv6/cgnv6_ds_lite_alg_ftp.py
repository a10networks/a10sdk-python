from a10sdk.common.A10BaseClass import A10BaseClass


class Ftp(A10BaseClass):
    
    """Class Description::
    DS-Lite FTP ALG (default: enabled).

    Class ftp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ftp_enable: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': Disable ALG; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/ds-lite/alg/ftp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ftp"
        self.a10_url="/axapi/v3/cgnv6/ds-lite/alg/ftp"
        self.DeviceProxy = ""
        self.ftp_enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


