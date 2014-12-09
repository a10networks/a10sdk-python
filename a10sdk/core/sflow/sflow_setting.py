from a10sdk.common.A10BaseClass import A10BaseClass


class Setting(A10BaseClass):
    
    """Class Description::
    Configure sFlow.

    Class setting supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param source_ip_use_mgmt: {"default": 0, "optional": true, "type": "number", "description": "Use management interface's IP address for source IP of sFlow packets", "format": "flag"}
    :param counter_polling_interval: {"description": "sFlow counter polling interval, default is 20", "format": "number", "default": 20, "optional": true, "maximum": 200, "minimum": 1, "type": "number"}
    :param packet_sampling_rate: {"description": "sFlow packet sampling rate, default is 1000", "format": "number", "default": 1000, "optional": true, "maximum": 1000000, "minimum": 10, "type": "number"}
    :param max_header: {"description": "Configure maximum number of bytes that should be copied from a sampled packet (default: 128) (The maximum number of bytes (Default: 128))", "format": "number", "default": 128, "optional": true, "maximum": 512, "minimum": 14, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/sflow/setting`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "setting"
        self.a10_url="/axapi/v3/sflow/setting"
        self.DeviceProxy = ""
        self.source_ip_use_mgmt = ""
        self.counter_polling_interval = ""
        self.packet_sampling_rate = ""
        self.max_header = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


