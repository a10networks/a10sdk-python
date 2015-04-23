from a10sdk.common.A10BaseClass import A10BaseClass


class Saml(A10BaseClass):
    
    """    :param service_provider_list: {"minItems": 1, "items": {"type": "service-provider"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"name": {"description": "Specify SAML authentication service provider name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "certificate": {"description": "SAML service provider certificate file (PFX format is required.)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "require-assertion-signed": {"type": "object", "properties": {"require-assertion-signed-enable": {"default": 0, "type": "number", "description": "Enable required signing of SAML assertion", "format": "flag"}}}, "single-logout-service": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "SLO-binding": {"enum": ["post", "redirect", "soap"], "type": "string", "description": "'post': POST binding of single logout service; 'redirect': Redirect binding of single logout service; 'soap': SOAP binding of single logout service; ", "format": "enum"}, "SLO-location": {"minLength": 1, "maxLength": 63, "type": "string", "description": "The location of name-id management service. (ex. /SAML/POST)", "format": "string-rlx"}}}]}, "service-url": {"description": "SAML service provider service URL (ex. https://www.a10networks.com/saml.sso)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "entity-id": {"description": "SAML service provider entity ID", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "assertion-consuming-service": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "assertion-index": {"description": "The index of assertion consuming service", "minimum": 0, "type": "number", "maximum": 5, "format": "number"}, "assertion-binding": {"enum": ["artifact", "paos", "post"], "type": "string", "description": "'artifact': Artifact binding of assertion consuming service; 'paos': PAOS binding of assertion consuming service; 'post': POST binding of assertion consuming service; ", "format": "enum"}, "assertion-location": {"minLength": 1, "maxLength": 63, "type": "string", "description": "The location of assertion consuming service endpoint. (ex. /SAML/POST)", "format": "string-rlx"}}}]}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "SP-metadata-export-req", "SP-metadata-export-success", "Login-auth-req", "Login-auth-resp", "ACS-req", "ACS-success", "ACS-authz-fail", "ACS-error", "SLO-req", "SLO-success", "SLO-error", "Other-error"], "type": "string", "description": "'all': all; 'SP-metadata-export-req': Metadata Export Request; 'SP-metadata-export-success': Metadata Export Success; 'Login-auth-req': Login Authentication Request; 'Login-auth-resp': Login Authentication Response; 'ACS-req': SAML Single-Sign-On Request; 'ACS-success': SAML Single-Sign-On Success; 'ACS-authz-fail': SAML Single-Sign-On Authorization Fail; 'ACS-error': SAML Single-Sign-On Error; 'SLO-req': Single Logout Request; 'SLO-success': Single Logout Success; 'SLO-error': Single Logout Error; 'Other-error': Other Error; ", "format": "enum"}}}]}, "saml-request-signed": {"type": "object", "properties": {"saml-request-signed-disable": {"default": 0, "type": "number", "description": "Disable signing signature for SAML (Authn/Artifact Resolve) requests", "format": "flag"}}}, "adfs-ws-federation": {"type": "object", "properties": {"ws-federation-enable": {"default": 0, "type": "number", "description": "Enable ADFS WS-Federation", "format": "flag"}}}, "soap-tls-certificate-validate": {"type": "object", "properties": {"soap-tls-certificate-validate-disable": {"default": 0, "type": "number", "description": "Disable verification for server certificate in TLS session when resolving artificate", "format": "flag"}}}, "artifact-resolution-service": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"artifact-location": {"minLength": 1, "maxLength": 63, "type": "string", "description": "The location of artifact resolution service. (ex. /SAML/POST)", "format": "string-rlx"}, "optional": true, "artifact-binding": {"enum": ["soap"], "type": "string", "description": "'soap': SOAP binding of artifact resolution service; ", "format": "enum"}, "artifact-index": {"description": "The index of artifact resolution service", "minimum": 0, "type": "number", "maximum": 5, "format": "number"}}}]}, "metadata-export-service": {"type": "object", "properties": {"md-export-location": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify the URI to export SP metadata (Export URI. Default is /A10SP_Metadata)", "format": "string-rlx"}, "sign-xml": {"default": 0, "type": "number", "description": "Sign exported SP metadata XML with SP's certificate", "format": "flag"}}}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/saml/service-provider/{name}"}
    :param identity_provider_list: {"minItems": 1, "items": {"type": "identity-provider"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "name": {"description": "SAML authentication identity provider name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "metadata": {"description": "URL of SAML identity provider's metadata file", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/saml/identity-provider/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure SAML related settings.

    Class saml supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/saml`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "saml"
        self.a10_url="/axapi/v3/aam/authentication/saml"
        self.DeviceProxy = ""
        self.A10WW_global = {}
        self.service_provider_list = []
        self.identity_provider_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


