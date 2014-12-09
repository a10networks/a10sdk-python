from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Spn_krb_success: {"description": "SPN Kerberos Success", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param Spn_krb_request: {"description": "SPN Kerberos Request", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Spn_krb_faiure: {"description": "SPN Kerberos Failure", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Spn_krb_success = ""
        self.Spn_krb_request = ""
        self.Spn_krb_faiure = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Instance(A10BaseClass):
    
    """Class Description::
    Statistics for the object instance.

    Class instance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify HTTP-Authenticate logon name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/logon/http-authenticate/instance/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "instance"
        self.a10_url="/axapi/v3/aam/authentication/logon/http-authenticate/instance/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


