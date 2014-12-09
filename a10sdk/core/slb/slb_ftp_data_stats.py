from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param sessions_num: {"description": "Total Data Sessions", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param port_out_of_range: {"description": "Drop Data Port out of range", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.sessions_num = ""
        self.port_out_of_range = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class FtpData(A10BaseClass):
    
    """Class Description::
    Statistics for the object ftp-data.

    Class ftp-data supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/ftp-data/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ftp-data"
        self.a10_url="/axapi/v3/slb/ftp-data/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


