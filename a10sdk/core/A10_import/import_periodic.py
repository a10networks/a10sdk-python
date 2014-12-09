from a10sdk.common.A10BaseClass import A10BaseClass


class ClassListList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param class_list: {"description": "Class List File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "class-list-list"
        self.DeviceProxy = ""
        self.period = ""
        self.remote_file = ""
        self.use_mgmt_port = ""
        self.class_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class BwListList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param bw_list: {"description": "Black white List File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "bw-list-list"
        self.DeviceProxy = ""
        self.remote_file = ""
        self.bw_list = ""
        self.use_mgmt_port = ""
        self.period = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpMapListList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip_map_list: {"description": "IP Map List File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-map-list-list"
        self.DeviceProxy = ""
        self.ip_map_list = ""
        self.remote_file = ""
        self.use_mgmt_port = ""
        self.period = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ImportPeriodic(A10BaseClass):
    
    """Class Description::
    Get files from remote site periodically.

    Class import-periodic supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ssl_key_list: {"minItems": 1, "items": {"type": "ssl-key"}, "uniqueItems": true, "array": [{"required": ["ssl-key"], "properties": {"csr-generate": {"default": 0, "optional": true, "type": "number", "description": "Generate CSR file", "format": "flag"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "ssl-key": {"description": "SSL Key File(enter bulk when import an archive file)", "format": "string", "minLength": 1, "optional": false, "maxLength": 255, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/ssl-key/{ssl-key}"}
    :param local_uri_file_list: {"minItems": 1, "items": {"type": "local-uri-file"}, "uniqueItems": true, "array": [{"required": ["local-uri-file"], "properties": {"local-uri-file": {"description": "Local URI files for http response", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/local-uri-file/{local-uri-file}"}
    :param aflex_list: {"minItems": 1, "items": {"type": "aflex"}, "uniqueItems": true, "array": [{"required": ["aflex"], "properties": {"aflex": {"description": "aFleX Script Source File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/aflex/{aflex}"}
    :param dnssec_ds_list: {"minItems": 1, "items": {"type": "dnssec-ds"}, "uniqueItems": true, "array": [{"required": ["dnssec-ds"], "properties": {"dnssec-ds": {"description": "DNSSEC DS file for child zone", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/dnssec-ds/{dnssec-ds}"}
    :param xml_schema_list: {"minItems": 1, "items": {"type": "xml-schema"}, "uniqueItems": true, "array": [{"required": ["xml-schema"], "properties": {"period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "xml-schema": {"description": "XML-Schema File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/xml-schema/{xml-schema}"}
    :param ssl_cert_list: {"minItems": 1, "items": {"type": "ssl-cert"}, "uniqueItems": true, "array": [{"required": ["ssl-cert"], "properties": {"pfx-password": {"description": "The password for certificate file (pfx type only)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}, "csr-generate": {"default": 0, "optional": true, "type": "number", "description": "Generate CSR file", "format": "flag"}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}, "certificate-type": {"optional": true, "enum": ["pem", "der", "pfx", "p7b"], "type": "string", "description": "'pem': pem; 'der': der; 'pfx': pfx; 'p7b': p7b; ", "format": "enum"}, "ssl-cert": {"description": "SSL Cert File(enter bulk when import an archive file)", "format": "string", "minLength": 1, "optional": false, "maxLength": 255, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/ssl-cert/{ssl-cert}"}
    :param dnssec_dnskey_list: {"minItems": 1, "items": {"type": "dnssec-dnskey"}, "uniqueItems": true, "array": [{"required": ["dnssec-dnskey"], "properties": {"remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "dnssec-dnskey": {"description": "DNSSEC DNSKEY(KSK) file for child zone", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/dnssec-dnskey/{dnssec-dnskey}"}
    :param geo_location_list: {"minItems": 1, "items": {"type": "geo-location"}, "uniqueItems": true, "array": [{"required": ["geo-location"], "properties": {"geo-location": {"description": "Geo-location CSV File", "partition-visibility": "shared", "minLength": 1, "format": "string", "optional": false, "maxLength": 63, "type": "string"}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/geo-location/{geo-location}"}
    :param policy_list: {"minItems": 1, "items": {"type": "policy"}, "uniqueItems": true, "array": [{"required": ["policy"], "properties": {"policy": {"description": "WAF policy File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/policy/{policy}"}
    :param class_list_list: {"minItems": 1, "items": {"type": "class-list"}, "uniqueItems": true, "array": [{"required": ["class-list"], "properties": {"period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "class-list": {"description": "Class List File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/class-list/{class-list}"}
    :param wsdl_list: {"minItems": 1, "items": {"type": "wsdl"}, "uniqueItems": true, "array": [{"required": ["wsdl"], "properties": {"wsdl": {"description": "Web Services Definition Language File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/wsdl/{wsdl}"}
    :param bw_list_list: {"minItems": 1, "items": {"type": "bw-list"}, "uniqueItems": true, "array": [{"required": ["bw-list"], "properties": {"remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "bw-list": {"description": "Black white List File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/bw-list/{bw-list}"}
    :param ip_map_list_list: {"minItems": 1, "items": {"type": "ip-map-list"}, "uniqueItems": true, "array": [{"required": ["ip-map-list"], "properties": {"ip-map-list": {"description": "IP Map List File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/ip-map-list/{ip-map-list}"}
    :param license_list: {"minItems": 1, "items": {"type": "license"}, "uniqueItems": true, "array": [{"required": ["license"], "properties": {"remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "license": {"description": "License File", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/license/{license}"}
    :param ssl_crl_list: {"minItems": 1, "items": {"type": "ssl-crl"}, "uniqueItems": true, "array": [{"required": ["ssl-crl"], "properties": {"csr-generate": {"default": 0, "optional": true, "type": "number", "description": "Generate CSR file", "format": "flag"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "ssl-crl": {"description": "SSL Crl File", "format": "string", "minLength": 1, "optional": false, "maxLength": 255, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/ssl-crl/{ssl-crl}"}
    :param ssl_cert_key_list: {"minItems": 1, "items": {"type": "ssl-cert-key"}, "uniqueItems": true, "array": [{"required": ["ssl-cert-key"], "properties": {"ssl-cert-key": {"optional": false, "enum": ["bulk"], "type": "string", "description": "'bulk': import an archive file; ", "format": "enum"}, "remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/ssl-cert-key/{ssl-cert-key}"}
    :param auth_portal_list: {"minItems": 1, "items": {"type": "auth-portal"}, "uniqueItems": true, "array": [{"required": ["auth-portal"], "properties": {"remote-file": {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}, "use-mgmt-port": {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}, "auth-portal": {"description": "Portal file for http authentication", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "period": {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}}}], "type": "array", "$ref": "/axapi/v3/import-periodic/auth-portal/{auth-portal}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/import-periodic`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "import-periodic"
        self.a10_url="/axapi/v3/import-periodic"
        self.DeviceProxy = ""
        self.ssl_key_list = []
        self.local_uri_file_list = []
        self.aflex_list = []
        self.dnssec_ds_list = []
        self.xml_schema_list = []
        self.ssl_cert_list = []
        self.dnssec_dnskey_list = []
        self.geo_location_list = []
        self.policy_list = []
        self.class_list_list = []
        self.wsdl_list = []
        self.bw_list_list = []
        self.ip_map_list_list = []
        self.license_list = []
        self.ssl_crl_list = []
        self.ssl_cert_key_list = []
        self.auth_portal_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


