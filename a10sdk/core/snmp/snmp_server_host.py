from a10sdk.common.A10BaseClass import A10BaseClass


class Host(A10BaseClass):
    
    """Class Description::
    Specify hosts to receive SNMP traps.

    Class host supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_host_list: {"minItems": 1, "items": {"type": "ipv6-host"}, "uniqueItems": true, "array": [{"required": ["ipv6-addr", "version"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv6-addr": {"optional": false, "type": "string", "description": "help IPV4 address of SNMP trap host", "format": "ipv6-address"}, "udp-port": {"description": "The trap host's UDP port number(default: 162)", "format": "number", "default": 162, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}, "v1-v2c-comm": {"description": "SNMPv1/v2c community string", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "version": {"description": "'v1': Use SNMPv1; 'v2c': Use SNMPv2c; 'v3': User SNMPv3; ", "format": "enum", "default": "v2c", "type": "string", "enum": ["v1", "v2c", "v3"], "optional": false}, "user": {"description": "SNMPv3 user to send traps (User Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/snmp-server/host/ipv6-host/{ipv6-addr}+{version}"}
    :param host_name_list: {"minItems": 1, "items": {"type": "host-name"}, "uniqueItems": true, "array": [{"required": ["hostname", "version"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "hostname": {"description": "Hostname of SNMP trap host", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}, "udp-port": {"description": "The trap host's UDP port number(default: 162)", "format": "number", "default": 162, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}, "v1-v2c-comm": {"description": "SNMPv1/v2c community string", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "user": {"description": "SNMPv3 user to send traps (User Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "version": {"description": "'v1': Use SNMPv1; 'v2c': Use SNMPv2c; 'v3': User SNMPv3; ", "format": "enum", "default": "v2c", "type": "string", "enum": ["v1", "v2c", "v3"], "optional": false}}}], "type": "array", "$ref": "/axapi/v3/snmp-server/host/host-name/{hostname}+{version}"}
    :param ipv4_host_list: {"minItems": 1, "items": {"type": "ipv4-host"}, "uniqueItems": true, "array": [{"required": ["ipv4-addr", "version"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv4-addr": {"optional": false, "type": "string", "description": "help IPV4 address of SNMP trap host", "format": "ipv4-address"}, "v1-v2c-comm": {"description": "SNMPv1/v2c community string", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "udp-port": {"description": "The trap host's UDP port number(default: 162)", "format": "number", "default": 162, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}, "version": {"description": "'v1': Use SNMPv1; 'v2c': Use SNMPv2c; 'v3': User SNMPv3; ", "format": "enum", "default": "v2c", "type": "string", "enum": ["v1", "v2c", "v3"], "optional": false}, "user": {"description": "SNMPv3 user to send traps (User Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/snmp-server/host/ipv4-host/{ipv4-addr}+{version}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/host`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "host"
        self.a10_url="/axapi/v3/snmp-server/host"
        self.DeviceProxy = ""
        self.ipv6_host_list = []
        self.host_name_list = []
        self.ipv4_host_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


