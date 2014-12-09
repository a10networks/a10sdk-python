from a10sdk.common.A10BaseClass import A10BaseClass


class Pcp(A10BaseClass):
    
    """Class Description::
    Port Control Protocol Template.

    Class pcp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param source_ipv6: {"optional": true, "type": "string", "description": "Specify source IPv6 address for IPv6 ANNOUNCE message", "format": "ipv6-address"}
    :param allow_third_party_from_lan: {"default": 0, "optional": true, "type": "number", "description": "Allow third party request coming from LAN (default is disabled)", "format": "flag"}
    :param name: {"description": "PCP Template name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param map: {"default": 0, "optional": true, "type": "number", "description": "PCP MAP Opcode (default is enabled)", "format": "flag"}
    :param allow_third_party_from_wan: {"default": 0, "optional": true, "type": "number", "description": "Allow third party request coming from WAN (default is disabled)", "format": "flag"}
    :param maximum: {"description": "To set maximum lifetime of PCP mappings (default 1440 minutes)", "format": "number", "default": 1440, "optional": true, "maximum": 1440, "minimum": 2, "type": "number"}
    :param disable_map_filter: {"default": 0, "optional": true, "type": "number", "description": "To disable processing of FILTER options in MAP request", "format": "flag"}
    :param peer: {"default": 0, "optional": true, "type": "number", "description": "PCP PEER Opcode (default is enabled)", "format": "flag"}
    :param minimum: {"description": "To set minimum lifetime of PCP mappings (default 2 minutes)", "format": "number", "default": 2, "optional": true, "maximum": 1440, "minimum": 2, "type": "number"}
    :param check_client_nonce: {"default": 0, "optional": true, "type": "number", "description": "To validate NONCE value in PCP request (default: disabled)", "format": "flag"}
    :param announce: {"default": 0, "optional": true, "type": "number", "description": "PCP ANNOUNCE Opcode (default is enabled)", "format": "flag"}
    :param source_ip: {"optional": true, "type": "string", "description": "Specify source IP address for IPv4 ANNOUNCE message", "format": "ipv4-address"}
    :param pcp_server_port: {"description": "PCP server listening port (default 5351) (PCP UDP destination port)", "format": "number", "default": 5351, "optional": true, "maximum": 65535, "minimum": 1024, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/template/pcp/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "pcp"
        self.a10_url="/axapi/v3/cgnv6/template/pcp/{name}"
        self.DeviceProxy = ""
        self.source_ipv6 = ""
        self.allow_third_party_from_lan = ""
        self.name = ""
        self.A10WW_map = ""
        self.allow_third_party_from_wan = ""
        self.maximum = ""
        self.disable_map_filter = ""
        self.peer = ""
        self.minimum = ""
        self.check_client_nonce = ""
        self.announce = ""
        self.source_ip = ""
        self.pcp_server_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


