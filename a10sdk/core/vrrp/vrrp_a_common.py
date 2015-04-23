from a10sdk.common.A10BaseClass import A10BaseClass


class HostidAppendToVrid(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param hostid_append_to_vrid_value: {"description": "hostid append to vrid num", "partition-visibility": "shared", "format": "number", "maximum": 31, "minimum": 1, "not": "hostid-append-to-vrid-default", "type": "number"}
    :param hostid_append_to_vrid_default: {"description": "hostid append to vrid default", "partition-visibility": "shared", "default": 0, "format": "flag", "not": "hostid-append-to-vrid-value", "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "hostid-append-to-vrid"
        self.DeviceProxy = ""
        self.hostid_append_to_vrid_value = ""
        self.hostid_append_to_vrid_default = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class InlineModeCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param inline_mode: {"default": 0, "partition-visibility": "shared", "type": "number", "description": "Enable Layer 2 Inline Hot Standby Mode", "format": "flag"}
    :param preferred_trunk: {"not": "preferred-port", "partition-visibility": "shared", "type": "number", "description": "Preferred trunk Port", "format": "interface"}
    :param preferred_port: {"not": "preferred-trunk", "partition-visibility": "shared", "type": "number", "description": "Preferred ethernet Port", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "inline-mode-cfg"
        self.DeviceProxy = ""
        self.inline_mode = ""
        self.preferred_trunk = ""
        self.preferred_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Common(A10BaseClass):
    
    """Class Description::
    HA VRRP-A Global Commands.

    Class common supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param hello_interval: {"description": "VRRP-A Hello Interval (1-255, in unit of 100millisec, default is 2)", "partition-visibility": "shared", "default": 2, "optional": true, "format": "number", "maximum": 255, "minimum": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param preemption_delay: {"description": "Delay before changing state from Active to Standby (1-255, in unit of 100millisec, default is 60)", "partition-visibility": "shared", "default": 60, "optional": true, "format": "number", "maximum": 255, "minimum": 1, "type": "number"}
    :param set_id: {"description": "Set-ID for HA configuration (Set id from 1 to 15)", "partition-visibility": "shared", "optional": true, "format": "number", "maximum": 15, "minimum": 1, "type": "number"}
    :param device_id: {"platform-specific-range": 1, "platform-specific-default": 1, "description": "Unique ID for each VRRP-A box (Device-id number)", "partition-visibility": "shared", "optional": true, "format": "number", "type": "number"}
    :param arp_retry: {"description": "Number of additional gratuitous ARPs sent out after HA failover (1-255, default is 4)", "partition-visibility": "shared", "default": 4, "optional": true, "format": "number", "maximum": 255, "minimum": 1, "type": "number"}
    :param dead_timer: {"description": "VRRP-A dead timer in terms of how many hello messages missed, default is 5 (2-255, default is 5)", "partition-visibility": "shared", "default": 5, "optional": true, "format": "number", "maximum": 255, "minimum": 2, "type": "number"}
    :param disable_default_vrid: {"description": "Disable default vrid", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param track_event_delay: {"description": "Delay before changing state after up/down event (Units of 100 milliseconds (default 30))", "partition-visibility": "shared", "default": 30, "optional": true, "format": "number", "maximum": 100, "minimum": 1, "type": "number"}
    :param action: {"description": "'enable': enable vrrp-a; 'disable': disable vrrp-a; ", "format": "enum", "default": "disable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param restart_time: {"description": "Time between restarting ports on standby system after transition", "partition-visibility": "shared", "default": 20, "optional": true, "format": "number", "maximum": 100, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/common`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "common"
        self.a10_url="/axapi/v3/vrrp-a/common"
        self.DeviceProxy = ""
        self.hello_interval = ""
        self.uuid = ""
        self.preemption_delay = ""
        self.set_id = ""
        self.device_id = ""
        self.arp_retry = ""
        self.dead_timer = ""
        self.disable_default_vrid = ""
        self.track_event_delay = ""
        self.action = ""
        self.hostid_append_to_vrid = {}
        self.restart_time = ""
        self.inline_mode_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


