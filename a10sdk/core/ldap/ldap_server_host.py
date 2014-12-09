from a10sdk.common.A10BaseClass import A10BaseClass


class Host(A10BaseClass):
    
    """Class Description::
    Specify the LDAP server's hostname or IP address.

    Class host supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ldap_hostname_list: {"minItems": 1, "items": {"type": "ldap-hostname"}, "uniqueItems": true, "array": [{"required": ["hostname"], "properties": {"port-cfg": {"type": "object", "properties": {"ssl": {"default": 0, "type": "number", "description": "Use SSL", "format": "flag"}, "port": {"description": "Specify the LDAP server's port (default 389 without ssl or 636 with ssl)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "timeout": {"description": "Specify the LDAP server's timeout (default 3)", "minimum": 1, "type": "number", "maximum": 60, "format": "number"}}}, "cn-value": {"description": "LDAP common name identifier (i.e.: cn, uid)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "hostname": {"description": "Hostname of LDAP server", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "dn-value": {"description": "LDAP distinguished name (dn)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ldap-server/host/ldap-hostname/{hostname}"}
    :param ipv4_list: {"minItems": 1, "items": {"type": "ipv4"}, "uniqueItems": true, "array": [{"required": ["ipv4-addr"], "properties": {"port-cfg": {"type": "object", "properties": {"ssl": {"default": 0, "type": "number", "description": "Use SSL", "format": "flag"}, "port": {"description": "Specify the LDAP server's port (default 389 without ssl or 636 with ssl)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "timeout": {"description": "Specify the LDAP server's timeout (default 3)", "minimum": 1, "type": "number", "maximum": 60, "format": "number"}}}, "ipv4-addr": {"optional": false, "type": "string", "description": "IPV4 address of ldap server", "format": "ipv4-address"}, "cn-value": {"description": "LDAP common name identifier (i.e.: cn, uid)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "dn-value": {"description": "LDAP distinguished name (dn)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/ldap-server/host/ipv4/{ipv4-addr}"}
    :param ipv6_list: {"minItems": 1, "items": {"type": "ipv6"}, "uniqueItems": true, "array": [{"required": ["ipv6-addr"], "properties": {"port-cfg": {"type": "object", "properties": {"ssl": {"default": 0, "type": "number", "description": "Use SSL", "format": "flag"}, "port": {"description": "Specify the LDAP server's port (default 389 without ssl or 636 with ssl)", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}, "timeout": {"description": "Specify the LDAP server's timeout (default 3)", "minimum": 1, "type": "number", "maximum": 60, "format": "number"}}}, "dn-value": {"description": "LDAP distinguished name (dn)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "cn-value": {"description": "LDAP common name identifier (i.e.: cn, uid)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}, "ipv6-addr": {"optional": false, "type": "string", "description": "IPV6 address of ldap server", "format": "ipv6-address"}}}], "type": "array", "$ref": "/axapi/v3/ldap-server/host/ipv6/{ipv6-addr}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ldap-server/host`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "host"
        self.a10_url="/axapi/v3/ldap-server/host"
        self.DeviceProxy = ""
        self.ldap_hostname_list = []
        self.ipv4_list = []
        self.ipv6_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


