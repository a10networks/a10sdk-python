from a10sdk.common.A10BaseClass import A10BaseClass


class SslSid(A10BaseClass):
    
    """Class Description::
    SSL session ID  persistence.

    Class ssl-sid supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param dont_honor_conn_rules: {"default": 0, "optional": true, "type": "number", "description": "Do not observe connection rate rules", "format": "flag"}
    :param name: {"description": "SSL session ID persistence template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param timeout: {"description": "Persistence timeout (in minutes)", "format": "number", "type": "number", "maximum": 2000, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/persist/ssl-sid/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "ssl-sid"
        self.a10_url="/axapi/v3/slb/template/persist/ssl-sid/{name}"
        self.DeviceProxy = ""
        self.dont_honor_conn_rules = ""
        self.name = ""
        self.timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


