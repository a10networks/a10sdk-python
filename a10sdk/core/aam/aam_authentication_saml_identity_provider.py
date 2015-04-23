from a10sdk.common.A10BaseClass import A10BaseClass


class IdentityProvider(A10BaseClass):
    
    """Class Description::
    Authentication identity provider.

    Class identity-provider supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param name: {"description": "SAML authentication identity provider name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param metadata: {"description": "URL of SAML identity provider's metadata file", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/saml/identity-provider/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "identity-provider"
        self.a10_url="/axapi/v3/aam/authentication/saml/identity-provider/{name}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.name = ""
        self.metadata = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


