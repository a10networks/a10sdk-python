from a10sdk.common.A10BaseClass import A10BaseClass


class SslException(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param exception_cert: {"type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ssl-exception"
        self.DeviceProxy = ""
        self.exception_cert = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param email_address2: {"type": "string", "format": "string"}
    :param email_address: {"type": "string", "format": "string"}
    :param interval: {"type": "number", "format": "number"}
    :param ssl_exception: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "exception-cert": {"type": "string", "format": "string"}}}]}
    :param before: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.email_address2 = ""
        self.email_address = ""
        self.interval = ""
        self.ssl_exception = []
        self.before = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SslCertExpireCheck(A10BaseClass):
    
    """Class Description::
    Operational Status for the object ssl-cert-expire-check.

    Class ssl-cert-expire-check supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/ssl-cert-expire-check/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ssl-cert-expire-check"
        self.a10_url="/axapi/v3/slb/ssl-cert-expire-check/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


