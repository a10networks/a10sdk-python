from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "Request", "Success", "Failure"], "type": "string", "description": "'all': all; 'Request': Request; 'Success': Success; 'Failure': Failure; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class WsFederation(A10BaseClass):
    
    """Class Description::
    WS-Federation Authentication Relay.

    Class ws-federation supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param application_server: {"optional": true, "enum": ["sharepoint", "exchange-owa"], "type": "string", "description": "'sharepoint': Microsoft SharePoint; 'exchange-owa': Microsoft Exchange OWA; ", "format": "enum"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "Request", "Success", "Failure"], "type": "string", "description": "'all': all; 'Request': Request; 'Success': Success; 'Failure': Failure; ", "format": "enum"}}}]}
    :param authentication_uri: {"description": "Specify WS-Federation relay URI, default is /_trust/", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param name: {"description": "Specify WS-Federation authentication relay name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/ws-federation/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "ws-federation"
        self.a10_url="/axapi/v3/aam/authentication/relay/ws-federation/{name}"
        self.DeviceProxy = ""
        self.application_server = ""
        self.sampling_enable = []
        self.authentication_uri = ""
        self.name = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


