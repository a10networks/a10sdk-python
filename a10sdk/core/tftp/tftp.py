from a10sdk.common.A10BaseClass import A10BaseClass


class Tftp(A10BaseClass):
    
    """Class Description::
    TFTP client configuration.

    Class tftp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param blksize: {"description": "TFTP client block size value (Block size (Blksize/Max file size. Example: 1K/64M, 8K/512M, 32K/2048M))", "format": "number", "type": "number", "maximum": 32768, "minimum": 512, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/tftp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "tftp"
        self.a10_url="/axapi/v3/tftp"
        self.DeviceProxy = ""
        self.blksize = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


