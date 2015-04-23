from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "cross_cpu_helper_created", "cross_cpu_helper_free", "cross_cpu_sent", "cross_cpu_rcv", "cross_cpu_helper_nat_pool_standby", "cross_cpu_helper_cpu_mismatch", "cross_cpu_bad_l3", "cross_cpu_bad_l4", "cross_cpu_no_session", "cross_cpu_helper_deleted", "cross_cpu_helper_free_retry_lookup", "cross_cpu_helper_free_not_found"], "type": "string", "description": "'all': all; 'cross_cpu_helper_created': Cross CPU Helper Created; 'cross_cpu_helper_free': Cross CPU Helper Free; 'cross_cpu_sent': Cross CPU Helper Packets Sent; 'cross_cpu_rcv': Cross CPU Helper Packets Received; 'cross_cpu_helper_nat_pool_standby': Cross CPU Helper Standby; 'cross_cpu_helper_cpu_mismatch': Cross CPU Helper CPU Mismatch; 'cross_cpu_bad_l3': Cross CPU Unsupported L3; 'cross_cpu_bad_l4': Cross CPU Unsupported L4; 'cross_cpu_no_session': Cross CPU No Session Found; 'cross_cpu_helper_deleted': Cross CPU Helper Deleted; 'cross_cpu_helper_free_retry_lookup': Cross CPU Helper Free Retry Lookup; 'cross_cpu_helper_free_not_found': Cross CPU Helper Free Not Found; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class NatGlobal(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "cross_cpu_helper_created", "cross_cpu_helper_free", "cross_cpu_sent", "cross_cpu_rcv", "cross_cpu_helper_nat_pool_standby", "cross_cpu_helper_cpu_mismatch", "cross_cpu_bad_l3", "cross_cpu_bad_l4", "cross_cpu_no_session", "cross_cpu_helper_deleted", "cross_cpu_helper_free_retry_lookup", "cross_cpu_helper_free_not_found"], "type": "string", "description": "'all': all; 'cross_cpu_helper_created': Cross CPU Helper Created; 'cross_cpu_helper_free': Cross CPU Helper Free; 'cross_cpu_sent': Cross CPU Helper Packets Sent; 'cross_cpu_rcv': Cross CPU Helper Packets Received; 'cross_cpu_helper_nat_pool_standby': Cross CPU Helper Standby; 'cross_cpu_helper_cpu_mismatch': Cross CPU Helper CPU Mismatch; 'cross_cpu_bad_l3': Cross CPU Unsupported L3; 'cross_cpu_bad_l4': Cross CPU Unsupported L4; 'cross_cpu_no_session': Cross CPU No Session Found; 'cross_cpu_helper_deleted': Cross CPU Helper Deleted; 'cross_cpu_helper_free_retry_lookup': Cross CPU Helper Free Retry Lookup; 'cross_cpu_helper_free_not_found': Cross CPU Helper Free Not Found; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Debug statistics for IP NAT.

    Class nat-global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/ip/nat/nat-global`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "nat-global"
        self.a10_url="/axapi/v3/ip/nat/nat-global"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


