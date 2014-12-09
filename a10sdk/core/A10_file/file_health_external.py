from a10sdk.common.A10BaseClass import A10BaseClass


class HealthExternal(A10BaseClass):
    
    """    :param dst_file: {"description": "destination file name for copy and rename action", "format": "string", "minLength": 1, "optional": true, "maxLength": 32, "type": "string"}
    :param description: {"description": "Describe the Program Function briefly", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param file: {"description": "Specify the Program Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param action: {"optional": true, "enum": ["create", "import", "export", "copy", "rename", "check", "replace", "delete"], "type": "string", "description": "'create': create; 'import': import; 'export': export; 'copy': copy; 'rename': rename; 'check': check; 'replace': replace; 'delete': delete; ", "format": "enum"}
    :param file_handle: {"description": "full path of the uploaded file", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param size: {"optional": true, "type": "number", "description": "syslog file size in byte", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Address the External Script Program.

    Class health-external supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/file/health-external`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "health-external"
        self.a10_url="/axapi/v3/file/health-external"
        self.DeviceProxy = ""
        self.dst_file = ""
        self.description = ""
        self.A10WW_file = ""
        self.action = ""
        self.file_handle = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


