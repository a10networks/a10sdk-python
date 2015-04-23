from a10sdk.common.A10BaseClass import A10BaseClass


class ClearCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param clear_sequence: {"description": "Specify the port physical port number", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param clear_all_sequence: {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param sessions: {"enum": ["all", "sequence"], "type": "string", "description": "'all': Clear all sessions; 'sequence': Sequence number; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "clear-cfg"
        self.DeviceProxy = ""
        self.clear_sequence = ""
        self.clear_all_sequence = ""
        self.sessions = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LinkEnableCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ena_sequence: {"description": "Sequence number (Specify the physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param enaeth: {"type": "number", "description": "Specify the physical port number (Ethernet interface number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "link-enable-cfg"
        self.DeviceProxy = ""
        self.ena_sequence = ""
        self.enaeth = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LinkUpCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param linkup_ethernet3: {"type": "number", "description": "Specify the port physical port number (Ethernet interface number)", "format": "interface"}
    :param linkup_ethernet2: {"type": "number", "description": "Specify the port physical port number (Ethernet interface number)", "format": "interface"}
    :param linkup_ethernet1: {"type": "number", "description": "Specify the port physical port number (Ethernet interface number)", "format": "interface"}
    :param link_up_sequence1: {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param link_up_sequence3: {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param link_up_sequence2: {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "link-up-cfg"
        self.DeviceProxy = ""
        self.linkup_ethernet3 = ""
        self.linkup_ethernet2 = ""
        self.linkup_ethernet1 = ""
        self.link_up_sequence1 = ""
        self.link_up_sequence3 = ""
        self.link_up_sequence2 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LinkDownCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param link_down_sequence1: {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param link_down_sequence2: {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param link_down_sequence3: {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param linkdown_ethernet2: {"type": "number", "description": "Specify the port physical port number (Ethernet interface number)", "format": "interface"}
    :param linkdown_ethernet3: {"type": "number", "description": "Specify the port physical port number (Ethernet interface number)", "format": "interface"}
    :param linkdown_ethernet1: {"type": "number", "description": "Specify the port physical port number (Ethernet interface number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "link-down-cfg"
        self.DeviceProxy = ""
        self.link_down_sequence1 = ""
        self.link_down_sequence2 = ""
        self.link_down_sequence3 = ""
        self.linkdown_ethernet2 = ""
        self.linkdown_ethernet3 = ""
        self.linkdown_ethernet1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LinkDisableCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param dis_sequence: {"description": "Sequence number (Specify the physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param diseth: {"type": "number", "description": "Specify the physical port number (Ethernet interface number)", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "link-disable-cfg"
        self.DeviceProxy = ""
        self.dis_sequence = ""
        self.diseth = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Monitor(A10BaseClass):
    
    """Class Description::
    Monitor template.

    Class monitor supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param clear_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"clear-sequence": {"description": "Specify the port physical port number", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "clear-all-sequence": {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "optional": true, "sessions": {"enum": ["all", "sequence"], "type": "string", "description": "'all': Clear all sessions; 'sequence': Sequence number; ", "format": "enum"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param link_enable_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ena-sequence": {"description": "Sequence number (Specify the physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "enaeth": {"type": "number", "description": "Specify the physical port number (Ethernet interface number)", "format": "interface"}, "optional": true}}]}
    :param link_up_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"linkup-ethernet3": {"type": "number", "description": "Specify the port physical port number (Ethernet interface number)", "format": "interface"}, "linkup-ethernet2": {"type": "number", "description": "Specify the port physical port number (Ethernet interface number)", "format": "interface"}, "linkup-ethernet1": {"type": "number", "description": "Specify the port physical port number (Ethernet interface number)", "format": "interface"}, "link-up-sequence1": {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "link-up-sequence3": {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "link-up-sequence2": {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "optional": true}}]}
    :param link_down_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"link-down-sequence1": {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "link-down-sequence2": {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "link-down-sequence3": {"description": "Sequence number (Specify the port physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "optional": true, "linkdown-ethernet2": {"type": "number", "description": "Specify the port physical port number (Ethernet interface number)", "format": "interface"}, "linkdown-ethernet3": {"type": "number", "description": "Specify the port physical port number (Ethernet interface number)", "format": "interface"}, "linkdown-ethernet1": {"type": "number", "description": "Specify the port physical port number (Ethernet interface number)", "format": "interface"}}}]}
    :param link_disable_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dis-sequence": {"description": "Sequence number (Specify the physical port number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "diseth": {"type": "number", "description": "Specify the physical port number (Ethernet interface number)", "format": "interface"}, "optional": true}}]}
    :param monitor_relation: {"description": "'monitor-and': Configures the monitors in current template to work with AND logic; 'monitor-or': Configures the monitors in current template to work with OR logic; ", "format": "enum", "default": "monitor-and", "type": "string", "enum": ["monitor-and", "monitor-or"], "optional": true}
    :param id: {"description": "Monitor template ID Number", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": false}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/monitor/{id}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "id"]

        self.b_key = "monitor"
        self.a10_url="/axapi/v3/slb/template/monitor/{id}"
        self.DeviceProxy = ""
        self.clear_cfg = []
        self.uuid = ""
        self.link_enable_cfg = []
        self.link_up_cfg = []
        self.link_down_cfg = []
        self.link_disable_cfg = []
        self.monitor_relation = ""
        self.A10WW_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


