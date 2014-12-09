from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param alg_pkts_xmitted_num: {"description": "ALG packets rexmitted", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param alg_pasv_helper_freed_unused: {"description": "PASV helper freed unused", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param alg_pasv_helper_created: {"description": "Total PASV helper sessions", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param alg_port_helper_created: {"description": "Total PORT helper sessions", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param sessions_num: {"description": "Total Control Sessions", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param alg_port_helper_nat_free: {"description": "PORT helper NAT free", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param alg_port_helper_freed_unused: {"description": "PORT helper freed unused", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param alg_pkts_num: {"description": "Total ALG packets", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.alg_pkts_xmitted_num = ""
        self.alg_pasv_helper_freed_unused = ""
        self.alg_pasv_helper_created = ""
        self.alg_port_helper_created = ""
        self.sessions_num = ""
        self.alg_port_helper_nat_free = ""
        self.alg_port_helper_freed_unused = ""
        self.alg_pkts_num = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FtpCtl(A10BaseClass):
    
    """Class Description::
    Statistics for the object ftp-ctl.

    Class ftp-ctl supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/ftp-ctl/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ftp-ctl"
        self.a10_url="/axapi/v3/slb/ftp-ctl/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


