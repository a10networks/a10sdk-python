from a10sdk.common.A10BaseClass import A10BaseClass


class Ipsec(A10BaseClass):
    
    """    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param packet_round_robin: {"default": 0, "optional": true, "type": "number", "description": "Enable packet round robin for IPsec packets", "format": "flag"}
    :param crypto_core: {"description": "Crypto cores assigned for IPsec processing", "format": "number", "default": 0, "optional": true, "maximum": 56, "minimum": 0, "type": "number"}
    :param crypto_mem: {"description": "Crypto memory percentage assigned for IPsec processing", "format": "number", "default": 0, "optional": true, "maximum": 100, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure Crypto Cores for IPsec processing.

    Class ipsec supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/ipsec`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ipsec"
        self.a10_url="/axapi/v3/system/ipsec"
        self.DeviceProxy = ""
        self.uuid = ""
        self.packet_round_robin = ""
        self.crypto_core = ""
        self.crypto_mem = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


