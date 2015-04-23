from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "Requests-to-A10SAML", "Responses-from-A10SAML", "SP-metadata-export-req", "SP-metadata-export-success", "Login-auth-req", "Login-auth-resp", "ACS-req", "ACS-success", "ACS-authz-fail", "ACS-error", "SLO-req", "SLO-success", "SLO-error", "Other-error"], "type": "string", "description": "'all': all; 'Requests-to-A10SAML': Total Request to A10 SAML Service; 'Responses-from-A10SAML': Total Response from A10 SAML Service; 'SP-metadata-export-req': Total Metadata Export Request; 'SP-metadata-export-success': Toal Metadata Export Success; 'Login-auth-req': Total Login Authentication Request; 'Login-auth-resp': Total Login Authentication Response; 'ACS-req': Total SAML Single-Sign-On Request; 'ACS-success': Total SAML Single-Sign-On Success; 'ACS-authz-fail': Total SAML Single-Sign-On Authorization Fail; 'ACS-error': Total SAML Single-Sign-On Error; 'SLO-req': Total Single Logout Request; 'SLO-success': Total Single Logout Success; 'SLO-error': Total Single Logout Error; 'Other-error': Total Other Error; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "Requests-to-A10SAML", "Responses-from-A10SAML", "SP-metadata-export-req", "SP-metadata-export-success", "Login-auth-req", "Login-auth-resp", "ACS-req", "ACS-success", "ACS-authz-fail", "ACS-error", "SLO-req", "SLO-success", "SLO-error", "Other-error"], "type": "string", "description": "'all': all; 'Requests-to-A10SAML': Total Request to A10 SAML Service; 'Responses-from-A10SAML': Total Response from A10 SAML Service; 'SP-metadata-export-req': Total Metadata Export Request; 'SP-metadata-export-success': Toal Metadata Export Success; 'Login-auth-req': Total Login Authentication Request; 'Login-auth-resp': Total Login Authentication Response; 'ACS-req': Total SAML Single-Sign-On Request; 'ACS-success': Total SAML Single-Sign-On Success; 'ACS-authz-fail': Total SAML Single-Sign-On Authorization Fail; 'ACS-error': Total SAML Single-Sign-On Error; 'SLO-req': Total Single Logout Request; 'SLO-success': Total Single Logout Success; 'SLO-error': Total Single Logout Error; 'Other-error': Total Other Error; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Global SAML statistics.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/saml/global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/aam/authentication/saml/global"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


