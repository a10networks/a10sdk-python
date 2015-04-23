from a10sdk.common.A10BaseClass import A10BaseClass


class AuthSamlIdp(A10BaseClass):
    
    """    :param dst_file: {"description": "Destination file name for copy and rename action", "format": "string", "minLength": 1, "optional": true, "maxLength": 32, "type": "string"}
    :param file: {"description": "SAML metadata local file name", "format": "string", "minLength": 1, "optional": true, "maxLength": 32, "type": "string"}
    :param verify_xml_signature: {"default": 0, "optional": true, "type": "number", "description": "Verify metadata's XML signature", "format": "flag"}
    :param action: {"optional": true, "enum": ["create", "import", "export", "copy", "rename", "check", "replace", "delete"], "type": "string", "description": "'create': create; 'import': import; 'export': export; 'copy': copy; 'rename': rename; 'check': check; 'replace': replace; 'delete': delete; ", "format": "enum"}
    :param file_handle: {"description": "Full path of the uploaded file", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param size: {"description": "SAML metadata file size in byte", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    SAML metadata file information and management commands.

    Class auth-saml-idp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/file/auth-saml-idp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "auth-saml-idp"
        self.a10_url="/axapi/v3/file/auth-saml-idp"
        self.DeviceProxy = ""
        self.dst_file = ""
        self.A10WW_file = ""
        self.verify_xml_signature = ""
        self.action = ""
        self.file_handle = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


