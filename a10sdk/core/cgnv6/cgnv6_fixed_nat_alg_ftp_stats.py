from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param lpsv_replies: {"description": "LPSV Replies From Server", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param port_requests: {"description": "PORT Requests From Client", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param epsv_replies: {"description": "EPSV Replies From Server", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param pasv_replies: {"description": "PASV Replies From Server", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param lprt_requests: {"description": "LPRT Requests From Client", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param eprt_requests: {"description": "EPRT Requests From Client", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.lpsv_replies = ""
        self.port_requests = ""
        self.epsv_replies = ""
        self.pasv_replies = ""
        self.lprt_requests = ""
        self.eprt_requests = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ftp(A10BaseClass):
    
    """Class Description::
    Statistics for the object ftp.

    Class ftp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/fixed-nat/alg/ftp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ftp"
        self.a10_url="/axapi/v3/cgnv6/fixed-nat/alg/ftp/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


