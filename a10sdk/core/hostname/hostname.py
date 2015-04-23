from a10sdk.common.A10BaseClass import A10BaseClass


class Hostname(A10BaseClass):
    
    """    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param value: {"optional": true, "platform-specific-default": 1, "type": "string", "description": "This System's Network Name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Set system's network name.

    Class hostname supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/hostname`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "hostname"
        self.a10_url="/axapi/v3/hostname"
        self.DeviceProxy = ""
        self.uuid = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


