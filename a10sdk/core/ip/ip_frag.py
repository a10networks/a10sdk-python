from a10sdk.common.A10BaseClass import A10BaseClass


class Frag(A10BaseClass):
    
    """Class Description::
    IP fragmentation parameters.

    Class frag supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param max_reassembly_sessions: {"description": "Max number of pending reassembly sessions allowed (default 100000)", "format": "number", "type": "number", "maximum": 200000, "minimum": 1, "optional": true}
    :param timeout: {"description": "Fragmentation timeout (in milliseconds 4 - 16000 (default is 1000))", "format": "number", "type": "number", "maximum": 16000, "minimum": 4, "optional": true}
    :param buff: {"description": "Max buff used for fragmentation (Buffer Value(10000-3000000))", "format": "number", "type": "number", "maximum": 3000000, "minimum": 10000, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/frag`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "frag"
        self.a10_url="/axapi/v3/ip/frag"
        self.DeviceProxy = ""
        self.max_reassembly_sessions = ""
        self.timeout = ""
        self.buff = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


