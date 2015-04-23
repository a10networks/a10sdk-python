from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "session-created", "placeholder-debug"], "type": "string", "description": "'all': all; 'session-created': ESP Sessions Created; 'placeholder-debug': Placeholder Debug; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Esp(A10BaseClass):
    
    """    :param esp_value: {"optional": true, "enum": ["enable"], "type": "string", "description": "'enable': Enable ESP ALG for LSN; ", "format": "enum"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "session-created", "placeholder-debug"], "type": "string", "description": "'all': all; 'session-created': ESP Sessions Created; 'placeholder-debug': Placeholder Debug; ", "format": "enum"}}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Change LSN ESP ALG Settings.

    Class esp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/lsn/alg/esp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "esp"
        self.a10_url="/axapi/v3/cgnv6/lsn/alg/esp"
        self.DeviceProxy = ""
        self.esp_value = ""
        self.sampling_enable = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


