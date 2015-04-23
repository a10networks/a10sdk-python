from a10sdk.common.A10BaseClass import A10BaseClass


class Lw4O6(A10BaseClass):
    
    """Class Description::
    Configure LW-4over6 interface.

    Class lw-4o6 supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param outside: {"default": 0, "optional": true, "type": "number", "description": "Configure LW-4over6 inside interface", "format": "flag"}
    :param inside: {"default": 0, "optional": true, "type": "number", "description": "Configure LW-4over6 outside interface", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/ethernet/{ifnum}/lw-4o6`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "lw-4o6"
        self.a10_url="/axapi/v3/interface/ethernet/{ifnum}/lw-4o6"
        self.DeviceProxy = ""
        self.outside = ""
        self.inside = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


