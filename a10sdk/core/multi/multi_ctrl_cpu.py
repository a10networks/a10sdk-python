from a10sdk.common.A10BaseClass import A10BaseClass


class MultiCtrlCpu(A10BaseClass):
    
    """    :param num_ctrl_cpus: {"description": "Enter a number between 1 and less than half of the total number of CPUs, default is 1", "format": "number", "type": "number", "maximum": 32, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Enable Multiple Control CPUs.

    Class multi-ctrl-cpu supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/multi-ctrl-cpu`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "multi-ctrl-cpu"
        self.a10_url="/axapi/v3/multi-ctrl-cpu"
        self.DeviceProxy = ""
        self.num_ctrl_cpus = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


