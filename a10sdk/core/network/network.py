from a10sdk.common.A10BaseClass import A10BaseClass


class Network(A10BaseClass):
    
    """    :param vlan_list: {"minItems": 1, "items": {"type": "vlan"}, "uniqueItems": true, "array": [{"required": ["vlan-num"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ve": {"description": "ve number", "format": "number", "type": "number", "maximum": 4094, "minimum": 2, "optional": true}, "untagged-trunk-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"untagged-trunk-start": {"type": "number", "description": "Trunk groups", "format": "number"}, "optional": true, "untagged-trunk-end": {"type": "number", "description": "Trunk Group", "format": "number"}}}]}, "untagged-lif": {"description": "Logical tunnel interface (Logical tunnel interface number)", "format": "number", "type": "number", "maximum": 128, "minimum": 1, "optional": true}, "untagged-eth-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"untagged-ethernet-end": {"type": "number", "description": "Ethernet port", "format": "interface"}, "untagged-ethernet-start": {"$ref": "/axapi/v3/interface/ethernet", "type": "number", "description": "Ethernet port (Interface number)", "format": "interface"}, "optional": true}}]}, "tagged-eth-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"tagged-ethernet-end": {"type": "number", "description": "Ethernet port", "format": "interface"}, "optional": true, "tagged-ethernet-start": {"$ref": "/axapi/v3/interface/ethernet", "type": "number", "description": "Ethernet port (Interface number)", "format": "interface"}}}]}, "tagged-trunk-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "tagged-trunk-start": {"type": "number", "description": "Trunk groups", "format": "number"}, "tagged-trunk-end": {"type": "number", "description": "Trunk Group", "format": "number"}}}]}, "vlan-num": {"description": "VLAN number", "format": "number", "type": "number", "maximum": 4094, "minimum": 2, "optional": false}, "name": {"description": "VLAN name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/network/vlan/{vlan-num}"}
    :param lacp_passthrough_list: {"minItems": 1, "items": {"type": "lacp-passthrough"}, "uniqueItems": true, "array": [{"required": ["peer-from", "peer-to"], "properties": {"peer-from": {"optional": false, "type": "number", "description": "Peer member to forward received LACP packets", "format": "interface"}, "peer-to": {"optional": false, "type": "number", "description": "Peer member to forward received LACP packets", "format": "interface"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/network/lacp-passthrough/{peer-from}+{peer-to}"}
    :param bpdu_fwd_group_list: {"minItems": 1, "items": {"type": "bpdu-fwd-group"}, "uniqueItems": true, "array": [{"required": ["bpdu-fwd-group-number"], "properties": {"bpdu-fwd-group-number": {"optional": false, "minimum": 1, "type": "number", "maximum": 8, "format": "number"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ethernet-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet-start": {"type": "number", "description": "Ethernet Port (Interface number)", "format": "interface"}, "ethernet-end": {"type": "number", "description": "Ethernet Port", "format": "interface"}, "optional": true}}]}}}], "type": "array", "$ref": "/axapi/v3/network/bpdu-fwd-group/{bpdu-fwd-group-number}"}
    :param bridge_vlan_group_list: {"minItems": 1, "items": {"type": "bridge-vlan-group"}, "uniqueItems": true, "array": [{"required": ["bridge-vlan-group-number"], "properties": {"vlan-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "vlan-start": {"$ref": "/axapi/v3/network/vlan", "type": "number", "description": "VLAN id", "format": "number"}, "vlan-end": {"type": "number", "description": "VLAN id", "format": "number"}}}]}, "ve": {"description": "Virtual Ethernet Port (Virtual Ethernet Port number)", "format": "number", "type": "number", "maximum": 4094, "minimum": 2, "optional": true}, "forward-traffic": {"description": "'forward-all-traffic': Forward all traffic between bridge members; 'forward-ip-traffic': Forward only IP traffic between bridge members (default); ", "format": "enum", "default": "forward-ip-traffic", "type": "string", "enum": ["forward-all-traffic", "forward-ip-traffic"], "optional": true}, "name": {"description": "Bridge Group Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "bridge-vlan-group-number": {"description": "Bridge VLAN Group Number", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": false}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/network/bridge-vlan-group/{bridge-vlan-group-number}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Configure Network Command.

    Class network supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "network"
        self.a10_url="/axapi/v3/network"
        self.DeviceProxy = ""
        self.arp = {}
        self.vlan_list = []
        self.lacp_passthrough_list = []
        self.bpdu_fwd_group_list = []
        self.vlan_global = {}
        self.ve_stats = {}
        self.mac_age_time = {}
        self.icmpv6_rate_limit = {}
        self.lacp = {}
        self.arp_timeout = {}
        self.bfd = {}
        self.icmp_rate_limit = {}
        self.bridge_vlan_group_list = []
        self.mac_address = {}
        self.lldp = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


