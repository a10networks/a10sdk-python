from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Bind_failure: {"description": "Total User Bind Failure", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param Authorize_failure: {"description": "Total Authorization Failure", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param Admin_Bind_failure: {"description": "Total Admin Bind Failure", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param Authorize_success: {"description": "Total Authorization Success", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param Timeout_error: {"description": "Total Timeout", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param Request: {"description": "Total Request", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param Admin_Bind_success: {"description": "Total Admin Bind Success", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Search_success: {"description": "Total Search Success", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param Other_error: {"description": "Total Other Error", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param Bind_success: {"description": "Total User Bind Success", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param Search_failure: {"description": "Total Search Failure", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Bind_failure = ""
        self.Authorize_failure = ""
        self.Admin_Bind_failure = ""
        self.Authorize_success = ""
        self.Timeout_error = ""
        self.Request = ""
        self.Admin_Bind_success = ""
        self.Search_success = ""
        self.Other_error = ""
        self.Bind_success = ""
        self.Search_failure = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ldap(A10BaseClass):
    
    """Class Description::
    Statistics for the object ldap.

    Class ldap supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"stats": {"type": "object", "properties": {"Bind-failure": {"description": "User Bind Failure", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}, "Authorize-failure": {"description": "Authorization Failure", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}, "Admin-Bind-failure": {"description": "Admin Bind Failure", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}, "Authorize-success": {"description": "Authorization Success", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}, "Timeout-error": {"description": "Timeout", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}, "Request": {"description": "Request", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}, "Admin-Bind-success": {"description": "Admin Bind Success", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}, "Search-success": {"description": "Search Success", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}, "Other-error": {"description": "Other Error", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}, "Bind-success": {"description": "User Bind Success", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}, "Search-failure": {"description": "Search Failure", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}}}, "name": {"description": "Specify LDAP authentication server name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/server/ldap/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/ldap/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ldap"
        self.a10_url="/axapi/v3/aam/authentication/server/ldap/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


