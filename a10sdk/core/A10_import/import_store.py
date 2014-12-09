from a10sdk.common.A10BaseClass import A10BaseClass


class Store(A10BaseClass):
    
    """    :param create: {"default": 0, "optional": true, "type": "number", "description": "Create an import store profile", "format": "flag"}
    :param name: {"description": "profile name to store remote url", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param remote_file: {"optional": true, "type": "string", "format": "url"}
    :param delete: {"default": 0, "optional": true, "type": "number", "description": "Delete an import store profile", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Create store name for remote url.

    Class store supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/import/store`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "store"
        self.a10_url="/axapi/v3/import/store"
        self.DeviceProxy = ""
        self.create = ""
        self.name = ""
        self.remote_file = ""
        self.delete = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


