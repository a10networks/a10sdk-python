from a10sdk.common.A10BaseClass import A10BaseClass


class OspfInlineCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ospf_inline: {"default": 0, "partition-visibility": "shared", "type": "number", "description": "Enable OSPF under Layer 3 Inline Hot Standby Mode", "format": "flag"}
    :param vlan: {"description": "Do not filter OSPF packet on specific vlan (Vlan number)", "minimum": 1, "type": "number", "maximum": 4094, "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ospf-inline-cfg"
        self.DeviceProxy = ""
        self.ospf_inline = ""
        self.vlan = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class L2InlinePeerIpCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param l2_inline_peer_ip: {"default": 0, "partition-visibility": "shared", "type": "number", "description": "Peer IP for Layer 2 inline mode", "format": "flag"}
    :param ip_address: {"type": "string", "description": "IP address (IPv4 address)", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "l2-inline-peer-ip-cfg"
        self.DeviceProxy = ""
        self.l2_inline_peer_ip = ""
        self.ip_address = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


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
    :param preferred_trunk: {"not": "preferred-port", "type": "number", "description": "Preferred trunk Port", "format": "interface"}
    :param preferred_port: {"not": "preferred-trunk", "type": "number", "description": "Preferred ethernet Port", "format": "interface"}
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

    :param enable: {"description": "Enable vrrp HA", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param hello_interval: {"description": "VRRP-A Hello Interval (1-255, in unit of 100millisec, default is 2)", "partition-visibility": "shared", "default": 2, "optional": true, "format": "number", "maximum": 255, "minimum": 1, "type": "number"}
    :param preemption_delay: {"description": "Delay before changing state from Active to Standby (1-255, in unit of 100millisec, default is 60)", "partition-visibility": "shared", "default": 60, "optional": true, "format": "number", "maximum": 255, "minimum": 1, "type": "number"}
    :param set_id: {"description": "Set-ID for HA configuration (Set id from 1 to 15)", "partition-visibility": "shared", "optional": true, "format": "number", "maximum": 15, "minimum": 1, "type": "number"}
    :param device_id: {"description": "Unique ID for each VRRP-A box (Device-id number)", "partition-visibility": "shared", "optional": true, "format": "number", "maximum": 8, "minimum": 1, "type": "number"}
    :param arp_retry: {"description": "Number of additional gratuitous ARPs sent out after HA failover (1-255, default is 4)", "partition-visibility": "shared", "default": 4, "optional": true, "format": "number", "maximum": 255, "minimum": 1, "type": "number"}
    :param dead_timer: {"description": "VRRP-A dead timer in terms of how many hello messages missed, default is 5 (2-255, default is 5)", "partition-visibility": "shared", "default": 5, "optional": true, "format": "number", "maximum": 255, "minimum": 2, "type": "number"}
    :param disable_default_vrid: {"description": "Disable default vrid", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param l3_inline_mode: {"description": "Enable Layer 3 Inline Hot Standby Mode", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param track_event_delay: {"description": "Delay before changing state after up/down event (Units of 100 milliseconds (default 30))", "partition-visibility": "shared", "default": 30, "optional": true, "format": "number", "maximum": 100, "minimum": 1, "type": "number"}
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
        self.ospf_inline_cfg = {}
        self.enable = ""
        self.hello_interval = ""
        self.preemption_delay = ""
        self.set_id = ""
        self.device_id = ""
        self.arp_retry = ""
        self.l2_inline_peer_ip_cfg = {}
        self.dead_timer = ""
        self.disable_default_vrid = ""
        self.l3_inline_mode = ""
        self.track_event_delay = ""
        self.hostid_append_to_vrid = {}
        self.restart_time = ""
        self.inline_mode_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


