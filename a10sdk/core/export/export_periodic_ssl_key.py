from a10sdk.common.A10BaseClass import A10BaseClass


class SslKey(A10BaseClass):
    
    """Class Description::
    SSL Key File.

    Class ssl-key supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param ssl_key: {"description": "SSL Key File", "format": "string", "minLength": 1, "optional": false, "maxLength": 255, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/export-periodic/ssl-key/{ssl_key}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ssl_key"]

        self.b_key = "ssl-key"
        self.a10_url="/axapi/v3/export-periodic/ssl-key/{ssl_key}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.period = ""
        self.remote_file = ""
        self.use_mgmt_port = ""
        self.ssl_key = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


