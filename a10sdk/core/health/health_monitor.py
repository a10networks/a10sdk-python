from a10sdk.common.A10BaseClass import A10BaseClass


class Monitor(A10BaseClass):
    
    """Class Description::
    Define the Health Monitor object.

    Class monitor supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param sample_threshold: {"description": "Number of samples in one epoch above which passive HC is enabled. If below or equal to the threshold, passive HC is disabled (Specify number of samples in one second (Default is 50). If the number of samples is 0, no action is taken)", "format": "number", "default": 50, "optional": true, "maximum": 10000, "minimum": 1, "type": "number"}
    :param override_ipv4: {"optional": true, "type": "string", "description": "Override implicitly inherited IPv4 address from target", "format": "ipv4-address"}
    :param retry: {"description": "Specify the Healthcheck Retries (Retry Count (default 3))", "format": "number", "optional": true, "maximum": 10, "minimum": 1, "default-depends-on": "health.global::retry", "type": "number"}
    :param name: {"description": "Monitor Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 29, "type": "string"}
    :param strict_retry_on_server_err_resp: {"default": 0, "optional": true, "type": "number", "description": "Require strictly retry", "format": "flag"}
    :param passive_interval: {"description": "Interval to do manual health checking while in passive mode (Specify value in seconds (Default is 10 s))", "format": "number", "default": 10, "optional": true, "maximum": 180, "minimum": 1, "type": "number"}
    :param override_port: {"description": "Override implicitly inherited port from target (Port number (1-65534))", "format": "number", "type": "number", "maximum": 65534, "minimum": 1, "optional": true}
    :param up_retry: {"description": "Specify the Healthcheck Retries before declaring target up (Up-retry count (default 1))", "format": "number", "optional": true, "maximum": 10, "minimum": 1, "default-depends-on": "health.global::up-retry", "type": "number"}
    :param interval: {"description": "Specify the Healthcheck Interval (Interval Value, in seconds (default 5))", "format": "number", "optional": true, "maximum": 180, "minimum": 1, "default-depends-on": "health.global::interval", "type": "number"}
    :param passive: {"default": 0, "optional": true, "type": "number", "description": "Specify passive mode", "format": "flag"}
    :param override_ipv6: {"optional": true, "type": "string", "description": "Override implicitly inherited IPv6 address from target", "format": "ipv6-address"}
    :param timeout: {"description": "Specify the Healthcheck Timeout (Timeout Value, in seconds(default 5), Timeout should be less than or equal to interval)", "format": "number", "optional": true, "maximum": 180, "minimum": 1, "default-depends-on": "health.global::timeout", "type": "number"}
    :param threshold: {"description": "Threshold percentage above which passive mode is enabled (Specify percentage (Default is 75%))", "format": "number", "default": 75, "optional": true, "maximum": 100, "minimum": 0, "type": "number"}
    :param disable_after_down: {"default": 0, "optional": true, "type": "number", "description": "Disable the target if health check failed", "format": "flag"}
    :param status_code: {"optional": true, "enum": ["status-code-2xx", "status-code-non-5xx"], "type": "string", "description": "'status-code-2xx': Enable passive mode with 2xx http status code; 'status-code-non-5xx': Enable passive mode with non-5xx http status code; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "monitor"
        self.a10_url="/axapi/v3/health/monitor/{name}"
        self.DeviceProxy = ""
        self.sample_threshold = ""
        self.override_ipv4 = ""
        self.retry = ""
        self.name = ""
        self.strict_retry_on_server_err_resp = ""
        self.passive_interval = ""
        self.override_port = ""
        self.up_retry = ""
        self.interval = ""
        self.passive = ""
        self.override_ipv6 = ""
        self.timeout = ""
        self.threshold = ""
        self.disable_after_down = ""
        self.method = {}
        self.status_code = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


