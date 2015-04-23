from a10sdk.common.A10BaseClass import A10BaseClass


class RemoteCaCert(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param remote_cert_name: {"minLength": 1, "maxLength": 127, "type": "string", "description": "CA Certificate DN", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "remote-ca-cert"
        self.DeviceProxy = ""
        self.remote_cert_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LocalAddress(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param local_ip: {"type": "string", "description": "Ipv4 address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "local-address"
        self.DeviceProxy = ""
        self.local_ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Vrid(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param default: {"default": 0, "not": "vrid-num", "type": "number", "description": "Default VRRP-A vrid", "format": "flag"}
    :param vrid_num: {"description": "Specify ha VRRP-A vrid", "format": "number", "maximum": 31, "minimum": 1, "not": "default", "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "vrid"
        self.DeviceProxy = ""
        self.default = ""
        self.vrid_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LocalCert(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param local_cert_name: {"minLength": 1, "maxLength": 64, "type": "string", "description": "Certificate File Name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "local-cert"
        self.DeviceProxy = ""
        self.local_cert_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Dpd(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param interval: {"description": "Interval time in seconds", "minimum": 0, "type": "number", "maximum": 10, "format": "number"}
    :param retry: {"description": "Retry times", "minimum": 1, "type": "number", "maximum": 10, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "dpd"
        self.DeviceProxy = ""
        self.interval = ""
        self.retry = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Key(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param key_passphrase: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Private Key Pass Phrase", "format": "string"}
    :param key_name: {"minLength": 1, "maxLength": 64, "type": "string", "description": "Private Key File Name", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "key"
        self.DeviceProxy = ""
        self.key_passphrase = ""
        self.key_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RemoteAddress(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param remote_ip: {"not": "dns", "type": "string", "description": "Ipv4 address", "format": "ipv4-address"}
    :param dns: {"description": "Remote IP based on Domain name", "format": "string", "minLength": 1, "maxLength": 128, "not": "remote-ip", "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "remote-address"
        self.DeviceProxy = ""
        self.remote_ip = ""
        self.dns = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EncCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param priority: {"description": "Prioritizes (1-10) security protocol, least value has highest priority", "format": "number", "default": 5, "maximum": 10, "minimum": 1, "type": "number"}
    :param encryption: {"enum": ["des", "3des", "aes-128", "aes-192", "aes-256", "null"], "type": "string", "description": "'des': Data Encryption Standard algorithm; '3des': Triple Data Encryption Standard algorithm; 'aes-128': Advanced Encryption Standard algorithm (key size: 128 bits); 'aes-192': Advanced Encryption Standard algorithm (key size: 192 bits); 'aes-256': Advanced Encryption Standard algorithm (key size: 256 bits); 'null': No encryption algorithm; ", "format": "enum"}
    :param hash: {"enum": ["md5", "sha1", "sha256", "null"], "type": "string", "description": "'md5': MD5 Dessage-Digest Algorithm; 'sha1': Secure Hash Algorithm 1; 'sha256': Secure Hash Algorithm 256; 'null': No hash algorithm; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "enc-cfg"
        self.DeviceProxy = ""
        self.priority = ""
        self.encryption = ""
        self.A10WW_hash = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AuthMethod(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param preshare_key: {"description": "Authenticate the remote gateway using a pre-shared key", "format": "string", "minLength": 1, "maxLength": 127, "not": "rsa-signature", "type": "string"}
    :param rsa_signature: {"default": 0, "not": "preshare-key", "type": "number", "description": "Authenticate the remote gateway using an RSA certificate", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "auth-method"
        self.DeviceProxy = ""
        self.preshare_key = ""
        self.rsa_signature = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IkeGateway(A10BaseClass):
    
    """Class Description::
    IKE-gateway settings.

    Class ike-gateway supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "IKE-gateway name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param dh_group: {"optional": true, "enum": ["1", "2", "5", "14", "15", "16", "18"], "type": "string", "description": "'1': Diffie-Hellman group 1 (Default); '2': Diffie-Hellman group 2; '5': Diffie-Hellman group 5; '14': Diffie-Hellman group 14; '15': Diffie-Hellman group 15; '16': Diffie-Hellman group 16; '18': Diffie-Hellman group 18; ", "format": "enum"}
    :param nat_traversal: {"default": 0, "optional": true, "type": "number", "format": "flag"}
    :param ike_version: {"optional": true, "enum": ["v1", "v2"], "type": "string", "description": "'v1': IKEv1 key exchange; 'v2': IKEv2 key exchange; ", "format": "enum"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param mode: {"optional": true, "enum": ["main", "aggressive"], "type": "string", "description": "'main': Negotiate Main mode (Default); 'aggressive': Negotiate Aggressive mode; ", "format": "enum"}
    :param lifetime: {"description": "IKE SA age in seconds", "format": "number", "default": 86400, "optional": true, "maximum": 86400, "minimum": 300, "type": "number"}
    :param remote_id: {"description": "Remote Gateway Identity", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param local_id: {"description": "Local Gateway Identity", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param enc_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"priority": {"description": "Prioritizes (1-10) security protocol, least value has highest priority", "format": "number", "default": 5, "maximum": 10, "minimum": 1, "type": "number"}, "encryption": {"enum": ["des", "3des", "aes-128", "aes-192", "aes-256", "null"], "type": "string", "description": "'des': Data Encryption Standard algorithm; '3des': Triple Data Encryption Standard algorithm; 'aes-128': Advanced Encryption Standard algorithm (key size: 128 bits); 'aes-192': Advanced Encryption Standard algorithm (key size: 192 bits); 'aes-256': Advanced Encryption Standard algorithm (key size: 256 bits); 'null': No encryption algorithm; ", "format": "enum"}, "hash": {"enum": ["md5", "sha1", "sha256", "null"], "type": "string", "description": "'md5': MD5 Dessage-Digest Algorithm; 'sha1': Secure Hash Algorithm 1; 'sha256': Secure Hash Algorithm 256; 'null': No hash algorithm; ", "format": "enum"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vpn/ike-gateway/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "ike-gateway"
        self.a10_url="/axapi/v3/vpn/ike-gateway/{name}"
        self.DeviceProxy = ""
        self.remote_ca_cert = {}
        self.local_address = {}
        self.name = ""
        self.dh_group = ""
        self.nat_traversal = ""
        self.vrid = {}
        self.ike_version = ""
        self.uuid = ""
        self.local_cert = {}
        self.dpd = {}
        self.mode = ""
        self.key = {}
        self.lifetime = ""
        self.remote_address = {}
        self.remote_id = ""
        self.local_id = ""
        self.enc_cfg = []
        self.auth_method = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


