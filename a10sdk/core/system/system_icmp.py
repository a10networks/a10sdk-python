from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "num", "inmsgs", "inerrors", "indestunreachs", "intimeexcds", "inparmprobs", "insrcquenchs", "inredirects", "inechos", "inechoreps", "intimestamps", "intimestampreps", "inaddrmasks", "inaddrmaskreps", "outmsgs", "outerrors", "outdestunreachs", "outtimeexcds", "outparmprobs", "outsrcquenchs", "outredirects", "outechos", "outechoreps", "outtimestamps", "outtimestampreps", "outaddrmasks", "outaddrmaskreps"], "type": "string", "description": "'all': all; 'num': Total number; 'inmsgs': In Messages; 'inerrors': In Errors; 'indestunreachs': In Destination Unreachable; 'intimeexcds': In TTL Exceeds; 'inparmprobs': In Parameter Problem; 'insrcquenchs': In Source Quench Error; 'inredirects': In Redirects; 'inechos': In Echo requests; 'inechoreps': In Echo replies; 'intimestamps': In Timestamp; 'intimestampreps': In Timestamp Rep; 'inaddrmasks': In Address Masks; 'inaddrmaskreps': In Address Mask Rep; 'outmsgs': Out Message; 'outerrors': Out Errors; 'outdestunreachs': Out Destination Unreachable; 'outtimeexcds': Out TTL Exceeds; 'outparmprobs': Out Parameter Problem; 'outsrcquenchs': Out Source Quench Error; 'outredirects': Out Redirects; 'outechos': Out Echo Requests; 'outechoreps': Out Echo Replies; 'outtimestamps': Out Time Stamp; 'outtimestampreps': Out Time Stamp Rep; 'outaddrmasks': Out Address Mask; 'outaddrmaskreps': Out Address Mask Rep; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Icmp(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "num", "inmsgs", "inerrors", "indestunreachs", "intimeexcds", "inparmprobs", "insrcquenchs", "inredirects", "inechos", "inechoreps", "intimestamps", "intimestampreps", "inaddrmasks", "inaddrmaskreps", "outmsgs", "outerrors", "outdestunreachs", "outtimeexcds", "outparmprobs", "outsrcquenchs", "outredirects", "outechos", "outechoreps", "outtimestamps", "outtimestampreps", "outaddrmasks", "outaddrmaskreps"], "type": "string", "description": "'all': all; 'num': Total number; 'inmsgs': In Messages; 'inerrors': In Errors; 'indestunreachs': In Destination Unreachable; 'intimeexcds': In TTL Exceeds; 'inparmprobs': In Parameter Problem; 'insrcquenchs': In Source Quench Error; 'inredirects': In Redirects; 'inechos': In Echo requests; 'inechoreps': In Echo replies; 'intimestamps': In Timestamp; 'intimestampreps': In Timestamp Rep; 'inaddrmasks': In Address Masks; 'inaddrmaskreps': In Address Mask Rep; 'outmsgs': Out Message; 'outerrors': Out Errors; 'outdestunreachs': Out Destination Unreachable; 'outtimeexcds': Out TTL Exceeds; 'outparmprobs': Out Parameter Problem; 'outsrcquenchs': Out Source Quench Error; 'outredirects': Out Redirects; 'outechos': Out Echo Requests; 'outechoreps': Out Echo Replies; 'outtimestamps': Out Time Stamp; 'outtimestampreps': Out Time Stamp Rep; 'outaddrmasks': Out Address Mask; 'outaddrmaskreps': Out Address Mask Rep; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Display ICMP statistics.

    Class icmp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/system/icmp`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "icmp"
        self.a10_url="/axapi/v3/system/icmp"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


