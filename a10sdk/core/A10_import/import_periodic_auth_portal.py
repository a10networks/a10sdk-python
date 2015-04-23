from a10sdk.common.A10BaseClass import A10BaseClass


class AuthPortal(A10BaseClass):
    
    """Class Description::
    Portal file for http authentication.

    Class auth-portal supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param remote_file: {"optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param auth_portal: {"description": "Portal file for http authentication", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param period: {"description": "Specify the period in second", "format": "number", "type": "number", "maximum": 31536000, "minimum": 60, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/import-periodic/auth-portal/{auth_portal}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "auth_portal"]

        self.b_key = "auth-portal"
        self.a10_url="/axapi/v3/import-periodic/auth-portal/{auth_portal}"
        self.DeviceProxy = ""
        self.remote_file = ""
        self.uuid = ""
        self.use_mgmt_port = ""
        self.auth_portal = ""
        self.period = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


