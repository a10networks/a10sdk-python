from a10sdk.common.A10BaseClass import A10BaseClass


class SignZoneNow(A10BaseClass):
    
    """    :param zone_name: {"description": "Specify the name for the DNS zone, empty means sign all zones", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    sign zone right now.

    Class sign-zone-now supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/dnssec/sign-zone-now`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "sign-zone-now"
        self.a10_url="/axapi/v3/dnssec/sign-zone-now"
        self.DeviceProxy = ""
        self.zone_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


