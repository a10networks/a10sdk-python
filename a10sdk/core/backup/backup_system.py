from a10sdk.common.A10BaseClass import A10BaseClass


class System(A10BaseClass):
    
    """    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param store_name: {"description": "Save backup store information", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Backup system files.

    Class system supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/backup/system`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "system"
        self.a10_url="/axapi/v3/backup/system"
        self.DeviceProxy = ""
        self.remote_file = ""
        self.use_mgmt_port = ""
        self.store_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


