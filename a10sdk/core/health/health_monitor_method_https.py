from a10sdk.common.A10BaseClass import A10BaseClass


class HttpsKerberosKdc(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param https_kerberos_portv6: {"description": "Specify the kdc port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param https_kerberos_port: {"description": "Specify the kdc port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param https_kerberos_hostip: {"description": "Kdc's hostname or IP address", "format": "host", "minLength": 1, "maxLength": 31, "not": "https-kerberos-hostipv6", "type": "string"}
    :param https_kerberos_hostipv6: {"not": "https-kerberos-hostip", "type": "string", "description": "Server's IPV6 address", "format": "ipv6-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "https-kerberos-kdc"
        self.DeviceProxy = ""
        self.https_kerberos_portv6 = ""
        self.https_kerberos_port = ""
        self.https_kerberos_hostip = ""
        self.https_kerberos_hostipv6 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Https(A10BaseClass):
    
    """Class Description::
    HTTPS type.

    Class https supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param https_kerberos_realm: {"description": "Specify realm of Kerberos server", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param post_type: {"optional": true, "enum": ["postdata", "postfile"], "type": "string", "description": "'postdata': Specify the HTTP post data; 'postfile': Specify the HTTP post data; ", "format": "enum"}
    :param url_path: {"description": "Specify URL path, default is \"/\"", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 500, "type": "string"}
    :param https_username: {"description": "Specify the username", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param key_phrase: {"description": "Password Phrase", "format": "password", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param https_postdata: {"description": "Specify the HTTP post data (Input post data here)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param https_key_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param https_expect: {"default": 0, "optional": true, "type": "number", "description": "Specify what you expect from the response message", "format": "flag"}
    :param https: {"default": 0, "optional": true, "type": "number", "description": "HTTPS type", "format": "flag"}
    :param https_host: {"description": "Specify \"Host:\" header used in request (enclose IPv6 address in [])", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param key_pass_phrase: {"default": 0, "optional": true, "type": "number", "description": "Client private key password phrase", "format": "flag"}
    :param https_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param url_type: {"optional": true, "enum": ["GET", "POST", "HEAD"], "type": "string", "description": "'GET': HTTP GET method; 'POST': HTTP POST method; 'HEAD': HTTP HEAD method; ", "format": "enum"}
    :param web_port: {"description": "Specify HTTPS port (Port Number (default 443))", "format": "number", "default": 443, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param disable_sslv2hello: {"default": 0, "optional": true, "type": "number", "description": "Disable SSLv2Hello for HTTPs", "format": "flag"}
    :param key: {"description": "Specify client private key (Key name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param https_password_string: {"description": "help Configure password, '' means empty passworddd", "format": "password", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param post_path: {"description": "Specify URL path, default is \"/\"", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 500, "type": "string"}
    :param https_postfile: {"description": "Specify the HTTP post data (Input post data file name here)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param https_password: {"default": 0, "optional": true, "type": "number", "description": "Specify the user password", "format": "flag"}
    :param cert: {"description": "Specify client certificate (Certificate name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param https_text: {"description": "Specify text expected", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "not": "https-response-code", "type": "string"}
    :param https_response_code: {"description": "Specify response code range (e.g. 200,400-430) (Format is xx,xx-xx (xx between [100, 899])", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "not": "https-text", "type": "string"}
    :param https_kerberos_auth: {"default": 0, "optional": true, "type": "number", "description": "Https Kerberos Auth", "format": "flag"}
    :param https_maintenance_code: {"description": "Specify response code for maintenance (Format is xx,xx-xx (xx between [100, 899])", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param https_url: {"default": 0, "optional": true, "type": "number", "description": "Specify URL string, default is GET /", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/https`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "https"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/https"
        self.DeviceProxy = ""
        self.https_kerberos_realm = ""
        self.post_type = ""
        self.url_path = ""
        self.https_username = ""
        self.key_phrase = ""
        self.https_postdata = ""
        self.https_key_encrypted = ""
        self.https_expect = ""
        self.https = ""
        self.https_host = ""
        self.key_pass_phrase = ""
        self.https_encrypted = ""
        self.url_type = ""
        self.web_port = ""
        self.disable_sslv2hello = ""
        self.https_kerberos_kdc = {}
        self.key = ""
        self.https_password_string = ""
        self.post_path = ""
        self.https_postfile = ""
        self.https_password = ""
        self.cert = ""
        self.https_text = ""
        self.https_response_code = ""
        self.https_kerberos_auth = ""
        self.https_maintenance_code = ""
        self.https_url = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


