from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Responses_from_A10SAML: {"description": "Total Response from A10 SAML Service", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param Login_auth_req: {"description": "Total Login Authentication Request", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param SLO_error: {"description": "Total Single Logout Error", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param SP_metadata_export_success: {"description": "Toal Metadata Export Success", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param SP_metadata_export_req: {"description": "Total Metadata Export Request", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param SLO_req: {"description": "Total Single Logout Request", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param Login_auth_resp: {"description": "Total Login Authentication Response", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param SLO_success: {"description": "Total Single Logout Success", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param ACS_success: {"description": "Total Assertion Consuming Service Success", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param ACS_error: {"description": "Total Assertion Consuming Service Error", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param Other_error: {"description": "Total Other Error", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param ACS_req: {"description": "Total Assertion Consuming Service Request", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param Requests_to_A10SAML: {"description": "Total Request to A10 SAML Service", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Responses_from_A10SAML = ""
        self.Login_auth_req = ""
        self.SLO_error = ""
        self.SP_metadata_export_success = ""
        self.SP_metadata_export_req = ""
        self.SLO_req = ""
        self.Login_auth_resp = ""
        self.SLO_success = ""
        self.ACS_success = ""
        self.ACS_error = ""
        self.Other_error = ""
        self.ACS_req = ""
        self.Requests_to_A10SAML = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """Class Description::
    Statistics for the object global.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/saml/global/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/aam/authentication/saml/global/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


