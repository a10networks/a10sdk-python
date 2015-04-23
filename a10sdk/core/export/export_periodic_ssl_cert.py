from a10sdk.common.A10BaseClass import A10BaseClass


class SslCert(A10BaseClass):
    
    """Class Description::
    SSL Cert File.

    Class ssl-cert supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ssl_cert: {"description": "SSL Cert File", "format": "string", "minLength": 1, "optional": false, "maxLength": 255, "type": "string"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/export-periodic/ssl-cert/{ssl_cert}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "ssl_cert"]

        self.b_key = "ssl-cert"
        self.a10_url="/axapi/v3/export-periodic/ssl-cert/{ssl_cert}"
        self.DeviceProxy = ""
        self.remote_file = ""
        self.uuid = ""
        self.ssl_cert = ""
        self.use_mgmt_port = ""
        self.period = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


