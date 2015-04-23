from a10sdk.common.A10BaseClass import A10BaseClass


class HttpAlg(A10BaseClass):
    
    """Class Description::
    HTTP-ALG Template.

    Class http-alg supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param header_name_client_ip: {"description": "Header name (default: X-Forwarded-For)", "format": "string", "default": "X-Forwarded-For", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param retry: {"description": "Specify the maximum retries allowed for sending an request to a RADIUS server (default 2) (The maximum retries allowed for sending an request to the radius server (default 2))", "format": "number", "default": 2, "optional": true, "maximum": 3, "minimum": 0, "type": "number"}
    :param retry_svr_num: {"description": "Specify the maximum RADIUS servers allowed to try (default 0)", "format": "number", "default": 0, "optional": true, "maximum": 1, "minimum": 0, "type": "number"}
    :param name: {"description": "HTTP-ALG template name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param request_insert_msisdn: {"default": 0, "optional": true, "type": "number", "description": "Insert MSISDN into HTTP request", "format": "flag"}
    :param radius_sg: {"description": "RADIUS service group (RADIUS service group name)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/cgnv6/service-group"}
    :param encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED secret string)", "format": "encrypted"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param request_insert_client_ip: {"default": 0, "optional": true, "type": "number", "description": "Insert Client IP into HTTP request", "format": "flag"}
    :param header_name_msisdn: {"description": "Header name (default: X-MSISDN)", "format": "string", "default": "X-MSISDN", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param timeout: {"description": "The maximum time allowed for waiting for a response from a radius server (default 2)", "format": "number", "default": 2, "optional": true, "maximum": 3, "minimum": 1, "type": "number"}
    :param include_tunnel_ip: {"default": 0, "optional": true, "type": "number", "description": "Include the tunnel IP (applies to DS-Lite and 6RD-NAT64 sessions)", "format": "flag"}
    :param method: {"description": "'append': Append if there is already a header (default); 'replace': Replace if there is already a header; ", "format": "enum", "default": "append", "type": "string", "enum": ["append", "replace"], "optional": true}
    :param secret_string: {"description": "The RADIUS secret", "format": "password", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/template/http-alg/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "http-alg"
        self.a10_url="/axapi/v3/cgnv6/template/http-alg/{name}"
        self.DeviceProxy = ""
        self.header_name_client_ip = ""
        self.retry = ""
        self.retry_svr_num = ""
        self.name = ""
        self.request_insert_msisdn = ""
        self.radius_sg = ""
        self.encrypted = ""
        self.uuid = ""
        self.request_insert_client_ip = ""
        self.header_name_msisdn = ""
        self.timeout = ""
        self.include_tunnel_ip = ""
        self.method = ""
        self.secret_string = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


