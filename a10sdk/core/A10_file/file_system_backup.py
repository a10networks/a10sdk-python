from a10sdk.common.A10BaseClass import A10BaseClass


class SystemBackup(A10BaseClass):
    
    """    :param file_handle: {"description": "full path of the uploaded file", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Backup system files.

    Class system-backup supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/file/system-backup`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "system-backup"
        self.a10_url="/axapi/v3/file/system-backup"
        self.DeviceProxy = ""
        self.file_handle = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


