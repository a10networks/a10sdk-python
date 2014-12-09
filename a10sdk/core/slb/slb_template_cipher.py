from a10sdk.common.A10BaseClass import A10BaseClass


class CipherCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param priority: {"description": "Cipher priority (Cipher priority (default 1))", "format": "number", "default": 1, "maximum": 100, "minimum": 1, "type": "number"}
    :param cipher_suite: {"enum": ["SSL3_RSA_DES_192_CBC3_SHA", "SSL3_RSA_DES_40_CBC_SHA", "SSL3_RSA_DES_64_CBC_SHA", "SSL3_RSA_RC4_128_MD5", "SSL3_RSA_RC4_128_SHA", "SSL3_RSA_RC4_40_MD5", "TLS1_RSA_AES_128_SHA", "TLS1_RSA_AES_256_SHA", "TLS1_RSA_EXPORT1024_RC4_56_MD5", "TLS1_RSA_EXPORT1024_RC4_56_SHA", "TLS1_RSA_AES_128_SHA256", "TLS1_RSA_AES_256_SHA256"], "type": "string", "description": "'SSL3_RSA_DES_192_CBC3_SHA': SSL3_RSA_DES_192_CBC3_SHA; 'SSL3_RSA_DES_40_CBC_SHA': SSL3_RSA_DES_40_CBC_SHA; 'SSL3_RSA_DES_64_CBC_SHA': SSL3_RSA_DES_64_CBC_SHA; 'SSL3_RSA_RC4_128_MD5': SSL3_RSA_RC4_128_MD5; 'SSL3_RSA_RC4_128_SHA': SSL3_RSA_RC4_128_SHA; 'SSL3_RSA_RC4_40_MD5': SSL3_RSA_RC4_40_MD5; 'TLS1_RSA_AES_128_SHA': TLS1_RSA_AES_128_SHA; 'TLS1_RSA_AES_256_SHA': TLS1_RSA_AES_256_SHA; 'TLS1_RSA_EXPORT1024_RC4_56_MD5': TLS1_RSA_EXPORT1024_RC4_56_MD5; 'TLS1_RSA_EXPORT1024_RC4_56_SHA': TLS1_RSA_EXPORT1024_RC4_56_SHA; 'TLS1_RSA_AES_128_SHA256': TLS1_RSA_AES_128_SHA256; 'TLS1_RSA_AES_256_SHA256': TLS1_RSA_AES_256_SHA256; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cipher-cfg"
        self.DeviceProxy = ""
        self.priority = ""
        self.cipher_suite = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Cipher(A10BaseClass):
    
    """Class Description::
    SSL Cipher Template.

    Class cipher supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Cipher Template Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param cipher_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"priority": {"description": "Cipher priority (Cipher priority (default 1))", "format": "number", "default": 1, "maximum": 100, "minimum": 1, "type": "number"}, "cipher-suite": {"enum": ["SSL3_RSA_DES_192_CBC3_SHA", "SSL3_RSA_DES_40_CBC_SHA", "SSL3_RSA_DES_64_CBC_SHA", "SSL3_RSA_RC4_128_MD5", "SSL3_RSA_RC4_128_SHA", "SSL3_RSA_RC4_40_MD5", "TLS1_RSA_AES_128_SHA", "TLS1_RSA_AES_256_SHA", "TLS1_RSA_EXPORT1024_RC4_56_MD5", "TLS1_RSA_EXPORT1024_RC4_56_SHA", "TLS1_RSA_AES_128_SHA256", "TLS1_RSA_AES_256_SHA256"], "type": "string", "description": "'SSL3_RSA_DES_192_CBC3_SHA': SSL3_RSA_DES_192_CBC3_SHA; 'SSL3_RSA_DES_40_CBC_SHA': SSL3_RSA_DES_40_CBC_SHA; 'SSL3_RSA_DES_64_CBC_SHA': SSL3_RSA_DES_64_CBC_SHA; 'SSL3_RSA_RC4_128_MD5': SSL3_RSA_RC4_128_MD5; 'SSL3_RSA_RC4_128_SHA': SSL3_RSA_RC4_128_SHA; 'SSL3_RSA_RC4_40_MD5': SSL3_RSA_RC4_40_MD5; 'TLS1_RSA_AES_128_SHA': TLS1_RSA_AES_128_SHA; 'TLS1_RSA_AES_256_SHA': TLS1_RSA_AES_256_SHA; 'TLS1_RSA_EXPORT1024_RC4_56_MD5': TLS1_RSA_EXPORT1024_RC4_56_MD5; 'TLS1_RSA_EXPORT1024_RC4_56_SHA': TLS1_RSA_EXPORT1024_RC4_56_SHA; 'TLS1_RSA_AES_128_SHA256': TLS1_RSA_AES_128_SHA256; 'TLS1_RSA_AES_256_SHA256': TLS1_RSA_AES_256_SHA256; ", "format": "enum"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/cipher/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "cipher"
        self.a10_url="/axapi/v3/slb/template/cipher/{name}"
        self.DeviceProxy = ""
        self.name = ""
        self.cipher_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


