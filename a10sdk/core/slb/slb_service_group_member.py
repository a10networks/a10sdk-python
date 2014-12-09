from a10sdk.common.A10BaseClass import A10BaseClass


class Member(A10BaseClass):
    
    """Class Description::
    Service Group Member.

    Class member supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param member_priority: {"description": "Priority of Port in the Group", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": true}
    :param name: {"description": "Member name", "format": "comp-string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/server"}
    :param fqdn_name: {"description": "Server hostname - Not applicable if real server is already defined", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param member_template: {"description": "Real server port template (Real server port template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/port"}
    :param host: {"optional": true, "type": "string", "description": "IP Address - Not applicable if real server is already defined", "format": "ipv4-address"}
    :param member_state: {"description": "'enable': Enable member service port; 'disable': Disable member service port; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param server_ipv6_addr: {"optional": true, "type": "string", "description": "IPV6 Address - Not applicable if real server is already defined", "format": "ipv6-address"}
    :param port: {"description": "Port number", "format": "number", "default": 65534, "optional": false, "maximum": 65534, "minimum": 0, "type": "number", "$ref": "/axapi/v3/slb/server/port"}
    :param member_stats_data_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable statistical data collection", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/service-group/{name}/member/{name}+{port}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name","port"]

        self.b_key = "member"
        self.a10_url="/axapi/v3/slb/service-group/{name}/member/{name}+{port}"
        self.DeviceProxy = ""
        self.member_priority = ""
        self.name = ""
        self.fqdn_name = ""
        self.member_template = ""
        self.host = ""
        self.member_state = ""
        self.server_ipv6_addr = ""
        self.port = ""
        self.member_stats_data_disable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


