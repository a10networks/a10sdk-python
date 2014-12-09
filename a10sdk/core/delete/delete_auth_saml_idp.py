from a10sdk.common.A10BaseClass import A10BaseClass


class AuthSamlIdp(A10BaseClass):
    
    """    :param saml_idp_name: {"description": "Local IDP metadata name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    SAML metadata of identity provider.

    Class auth-saml-idp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/delete/auth-saml-idp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "auth-saml-idp"
        self.a10_url="/axapi/v3/delete/auth-saml-idp"
        self.DeviceProxy = ""
        self.saml_idp_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


