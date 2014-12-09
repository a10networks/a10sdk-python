from a10sdk.common.A10BaseClass import A10BaseClass


class Restore(A10BaseClass):
    
    """    :param remote_file: {"optional": true, "type": "string", "description": "Remote file path", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Restore system files.

    Class restore supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/restore`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "restore"
        self.a10_url="/axapi/v3/restore"
        self.DeviceProxy = ""
        self.remote_file = ""
        self.use_mgmt_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


