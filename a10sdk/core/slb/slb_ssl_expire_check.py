from a10sdk.common.A10BaseClass import A10BaseClass


class SslExpireCheck(A10BaseClass):
    
    """Class Description::
    SSL certificate expiration check.

    Class ssl-expire-check supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ssl_expire_email_address: {"description": "Config Email address for certificate expiration check", "format": "email-addr", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param interval_days: {"description": "The interval of days notice after expiration, default is 2", "format": "number", "default": 2, "optional": true, "maximum": 5, "minimum": 1, "type": "number"}
    :param expire_address1: {"description": "Email address for certificate expiration check", "format": "email-addr", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param before: {"description": "The number of days in advance notice before expiration, default is 5", "format": "number", "default": 5, "optional": true, "maximum": 60, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/ssl-expire-check`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ssl-expire-check"
        self.a10_url="/axapi/v3/slb/ssl-expire-check"
        self.DeviceProxy = ""
        self.exception = {}
        self.uuid = ""
        self.ssl_expire_email_address = ""
        self.interval_days = ""
        self.expire_address1 = ""
        self.before = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


