from a10sdk.common.A10BaseClass import A10BaseClass


class EqualsList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param equals: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string equals another string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "equals-list"
        self.DeviceProxy = ""
        self.equals = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ContainsList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param contains: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string contains another string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "contains-list"
        self.DeviceProxy = ""
        self.contains = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class EndsWithList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ends_with: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string ends with another string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ends-with-list"
        self.DeviceProxy = ""
        self.ends_with = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServerNameList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param server_name: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Server name indication in Client hello extension (Server name String)", "format": "string"}
    :param server_key: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Server Private Key associated to SNI (Server Private Key Name)", "format": "string"}
    :param server_passphrase: {"minLength": 1, "maxLength": 63, "type": "string", "description": "help Password Phrase", "format": "password"}
    :param server_encrypted: {"type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param server_cert: {"minLength": 1, "maxLength": 255, "type": "string", "description": "Server Certificate associated to SNI (Server Certificate Name)", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "server-name-list"
        self.DeviceProxy = ""
        self.server_name = ""
        self.server_key = ""
        self.server_passphrase = ""
        self.server_encrypted = ""
        self.server_cert = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CaCerts(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ca_cert: {"minLength": 1, "maxLength": 255, "type": "string", "description": "CA Certificate (CA Certificate Name)", "format": "string"}
    :param client_ocsp: {"default": 0, "type": "number", "description": "Specify ocsp authentication server(s) for client certificate verification", "format": "flag"}
    :param client_ocsp_sg: {"description": "Specify service-group (Service group name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/aam/authentication/service-group"}
    :param client_ocsp_srvr: {"description": "Specify authentication server", "format": "string-rlx", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authentication/server/ocsp"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ca-certs"
        self.DeviceProxy = ""
        self.ca_cert = ""
        self.client_ocsp = ""
        self.client_ocsp_sg = ""
        self.client_ocsp_srvr = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class CipherWithoutPrioList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cipher_wo_prio: {"enum": ["SSL3_RSA_DES_192_CBC3_SHA", "SSL3_RSA_DES_40_CBC_SHA", "SSL3_RSA_DES_64_CBC_SHA", "SSL3_RSA_RC4_128_MD5", "SSL3_RSA_RC4_128_SHA", "SSL3_RSA_RC4_40_MD5", "TLS1_RSA_AES_128_SHA", "TLS1_RSA_AES_256_SHA", "TLS1_RSA_EXPORT1024_RC4_56_MD5", "TLS1_RSA_EXPORT1024_RC4_56_SHA", "TLS1_RSA_AES_128_SHA256", "TLS1_RSA_AES_256_SHA256"], "type": "string", "description": "'SSL3_RSA_DES_192_CBC3_SHA': SSL3_RSA_DES_192_CBC3_SHA; 'SSL3_RSA_DES_40_CBC_SHA': SSL3_RSA_DES_40_CBC_SHA; 'SSL3_RSA_DES_64_CBC_SHA': SSL3_RSA_DES_64_CBC_SHA; 'SSL3_RSA_RC4_128_MD5': SSL3_RSA_RC4_128_MD5; 'SSL3_RSA_RC4_128_SHA': SSL3_RSA_RC4_128_SHA; 'SSL3_RSA_RC4_40_MD5': SSL3_RSA_RC4_40_MD5; 'TLS1_RSA_AES_128_SHA': TLS1_RSA_AES_128_SHA; 'TLS1_RSA_AES_256_SHA': TLS1_RSA_AES_256_SHA; 'TLS1_RSA_EXPORT1024_RC4_56_MD5': TLS1_RSA_EXPORT1024_RC4_56_MD5; 'TLS1_RSA_EXPORT1024_RC4_56_SHA': TLS1_RSA_EXPORT1024_RC4_56_SHA; 'TLS1_RSA_AES_128_SHA256': TLS1_RSA_AES_128_SHA256; 'TLS1_RSA_AES_256_SHA256': TLS1_RSA_AES_256_SHA256; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cipher-without-prio-list"
        self.DeviceProxy = ""
        self.cipher_wo_prio = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class StartsWithList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param starts_with: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string starts with another string", "format": "string-rlx"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "starts-with-list"
        self.DeviceProxy = ""
        self.starts_with = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ClientSsl(A10BaseClass):
    
    """Class Description::
    Client SSL Template.

    Class client-ssl supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param chain_cert: {"description": "Chain Certificate (Chain Certificate Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param session_cache_timeout: {"description": "Session Cache Timeout (Timeout value, in seconds)", "format": "number", "type": "number", "maximum": 604800, "minimum": 0, "optional": true}
    :param ocspst_sg: {"description": "Specify authentication service group", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "not": "ocspst-srvr", "type": "string", "$ref": "/axapi/v3/aam/authentication/service-group"}
    :param auth_username: {"description": "Specify the Username Field in the Client Certificate(If multi-fields are specificed, prior one has higher priority)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param authorization: {"default": 0, "optional": true, "type": "number", "description": "Specify LDAP server for client SSL authorizaiton", "format": "flag"}
    :param ocspst_sg_hours: {"description": "Specify update period, in hours", "format": "number", "optional": true, "not-list": ["ocspst-sg-days", "ocspst-sg-minutes"], "maximum": 44640, "minimum": 1, "type": "number"}
    :param ocspst_sg_days: {"description": "Specify update period, in days", "format": "number", "optional": true, "not-list": ["ocspst-sg-hours", "ocspst-sg-minutes"], "maximum": 31, "minimum": 1, "type": "number"}
    :param ldap_search_filter: {"description": "Specify LDAP search filter", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param authen_name: {"description": "Specify authorization LDAP server name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "not": "auth-sg", "type": "string", "$ref": "/axapi/v3/aam/authentication/server/ldap"}
    :param ocsp_stapling: {"default": 0, "optional": true, "type": "number", "description": "Config OCSP stapling support", "format": "flag"}
    :param forward_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param ocspst_srvr: {"description": "Specify OCSP authentication server", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "not": "ocspst-sg", "type": "string", "$ref": "/axapi/v3/aam/authentication/server/ocsp"}
    :param class_list_name: {"description": "Class List Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param forward_proxy_ca_cert: {"description": "CA Certificate for forward proxy (SSL forward proxy CA Certificate Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param ocspst_sg_timeout: {"description": "Specify retry timeout (Default is 30 mins)", "format": "number", "type": "number", "maximum": 44640, "minimum": 1, "optional": true}
    :param ssl_false_start_disable: {"default": 0, "optional": true, "type": "number", "description": "disable SSL False Start", "format": "flag"}
    :param key_passphrase: {"description": "Password Phrase", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param template_cipher: {"description": "Cipher Template (Cipher Config Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param ocspst_srvr_minutes: {"description": "Specify update period, in minutes", "format": "number", "optional": true, "not-list": ["ocspst-srvr-days", "ocspst-srvr-hours"], "maximum": 60, "minimum": 1, "type": "number"}
    :param auth_sg: {"description": "Specify authorization LDAP service group", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "not": "authen-name", "type": "string", "$ref": "/axapi/v3/aam/authentication/service-group"}
    :param key_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param equals_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "equals": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string equals another string", "format": "string-rlx"}}}]}
    :param session_ticket_lifetime: {"optional": true, "type": "number", "description": "Session ticket lieftime in seconds from stateless session resumption (Lifetime value in seconds)", "format": "number"}
    :param forward_passphrase: {"description": "Password Phrase", "format": "password", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param ldap_base_dn_from_cert: {"default": 0, "optional": true, "type": "number", "description": "Use Subject DN as LDAP search base DN", "format": "flag"}
    :param contains_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"contains": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string contains another string", "format": "string-rlx"}, "optional": true}}]}
    :param forward_proxy_ca_key: {"description": "CA Private Key for forward proxy (SSL forward proxy CA Key Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param ocspst_srvr_days: {"description": "Specify update period, in days", "format": "number", "optional": true, "not-list": ["ocspst-srvr-hours", "ocspst-srvr-minutes"], "maximum": 31, "minimum": 1, "type": "number"}
    :param session_cache_size: {"description": "Session Cache Size (Specify 0 to disable Session ID reuse.)", "format": "number", "type": "number", "maximum": 8000000, "minimum": 0, "optional": true}
    :param client_certificate: {"description": "'Ignore': Don't request client certificate; 'Require': Require client certificate; 'Request': Request client certificate; ", "format": "enum", "default": "Ignore", "type": "string", "enum": ["Ignore", "Require", "Request"], "optional": true}
    :param ends_with_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ends-with": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string ends with another string", "format": "string-rlx"}, "optional": true}}]}
    :param ocspst_ca_cert: {"description": "CA certificate", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param ocspst_ocsp: {"default": 0, "optional": true, "type": "number", "description": "Specify OCSP Authentication", "format": "flag"}
    :param forward_proxy_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable SSL forward proxy", "format": "flag"}
    :param key: {"description": "Server Private Key (Key Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param sslv2_bypass_service_group: {"description": "Service Group for Bypass SSLV2 (Service Group Name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/service-group"}
    :param server_name_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"server-name": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Server name indication in Client hello extension (Server name String)", "format": "string"}, "server-key": {"minLength": 1, "maxLength": 255, "type": "string", "description": "Server Private Key associated to SNI (Server Private Key Name)", "format": "string"}, "server-passphrase": {"minLength": 1, "maxLength": 63, "type": "string", "description": "help Password Phrase", "format": "password"}, "optional": true, "server-encrypted": {"type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}, "server-cert": {"minLength": 1, "maxLength": 255, "type": "string", "description": "Server Certificate associated to SNI (Server Certificate Name)", "format": "string"}}}]}
    :param auth_sg_filter: {"description": "Specify LDAP search filter", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param ca_certs: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ca-cert": {"minLength": 1, "maxLength": 255, "type": "string", "description": "CA Certificate (CA Certificate Name)", "format": "string"}, "client-ocsp": {"default": 0, "type": "number", "description": "Specify ocsp authentication server(s) for client certificate verification", "format": "flag"}, "client-ocsp-sg": {"description": "Specify service-group (Service group name)", "format": "string-rlx", "minLength": 1, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/aam/authentication/service-group"}, "optional": true, "client-ocsp-srvr": {"description": "Specify authentication server", "format": "string-rlx", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/aam/authentication/server/ocsp"}}}]}
    :param disable_sslv3: {"default": 0, "optional": true, "type": "number", "description": "Reject Client requests for SSL version 3", "format": "flag"}
    :param ocspst_srvr_timeout: {"description": "Specify retry timeout (Default is 30 mins)", "format": "number", "type": "number", "maximum": 44640, "minimum": 1, "optional": true}
    :param name: {"description": "Client SSL Template Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param auth_sg_dn: {"default": 0, "optional": true, "type": "number", "description": "Use Subject DN as LDAP search base DN", "format": "flag"}
    :param ocspst_sg_period: {"default": 0, "optional": true, "type": "number", "description": "Specify certificate status update period (Default is 1 hour)", "format": "flag"}
    :param ocspst_srvr_hours: {"description": "Specify update period, in hours", "format": "number", "optional": true, "not-list": ["ocspst-srvr-days", "ocspst-srvr-minutes"], "maximum": 44640, "minimum": 1, "type": "number"}
    :param cert: {"description": "Server Certificate (Certificate Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param ocspst_srvr_period: {"default": 0, "optional": true, "type": "number", "description": "Specify certificate status update period (Default is 1 hour)", "format": "flag"}
    :param crl: {"description": "Certificate Revocation Lists (Certificate Revocation Lists file name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param case_insensitive: {"default": 0, "optional": true, "type": "number", "description": "Case insensitive forward proxy bypass", "format": "flag"}
    :param cipher_without_prio_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"cipher-wo-prio": {"enum": ["SSL3_RSA_DES_192_CBC3_SHA", "SSL3_RSA_DES_40_CBC_SHA", "SSL3_RSA_DES_64_CBC_SHA", "SSL3_RSA_RC4_128_MD5", "SSL3_RSA_RC4_128_SHA", "SSL3_RSA_RC4_40_MD5", "TLS1_RSA_AES_128_SHA", "TLS1_RSA_AES_256_SHA", "TLS1_RSA_EXPORT1024_RC4_56_MD5", "TLS1_RSA_EXPORT1024_RC4_56_SHA", "TLS1_RSA_AES_128_SHA256", "TLS1_RSA_AES_256_SHA256"], "type": "string", "description": "'SSL3_RSA_DES_192_CBC3_SHA': SSL3_RSA_DES_192_CBC3_SHA; 'SSL3_RSA_DES_40_CBC_SHA': SSL3_RSA_DES_40_CBC_SHA; 'SSL3_RSA_DES_64_CBC_SHA': SSL3_RSA_DES_64_CBC_SHA; 'SSL3_RSA_RC4_128_MD5': SSL3_RSA_RC4_128_MD5; 'SSL3_RSA_RC4_128_SHA': SSL3_RSA_RC4_128_SHA; 'SSL3_RSA_RC4_40_MD5': SSL3_RSA_RC4_40_MD5; 'TLS1_RSA_AES_128_SHA': TLS1_RSA_AES_128_SHA; 'TLS1_RSA_AES_256_SHA': TLS1_RSA_AES_256_SHA; 'TLS1_RSA_EXPORT1024_RC4_56_MD5': TLS1_RSA_EXPORT1024_RC4_56_MD5; 'TLS1_RSA_EXPORT1024_RC4_56_SHA': TLS1_RSA_EXPORT1024_RC4_56_SHA; 'TLS1_RSA_AES_128_SHA256': TLS1_RSA_AES_128_SHA256; 'TLS1_RSA_AES_256_SHA256': TLS1_RSA_AES_256_SHA256; ", "format": "enum"}, "optional": true}}]}
    :param ocspst_sg_minutes: {"description": "Specify update period, in minutes", "format": "number", "optional": true, "not-list": ["ocspst-sg-days", "ocspst-sg-hours"], "maximum": 60, "minimum": 1, "type": "number"}
    :param starts_with_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"starts-with": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Forward proxy bypass if SNI string starts with another string", "format": "string-rlx"}, "optional": true}}]}
    :param close_notify: {"default": 0, "optional": true, "type": "number", "description": "Send close notification when terminate connection", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/client-ssl/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "client-ssl"
        self.a10_url="/axapi/v3/slb/template/client-ssl/{name}"
        self.DeviceProxy = ""
        self.chain_cert = ""
        self.session_cache_timeout = ""
        self.ocspst_sg = ""
        self.auth_username = ""
        self.authorization = ""
        self.ocspst_sg_hours = ""
        self.ocspst_sg_days = ""
        self.ldap_search_filter = ""
        self.authen_name = ""
        self.ocsp_stapling = ""
        self.forward_encrypted = ""
        self.ocspst_srvr = ""
        self.class_list_name = ""
        self.forward_proxy_ca_cert = ""
        self.ocspst_sg_timeout = ""
        self.ssl_false_start_disable = ""
        self.key_passphrase = ""
        self.template_cipher = ""
        self.ocspst_srvr_minutes = ""
        self.auth_sg = ""
        self.key_encrypted = ""
        self.equals_list = []
        self.session_ticket_lifetime = ""
        self.forward_passphrase = ""
        self.ldap_base_dn_from_cert = ""
        self.contains_list = []
        self.forward_proxy_ca_key = ""
        self.ocspst_srvr_days = ""
        self.session_cache_size = ""
        self.client_certificate = ""
        self.ends_with_list = []
        self.ocspst_ca_cert = ""
        self.ocspst_ocsp = ""
        self.forward_proxy_enable = ""
        self.key = ""
        self.sslv2_bypass_service_group = ""
        self.server_name_list = []
        self.auth_sg_filter = ""
        self.ca_certs = []
        self.disable_sslv3 = ""
        self.ocspst_srvr_timeout = ""
        self.name = ""
        self.auth_sg_dn = ""
        self.ocspst_sg_period = ""
        self.ocspst_srvr_hours = ""
        self.cert = ""
        self.ocspst_srvr_period = ""
        self.crl = ""
        self.case_insensitive = ""
        self.cipher_without_prio_list = []
        self.ocspst_sg_minutes = ""
        self.starts_with_list = []
        self.close_notify = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


