from a10sdk.common.A10BaseClass import A10BaseClass


class SslCerts(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param status: {"type": "string", "format": "string"}
    :param name: {"type": "string", "format": "string"}
    :param notbefore: {"type": "string", "format": "string"}
    :param notafter: {"type": "string", "format": "string"}
    :param common_name: {"type": "string", "format": "string"}
    :param organization: {"type": "string", "format": "string"}
    :param serial: {"type": "string", "format": "string"}
    :param issuer: {"type": "string", "format": "string"}
    :param type: {"type": "string", "format": "string"}
    :param subject: {"type": "string", "format": "string"}
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

    :param ssl_certs: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"status": {"type": "string", "format": "string"}, "name": {"type": "string", "format": "string"}, "notbefore": {"type": "string", "format": "string"}, "optional": true, "notafter": {"type": "string", "format": "string"}, "common-name": {"type": "string", "format": "string"}, "organization": {"type": "string", "format": "string"}, "serial": {"type": "string", "format": "string"}, "issuer": {"type": "string", "format": "string"}, "type": {"type": "string", "format": "string"}, "subject": {"type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.ssl_certs = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SslCaCert(A10BaseClass):
    
    """Class Description::
    Operational Status for the object ssl-ca-cert.

    Class ssl-ca-cert supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/ssl-ca-cert/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ssl-ca-cert"
        self.a10_url="/axapi/v3/slb/ssl-ca-cert/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


