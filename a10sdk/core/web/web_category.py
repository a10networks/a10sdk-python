from a10sdk.common.A10BaseClass import A10BaseClass


class WebCategory(A10BaseClass):
    
    """    :param cloud_query_disable: {"description": "Disables cloud queries for URL's not present in local database(default enable)", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param rtu_update_interval: {"description": "Interval to check for real time updates if enabled in mins(default 60)", "partition-visibility": "shared", "default": 60, "optional": true, "format": "number", "maximum": 14400, "minimum": 10, "type": "number"}
    :param enable: {"description": "Enable BrightCloud SDK", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param use_mgmt_port: {"description": "Use management interface for all communication with BrightCloud", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param database_server: {"description": "BrightCloud Database Server", "partition-visibility": "shared", "minLength": 1, "format": "string", "optional": true, "maxLength": 255, "type": "string"}
    :param db_update_time: {"optional": true, "partition-visibility": "shared", "type": "string", "description": "Time of day to update database (default: 00:00)", "format": "time-hhmm"}
    :param server_timeout: {"description": "BrightCloud Servers Timeout in seconds (default: 30s)", "partition-visibility": "shared", "default": 30, "optional": true, "format": "number", "maximum": 300, "minimum": 1, "type": "number"}
    :param server: {"description": "BrightCloud Query Server", "partition-visibility": "shared", "minLength": 1, "format": "string", "optional": true, "maxLength": 255, "type": "string"}
    :param remote_syslog_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable data plane logging to a remote syslog server", "format": "flag"}
    :param rtu_update_disable: {"description": "Disables real time updates(default enable)", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param port: {"description": "BrightCloud Query Server Listening Port(default 80)", "partition-visibility": "shared", "default": 80, "optional": true, "format": "number", "maximum": 65535, "minimum": 1, "type": "number"}
    :param ssl_port: {"description": "BrightCloud Servers SSL Port(default 443)", "partition-visibility": "shared", "default": 443, "optional": true, "format": "number", "maximum": 65535, "minimum": 1, "type": "number"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Web-Category Commands.

    Class web-category supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/web-category`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "web-category"
        self.a10_url="/axapi/v3/web-category"
        self.DeviceProxy = ""
        self.cloud_query_disable = ""
        self.rtu_update_interval = ""
        self.enable = ""
        self.use_mgmt_port = ""
        self.database_server = ""
        self.db_update_time = ""
        self.server_timeout = ""
        self.server = ""
        self.remote_syslog_enable = ""
        self.rtu_update_disable = ""
        self.port = ""
        self.ssl_port = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


