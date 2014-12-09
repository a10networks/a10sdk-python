from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Bind_failure: {"description": "User Bind Failure", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param Authorize_failure: {"description": "Authorization Failure", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param Admin_Bind_failure: {"description": "Admin Bind Failure", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param Authorize_success: {"description": "Authorization Success", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param Timeout_error: {"description": "Timeout", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param Request: {"description": "Request", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param Admin_Bind_success: {"description": "Admin Bind Success", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Search_success: {"description": "Search Success", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param Other_error: {"description": "Other Error", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param Bind_success: {"description": "User Bind Success", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param Search_failure: {"description": "Search Failure", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
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


class Instance(A10BaseClass):
    
    """Class Description::
    Statistics for the object instance.

    Class instance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify LDAP authentication server name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/ldap/instance/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "instance"
        self.a10_url="/axapi/v3/aam/authentication/server/ldap/instance/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


