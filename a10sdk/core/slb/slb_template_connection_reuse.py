from a10sdk.common.A10BaseClass import A10BaseClass


class ConnectionReuse(A10BaseClass):
    
    """Class Description::
    Connection Reuse.

    Class connection-reuse supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param preopen: {"default": 0, "optional": true, "type": "number", "description": "Preopen server connection", "format": "flag"}
    :param name: {"description": "Connection Reuse Template Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param keep_alive_conn: {"default": 0, "optional": true, "type": "number", "description": "Keep a number of server connections open", "format": "flag"}
    :param timeout: {"description": "Timeout in seconds. Multiple of 60 (def 2400)", "format": "number", "default": 2400, "optional": true, "maximum": 3600, "minimum": 60, "type": "number"}
    :param num_conn_per_port: {"description": "Connections per Server Port (default 100)", "format": "number", "default": 100, "optional": true, "maximum": 1024, "minimum": 1, "type": "number"}
    :param limit_per_server: {"description": "Max Server Connections allowed (Connections per Server Port (default 1000))", "format": "number", "default": 1000, "optional": true, "maximum": 65535, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/connection-reuse/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "connection-reuse"
        self.a10_url="/axapi/v3/slb/template/connection-reuse/{name}"
        self.DeviceProxy = ""
        self.preopen = ""
        self.name = ""
        self.keep_alive_conn = ""
        self.timeout = ""
        self.num_conn_per_port = ""
        self.limit_per_server = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


