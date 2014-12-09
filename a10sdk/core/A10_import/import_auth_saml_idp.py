from a10sdk.common.A10BaseClass import A10BaseClass


class AuthSamlIdp(A10BaseClass):
    
    """    :param remote_file: {"optional": true, "type": "string", "description": "Profile name for remote url", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param verify_xml_signature: {"default": 0, "optional": true, "type": "number", "description": "Verify metadata's XML signature", "format": "flag"}
    :param saml_idp_name: {"description": "Metadata name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param overwrite: {"default": 0, "optional": true, "type": "number", "description": "Overwrite existing file", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    SAML metadata of identity provider.

    Class auth-saml-idp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/import/auth-saml-idp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "auth-saml-idp"
        self.a10_url="/axapi/v3/import/auth-saml-idp"
        self.DeviceProxy = ""
        self.remote_file = ""
        self.use_mgmt_port = ""
        self.verify_xml_signature = ""
        self.saml_idp_name = ""
        self.overwrite = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


