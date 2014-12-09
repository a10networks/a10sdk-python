from a10sdk.common.A10BaseClass import A10BaseClass


class FailSafe(A10BaseClass):
    
    """Class Description::
    Fail Safe Global Commands.

    Class fail-safe supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param session_mem_recovery_threshold: {"description": "Session memory recovery threshold (percentage) (Percentage of available session memory (default 30%))", "format": "number", "default": 30, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param log: {"description": "Log the event", "format": "flag", "default": 0, "optional": true, "not": "kill", "type": "number"}
    :param fpga_buff_recovery_threshold: {"description": "FPGA buffers recovery threshold (Units of 256 buffers (default 2))", "format": "number", "default": 2, "optional": true, "maximum": 10, "minimum": 1, "type": "number"}
    :param hw_error_recovery_timeout: {"description": "Hardware error recovery timeout (minutes) (waiting time of recovery from hardware errors (default 0))", "format": "number", "type": "number", "maximum": 1440, "minimum": 1, "optional": true}
    :param sw_error_monitor_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable fail-safe software error monitor", "format": "flag"}
    :param hw_error_monitor_disable: {"description": "Disable fail-safe hardware error monitor", "format": "flag", "default": 0, "optional": true, "not": "hw-error-monitor-enable", "type": "number"}
    :param kill: {"description": "Stop the traffic and log the event", "format": "flag", "default": 0, "optional": true, "not": "log", "type": "number"}
    :param hw_error_monitor_enable: {"description": "Enable fail-safe hardware error monitor", "format": "flag", "default": 1, "optional": true, "not": "hw-error-monitor-disable", "type": "number"}
    :param total_memory_size_check: {"description": "Check total memory size of current system (Size of memory (GB))", "format": "number", "type": "number", "maximum": 256, "minimum": 1, "optional": true}
    :param sw_error_recovery_timeout: {"description": "Software error recovery timeout (minutes) (waiting time of recovery from software errors (default 3))", "format": "number", "default": 3, "optional": true, "maximum": 1440, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/fail-safe`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "fail-safe"
        self.a10_url="/axapi/v3/fail-safe"
        self.DeviceProxy = ""
        self.session_mem_recovery_threshold = ""
        self.log = ""
        self.fpga_buff_recovery_threshold = ""
        self.hw_error_recovery_timeout = ""
        self.sw_error_monitor_enable = ""
        self.hw_error_monitor_disable = ""
        self.kill = ""
        self.hw_error_monitor_enable = ""
        self.total_memory_size_check = ""
        self.sw_error_recovery_timeout = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


