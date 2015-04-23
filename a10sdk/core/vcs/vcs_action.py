from a10sdk.common.A10BaseClass import A10BaseClass


class Action(A10BaseClass):
    
    """    :param action: {"description": "'enable': enable VCS; 'disable': disable VCS; ", "format": "enum", "default": "disable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    action for aVCS.

    Class action supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs/action`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "action"
        self.a10_url="/axapi/v3/vcs/action"
        self.DeviceProxy = ""
        self.action = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


