from a10sdk.common.A10BaseClass import A10BaseClass


class Crl(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param crl_sec: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Secondary CRL File Name or URL (http://www.example.com/ocsp) (only .der filetypes)", "format": "string-rlx"}
    :param crl_pri: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Primary CRL File Name or URL (http://www.example.com/ocsp) (only .der filetypes)", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "crl"
        self.DeviceProxy = ""
        self.crl_sec = ""
        self.crl_pri = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ocsp(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ocsp_pri: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Primary OCSP Authentication Server", "format": "string"}
    :param ocsp_sec: {"minLength": 1, "maxLength": 31, "type": "string", "description": "Secondary OCSP Authentication Server", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ocsp"
        self.DeviceProxy = ""
        self.ocsp_pri = ""
        self.ocsp_sec = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Revocation(A10BaseClass):
    
    """Class Description::
    IPsec VPN revocation settings.

    Class revocation supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ca: {"description": "Certificate Authority file name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param name: {"description": "Revocation name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vpn/revocation/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "revocation"
        self.a10_url="/axapi/v3/vpn/revocation/{name}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.ca = ""
        self.name = ""
        self.crl = {}
        self.ocsp = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


