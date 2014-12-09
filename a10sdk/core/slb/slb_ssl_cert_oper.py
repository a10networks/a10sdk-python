from a10sdk.common.A10BaseClass import A10BaseClass


class SslCerts(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param status: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param name: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param notbefore: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param notafter: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param common_name: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param organization: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param serial: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param issuer: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param type: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param subject: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ssl-certs"
        self.DeviceProxy = ""
        self.status = ""
        self.name = ""
        self.notbefore = ""
        self.notafter = ""
        self.common_name = ""
        self.organization = ""
        self.serial = ""
        self.issuer = ""
        self.A10WW_type = ""
        self.subject = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ssl_certs: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"status": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "name": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "notbefore": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "optional": true, "notafter": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "common-name": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "organization": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "serial": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "issuer": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "type": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "subject": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.ssl_certs = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SslCert(A10BaseClass):
    
    """Class Description::
    Operational Status for the object ssl-cert.

    Class ssl-cert supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/ssl-cert/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ssl-cert"
        self.a10_url="/axapi/v3/slb/ssl-cert/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


