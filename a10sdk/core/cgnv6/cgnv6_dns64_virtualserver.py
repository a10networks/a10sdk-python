from a10sdk.common.A10BaseClass import A10BaseClass


class Dns64Virtualserver(A10BaseClass):
    
    """Class Description::
    Create a DNS64 Virtual Server.

    Class dns64-virtualserver supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param use_if_ip: {"description": "Use Interface IP", "format": "flag", "default": 0, "type": "number", "plat-pos-list": ["soft-ax"], "optional": true}
    :param port_list: {"minItems": 1, "items": {"type": "port"}, "uniqueItems": true, "array": [{"required": ["port-number", "protocol"], "properties": {"protocol": {"optional": false, "enum": ["dns-udp"], "type": "string", "description": "'dns-udp': DNS service over UDP; ", "format": "enum"}, "precedence": {"default": 0, "optional": true, "type": "number", "description": "Set auto NAT pool as higher precedence for source NAT", "format": "flag"}, "auto": {"default": 0, "optional": true, "type": "number", "description": "Configure auto NAT for the vport", "format": "flag"}, "template-policy": {"description": "Policy Template (Policy template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/policy"}, "port-number": {"description": "Port", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}, "template-dns": {"description": "DNS template (DNS template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/dns"}, "service-group": {"description": "Bind a Service Group to this Virtual Server (Service Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/cgnv6/service-group"}, "action": {"description": "'enable': Enable; 'disable': Disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}, "pool": {"description": "Specify NAT pool or pool group", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}}}], "type": "array", "$ref": "/axapi/v3/cgnv6/dns64-virtualserver/{name}/port/{port-number}+{protocol}"}
    :param name: {"description": "CGNV6 Virtual Server Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param template_policy: {"description": "Policy template name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/policy"}
    :param vrid: {"description": "Join a vrrp group (Specify ha VRRP-A vrid)", "format": "number", "type": "number", "maximum": 31, "minimum": 1, "optional": true}
    :param enable_disable_action: {"description": "'enable': Enable Virtual Server (default); 'disable': Disable Virtual Server; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param policy: {"default": 0, "optional": true, "type": "number", "description": "Policy template", "format": "flag"}
    :param netmask: {"optional": true, "modify-not-allowed": 1, "type": "string", "description": "IP subnet mask", "format": "ipv4-netmask-brief"}
    :param ip_address: {"description": "IP Address", "format": "ipv4-address", "type": "string", "modify-not-allowed": 1, "not": "ipv6-address", "optional": true}
    :param ipv6_address: {"description": "IPV6 address", "format": "ipv6-address", "type": "string", "modify-not-allowed": 1, "not": "ip-address", "optional": true}
    :param ethernet: {"optional": true, "plat-pos-list": ["soft-ax"], "type": "number", "description": "Ethernet interface", "format": "interface"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/dns64-virtualserver/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "dns64-virtualserver"
        self.a10_url="/axapi/v3/cgnv6/dns64-virtualserver/{name}"
        self.DeviceProxy = ""
        self.use_if_ip = ""
        self.port_list = []
        self.name = ""
        self.template_policy = ""
        self.vrid = ""
        self.enable_disable_action = ""
        self.policy = ""
        self.netmask = ""
        self.ip_address = ""
        self.ipv6_address = ""
        self.ethernet = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


