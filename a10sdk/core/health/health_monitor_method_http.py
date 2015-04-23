from a10sdk.common.A10BaseClass import A10BaseClass


class HttpKerberosKdc(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param http_kerberos_hostipv6: {"not": "http-kerberos-hostip", "type": "string", "description": "Server's IPV6 address", "format": "ipv6-address"}
    :param http_kerberos_port: {"description": "Specify the kdc port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param http_kerberos_portv6: {"description": "Specify the kdc port", "minimum": 1, "type": "number", "maximum": 65535, "format": "number"}
    :param http_kerberos_hostip: {"description": "Kdc's hostname or IP address", "format": "host", "minLength": 1, "maxLength": 31, "not": "http-kerberos-hostipv6", "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "http-kerberos-kdc"
        self.DeviceProxy = ""
        self.http_kerberos_hostipv6 = ""
        self.http_kerberos_port = ""
        self.http_kerberos_portv6 = ""
        self.http_kerberos_hostip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Http(A10BaseClass):
    
    """Class Description::
    HTTP type.

    Class http supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param http_url: {"default": 0, "optional": true, "type": "number", "description": "Specify URL string, default is GET /", "format": "flag"}
    :param http_maintenance_code: {"description": "Specify response code for maintenance (Format is xx,xx-xx (xx between [100, 899]))", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param http_kerberos_auth: {"default": 0, "optional": true, "type": "number", "description": "Http Kerberos Auth", "format": "flag"}
    :param http_postfile: {"description": "Specify the HTTP post data (Input post data file name here)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param post_type: {"optional": true, "enum": ["postdata", "postfile"], "type": "string", "description": "'postdata': Specify the HTTP post data; 'postfile': Specify the HTTP post data; ", "format": "enum"}
    :param http_password_string: {"description": "Specify password, '' means empty passworddd", "format": "password", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param url_path: {"description": "Specify URL path, default is \"/\"", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 500, "type": "string"}
    :param http_response_code: {"description": "Specify response code range (e.g. 200,400-430) (Format is xx,xx-xx (xx between [100, 899]))", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "not": "http-text", "type": "string"}
    :param http_host: {"description": "Specify \"Host:\" header used in request (enclose IPv6 address in [])", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param http: {"default": 0, "optional": true, "type": "number", "description": "HTTP type", "format": "flag"}
    :param url_type: {"optional": true, "enum": ["GET", "POST", "HEAD"], "type": "string", "description": "'GET': HTTP GET method; 'POST': HTTP POST method; 'HEAD': HTTP HEAD method; ", "format": "enum"}
    :param http_postdata: {"description": "Specify the HTTP post data (Input post data here)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param http_text: {"description": "Specify text expected", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "not": "http-response-code", "type": "string"}
    :param http_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param http_kerberos_realm: {"description": "Specify realm of Kerberos server", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param http_password: {"default": 0, "optional": true, "type": "number", "description": "Specify the user password", "format": "flag"}
    :param http_expect: {"default": 0, "optional": true, "type": "number", "description": "Specify what you expect from the response message", "format": "flag"}
    :param post_path: {"description": "Specify URL path, default is \"/\"", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 500, "type": "string"}
    :param http_username: {"description": "Specify the username", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param http_port: {"description": "Specify HTTP Port (Specify port number (default 80))", "format": "number", "default": 80, "optional": true, "maximum": 65534, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/http`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "http"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/http"
        self.DeviceProxy = ""
        self.http_url = ""
        self.http_maintenance_code = ""
        self.http_kerberos_auth = ""
        self.http_postfile = ""
        self.uuid = ""
        self.post_type = ""
        self.http_password_string = ""
        self.url_path = ""
        self.http_response_code = ""
        self.http_host = ""
        self.http = ""
        self.url_type = ""
        self.http_postdata = ""
        self.http_text = ""
        self.http_encrypted = ""
        self.http_kerberos_realm = ""
        self.http_password = ""
        self.http_kerberos_kdc = {}
        self.http_expect = ""
        self.post_path = ""
        self.http_username = ""
        self.http_port = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


