from a10sdk.common.A10BaseClass import A10BaseClass


class Dnskey(A10BaseClass):
    
    """    :param key_delete: {"default": 0, "optional": true, "type": "number", "description": "Delete the DNSKEY file", "format": "flag"}
    :param zone_name: {"description": "DNS zone name of the child zone", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    DNSKEY Resource Records of child zones.

    Class dnskey supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/dnssec/dnskey`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dnskey"
        self.a10_url="/axapi/v3/dnssec/dnskey"
        self.DeviceProxy = ""
        self.key_delete = ""
        self.zone_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


