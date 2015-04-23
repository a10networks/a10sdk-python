from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "sessions_num", "alg_pkts_num", "alg_pkts_xmitted_num", "alg_port_helper_created", "alg_pasv_helper_created", "alg_port_helper_freed_unused", "alg_pasv_helper_freed_unused", "alg_port_helper_nat_free"], "type": "string", "description": "'all': all; 'sessions_num': Total Control Sessions; 'alg_pkts_num': Total ALG packets; 'alg_pkts_xmitted_num': ALG packets rexmitted; 'alg_port_helper_created': Total PORT helper sessions; 'alg_pasv_helper_created': Total PASV helper sessions; 'alg_port_helper_freed_unused': PORT helper freed unused; 'alg_pasv_helper_freed_unused': PASV helper freed unused; 'alg_port_helper_nat_free': PORT helper NAT free; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FtpCtl(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "sessions_num", "alg_pkts_num", "alg_pkts_xmitted_num", "alg_port_helper_created", "alg_pasv_helper_created", "alg_port_helper_freed_unused", "alg_pasv_helper_freed_unused", "alg_port_helper_nat_free"], "type": "string", "description": "'all': all; 'sessions_num': Total Control Sessions; 'alg_pkts_num': Total ALG packets; 'alg_pkts_xmitted_num': ALG packets rexmitted; 'alg_port_helper_created': Total PORT helper sessions; 'alg_pasv_helper_created': Total PASV helper sessions; 'alg_port_helper_freed_unused': PORT helper freed unused; 'alg_pasv_helper_freed_unused': PASV helper freed unused; 'alg_port_helper_nat_free': PORT helper NAT free; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show FTP Statistics.

    Class ftp-ctl supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/ftp-ctl`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ftp-ctl"
        self.a10_url="/axapi/v3/slb/ftp-ctl"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


