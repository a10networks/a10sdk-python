from a10sdk.common.A10BaseClass import A10BaseClass


class Network(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param broadcast: {"default": 0, "not-list": ["non-broadcast", "point-to-point", "point-to-multipoint"], "type": "number", "description": "Specify OSPF broadcast multi-access network", "format": "flag"}
    :param point_to_multipoint: {"default": 0, "not-list": ["broadcast", "non-broadcast", "point-to-point"], "type": "number", "description": "Specify OSPF point-to-multipoint network", "format": "flag"}
    :param non_broadcast: {"default": 0, "not-list": ["broadcast", "point-to-point", "point-to-multipoint"], "type": "number", "description": "Specify OSPF NBMA network", "format": "flag"}
    :param point_to_point: {"default": 0, "not-list": ["broadcast", "non-broadcast", "point-to-multipoint"], "type": "number", "description": "Specify OSPF point-to-point network", "format": "flag"}
    :param p2mp_nbma: {"default": 0, "type": "number", "description": "Specify non-broadcast point-to-multipoint network", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "network"
        self.DeviceProxy = ""
        self.broadcast = ""
        self.point_to_multipoint = ""
        self.non_broadcast = ""
        self.point_to_point = ""
        self.p2mp_nbma = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class AuthenticationCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param authentication: {"default": 0, "type": "number", "description": "Enable authentication", "format": "flag"}
    :param value: {"enum": ["message-digest", "null"], "type": "string", "description": "'message-digest': Use message-digest authentication; 'null': Use no authentication; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "authentication-cfg"
        self.DeviceProxy = ""
        self.authentication = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DatabaseFilterCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param database_filter: {"enum": ["all"], "type": "string", "description": "'all': Filter all LSA; ", "format": "enum"}
    :param out: {"default": 0, "type": "number", "description": "Outgoing LSA", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "database-filter-cfg"
        self.DeviceProxy = ""
        self.database_filter = ""
        self.out = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class BfdCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param disable: {"default": 0, "type": "number", "description": "Disable BFD", "format": "flag"}
    :param bfd: {"default": 0, "type": "number", "description": "Bidirectional Forwarding Detection (BFD)", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "bfd-cfg"
        self.DeviceProxy = ""
        self.disable = ""
        self.bfd = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Md5(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param md5_value: {"minLength": 1, "maxLength": 16, "type": "string", "description": "The OSPF password (1-16)", "format": "password"}
    :param encrypted: {"type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "md5"
        self.DeviceProxy = ""
        self.md5_value = ""
        self.encrypted = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MessageDigestCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param message_digest_key: {"description": "Message digest authentication password (key) (Key id)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "message-digest-cfg"
        self.DeviceProxy = ""
        self.message_digest_key = ""
        self.md5 = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class OspfGlobal(A10BaseClass):
    
    """Class Description::
    Global setting for Open Shortest Path First for IPv4 (OSPF).

    Class ospf-global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param dead_interval: {"description": "Interval after which a neighbor is declared dead (Seconds)", "format": "number", "default": 40, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param authentication_key: {"description": "Authentication password (key) (The OSPF password (key))", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 8, "type": "string"}
    :param mtu_ignore: {"default": 0, "optional": true, "type": "number", "description": "Ignores the MTU in DBD packets", "format": "flag"}
    :param retransmit_interval: {"description": "Time between retransmitting lost link state advertisements (Seconds)", "format": "number", "default": 5, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param transmit_delay: {"description": "Link state transmit delay (Seconds)", "format": "number", "default": 1, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param disable: {"optional": true, "enum": ["all"], "type": "string", "description": "'all': All functionality; ", "format": "enum"}
    :param cost: {"description": "Interface cost", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param hello_interval: {"description": "Time between HELLO packets (Seconds)", "format": "number", "default": 10, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param mtu: {"description": "OSPF interface MTU (MTU size)", "format": "number", "type": "number", "maximum": 65535, "minimum": 576, "optional": true}
    :param message_digest_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"message-digest-key": {"description": "Message digest authentication password (key) (Key id)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "optional": true, "md5": {"type": "object", "properties": {"md5-value": {"minLength": 1, "maxLength": 16, "type": "string", "description": "The OSPF password (1-16)", "format": "password"}, "encrypted": {"type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}}}}}]}
    :param priority: {"description": "Router priority", "format": "number", "default": 1, "optional": true, "maximum": 255, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/trunk/{ifnum}/ip/ospf/ospf-global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ospf-global"
        self.a10_url="/axapi/v3/interface/trunk/{ifnum}/ip/ospf/ospf-global"
        self.DeviceProxy = ""
        self.dead_interval = ""
        self.authentication_key = ""
        self.network = {}
        self.mtu_ignore = ""
        self.retransmit_interval = ""
        self.transmit_delay = ""
        self.disable = ""
        self.authentication_cfg = {}
        self.database_filter_cfg = {}
        self.bfd_cfg = {}
        self.cost = ""
        self.hello_interval = ""
        self.mtu = ""
        self.message_digest_cfg = []
        self.priority = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


