from a10sdk.common.A10BaseClass import A10BaseClass


class Port(A10BaseClass):
    
    """Class Description::
    Virtual Port.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param protocol: {"optional": false, "enum": ["dns-udp"], "type": "string", "description": "'dns-udp': DNS service over UDP; ", "format": "enum"}
    :param precedence: {"default": 0, "optional": true, "type": "number", "description": "Set auto NAT pool as higher precedence for source NAT", "format": "flag"}
    :param auto: {"default": 0, "optional": true, "type": "number", "description": "Configure auto NAT for the vport", "format": "flag"}
    :param template_policy: {"description": "Policy Template (Policy template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/policy"}
    :param port_number: {"description": "Port", "format": "number", "type": "number", "maximum": 65534, "minimum": 0, "optional": false}
    :param template_dns: {"description": "DNS template (DNS template name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/template/dns"}
    :param service_group: {"description": "Bind a Service Group to this Virtual Server (Service Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/cgnv6/service-group"}
    :param action: {"description": "'enable': Enable; 'disable': Disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param pool: {"description": "Specify NAT pool or pool group", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 128, "type": "string", "$ref": "/axapi/v3/ip/nat/pool"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/dns64-virtualserver/{name}/port/{port_number}+{protocol}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "port_number","protocol"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/cgnv6/dns64-virtualserver/{name}/port/{port_number}+{protocol}"
        self.DeviceProxy = ""
        self.protocol = ""
        self.precedence = ""
        self.auto = ""
        self.template_policy = ""
        self.port_number = ""
        self.template_dns = ""
        self.service_group = ""
        self.action = ""
        self.pool = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


