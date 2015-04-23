from a10sdk.common.A10BaseClass import A10BaseClass


class Community(A10BaseClass):
    
    """Class Description::
    Define a community who can access the SNMP engine.

    Class community supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param read_list: {"minItems": 1, "items": {"type": "read"}, "uniqueItems": true, "array": [{"required": ["user"], "properties": {"oid-list": {"minItems": 1, "items": {"type": "oid"}, "uniqueItems": true, "array": [{"required": ["oid-val"], "properties": {"remote": {"type": "object", "properties": {"host-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dns-host": {"minLength": 1, "maxLength": 31, "type": "string", "description": "DNS remote host", "format": "string"}, "optional": true, "ipv4-mask": {"type": "string", "description": "IPV4 mask", "format": "ipv4-netmask"}}}]}, "ipv4-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ipv4-host": {"type": "string", "description": "IPV4 remote host", "format": "ipv4-address"}, "ipv4-mask": {"type": "string", "description": "IPV4 mask", "format": "ipv4-netmask"}}}]}, "ipv6-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv6-host": {"type": "string", "description": "IPV6 remote host", "format": "ipv6-address"}, "optional": true, "ipv6-mask": {"description": "IPV6 mask", "minimum": 1, "type": "number", "maximum": 128, "format": "number"}}}]}}}, "oid-val": {"description": "specific the oid (The oid value, object-key)", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/snmp-server/community/read/{user}/oid/{oid-val}"}, "remote": {"type": "object", "properties": {"host-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"dns-host": {"minLength": 1, "maxLength": 31, "type": "string", "description": "DNS remote host", "format": "string"}, "optional": true, "ipv4-mask": {"type": "string", "description": "IPV4 mask", "format": "ipv4-netmask"}}}]}, "ipv4-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "ipv4-host": {"type": "string", "description": "IPV4 remote host", "format": "ipv4-address"}, "ipv4-mask": {"type": "string", "description": "IPV4 mask", "format": "ipv4-netmask"}}}]}, "ipv6-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv6-host": {"type": "string", "description": "IPV6 remote host", "format": "ipv6-address"}, "optional": true, "ipv6-mask": {"description": "IPV6 mask", "minimum": 1, "type": "number", "maximum": 128, "format": "number"}}}]}}}, "user": {"description": "SNMPv1/v2c community string", "format": "string", "minLength": 1, "optional": false, "maxLength": 31, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/snmp-server/community/read/{user}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/snmp-server/community`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "community"
        self.a10_url="/axapi/v3/snmp-server/community"
        self.DeviceProxy = ""
        self.read_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


