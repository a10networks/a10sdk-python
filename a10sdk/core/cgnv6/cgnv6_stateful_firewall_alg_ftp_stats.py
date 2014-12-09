from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param client_eprt_request: {"description": "EPRT Requests From Client", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param server_epsv_reply: {"description": "EPSV Replies From Server", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param client_port_request: {"description": "PORT Requests From Client", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param server_pasv_reply: {"description": "PASV Replies From Server", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.client_eprt_request = ""
        self.server_epsv_reply = ""
        self.client_port_request = ""
        self.server_pasv_reply = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ftp(A10BaseClass):
    
    """Class Description::
    Statistics for the object ftp.

    Class ftp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/cgnv6/stateful-firewall/alg/ftp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ftp"
        self.a10_url="/axapi/v3/cgnv6/stateful-firewall/alg/ftp/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


