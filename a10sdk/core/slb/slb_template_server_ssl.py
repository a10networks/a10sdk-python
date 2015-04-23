from a10sdk.common.A10BaseClass import A10BaseClass


class EcList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ec: {"enum": ["secp256r1", "secp384r1"], "type": "string", "description": "'secp256r1': X9_62_prime256v1; 'secp384r1': secp384r1; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ec-list"
        self.DeviceProxy = ""
        self.ec = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CipherWithoutPrioList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cipher_wo_prio: {"not": "cipher-template", "enum": ["SSL3_RSA_DES_192_CBC3_SHA", "SSL3_RSA_DES_40_CBC_SHA", "SSL3_RSA_DES_64_CBC_SHA", "SSL3_RSA_RC4_128_MD5", "SSL3_RSA_RC4_128_SHA", "SSL3_RSA_RC4_40_MD5", "TLS1_RSA_AES_128_SHA", "TLS1_RSA_AES_256_SHA", "TLS1_RSA_EXPORT1024_RC4_56_MD5", "TLS1_RSA_EXPORT1024_RC4_56_SHA", "TLS1_RSA_AES_128_SHA256", "TLS1_RSA_AES_256_SHA256", "TLS1_DHE_RSA_AES_128_GCM_SHA256", "TLS1_DHE_RSA_AES_128_SHA", "TLS1_DHE_RSA_AES_128_SHA256", "TLS1_DHE_RSA_AES_256_GCM_SHA384", "TLS1_DHE_RSA_AES_256_SHA", "TLS1_DHE_RSA_AES_256_SHA256", "TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256", "TLS1_ECDHE_ECDSA_AES_128_SHA", "TLS1_ECDHE_ECDSA_AES_128_SHA256", "TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384", "TLS1_ECDHE_ECDSA_AES_256_SHA", "TLS1_ECDHE_RSA_AES_128_GCM_SHA256", "TLS1_ECDHE_RSA_AES_128_SHA", "TLS1_ECDHE_RSA_AES_128_SHA256", "TLS1_ECDHE_RSA_AES_256_GCM_SHA384", "TLS1_ECDHE_RSA_AES_256_SHA", "TLS1_RSA_AES_128_GCM_SHA256", "TLS1_RSA_AES_256_GCM_SHA384"], "type": "string", "description": "'SSL3_RSA_DES_192_CBC3_SHA': SSL3_RSA_DES_192_CBC3_SHA; 'SSL3_RSA_DES_40_CBC_SHA': SSL3_RSA_DES_40_CBC_SHA; 'SSL3_RSA_DES_64_CBC_SHA': SSL3_RSA_DES_64_CBC_SHA; 'SSL3_RSA_RC4_128_MD5': SSL3_RSA_RC4_128_MD5; 'SSL3_RSA_RC4_128_SHA': SSL3_RSA_RC4_128_SHA; 'SSL3_RSA_RC4_40_MD5': SSL3_RSA_RC4_40_MD5; 'TLS1_RSA_AES_128_SHA': TLS1_RSA_AES_128_SHA; 'TLS1_RSA_AES_256_SHA': TLS1_RSA_AES_256_SHA; 'TLS1_RSA_EXPORT1024_RC4_56_MD5': TLS1_RSA_EXPORT1024_RC4_56_MD5; 'TLS1_RSA_EXPORT1024_RC4_56_SHA': TLS1_RSA_EXPORT1024_RC4_56_SHA; 'TLS1_RSA_AES_128_SHA256': TLS1_RSA_AES_128_SHA256; 'TLS1_RSA_AES_256_SHA256': TLS1_RSA_AES_256_SHA256; 'TLS1_DHE_RSA_AES_128_GCM_SHA256': TLS1_DHE_RSA_AES_128_GCM_SHA256; 'TLS1_DHE_RSA_AES_128_SHA': TLS1_DHE_RSA_AES_128_SHA; 'TLS1_DHE_RSA_AES_128_SHA256': TLS1_DHE_RSA_AES_128_SHA256; 'TLS1_DHE_RSA_AES_256_GCM_SHA384': TLS1_DHE_RSA_AES_256_GCM_SHA384; 'TLS1_DHE_RSA_AES_256_SHA': TLS1_DHE_RSA_AES_256_SHA; 'TLS1_DHE_RSA_AES_256_SHA256': TLS1_DHE_RSA_AES_256_SHA256; 'TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256': TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256; 'TLS1_ECDHE_ECDSA_AES_128_SHA': TLS1_ECDHE_ECDSA_AES_128_SHA; 'TLS1_ECDHE_ECDSA_AES_128_SHA256': TLS1_ECDHE_ECDSA_AES_128_SHA256; 'TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384': TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_ECDSA_AES_256_SHA': TLS1_ECDHE_ECDSA_AES_256_SHA; 'TLS1_ECDHE_RSA_AES_128_GCM_SHA256': TLS1_ECDHE_RSA_AES_128_GCM_SHA256; 'TLS1_ECDHE_RSA_AES_128_SHA': TLS1_ECDHE_RSA_AES_128_SHA; 'TLS1_ECDHE_RSA_AES_128_SHA256': TLS1_ECDHE_RSA_AES_128_SHA256; 'TLS1_ECDHE_RSA_AES_256_GCM_SHA384': TLS1_ECDHE_RSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_RSA_AES_256_SHA': TLS1_ECDHE_RSA_AES_256_SHA; 'TLS1_RSA_AES_128_GCM_SHA256': TLS1_RSA_AES_128_GCM_SHA256; 'TLS1_RSA_AES_256_GCM_SHA384': TLS1_RSA_AES_256_GCM_SHA384; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cipher-without-prio-list"
        self.DeviceProxy = ""
        self.cipher_wo_prio = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServerCertificateError(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param error_type: {"enum": ["email", "ignore", "logging", "trap"], "type": "string", "description": "'email': Notify the error via email; 'ignore': Ignore the error, which mean the connection can continue; 'logging': Log the error; 'trap': Notify the error by SNMP trap; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "server-certificate-error"
        self.DeviceProxy = ""
        self.error_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CaCerts(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ca_cert: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Specify CA certificate", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ca-certs"
        self.DeviceProxy = ""
        self.ca_cert = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServerSsl(A10BaseClass):
    
    """Class Description::
    Server Side SSL Template.

    Class server-ssl supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param key: {"description": "Client private-key (Key Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param name: {"description": "Server SSL Template Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param session_cache_timeout: {"description": "Session Cache Timeout (Timeout value, in seconds)", "format": "number", "type": "number", "maximum": 7200, "minimum": 1, "optional": true}
    :param session_cache_size: {"description": "Session Cache Size (Specify 0 to disable Session ID reuse.)", "format": "number", "type": "number", "maximum": 128, "minimum": 0, "optional": true}
    :param encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param cipher_template: {"description": "Cipher Template (Cipher Config Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "not": "cipher-wo-prio", "type": "string", "$ref": "/axapi/v3/slb/template/cipher"}
    :param dh_type: {"optional": true, "enum": ["1024", "1024-dsa", "2048", "512"], "type": "string", "description": "'1024': 1024; '1024-dsa': 1024-dsa; '2048': 2048; '512': 512; ", "format": "enum"}
    :param cert: {"description": "Specify Client certificate (Certificate Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param version: {"description": "TLS/SSL version, default is TLS1.0 (TLS/SSL version: 30-SSLv3.0, 31-TLSv1.0, 32-TLSv1.1 and 33-TLSv1.2)", "format": "number", "type": "number", "maximum": 33, "minimum": 30, "optional": true}
    :param forward_proxy_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable SSL forward proxy", "format": "flag"}
    :param close_notify: {"default": 0, "optional": true, "type": "number", "description": "Send close notification when terminate connection", "format": "flag"}
    :param ec_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ec": {"enum": ["secp256r1", "secp384r1"], "type": "string", "description": "'secp256r1': X9_62_prime256v1; 'secp384r1': secp384r1; ", "format": "enum"}}}]}
    :param session_ticket_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable server side session ticket support", "format": "flag"}
    :param cipher_without_prio_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cipher-wo-prio": {"not": "cipher-template", "enum": ["SSL3_RSA_DES_192_CBC3_SHA", "SSL3_RSA_DES_40_CBC_SHA", "SSL3_RSA_DES_64_CBC_SHA", "SSL3_RSA_RC4_128_MD5", "SSL3_RSA_RC4_128_SHA", "SSL3_RSA_RC4_40_MD5", "TLS1_RSA_AES_128_SHA", "TLS1_RSA_AES_256_SHA", "TLS1_RSA_EXPORT1024_RC4_56_MD5", "TLS1_RSA_EXPORT1024_RC4_56_SHA", "TLS1_RSA_AES_128_SHA256", "TLS1_RSA_AES_256_SHA256", "TLS1_DHE_RSA_AES_128_GCM_SHA256", "TLS1_DHE_RSA_AES_128_SHA", "TLS1_DHE_RSA_AES_128_SHA256", "TLS1_DHE_RSA_AES_256_GCM_SHA384", "TLS1_DHE_RSA_AES_256_SHA", "TLS1_DHE_RSA_AES_256_SHA256", "TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256", "TLS1_ECDHE_ECDSA_AES_128_SHA", "TLS1_ECDHE_ECDSA_AES_128_SHA256", "TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384", "TLS1_ECDHE_ECDSA_AES_256_SHA", "TLS1_ECDHE_RSA_AES_128_GCM_SHA256", "TLS1_ECDHE_RSA_AES_128_SHA", "TLS1_ECDHE_RSA_AES_128_SHA256", "TLS1_ECDHE_RSA_AES_256_GCM_SHA384", "TLS1_ECDHE_RSA_AES_256_SHA", "TLS1_RSA_AES_128_GCM_SHA256", "TLS1_RSA_AES_256_GCM_SHA384"], "type": "string", "description": "'SSL3_RSA_DES_192_CBC3_SHA': SSL3_RSA_DES_192_CBC3_SHA; 'SSL3_RSA_DES_40_CBC_SHA': SSL3_RSA_DES_40_CBC_SHA; 'SSL3_RSA_DES_64_CBC_SHA': SSL3_RSA_DES_64_CBC_SHA; 'SSL3_RSA_RC4_128_MD5': SSL3_RSA_RC4_128_MD5; 'SSL3_RSA_RC4_128_SHA': SSL3_RSA_RC4_128_SHA; 'SSL3_RSA_RC4_40_MD5': SSL3_RSA_RC4_40_MD5; 'TLS1_RSA_AES_128_SHA': TLS1_RSA_AES_128_SHA; 'TLS1_RSA_AES_256_SHA': TLS1_RSA_AES_256_SHA; 'TLS1_RSA_EXPORT1024_RC4_56_MD5': TLS1_RSA_EXPORT1024_RC4_56_MD5; 'TLS1_RSA_EXPORT1024_RC4_56_SHA': TLS1_RSA_EXPORT1024_RC4_56_SHA; 'TLS1_RSA_AES_128_SHA256': TLS1_RSA_AES_128_SHA256; 'TLS1_RSA_AES_256_SHA256': TLS1_RSA_AES_256_SHA256; 'TLS1_DHE_RSA_AES_128_GCM_SHA256': TLS1_DHE_RSA_AES_128_GCM_SHA256; 'TLS1_DHE_RSA_AES_128_SHA': TLS1_DHE_RSA_AES_128_SHA; 'TLS1_DHE_RSA_AES_128_SHA256': TLS1_DHE_RSA_AES_128_SHA256; 'TLS1_DHE_RSA_AES_256_GCM_SHA384': TLS1_DHE_RSA_AES_256_GCM_SHA384; 'TLS1_DHE_RSA_AES_256_SHA': TLS1_DHE_RSA_AES_256_SHA; 'TLS1_DHE_RSA_AES_256_SHA256': TLS1_DHE_RSA_AES_256_SHA256; 'TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256': TLS1_ECDHE_ECDSA_AES_128_GCM_SHA256; 'TLS1_ECDHE_ECDSA_AES_128_SHA': TLS1_ECDHE_ECDSA_AES_128_SHA; 'TLS1_ECDHE_ECDSA_AES_128_SHA256': TLS1_ECDHE_ECDSA_AES_128_SHA256; 'TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384': TLS1_ECDHE_ECDSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_ECDSA_AES_256_SHA': TLS1_ECDHE_ECDSA_AES_256_SHA; 'TLS1_ECDHE_RSA_AES_128_GCM_SHA256': TLS1_ECDHE_RSA_AES_128_GCM_SHA256; 'TLS1_ECDHE_RSA_AES_128_SHA': TLS1_ECDHE_RSA_AES_128_SHA; 'TLS1_ECDHE_RSA_AES_128_SHA256': TLS1_ECDHE_RSA_AES_128_SHA256; 'TLS1_ECDHE_RSA_AES_256_GCM_SHA384': TLS1_ECDHE_RSA_AES_256_GCM_SHA384; 'TLS1_ECDHE_RSA_AES_256_SHA': TLS1_ECDHE_RSA_AES_256_SHA; 'TLS1_RSA_AES_128_GCM_SHA256': TLS1_RSA_AES_128_GCM_SHA256; 'TLS1_RSA_AES_256_GCM_SHA384': TLS1_RSA_AES_256_GCM_SHA384; ", "format": "enum"}, "optional": true}}]}
    :param passphrase: {"description": "Password Phrase", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param server_certificate_error: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"error-type": {"enum": ["email", "ignore", "logging", "trap"], "type": "string", "description": "'email': Notify the error via email; 'ignore': Ignore the error, which mean the connection can continue; 'logging': Log the error; 'trap': Notify the error by SNMP trap; ", "format": "enum"}, "optional": true}}]}
    :param ca_certs: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ca-cert": {"minLength": 1, "maxLength": 255, "type": "string", "description": "Specify CA certificate", "format": "string"}, "optional": true}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/server-ssl/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "server-ssl"
        self.a10_url="/axapi/v3/slb/template/server-ssl/{name}"
        self.DeviceProxy = ""
        self.key = ""
        self.name = ""
        self.session_cache_timeout = ""
        self.session_cache_size = ""
        self.encrypted = ""
        self.cipher_template = ""
        self.dh_type = ""
        self.cert = ""
        self.version = ""
        self.forward_proxy_enable = ""
        self.close_notify = ""
        self.ec_list = []
        self.session_ticket_enable = ""
        self.cipher_without_prio_list = []
        self.passphrase = ""
        self.server_certificate_error = []
        self.ca_certs = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


