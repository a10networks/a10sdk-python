from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Login_auth_req: {"description": "Login Authentication Request", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param SLO_error: {"description": "Single Logout Error", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param SP_metadata_export_success: {"description": "Metadata Export Success", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param SLO_req: {"description": "Single Logout Request", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param Login_auth_resp: {"description": "Login Authentication Response", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param SLO_success: {"description": "Single Logout Success", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param ACS_success: {"description": "Assertion Consuming Service Success", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param ACS_error: {"description": "Assertion Consuming Service Error", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param Other_error: {"description": "Other Error", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param ACS_req: {"description": "Assertion Consuming Service Request", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param SP_metadata_export_req: {"description": "Metadata Export Request", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Login_auth_req = ""
        self.SLO_error = ""
        self.SP_metadata_export_success = ""
        self.SLO_req = ""
        self.Login_auth_resp = ""
        self.SLO_success = ""
        self.ACS_success = ""
        self.ACS_error = ""
        self.Other_error = ""
        self.ACS_req = ""
        self.SP_metadata_export_req = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServiceProvider(A10BaseClass):
    
    """Class Description::
    Statistics for the object service-provider.

    Class service-provider supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify SAML authentication service provider name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/saml/service-provider/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "service-provider"
        self.a10_url="/axapi/v3/aam/authentication/saml/service-provider/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


