from a10sdk.common.A10BaseClass import A10BaseClass


class PriorityList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param priority: {"description": "Set priority for Designated Router election (Priority value)", "format": "number", "default": 64, "maximum": 127, "minimum": 0, "type": "number"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify priority for level-1 routing; 'level-2': Specify priority for level-2 routing; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "priority-list"
        self.DeviceProxy = ""
        self.priority = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HelloIntervalMinimalList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hello_interval_minimal: {"default": 0, "type": "number", "description": "Set Hello holdtime 1 second, interval depends on multiplier", "format": "flag"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify hello-interval for level-1 IIHs; 'level-2': Specify hello-interval for level-2 IIHs; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "hello-interval-minimal-list"
        self.DeviceProxy = ""
        self.hello_interval_minimal = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MeshGroup(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param value: {"description": "Mesh group number", "format": "number", "maximum": 4294967295, "minimum": 1, "not": "blocked", "type": "number"}
    :param blocked: {"default": 0, "not": "value", "type": "number", "description": "Block LSPs on this interface", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "mesh-group"
        self.DeviceProxy = ""
        self.value = ""
        self.blocked = ""

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


class CsnpIntervalList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Speficy interval for level-1 CSNPs; 'level-2': Specify interval for level-2 CSNPs; ", "format": "enum"}
    :param csnp_interval: {"description": "Set CSNP interval in seconds (CSNP interval value)", "format": "number", "default": 10, "maximum": 65535, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "csnp-interval-list"
        self.DeviceProxy = ""
        self.level = ""
        self.csnp_interval = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PasswordList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param password: {"minLength": 1, "maxLength": 254, "type": "string", "description": "Configure the authentication password for interface", "format": "string-rlx"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify password for level-1 PDUs; 'level-2': Specify password for level-2 PDUs; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "password-list"
        self.DeviceProxy = ""
        self.password = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class KeyChainList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param key_chain: {"minLength": 1, "maxLength": 128, "type": "string", "description": "Authentication key-chain (Name of key-chain)", "format": "string"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify authentication key-chain for level-1 PDUs; 'level-2': Specify authentication key-chain for level-2 PDUs; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "key-chain-list"
        self.DeviceProxy = ""
        self.key_chain = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ModeList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param mode: {"enum": ["md5"], "type": "string", "description": "'md5': Keyed message digest; ", "format": "enum"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify authentication mode for level-1 PDUs; 'level-2': Specify authentication mode for level-2 PDUs; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "mode-list"
        self.DeviceProxy = ""
        self.mode = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class SendOnlyList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param send_only: {"default": 0, "type": "number", "description": "Authentication send-only", "format": "flag"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify authentication send-only for level-1 PDUs; 'level-2': Specify authentication send-only for level-2 PDUs; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "send-only-list"
        self.DeviceProxy = ""
        self.send_only = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Authentication(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param key_chain_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"key-chain": {"minLength": 1, "maxLength": 128, "type": "string", "description": "Authentication key-chain (Name of key-chain)", "format": "string"}, "optional": true, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify authentication key-chain for level-1 PDUs; 'level-2': Specify authentication key-chain for level-2 PDUs; ", "format": "enum"}}}]}
    :param mode_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "mode": {"enum": ["md5"], "type": "string", "description": "'md5': Keyed message digest; ", "format": "enum"}, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify authentication mode for level-1 PDUs; 'level-2': Specify authentication mode for level-2 PDUs; ", "format": "enum"}}}]}
    :param send_only_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"send-only": {"default": 0, "type": "number", "description": "Authentication send-only", "format": "flag"}, "optional": true, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify authentication send-only for level-1 PDUs; 'level-2': Specify authentication send-only for level-2 PDUs; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "authentication"
        self.DeviceProxy = ""
        self.key_chain_list = []
        self.mode_list = []
        self.send_only_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class WideMetricList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param wide_metric: {"description": "Configure the wide metric for interface", "format": "number", "default": 10, "maximum": 16777214, "minimum": 1, "type": "number"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Apply metric to level-1 links; 'level-2': Apply metric to level-2 links; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "wide-metric-list"
        self.DeviceProxy = ""
        self.wide_metric = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HelloIntervalList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hello_interval: {"description": "Set Hello interval in seconds (Hello interval value)", "format": "number", "default": 10, "maximum": 65535, "minimum": 1, "type": "number"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify hello-interval for level-1 IIHs; 'level-2': Specify hello-interval for level-2 IIHs; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "hello-interval-list"
        self.DeviceProxy = ""
        self.hello_interval = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class HelloMultiplierList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hello_multiplier: {"description": "Set multiplier for Hello holding time (Hello multiplier value)", "format": "number", "default": 3, "maximum": 100, "minimum": 2, "type": "number"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify hello multiplier for level-1 IIHs; 'level-2': Specify hello multiplier for level-2 IIHs; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "hello-multiplier-list"
        self.DeviceProxy = ""
        self.hello_multiplier = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MetricList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param metric: {"description": "Configure the metric for interface (Default metric)", "format": "number", "default": 10, "maximum": 63, "minimum": 1, "type": "number"}
    :param level: {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Apply metric to level-1 links; 'level-2': Apply metric to level-2 links; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "metric-list"
        self.DeviceProxy = ""
        self.metric = ""
        self.level = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Isis(A10BaseClass):
    
    """Class Description::
    ISIS.

    Class isis supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param priority_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"priority": {"description": "Set priority for Designated Router election (Priority value)", "format": "number", "default": 64, "maximum": 127, "minimum": 0, "type": "number"}, "optional": true, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify priority for level-1 routing; 'level-2': Specify priority for level-2 routing; ", "format": "enum"}}}]}
    :param hello_interval_minimal_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"hello-interval-minimal": {"default": 0, "type": "number", "description": "Set Hello holdtime 1 second, interval depends on multiplier", "format": "flag"}, "optional": true, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify hello-interval for level-1 IIHs; 'level-2': Specify hello-interval for level-2 IIHs; ", "format": "enum"}}}]}
    :param csnp_interval_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Speficy interval for level-1 CSNPs; 'level-2': Specify interval for level-2 CSNPs; ", "format": "enum"}, "optional": true, "csnp-interval": {"description": "Set CSNP interval in seconds (CSNP interval value)", "format": "number", "default": 10, "maximum": 65535, "minimum": 1, "type": "number"}}}]}
    :param retransmit_interval: {"description": "Set per-LSP retransmission interval (Interval between retransmissions of the same LSP (seconds))", "format": "number", "default": 5, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param password_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"password": {"minLength": 1, "maxLength": 254, "type": "string", "description": "Configure the authentication password for interface", "format": "string-rlx"}, "optional": true, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify password for level-1 PDUs; 'level-2': Specify password for level-2 PDUs; ", "format": "enum"}}}]}
    :param wide_metric_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "wide-metric": {"description": "Configure the wide metric for interface", "format": "number", "default": 10, "maximum": 16777214, "minimum": 1, "type": "number"}, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Apply metric to level-1 links; 'level-2': Apply metric to level-2 links; ", "format": "enum"}}}]}
    :param hello_interval_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "hello-interval": {"description": "Set Hello interval in seconds (Hello interval value)", "format": "number", "default": 10, "maximum": 65535, "minimum": 1, "type": "number"}, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify hello-interval for level-1 IIHs; 'level-2': Specify hello-interval for level-2 IIHs; ", "format": "enum"}}}]}
    :param lsp_interval: {"description": "Set LSP transmission interval (LSP transmission interval (milliseconds))", "format": "number", "default": 33, "optional": true, "maximum": 4294967295, "minimum": 1, "type": "number"}
    :param circuit_type: {"description": "'level-1': Level-1 only adjacencies are formed; 'level-1-2': Level-1-2 adjacencies are formed; 'level-2-only': Level-2 only adjacencies are formed; ", "format": "enum", "default": "level-1-2", "type": "string", "enum": ["level-1", "level-1-2", "level-2-only"], "optional": true}
    :param hello_multiplier_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "hello-multiplier": {"description": "Set multiplier for Hello holding time (Hello multiplier value)", "format": "number", "default": 3, "maximum": 100, "minimum": 2, "type": "number"}, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Specify hello multiplier for level-1 IIHs; 'level-2': Specify hello multiplier for level-2 IIHs; ", "format": "enum"}}}]}
    :param metric_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"metric": {"description": "Configure the metric for interface (Default metric)", "format": "number", "default": 10, "maximum": 63, "minimum": 1, "type": "number"}, "optional": true, "level": {"enum": ["level-1", "level-2"], "type": "string", "description": "'level-1': Apply metric to level-1 links; 'level-2': Apply metric to level-2 links; ", "format": "enum"}}}]}
    :param hello: {"optional": true, "enum": ["padding"], "type": "string", "description": "'padding': Pad hello packets; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/interface/loopback/{ifnum}/isis`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "isis"
        self.a10_url="/axapi/v3/interface/loopback/{ifnum}/isis"
        self.DeviceProxy = ""
        self.priority_list = []
        self.hello_interval_minimal_list = []
        self.mesh_group = {}
        self.bfd_cfg = {}
        self.csnp_interval_list = []
        self.retransmit_interval = ""
        self.password_list = []
        self.authentication = {}
        self.wide_metric_list = []
        self.hello_interval_list = []
        self.lsp_interval = ""
        self.circuit_type = ""
        self.hello_multiplier_list = []
        self.metric_list = []
        self.hello = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


