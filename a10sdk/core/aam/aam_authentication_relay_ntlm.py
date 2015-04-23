from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "Success", "Failure", "Request", "Response", "Http-code-200", "Http-code-400", "Http-code-401", "Http-code-403", "Http-code-404", "Http-code-500", "Http-code-503", "Http-code-other", "Buffer-alloc-fail", "Encoding-fail", "Insert-header-fail", "Parse-header-fail", "Internal-error"], "type": "string", "description": "'all': all; 'Success': Success; 'Failure': Failure; 'Request': Request; 'Response': Response; 'Http-code-200': HTTP 200 OK; 'Http-code-400': HTTP 400 Bad Request; 'Http-code-401': HTTP 401 Unauthorized; 'Http-code-403': HTTP 403 Forbidden; 'Http-code-404': HTTP 404 Not Found; 'Http-code-500': HTTP 500 Internal Server Error; 'Http-code-503': HTTP 503 Service Unavailable; 'Http-code-other': Other HTTP Response; 'Buffer-alloc-fail': Buffer Allocation Failure; 'Encoding-fail': Encoding Failure; 'Insert-header-fail': Insert Header Failure; 'Parse-header-fail': Parse Header Failure; 'Internal-error': Internal Error; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ntlm(A10BaseClass):
    
    """Class Description::
    NTLM Authentication Relay.

    Class ntlm supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param domain: {"description": "Specify NTLM domain, default is null", "format": "string", "minLength": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param version: {"description": "Specify NTLM version, default is NTLM 2", "format": "number", "default": 2, "optional": true, "maximum": 2, "minimum": 1, "type": "number"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "Success", "Failure", "Request", "Response", "Http-code-200", "Http-code-400", "Http-code-401", "Http-code-403", "Http-code-404", "Http-code-500", "Http-code-503", "Http-code-other", "Buffer-alloc-fail", "Encoding-fail", "Insert-header-fail", "Parse-header-fail", "Internal-error"], "type": "string", "description": "'all': all; 'Success': Success; 'Failure': Failure; 'Request': Request; 'Response': Response; 'Http-code-200': HTTP 200 OK; 'Http-code-400': HTTP 400 Bad Request; 'Http-code-401': HTTP 401 Unauthorized; 'Http-code-403': HTTP 403 Forbidden; 'Http-code-404': HTTP 404 Not Found; 'Http-code-500': HTTP 500 Internal Server Error; 'Http-code-503': HTTP 503 Service Unavailable; 'Http-code-other': Other HTTP Response; 'Buffer-alloc-fail': Buffer Allocation Failure; 'Encoding-fail': Encoding Failure; 'Insert-header-fail': Insert Header Failure; 'Parse-header-fail': Parse Header Failure; 'Internal-error': Internal Error; ", "format": "enum"}}}]}
    :param name: {"description": "Specify NTLM authentication relay name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/ntlm/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "ntlm"
        self.a10_url="/axapi/v3/aam/authentication/relay/ntlm/{name}"
        self.DeviceProxy = ""
        self.domain = ""
        self.version = ""
        self.sampling_enable = []
        self.name = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


