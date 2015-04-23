from a10sdk.common.A10BaseClass import A10BaseClass


class Relay(A10BaseClass):
    
    """    :param ws_federation_list: {"minItems": 1, "items": {"type": "ws-federation"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"application-server": {"optional": true, "enum": ["sharepoint", "exchange-owa"], "type": "string", "description": "'sharepoint': Microsoft SharePoint; 'exchange-owa': Microsoft Exchange OWA; ", "format": "enum"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "Request", "Success", "Failure"], "type": "string", "description": "'all': all; 'Request': Request; 'Success': Success; 'Failure': Failure; ", "format": "enum"}}}]}, "authentication-uri": {"description": "Specify WS-Federation relay URI, default is /_trust/", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "name": {"description": "Specify WS-Federation authentication relay name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/relay/ws-federation/{name}"}
    :param ntlm_list: {"minItems": 1, "items": {"type": "ntlm"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"domain": {"description": "Specify NTLM domain, default is null", "format": "string", "minLength": 1, "optional": true, "maxLength": 64, "type": "string"}, "version": {"description": "Specify NTLM version, default is NTLM 2", "format": "number", "default": 2, "optional": true, "maximum": 2, "minimum": 1, "type": "number"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "Success", "Failure", "Request", "Response", "Http-code-200", "Http-code-400", "Http-code-401", "Http-code-403", "Http-code-404", "Http-code-500", "Http-code-503", "Http-code-other", "Buffer-alloc-fail", "Encoding-fail", "Insert-header-fail", "Parse-header-fail", "Internal-error"], "type": "string", "description": "'all': all; 'Success': Success; 'Failure': Failure; 'Request': Request; 'Response': Response; 'Http-code-200': HTTP 200 OK; 'Http-code-400': HTTP 400 Bad Request; 'Http-code-401': HTTP 401 Unauthorized; 'Http-code-403': HTTP 403 Forbidden; 'Http-code-404': HTTP 404 Not Found; 'Http-code-500': HTTP 500 Internal Server Error; 'Http-code-503': HTTP 503 Service Unavailable; 'Http-code-other': Other HTTP Response; 'Buffer-alloc-fail': Buffer Allocation Failure; 'Encoding-fail': Encoding Failure; 'Insert-header-fail': Insert Header Failure; 'Parse-header-fail': Parse Header Failure; 'Internal-error': Internal Error; ", "format": "enum"}}}]}, "name": {"description": "Specify NTLM authentication relay name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/relay/ntlm/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Authentication relay configuration.

    Class relay supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "relay"
        self.a10_url="/axapi/v3/aam/authentication/relay"
        self.DeviceProxy = ""
        self.ws_federation_list = []
        self.ntlm_list = []
        self.form_based = {}
        self.kerberos = {}
        self.http_basic = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


