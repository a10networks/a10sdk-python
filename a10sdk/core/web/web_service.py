from a10sdk.common.A10BaseClass import A10BaseClass


class WebService(A10BaseClass):
    
    """Class Description::
    Configure Web Services.

    Class web-service supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param axapi_session_limit: {"description": "Set Web service axapi Session Limit (Session limit (default 30))", "format": "number", "default": 30, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param axapi_idle: {"description": "Idle timeout of a xml service connection in minutes (Connection idle timeout value in minutes)", "partition-visibility": "shared", "default": 10, "optional": true, "format": "number", "maximum": 60, "minimum": 0, "type": "number"}
    :param server_disable: {"description": "Disable", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param secure_port: {"description": "Set web secure server port number for listening (Secure Port Number(default 443))", "partition-visibility": "shared", "default": 443, "optional": true, "format": "number", "maximum": 65535, "minimum": 1, "type": "number"}
    :param auto_redirt_disable: {"description": "Diable", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param port: {"description": "Set Web Server Port (Port number(default 80))", "partition-visibility": "shared", "default": 80, "optional": true, "format": "number", "maximum": 65535, "minimum": 1, "type": "number"}
    :param secure_server_disable: {"description": "Disable", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/web-service`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "web-service"
        self.a10_url="/axapi/v3/web-service"
        self.DeviceProxy = ""
        self.axapi_session_limit = ""
        self.axapi_idle = ""
        self.server_disable = ""
        self.secure_port = ""
        self.auto_redirt_disable = ""
        self.port = ""
        self.secure_server_disable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


