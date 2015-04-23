from a10sdk.common.A10BaseClass import A10BaseClass


class Snmp(A10BaseClass):
    
    """Class Description::
    Specify SNMP template.

    Class snmp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param username: {"description": "Specify username (User name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param interval: {"description": "Specify interval, default is 3 (Interval, unit: second, default is 3)", "format": "number", "default": 3, "optional": true, "maximum": 999, "minimum": 1, "type": "number"}
    :param priv_proto: {"description": "'aes': AES; 'des': DES; ", "format": "enum", "default": "des", "type": "string", "enum": ["aes", "des"], "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param context_name: {"description": "Specify context name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param auth_key: {"description": "Specify authentication key (Specify key)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param oid: {"description": "Specify OID", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param security_level: {"description": "'no-auth': No authentication; 'auth-no-priv': Authentication, but no privacy; 'auth-priv': Authentication and privacy; ", "format": "enum", "default": "no-auth", "type": "string", "enum": ["no-auth", "auth-no-priv", "auth-priv"], "optional": true}
    :param community: {"description": "Specify community for version 2c (Community name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param port: {"description": "Specify port, default is 161 (Port Number, default is 161)", "format": "number", "default": 161, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param host: {"description": "Specify host (Host name or ip address)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param version: {"description": "'v1': Version 1; 'v2c': Version 2c; 'v3': Version 3; ", "format": "enum", "default": "v3", "type": "string", "enum": ["v1", "v2c", "v3"], "optional": true}
    :param interface: {"description": "Specify Interface ID", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param priv_key: {"description": "Specify privacy key (Specify key)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param auth_proto: {"description": "'sha': SHA; 'md5': MD5; ", "format": "enum", "default": "md5", "type": "string", "enum": ["sha", "md5"], "optional": true}
    :param security_engine_id: {"description": "Specify security engine ID", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param snmp_name: {"description": "Specify name of snmp template", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param context_engine_id: {"description": "Specify context engine ID", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/template/snmp/{snmp_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "snmp_name"]

        self.b_key = "snmp"
        self.a10_url="/axapi/v3/gslb/template/snmp/{snmp_name}"
        self.DeviceProxy = ""
        self.username = ""
        self.interval = ""
        self.priv_proto = ""
        self.uuid = ""
        self.context_name = ""
        self.auth_key = ""
        self.oid = ""
        self.security_level = ""
        self.community = ""
        self.port = ""
        self.host = ""
        self.version = ""
        self.interface = ""
        self.priv_key = ""
        self.auth_proto = ""
        self.security_engine_id = ""
        self.snmp_name = ""
        self.context_engine_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


