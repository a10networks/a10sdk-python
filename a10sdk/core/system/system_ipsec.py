from a10sdk.common.A10BaseClass import A10BaseClass


class Ipsec(A10BaseClass):
    
    """Class Description::
    Configure Crypto Cores for IPsec processing.

    Class ipsec supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param crypto_core: {"description": "Crypto cores assigned for IPsec processing", "format": "number", "default": 0, "optional": true, "maximum": 56, "minimum": 0, "type": "number"}
    :param crypto_mem: {"description": "Crypto memory percentage assigned for IPsec processing", "format": "number", "default": 0, "optional": true, "maximum": 100, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/ipsec`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ipsec"
        self.a10_url="/axapi/v3/system/ipsec"
        self.DeviceProxy = ""
        self.crypto_core = ""
        self.crypto_mem = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


