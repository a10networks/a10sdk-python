from a10sdk.common.A10BaseClass import A10BaseClass


class RequireAssertionSigned(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param require_assertion_signed_enable: {"default": 0, "type": "number", "description": "Enable required signing of SAML assertion", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "require-assertion-signed"
        self.DeviceProxy = ""
        self.require_assertion_signed_enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SingleLogoutService(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param SLO_binding: {"enum": ["post", "redirect", "soap"], "type": "string", "description": "'post': POST binding of single logout service; 'redirect': Redirect binding of single logout service; 'soap': SOAP binding of single logout service; ", "format": "enum"}
    :param SLO_location: {"minLength": 1, "maxLength": 63, "type": "string", "description": "The location of name-id management service. (ex. /SAML/POST)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "single-logout-service"
        self.DeviceProxy = ""
        self.SLO_binding = ""
        self.SLO_location = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AssertionConsumingService(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param assertion_index: {"description": "The index of assertion consuming service", "minimum": 0, "type": "number", "maximum": 5, "format": "number"}
    :param assertion_binding: {"enum": ["artifact", "paos", "post"], "type": "string", "description": "'artifact': Artifact binding of assertion consuming service; 'paos': PAOS binding of assertion consuming service; 'post': POST binding of assertion consuming service; ", "format": "enum"}
    :param assertion_location: {"minLength": 1, "maxLength": 63, "type": "string", "description": "The location of assertion consuming service endpoint. (ex. /SAML/POST)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "assertion-consuming-service"
        self.DeviceProxy = ""
        self.assertion_index = ""
        self.assertion_binding = ""
        self.assertion_location = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SamlRequestSigned(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param saml_request_signed_disable: {"default": 0, "type": "number", "description": "Disable signing signature for SAML (Authn/Artifact Resolve) requests", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "saml-request-signed"
        self.DeviceProxy = ""
        self.saml_request_signed_disable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SoapTlsCertificateValidate(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param soap_tls_certificate_validate_disable: {"default": 0, "type": "number", "description": "Disable verification for server certificate in TLS session when resolving artificate", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "soap-tls-certificate-validate"
        self.DeviceProxy = ""
        self.soap_tls_certificate_validate_disable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ArtifactResolutionService(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param artifact_location: {"minLength": 1, "maxLength": 63, "type": "string", "description": "The location of artifact resolution service. (ex. /SAML/POST)", "format": "string-rlx"}
    :param artifact_binding: {"enum": ["soap"], "type": "string", "description": "'soap': SOAP binding of artifact resolution service; ", "format": "enum"}
    :param artifact_index: {"description": "The index of artifact resolution service", "minimum": 0, "type": "number", "maximum": 5, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "artifact-resolution-service"
        self.DeviceProxy = ""
        self.artifact_location = ""
        self.artifact_binding = ""
        self.artifact_index = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MetadataExportService(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param md_export_location: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify the URI to export SP metadata (Export URI. Default is /A10SP_Metadata)", "format": "string-rlx"}
    :param sign_xml: {"default": 0, "type": "number", "description": "Sign exported SP metadata XML with SP's certificate", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "metadata-export-service"
        self.DeviceProxy = ""
        self.md_export_location = ""
        self.sign_xml = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServiceProvider(A10BaseClass):
    
    """Class Description::
    Authentication service provider.

    Class service-provider supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify SAML authentication service provider name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param certificate: {"description": "SAML service provider certificate file", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param single_logout_service: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "SLO-binding": {"enum": ["post", "redirect", "soap"], "type": "string", "description": "'post': POST binding of single logout service; 'redirect': Redirect binding of single logout service; 'soap': SOAP binding of single logout service; ", "format": "enum"}, "SLO-location": {"minLength": 1, "maxLength": 63, "type": "string", "description": "The location of name-id management service. (ex. /SAML/POST)", "format": "string-rlx"}}}]}
    :param service_url: {"description": "SAML service provider service URL (ex. https://www.a10networks.com/saml.sso)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param entity_id: {"description": "SAML service provider entity ID", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param assertion_consuming_service: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "assertion-index": {"description": "The index of assertion consuming service", "minimum": 0, "type": "number", "maximum": 5, "format": "number"}, "assertion-binding": {"enum": ["artifact", "paos", "post"], "type": "string", "description": "'artifact': Artifact binding of assertion consuming service; 'paos': PAOS binding of assertion consuming service; 'post': POST binding of assertion consuming service; ", "format": "enum"}, "assertion-location": {"minLength": 1, "maxLength": 63, "type": "string", "description": "The location of assertion consuming service endpoint. (ex. /SAML/POST)", "format": "string-rlx"}}}]}
    :param artifact_resolution_service: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"artifact-location": {"minLength": 1, "maxLength": 63, "type": "string", "description": "The location of artifact resolution service. (ex. /SAML/POST)", "format": "string-rlx"}, "optional": true, "artifact-binding": {"enum": ["soap"], "type": "string", "description": "'soap': SOAP binding of artifact resolution service; ", "format": "enum"}, "artifact-index": {"description": "The index of artifact resolution service", "minimum": 0, "type": "number", "maximum": 5, "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/saml/service-provider/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "service-provider"
        self.a10_url="/axapi/v3/aam/authentication/saml/service-provider/{name}"
        self.DeviceProxy = ""
        self.name = ""
        self.certificate = ""
        self.require_assertion_signed = {}
        self.single_logout_service = []
        self.service_url = ""
        self.entity_id = ""
        self.assertion_consuming_service = []
        self.saml_request_signed = {}
        self.soap_tls_certificate_validate = {}
        self.artifact_resolution_service = []
        self.metadata_export_service = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


