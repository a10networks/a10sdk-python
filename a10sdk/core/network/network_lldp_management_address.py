from a10sdk.common.A10BaseClass import A10BaseClass


class ManagementAddress(A10BaseClass):
    
    """Class Description::
    Configure lldp management address.

    Class management-address supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ipv6_addr_list: {"minItems": 1, "items": {"type": "ipv6-addr"}, "uniqueItems": true, "array": [{"required": ["ipv6"], "properties": {"interface-ipv6": {"type": "object", "properties": {"ipv6-ve": {"description": "configure lldp management-address interface ve (lldp management-address interface port number)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}, "ipv6-eth": {"type": "number", "description": "configure lldp management-address interface ethernet (lldp management-address interface port number)", "format": "interface"}, "ipv6-mgmt": {"default": 0, "type": "number", "description": "configure lldp management-address interface management", "format": "flag"}}}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv6": {"optional": false, "type": "string", "description": "Configure lldp management-address, subtype is ipv6 (lldp management-address ipv6 address)", "format": "ipv6-address"}}}], "type": "array", "$ref": "/axapi/v3/network/lldp/management-address/ipv6-addr/{ipv6}"}
    :param ipv4_addr_list: {"minItems": 1, "items": {"type": "ipv4-addr"}, "uniqueItems": true, "array": [{"required": ["ipv4"], "properties": {"uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv4": {"optional": false, "type": "string", "description": "Configure lldp management-address, subtype is ipv4 (lldp management-address ipv4 address)", "format": "ipv4-address"}, "interface-ipv4": {"type": "object", "properties": {"ipv4-eth": {"type": "number", "description": "configure lldp management-address interface ethernet (lldp management-address interface port number)", "format": "interface"}, "ipv4-mgmt": {"default": 0, "type": "number", "description": "configure lldp management-address interface management", "format": "flag"}, "ipv4-ve": {"description": "configure lldp management-address interface ve (lldp management-address interface port number)", "minimum": 2, "type": "number", "maximum": 4094, "format": "number"}}}}}], "type": "array", "$ref": "/axapi/v3/network/lldp/management-address/ipv4-addr/{ipv4}"}
    :param dns_list: {"minItems": 1, "items": {"type": "dns"}, "uniqueItems": true, "array": [{"required": ["dns"], "properties": {"interface": {"type": "object", "properties": {"ethernet": {"not-list": ["ve", "management"], "type": "number", "description": "configure lldp management-address interface ethernet (lldp management-address interface port number)", "format": "interface"}, "management": {"default": 0, "not-list": ["ethernet", "ve"], "type": "number", "description": "configure lldp management-address interface management", "format": "flag"}, "ve": {"description": "configure lldp management-address interface management (lldp management-address interface port number)", "format": "number", "not-list": ["ethernet", "management"], "maximum": 4094, "minimum": 2, "type": "number"}}}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "dns": {"description": "Configure lldp management-address, subtype is dns (lldp management-address dns address)", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/network/lldp/management-address/dns/{dns}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/network/lldp/management-address`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "management-address"
        self.a10_url="/axapi/v3/network/lldp/management-address"
        self.DeviceProxy = ""
        self.ipv6_addr_list = []
        self.ipv4_addr_list = []
        self.dns_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


