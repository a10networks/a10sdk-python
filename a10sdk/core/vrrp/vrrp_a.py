from a10sdk.common.A10BaseClass import A10BaseClass


class EthernetCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param flap_ethernet_end: {"type": "number", "description": "Ethernet Port", "format": "interface"}
    :param flap_ethernet_start: {"type": "number", "description": "Ethernet Port", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ethernet-cfg"
        self.DeviceProxy = ""
        self.flap_ethernet_end = ""
        self.flap_ethernet_start = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class RestartPortList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ethernet_cfg: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "flap-ethernet-end": {"type": "number", "description": "Ethernet Port", "format": "interface"}, "flap-ethernet-start": {"type": "number", "description": "Ethernet Port", "format": "interface"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "restart-port-list"
        self.DeviceProxy = ""
        self.ethernet_cfg = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class VrrpA(A10BaseClass):
    
    """Class Description::
    HA VRRP-A Global Commands.

    Class vrrp-a supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vrid_list: {"minItems": 1, "items": {"type": "vrid"}, "uniqueItems": true, "array": [{"required": ["vrid-val"], "properties": {"preempt-mode": {"type": "object", "properties": {"threshold": {"description": "preemption threshold (preemption threshhold (1-255), default 1)", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}, "disable": {"default": 0, "type": "number", "description": "disable preemption", "format": "flag"}}}, "blade-parameters": {"type": "object", "properties": {"priority": {"description": "VRRP-A priorty (Priority, default is 150)", "format": "number", "default": 150, "maximum": 255, "minimum": 1, "type": "number"}, "fail-over-policy-template": {"description": "Apply a fail over policy template (VRRP-A fail over policy template name)", "format": "string", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/vrrp-a/fail-over-policy-template"}, "tracking-options": {"type": "object", "properties": {"interface": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet Interface (Ethernet interface number)", "format": "interface"}, "optional": true, "priority-cost": {"description": "The amount the priority will decrease", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}}}]}, "route": {"type": "object", "properties": {"ipv6-destination-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"description": "Route's administrative distance (default: match any)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "v6mask": {"description": "IPv6 Destination Prefix", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}, "protocol": {"enum": ["any", "static", "dynamic"], "type": "string", "description": "'any': Match any routing protocol (default); 'static': Match only static routes (added by user); 'dynamic': Match routes added by dynamic routing protocols (e.g. OSPF); ", "format": "enum"}, "priority-cost": {"description": "The amount the priority will decrease if the route is missing (The amount the priority will decrease if the route is not present)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "ipv6-destination": {"type": "string", "description": "IPv6 Destination Prefix", "format": "ipv6-address"}, "gatewayv6": {"type": "string", "description": "Match the route's gateway (next-hop) (default: match any)", "format": "ipv6-address"}, "optional": true}}]}, "ip-destination-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"description": "Route's administrative distance (default: match any)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "protocol": {"enum": ["any", "static", "dynamic"], "type": "string", "description": "'any': Match any routing protocol (default); 'static': Match only static routes (added by user); 'dynamic': Match routes added by dynamic routing protocols (e.g. OSPF); ", "format": "enum"}, "mask": {"type": "string", "description": "Destination prefix mask", "format": "ipv4-netmask"}, "priority-cost": {"description": "The amount the priority will decrease if the route is missing (The amount the priority will decrease if the route is not present)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "ip-destination": {"type": "string", "description": "Destination prefix", "format": "ipv4-address"}, "optional": true, "gateway": {"type": "string", "description": "Match the route's gateway (next-hop) (default: match any)", "format": "ipv4-address"}}}]}}}, "vlan-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"vlan": {"description": "VLAN tracking (VLAN id)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}, "optional": true, "timeout": {"minimum": 2, "type": "number", "maximum": 600, "format": "number"}, "priority-cost": {"description": "The amount the priority will decrease", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}}}]}, "trunk-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"per-port-pri": {"description": "per port priority", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}, "priority-cost": {"description": "The amount the priority will decrease", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "optional": true, "trunk": {"description": "trunk tracking (Trunk Number)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}}}]}, "gateway": {"type": "object", "properties": {"ipv4-gateway-list": {"minItems": 1, "items": {"type": "ipv4-gateway"}, "uniqueItems": true, "array": [{"required": ["ip-address"], "properties": {"ip-address": {"optional": false, "type": "string", "description": "IP Address", "format": "ipv4-address"}, "priority-cost": {"description": "The amount the priority will decrease", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/vrrp-a/vrid/{vrid-val}/blade-parameters/tracking-options/gateway/ipv4-gateway/{ip-address}"}, "ipv6-gateway-list": {"minItems": 1, "items": {"type": "ipv6-gateway"}, "uniqueItems": true, "array": [{"required": ["ipv6-address"], "properties": {"ipv6-address": {"optional": false, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}, "priority-cost": {"description": "The amount the priority will decrease", "format": "number", "type": "number", "maximum": 255, "minimum": 1, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/vrrp-a/vrid/{vrid-val}/blade-parameters/tracking-options/gateway/ipv6-gateway/{ipv6-address}"}}}}}}}, "floating-ip": {"type": "object", "properties": {"ipv6-address-part-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet (for link-local address only)", "format": "interface"}, "ipv6-address-partition": {"partition-visibility": "private", "platform-specific-default": 1, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}, "optional": true, "ve": {"description": "VE interface (for link-local address only)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}, "trunk": {"description": "Trunk interface (for link-local address only)", "minimum": 1, "type": "number", "maximum": 4096, "format": "number"}}}]}, "ip-address-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ip-address": {"partition-visibility": "shared", "platform-specific-default": 1, "type": "string", "description": "IP Address", "format": "ipv4-address"}}}]}, "ip-address-part-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ip-address-partition": {"partition-visibility": "private", "platform-specific-default": 1, "type": "string", "description": "IP Address", "format": "ipv4-address"}, "optional": true}}]}, "ipv6-address-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv6-address": {"partition-visibility": "shared", "platform-specific-default": 1, "type": "string", "description": "IPV6 address", "format": "ipv6-address"}, "ethernet": {"type": "number", "description": "Ethernet (for link-local address only)", "format": "interface"}, "optional": true, "ve": {"description": "VE interface (for link-local address only)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}, "trunk": {"description": "Trunk interface (for link-local address only)", "minimum": 1, "type": "number", "maximum": 4096, "format": "number"}}}]}}}, "vrid-val": {"description": "Specify ha VRRP-A vrid", "format": "number", "default": 0, "optional": false, "maximum": 31, "minimum": 0, "type": "number"}, "follow": {"type": "object", "properties": {"vrid-lead": {"description": "Define a VRRP-A VRID leader", "partition-visibility": "private", "minLength": 1, "format": "string", "maxLength": 128, "type": "string"}}}}}], "type": "array", "$ref": "/axapi/v3/vrrp-a/vrid/{vrid-val}"}
    :param force_self_standby_persistent_list: {"minItems": 1, "items": {"type": "force-self-standby-persistent"}, "uniqueItems": true, "array": [{"required": ["vrid"], "properties": {"vrid": {"description": "Specify one VRRP-A vrid to force into standby state", "format": "number", "type": "number", "maximum": 31, "minimum": 0, "optional": false}}}], "type": "array", "$ref": "/axapi/v3/vrrp-a/force-self-standby-persistent/{vrid}"}
    :param fail_over_policy_template_list: {"minItems": 1, "items": {"type": "fail-over-policy-template"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"vlan-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"vlan": {"description": "VLAN tracking (VLAN id)", "minimum": 1, "type": "number", "maximum": 4094, "format": "number"}, "optional": true, "weight": {"description": "The failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "timeout": {"minimum": 2, "type": "number", "maximum": 600, "format": "number"}}}]}, "name": {"description": "VRRP-A fail over policy template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}, "route": {"type": "object", "properties": {"ipv6-destination-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"description": "Route's administrative distance (default: match any)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "v6mask": {"description": "IPv6 Destination Prefix", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}, "protocol": {"enum": ["any", "static", "dynamic"], "type": "string", "description": "'any': Match any routing protocol (default); 'static': Match only static routes (added by user); 'dynamic': Match routes added by dynamic routing protocols (e.g. OSPF); ", "format": "enum"}, "weight": {"description": "The amount the priority will decrease if the route is missing (The amount the priority will decrease if the route is not present)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "ipv6-destination": {"type": "string", "description": "IPv6 Destination Prefix", "format": "ipv6-address"}, "gatewayv6": {"type": "string", "description": "Match the route's gateway (next-hop) (default: match any)", "format": "ipv6-address"}, "optional": true}}]}, "ip-destination-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"distance": {"description": "Route's administrative distance(default: match any)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "protocol": {"enum": ["any", "static", "dynamic"], "type": "string", "description": "'any': Match any routing protocol (default); 'static': Match only static routes (added by user); 'dynamic': Match routes added by dynamic routing protocols (e.g. OSPF); ", "format": "enum"}, "weight": {"description": "The amount the priority will decrease if the route is missing (The amount the priority will decrease if the route is not present)", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "mask": {"type": "string", "description": "Destination prefix mask", "format": "ipv4-netmask"}, "ip-destination": {"type": "string", "description": "Destination prefix", "format": "ipv4-address"}, "optional": true, "gateway": {"type": "string", "format": "ipv4-address"}}}]}}}, "interface": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ethernet": {"type": "number", "description": "Ethernet Interface (Ethernet interface number)", "format": "interface"}, "optional": true, "weight": {"description": "The failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}}}]}, "gateway": {"type": "object", "properties": {"gw-ipv4-address-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "weight": {"description": "The failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "gw-ipv4-address": {"type": "string", "description": "IP Address", "format": "ipv4-address"}}}]}, "gw-ipv6-address-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "gw-ipv6-address": {"type": "string", "description": "IPV6 address", "format": "ipv6-address"}, "weight": {"description": "The failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}}}]}}}, "trunk-cfg": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"per-port-weight": {"description": "Per port failover weight", "format": "number", "default": 1, "maximum": 255, "minimum": 1, "type": "number"}, "optional": true, "weight": {"description": "failover event weight", "minimum": 1, "type": "number", "maximum": 255, "format": "number"}, "trunk": {"description": "trunk tracking (trunk id)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}}}]}}}], "type": "array", "$ref": "/axapi/v3/vrrp-a/fail-over-policy-template/{name}"}
    :param vrid_lead_list: {"minItems": 1, "items": {"type": "vrid-lead"}, "uniqueItems": true, "array": [{"required": ["vrid-lead-str"], "properties": {"vrid-lead-str": {"description": "VRRP-A VRID leader name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "partition": {"type": "object", "properties": {"shared-cfg": {"type": "object", "properties": {"shared": {"default": 0, "not": "name", "type": "number", "description": "Shared partition", "format": "flag"}, "vrid": {"default": 0, "type": "number", "description": "VRRP-A id", "format": "flag"}, "vrid-value": {"description": "Specify ha VRRP-A vrid", "minimum": 0, "type": "number", "maximum": 31, "format": "number"}}}, "name-cfg": {"type": "object", "properties": {"vrid-value": {"description": "Specify ha VRRP-A vrid", "minimum": 0, "type": "number", "maximum": 7, "format": "number"}, "vrid": {"default": 0, "type": "number", "description": "VRRP-A id", "format": "flag"}, "name": {"description": "Partition name", "format": "string", "minLength": 1, "maxLength": 14, "not": "shared", "type": "string"}}}, "partition": {"default": 0, "type": "number", "description": "Partition name", "format": "flag"}}}}}], "type": "array", "$ref": "/axapi/v3/vrrp-a/vrid-lead/{vrid-lead-str}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "vrrp-a"
        self.a10_url="/axapi/v3/vrrp-a"
        self.DeviceProxy = ""
        self.vrid_list = []
        self.force_self_standby_persistent_list = []
        self.force_self_standby = {}
        self.peer_group = {}
        self.fail_over_policy_template_list = []
        self.vrid_lead_list = []
        self.common = {}
        self.interface = {}
        self.restart_port_list = {}
        self.preferred_session_sync_port = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


