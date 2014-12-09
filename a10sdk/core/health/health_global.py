from a10sdk.common.A10BaseClass import A10BaseClass


class Global(A10BaseClass):
    
    """Class Description::
    Define the Health Monitor global default.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param disable_auto_adjust: {"default": 0, "optional": true, "type": "number", "description": "Disable the Health Check Rate Auto Adjustment", "format": "flag"}
    :param external_rate: {"description": "Define the External Health Check Rate (Number of External Script Programs (default 2))", "format": "number", "default": 2, "optional": true, "maximum": 999, "minimum": 1, "type": "number"}
    :param multi_process: {"description": "Start Health Monitoring in Multi-Process Mode (Specify the number of multiple processes (default 1))", "format": "number", "default": 1, "optional": true, "maximum": 20, "minimum": 1, "type": "number"}
    :param interval: {"description": "Specify the Healthcheck Interval (Interval Value, in seconds (default 5))", "format": "number", "default": 5, "optional": true, "maximum": 180, "minimum": 1, "type": "number"}
    :param check_rate: {"description": "Health Check Rate per 500ms (default 1000)", "format": "number", "default": 1000, "optional": true, "maximum": 50000, "minimum": 1, "type": "number"}
    :param per: {"description": "Specify the Unit Time for the rate (Specify the Unit Time, multiple of 100ms)", "format": "number", "default": 2, "optional": true, "maximum": 20, "minimum": 1, "type": "number"}
    :param retry: {"description": "Specify the Healthcheck Retries (Retry Count (default 3))", "format": "number", "default": 3, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}
    :param up_retry: {"description": "Specify the Healthcheck Retries before declaring target up (Up-retry count (default 1))", "format": "number", "default": 1, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}
    :param timeout: {"description": "Specify the Healthcheck Timeout (Timeout Value, in seconds (default 5), Timeout should be less than or equal to interval)", "format": "number", "default": 5, "optional": true, "maximum": 180, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/health/global"
        self.DeviceProxy = ""
        self.disable_auto_adjust = ""
        self.external_rate = ""
        self.multi_process = ""
        self.interval = ""
        self.check_rate = ""
        self.per = ""
        self.retry = ""
        self.up_retry = ""
        self.timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


