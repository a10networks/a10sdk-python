from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param total_system_memory: {"type": "number", "format": "number"}
    :param total_free_fpga_buff: {"type": "number", "format": "number"}
    :param total_fpga_buffers: {"type": "number", "format": "number"}
    :param free_fpga_buffers: {"type": "number", "format": "number"}
    :param free_session_memory: {"type": "number", "format": "number"}
    :param avail_fpga_buff_domain1: {"type": "number", "format": "number"}
    :param avail_fpga_buff_domain2: {"type": "number", "format": "number"}
    :param total_session_memory: {"type": "number", "format": "number"}
    :param fpga_buff_recovery_threshold: {"type": "number", "format": "number"}
    :param sess_mem_recovery_threshold: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.total_system_memory = ""
        self.total_free_fpga_buff = ""
        self.total_fpga_buffers = ""
        self.free_fpga_buffers = ""
        self.free_session_memory = ""
        self.avail_fpga_buff_domain1 = ""
        self.avail_fpga_buff_domain2 = ""
        self.total_session_memory = ""
        self.fpga_buff_recovery_threshold = ""
        self.sess_mem_recovery_threshold = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FailSafe(A10BaseClass):
    
    """Class Description::
    Operational Status for the object fail-safe.

    Class fail-safe supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/fail-safe/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "fail-safe"
        self.a10_url="/axapi/v3/fail-safe/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


