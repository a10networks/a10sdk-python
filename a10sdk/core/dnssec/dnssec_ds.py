from a10sdk.common.A10BaseClass import A10BaseClass


class Ds(A10BaseClass):
    
    """    :param ds_delete: {"default": 0, "optional": true, "type": "number", "description": "Delete the DS file", "format": "flag"}
    :param zone_name: {"description": "DNS zone name of the child zone", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Delegation Signer(DS) Resource Records of child zones.

    Class ds supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/dnssec/ds`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ds"
        self.a10_url="/axapi/v3/dnssec/ds"
        self.DeviceProxy = ""
        self.ds_delete = ""
        self.zone_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


