from a10sdk.common.A10BaseClass import A10BaseClass


class Bind(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param tunnel: {"description": "Tunnel interface index", "format": "number", "maximum": 128, "minimum": 1, "type": "number", "$ref": "/axapi/v3/interface/tunnel"}
    :param next_hop: {"type": "string", "description": "IPsec Next Hop IP Address", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "bind"
        self.DeviceProxy = ""
        self.tunnel = ""
        self.next_hop = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ipv4(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param remote: {"type": "string", "description": "IPv4 Address", "format": "ipv4-address"}
    :param local_protocol: {"description": "IP Protocol Number (0-255)", "minimum": 0, "type": "number", "maximum": 255, "format": "number"}
    :param local_port: {"description": "Port Number", "minimum": 0, "type": "number", "maximum": 65535, "format": "number"}
    :param remote_port: {"description": "Port Number", "minimum": 0, "type": "number", "maximum": 65535, "format": "number"}
    :param local_netmask: {"type": "string", "description": "IPv4 Address Network Mask", "format": "ipv4-netmask"}
    :param remote_netmask: {"type": "string", "description": "IPv4 Address Network Mask", "format": "ipv4-netmask"}
    :param remote_protocol: {"description": "IP Protocol Number (0-255)", "minimum": 0, "type": "number", "maximum": 255, "format": "number"}
    :param local: {"type": "string", "description": "Local Traffic Selector", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ipv4"
        self.DeviceProxy = ""
        self.remote = ""
        self.local_protocol = ""
        self.local_port = ""
        self.remote_port = ""
        self.local_netmask = ""
        self.remote_netmask = ""
        self.remote_protocol = ""
        self.local = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TrafficSelector(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "traffic-selector"
        self.DeviceProxy = ""
        self.ipv4 = {}

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


class Ipsec(A10BaseClass):
    
    """Class Description::
    IPsec settings.

    Class ipsec supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param lifebytes: {"description": "IPsec SA age in megabytes", "format": "number", "default": 0, "optional": true, "maximum": 8000000, "minimum": 0, "type": "number"}
    :param ike_gateway: {"description": "Gateway to use for IPsec SA", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string", "$ref": "/axapi/v3/vpn/ike-gateway"}
    :param name: {"description": "IPsec name", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}
    :param dh_group: {"optional": true, "enum": ["0", "1", "2", "5", "14", "15", "16", "18"], "type": "string", "description": "'0': Diffie-Hellman group 0 (Default); '1': Diffie-Hellman group 1; '2': Diffie-Hellman group 2; '5': Diffie-Hellman group 5; '14': Diffie-Hellman group 14; '15': Diffie-Hellman group 15; '16': Diffie-Hellman group 16; '18': Diffie-Hellman group 18; ", "format": "enum"}
    :param proto: {"description": "'esp': Encapsulating security protocol (Default); ", "format": "enum", "default": "esp", "type": "string", "enum": ["esp"], "optional": true}
    :param up: {"default": 0, "optional": true, "type": "number", "description": "Initiates SA negotiation to bring the IPsec connection up", "format": "flag"}
    :param anti_replay_window: {"optional": true, "enum": ["0", "16", "32", "64", "128", "256"], "type": "string", "description": "'0': Disable Anti-Replay Window Check; '16': Window Size of 16 bits; '32': Window Size of 32 bits; '64': Window Size of 64 bits; '128': Window Size of 128 bits; '256': Window Size of 256 bits; ", "format": "enum"}
    :param mode: {"description": "'tunnel': Encapsulating the packet in IPsec tunnel mode (Default); ", "format": "enum", "default": "tunnel", "type": "string", "enum": ["tunnel"], "optional": true}
    :param lifetime: {"description": "IPsec SA age in seconds", "format": "number", "default": 28800, "optional": true, "maximum": 28800, "minimum": 30, "type": "number"}
    :param enc_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"priority": {"description": "Prioritizes (1-10) security protocol, least value has highest priority", "format": "number", "default": 5, "maximum": 10, "minimum": 1, "type": "number"}, "encryption": {"enum": ["des", "3des", "aes-128", "aes-192", "aes-256", "null"], "type": "string", "description": "'des': Data Encryption Standard algorithm; '3des': Triple Data Encryption Standard algorithm; 'aes-128': Advanced Encryption Standard algorithm (key size: 128 bits); 'aes-192': Advanced Encryption Standard algorithm (key size: 192 bits); 'aes-256': Advanced Encryption Standard algorithm (key size: 256 bits); 'null': No encryption algorithm; ", "format": "enum"}, "hash": {"enum": ["md5", "sha1", "sha256", "null"], "type": "string", "description": "'md5': MD5 Dessage-Digest Algorithm; 'sha1': Secure Hash Algorithm 1; 'sha256': Secure Hash Algorithm 256; 'null': No hash algorithm; ", "format": "enum"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vpn/ipsec/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "ipsec"
        self.a10_url="/axapi/v3/vpn/ipsec/{name}"
        self.DeviceProxy = ""
        self.lifebytes = ""
        self.ike_gateway = ""
        self.name = ""
        self.dh_group = ""
        self.proto = ""
        self.bind = {}
        self.up = ""
        self.anti_replay_window = ""
        self.traffic_selector = {}
        self.mode = ""
        self.lifetime = ""
        self.enc_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


