from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "curr_conn", "total_conn", "total_fwd_bytes", "total_fwd_packets", "total_rev_bytes", "total_rev_packets", "curr_pconn"], "type": "string", "description": "'all': all; 'curr_conn': Current connections; 'total_conn': Total connections; 'total_fwd_bytes': Forward bytes; 'total_fwd_packets': Forward packets; 'total_rev_bytes': Reverse bytes; 'total_rev_packets': Reverse packets; 'curr_pconn': Persistent connections; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Passthrough(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr_conn", "total_conn", "total_fwd_bytes", "total_fwd_packets", "total_rev_bytes", "total_rev_packets", "curr_pconn"], "type": "string", "description": "'all': all; 'curr_conn': Current connections; 'total_conn': Total connections; 'total_fwd_bytes': Forward bytes; 'total_fwd_packets': Forward packets; 'total_rev_bytes': Reverse bytes; 'total_rev_packets': Reverse packets; 'curr_pconn': Persistent connections; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    passthrough session stats.

    Class passthrough supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/passthrough`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "passthrough"
        self.a10_url="/axapi/v3/slb/passthrough"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


