from a10sdk.common.A10BaseClass import A10BaseClass


class Cookie(A10BaseClass):
    
    """Class Description::
    Cookie persistence.

    Class cookie supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param domain: {"description": "Set cookie domain", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param secure: {"default": 0, "optional": true, "type": "number", "description": "Enable secure attribute", "format": "flag"}
    :param cookie_name: {"description": "Set cookie name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param dont_honor_conn_rules: {"default": 0, "optional": true, "type": "number", "description": "Do not observe connection rate rules", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param server: {"description": "Persist to the same server, default is port", "format": "flag", "default": 0, "optional": true, "not": "service-group", "type": "number"}
    :param server_service_group: {"default": 0, "optional": true, "type": "number", "description": "Persist to the same server and within the same service group", "format": "flag"}
    :param service_group: {"description": "Persist within the same service group", "format": "flag", "default": 0, "optional": true, "not": "server", "type": "number"}
    :param expire: {"description": "Set cookie expiration time (Expiration in seconds)", "format": "number", "type": "number", "maximum": 31536000, "minimum": 0, "optional": true}
    :param match_type: {"default": 0, "optional": true, "type": "number", "description": "Persist for server, default is port", "format": "flag"}
    :param path: {"description": "Set cookie path (Cookie path, default is \"/\")", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param pass_thru: {"default": 0, "optional": true, "type": "number", "description": "Pass thru mode - Server sends the persist cookie", "format": "flag"}
    :param scan_all_members: {"default": 0, "optional": true, "type": "number", "description": "Persist within the same server SCAN", "format": "flag"}
    :param insert_always: {"default": 0, "optional": true, "type": "number", "description": "Insert persist cookie to every reponse", "format": "flag"}
    :param httponly: {"default": 0, "optional": true, "type": "number", "description": "Enable HttpOnly attribute", "format": "flag"}
    :param name: {"description": "Cookie persistence (Cookie persistence template name)", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/persist/cookie/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "cookie"
        self.a10_url="/axapi/v3/slb/template/persist/cookie/{name}"
        self.DeviceProxy = ""
        self.domain = ""
        self.secure = ""
        self.cookie_name = ""
        self.dont_honor_conn_rules = ""
        self.uuid = ""
        self.server = ""
        self.server_service_group = ""
        self.service_group = ""
        self.expire = ""
        self.match_type = ""
        self.path = ""
        self.pass_thru = ""
        self.scan_all_members = ""
        self.insert_always = ""
        self.httponly = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


