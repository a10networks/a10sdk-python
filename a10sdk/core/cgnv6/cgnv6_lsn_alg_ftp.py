from a10sdk.common.A10BaseClass import A10BaseClass


class Ftp(A10BaseClass):
    
    """Class Description::
    Change LSN FTP ALG Settings.

    Class ftp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ftp_value: {"optional": true, "enum": ["disable"], "type": "string", "description": "'disable': Disable FTP ALG for LSN; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/alg/ftp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ftp"
        self.a10_url="/axapi/v3/cgnv6/lsn/alg/ftp"
        self.DeviceProxy = ""
        self.ftp_value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


