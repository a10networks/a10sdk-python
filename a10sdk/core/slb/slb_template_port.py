from a10sdk.common.A10BaseClass import A10BaseClass


class Port(A10BaseClass):
    
    """Class Description::
    Port template.

    Class port supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param health_check_disable: {"description": "Disable configured health check configuration", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param stats_data_action: {"description": "'stats-data-enable': Enable statistical data collection for real server port; 'stats-data-disable': Disable statistical data collection for real server port; ", "format": "enum", "default": "stats-data-enable", "type": "string", "enum": ["stats-data-enable", "stats-data-disable"], "optional": true}
    :param dest_nat: {"default": 0, "optional": true, "type": "number", "description": "Destination NAT", "format": "flag"}
    :param request_rate_limit: {"description": "Request rate limit", "format": "number", "type": "number", "maximum": 1048575, "minimum": 1, "optional": true}
    :param dynamic_member_priority: {"description": "Set dynamic member's priority (Initial priority (default is 16))", "format": "number", "default": 16, "optional": true, "maximum": 16, "minimum": 1, "type": "number"}
    :param till: {"description": "Slow start ends when slow start connection limit reaches a number (default 4096) (Slow start ends when connection limit reaches this number)", "format": "number", "default": 4096, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param slow_start: {"default": 0, "optional": true, "type": "number", "description": "Slowly ramp up the connection number after port is up", "format": "flag"}
    :param decrement: {"default": 0, "optional": true, "type": "number", "description": "Decrease dynamic member's priority after every round of DNS query", "format": "flag"}
    :param conn_limit: {"description": "Connection limit", "format": "number", "type": "number", "maximum": 8000000, "minimum": 1, "optional": true}
    :param retry: {"description": "Maximum retry times before reassign this connection to another server/port (default is 2) (The maximum retry number)", "format": "number", "default": 2, "optional": true, "maximum": 7, "minimum": 0, "type": "number"}
    :param weight: {"description": "Weight (port weight)", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}
    :param inband_health_check: {"default": 0, "optional": true, "type": "number", "description": "Use inband traffic to detect port's health status", "format": "flag"}
    :param initial_slow_start: {"description": "Initial slow start connection limit (default 128)", "format": "number", "default": 128, "optional": true, "maximum": 4095, "minimum": 1, "type": "number"}
    :param rate_interval: {"description": "'100ms': Use 100 ms as sampling interval; 'second': Use 1 second as sampling interval; ", "format": "enum", "default": "second", "type": "string", "enum": ["100ms", "second"], "optional": true}
    :param no_ssl: {"default": 0, "optional": true, "type": "number", "description": "No SSL", "format": "flag"}
    :param request_rate_interval: {"description": "'100ms': Use 100 ms as sampling interval; 'second': Use 1 second as sampling interval; ", "format": "enum", "default": "second", "type": "string", "enum": ["100ms", "second"], "optional": true}
    :param add: {"description": "Slow start connection limit add by a number every interval (Add by this number every interval)", "format": "number", "optional": true, "maximum": 4095, "minimum": 1, "not": "times", "type": "number"}
    :param down_grace_period: {"description": "Port down grace period", "format": "number", "type": "number", "maximum": 86400, "minimum": 1, "optional": true}
    :param resume: {"description": "Resume accepting new connection after connection number drops below threshold (Connection resume threshold)", "format": "number", "type": "number", "maximum": 1048575, "minimum": 1, "optional": true}
    :param dscp: {"description": "Differentiated Services Code Point (DSCP to Real Server IP Mapping Value)", "format": "number", "type": "number", "maximum": 63, "minimum": 1, "optional": true}
    :param every: {"description": "Slow start connection limit increment interval (default 10)", "format": "number", "default": 10, "optional": true, "maximum": 60, "minimum": 1, "type": "number"}
    :param conn_limit_no_logging: {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}
    :param extended_stats: {"default": 0, "optional": true, "type": "number", "description": "Enable extended statistics on real server port", "format": "flag"}
    :param decrement_val: {"description": "Decrease after every round of DNS query (default is 0)", "format": "number", "default": 0, "optional": true, "maximum": 7, "minimum": 0, "type": "number"}
    :param reset: {"default": 0, "optional": true, "type": "number", "description": "Send client reset when connection rate over limit", "format": "flag"}
    :param conn_rate_limit_no_logging: {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}
    :param name: {"description": "Port template name", "format": "string", "default": "default", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param times: {"description": "Slow start connection limit multiply by a number every interval (default 2) (Multiply by this number every interval)", "format": "number", "default": 2, "optional": true, "maximum": 10, "minimum": 2, "not": "add", "type": "number"}
    :param request_rate_no_logging: {"default": 0, "optional": true, "type": "number", "description": "Do not log connection over limit event", "format": "flag"}
    :param conn_rate_limit: {"description": "Connection rate limit", "format": "number", "type": "number", "maximum": 1048575, "minimum": 1, "optional": true}
    :param source_nat: {"description": "Source NAT (IP NAT Pool or pool group name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param reassign: {"description": "Maximum reassign times before declear the server/port down (default is 25) (The maximum reassign number)", "format": "number", "default": 25, "optional": true, "maximum": 255, "minimum": 0, "type": "number"}
    :param health_check: {"description": "Health Check Monitor (Health monitor name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/port/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "port"
        self.a10_url="/axapi/v3/slb/template/port/{name}"
        self.DeviceProxy = ""
        self.health_check_disable = ""
        self.stats_data_action = ""
        self.dest_nat = ""
        self.request_rate_limit = ""
        self.dynamic_member_priority = ""
        self.till = ""
        self.slow_start = ""
        self.decrement = ""
        self.conn_limit = ""
        self.retry = ""
        self.weight = ""
        self.inband_health_check = ""
        self.initial_slow_start = ""
        self.rate_interval = ""
        self.no_ssl = ""
        self.request_rate_interval = ""
        self.add = ""
        self.down_grace_period = ""
        self.resume = ""
        self.dscp = ""
        self.every = ""
        self.conn_limit_no_logging = ""
        self.extended_stats = ""
        self.decrement_val = ""
        self.reset = ""
        self.conn_rate_limit_no_logging = ""
        self.name = ""
        self.times = ""
        self.request_rate_no_logging = ""
        self.conn_rate_limit = ""
        self.source_nat = ""
        self.reassign = ""
        self.health_check = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


