from a10sdk.common.A10BaseClass import A10BaseClass


class SslKey(A10BaseClass):
    
    """    :param csr_generate: {"default": 0, "optional": true, "type": "number", "description": "Generate CSR file", "format": "flag"}
    :param dst_file: {"description": "destination file name for copy and rename action", "format": "string", "minLength": 1, "optional": true, "maxLength": 32, "type": "string"}
    :param file: {"description": "ssl key local file name", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param action: {"optional": true, "enum": ["create", "import", "export", "copy", "rename", "check", "replace", "delete"], "type": "string", "description": "'create': create; 'import': import; 'export': export; 'copy': copy; 'rename': rename; 'check': check; 'replace': replace; 'delete': delete; ", "format": "enum"}
    :param file_handle: {"description": "full path of the uploaded file", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param size: {"optional": true, "type": "number", "description": "ssl key file size in byte", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    ssl key file information and management commands.

    Class ssl-key supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/file/ssl-key`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ssl-key"
        self.a10_url="/axapi/v3/file/ssl-key"
        self.DeviceProxy = ""
        self.csr_generate = ""
        self.dst_file = ""
        self.A10WW_file = ""
        self.action = ""
        self.file_handle = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


