from a10sdk.common.A10BaseClass import A10BaseClass


class Template(A10BaseClass):
    
    """Class Description::
    Specify a GSLB template.

    Class template supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param snmp_list: {"minItems": 1, "items": {"type": "snmp"}, "uniqueItems": true, "array": [{"required": ["snmp-name"], "properties": {"username": {"description": "Specify username (User name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "interval": {"description": "Specify interval, default is 3 (Interval, unit: second, default is 3)", "format": "number", "default": 3, "optional": true, "maximum": 999, "minimum": 1, "type": "number"}, "priv-proto": {"description": "'aes': AES; 'des': DES; ", "format": "enum", "default": "des", "type": "string", "enum": ["aes", "des"], "optional": true}, "context-name": {"description": "Specify context name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "auth-key": {"description": "Specify authentication key (Specify key)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "oid": {"description": "Specify OID", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "security-level": {"description": "'no-auth': No authentication; 'auth-no-priv': Authentication, but no privacy; 'auth-priv': Authentication and privacy; ", "format": "enum", "default": "no-auth", "type": "string", "enum": ["no-auth", "auth-no-priv", "auth-priv"], "optional": true}, "community": {"description": "Specify community for version 2c (Community name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "port": {"description": "Specify port, default is 161 (Port Number, default is 161)", "format": "number", "default": 161, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}, "host": {"description": "Specify host (Host name or ip address)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "version": {"description": "'v1': Version 1; 'v2c': Version 2c; 'v3': Version 3; ", "format": "enum", "default": "v3", "type": "string", "enum": ["v1", "v2c", "v3"], "optional": true}, "interface": {"optional": true, "type": "number", "description": "Specify Interface ID", "format": "number"}, "priv-key": {"description": "Specify privacy key (Specify key)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "auth-proto": {"description": "'sha': SHA; 'md5': MD5; ", "format": "enum", "default": "md5", "type": "string", "enum": ["sha", "md5"], "optional": true}, "security-engine-id": {"description": "Specify security engine ID", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}, "snmp-name": {"description": "Specify name of snmp template", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "context-engine-id": {"description": "Specify context engine ID", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/template/snmp/{snmp-name}"}
    :param csv_list: {"minItems": 1, "items": {"type": "csv"}, "uniqueItems": true, "array": [{"required": ["csv-name"], "properties": {"delim-char": {"description": "enter a delimiter character, default \",\"", "format": "string-rlx", "default": ",", "minLength": 1, "optional": true, "maxLength": 1, "not": "delim-num", "type": "string"}, "multiple-fields": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"field": {"description": "Field index number (Index of Field)", "minimum": 1, "type": "number", "maximum": 64, "format": "number"}, "optional": true, "csv-type": {"enum": ["ip-from", "ip-to-mask", "continent", "country", "state", "city"], "type": "string", "description": "'ip-from': Beginning address of IP range or subnet; 'ip-to-mask': Ending address of IP range or Mask; 'continent': Continent; 'country': Country; 'state': State or province; 'city': City; ", "format": "enum"}}}]}, "ipv6-enable": {"default": 0, "optional": true, "type": "number", "description": "Support IPv6 IP ranges", "format": "flag"}, "csv-name": {"description": "Specify name of csv template", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "delim-num": {"description": "enter a delimiter number, default 44 (\",\")", "format": "number", "default": 44, "optional": true, "maximum": 255, "minimum": 0, "not": "delim-char", "type": "number"}}}], "type": "array", "$ref": "/axapi/v3/gslb/template/csv/{csv-name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/template`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "template"
        self.a10_url="/axapi/v3/gslb/template"
        self.DeviceProxy = ""
        self.snmp_list = []
        self.csv_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


