from a10sdk.common.A10BaseClass import A10BaseClass


class Copy(A10BaseClass):
    
    """    :param profile: {"description": "From Startup-config Profile", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param dest_profile: {"description": "Local Configuration Profile Name", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param dest_remote_file: {"optional": true, "type": "string", "description": "Remote file path", "format": "url"}
    :param remote_file: {"optional": true, "type": "string", "description": "Remote file path", "format": "url"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param dest_use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as destination port", "format": "flag"}
    :param startup_config: {"default": 0, "optional": true, "type": "number", "description": "From Startup Config", "format": "flag"}
    :param to_profile: {"description": "To Local Configuration Profile", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param to_startup_config: {"default": 0, "optional": true, "type": "number", "description": "To Startup Config", "format": "flag"}
    :param running_config: {"default": 0, "optional": true, "type": "number", "description": "From Running Config", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Copy configuration to/from remote server.

    Class copy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/copy`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "copy"
        self.a10_url="/axapi/v3/copy"
        self.DeviceProxy = ""
        self.profile = ""
        self.dest_profile = ""
        self.dest_remote_file = ""
        self.remote_file = ""
        self.use_mgmt_port = ""
        self.dest_use_mgmt_port = ""
        self.startup_config = ""
        self.to_profile = ""
        self.to_startup_config = ""
        self.running_config = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


