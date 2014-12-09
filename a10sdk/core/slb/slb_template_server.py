from a10sdk.common.A10BaseClass import A10BaseClass


class Server(A10BaseClass):
    
    """Class Description::
    Server template.

    Class server supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param health_check_disable: {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param stats_data_action: {"description": "'stats-data-enable': Enable statistical data collection for real server; 'stats-data-disable': Disable statistical data collection for real server; ", "format": "enum", "default": "stats-data-enable", "type": "string", "enum": ["stats-data-enable", "stats-data-disable"], "optional": true}
    :param spoofing_cache: {"default": 0, "optional": true, "type": "number", "description": "Servers under the template are spoofing cache", "format": "flag"}
    :param weight: {"description": "Weight for the Real Servers (Connection Weight)", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}
    :param slow_start: {"default": 0, "optional": true, "type": "number", "description": "Slowly ramp up the connection number after server is up", "format": "flag"}
    :param conn_limit: {"description": "Connection limit", "format": "number", "type": "number", "maximum": 8000000, "minimum": 1, "optional": true}
    :param initial_slow_start: {"description": "Initial slow start connection limit (default 128)", "format": "number", "default": 128, "optional": true, "maximum": 4095, "minimum": 1, "type": "number"}
    :param max_dynamic_server: {"description": "Maximum dynamic server number (Maximum dynamic server number (default is 255))", "format": "number", "default": 255, "optional": true, "maximum": 1023, "minimum": 1, "type": "number"}
    :param rate_interval: {"description": "'100ms': Use 100 ms as sampling interval; 'second': Use 1 second as sampling interval; ", "format": "enum", "default": "second", "type": "string", "enum": ["100ms", "second"], "optional": true}
    :param till: {"description": "Slow start ends when slow start connection limit reaches a number (default 4096) (Slow start ends when connection limit reaches this number)", "format": "number", "default": 4096, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param add: {"description": "Slow start connection limit add by a number every interval (Add by this number every interval)", "format": "number", "optional": true, "maximum": 4095, "minimum": 1, "not": "times", "type": "number"}
    :param min_ttl_ratio: {"description": "Minimum TTL to DNS query interval ratio (Minimum TTL ratio (default is 2))", "format": "number", "default": 2, "optional": true, "maximum": 15, "minimum": 1, "type": "number"}
    :param dynamic_server_prefix: {"description": "Prefix of dynamic server (Prefix of dynamic server (default is \"DRS\"))", "format": "string", "default": "DRS", "minLength": 1, "optional": true, "maxLength": 3, "type": "string"}
    :param resume: {"description": "Resume accepting new connection after connection number drops below threshold (Connection resume threshold)", "format": "number", "type": "number", "maximum": 1048575, "minimum": 1, "optional": true}
    :param every: {"description": "Slow start connection limit increment interval (default 10)", "format": "number", "default": 10, "optional": true, "maximum": 60, "minimum": 1, "type": "number"}
    :param conn_limit_no_logging: {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}
    :param extended_stats: {"default": 0, "optional": true, "type": "number", "description": "Enable extended statistics on real server", "format": "flag"}
    :param conn_rate_limit_no_logging: {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}
    :param name: {"description": "Server template name", "format": "string", "default": "default", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param times: {"description": "Slow start connection limit multiply by a number every interval (default 2) (Multiply by this number every interval)", "format": "number", "default": 2, "optional": true, "maximum": 10, "minimum": 2, "not": "add", "type": "number"}
    :param log_selection_failure: {"default": 0, "optional": true, "type": "number", "description": "Enable real-time logging for server selection failure event", "format": "flag"}
    :param conn_rate_limit: {"description": "Connection rate limit", "format": "number", "type": "number", "maximum": 1048575, "minimum": 1, "optional": true}
    :param dns_query_interval: {"description": "The interval to query DNS server for the hostname (DNS query interval (in minute, default is 10))", "format": "number", "default": 10, "optional": true, "maximum": 1440, "minimum": 1, "type": "number"}
    :param health_check: {"description": "Health Check Monitor (Health monitor name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/server/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "server"
        self.a10_url="/axapi/v3/slb/template/server/{name}"
        self.DeviceProxy = ""
        self.health_check_disable = ""
        self.stats_data_action = ""
        self.spoofing_cache = ""
        self.weight = ""
        self.slow_start = ""
        self.conn_limit = ""
        self.initial_slow_start = ""
        self.max_dynamic_server = ""
        self.rate_interval = ""
        self.till = ""
        self.add = ""
        self.min_ttl_ratio = ""
        self.dynamic_server_prefix = ""
        self.resume = ""
        self.every = ""
        self.conn_limit_no_logging = ""
        self.extended_stats = ""
        self.conn_rate_limit_no_logging = ""
        self.name = ""
        self.times = ""
        self.log_selection_failure = ""
        self.conn_rate_limit = ""
        self.dns_query_interval = ""
        self.health_check = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


