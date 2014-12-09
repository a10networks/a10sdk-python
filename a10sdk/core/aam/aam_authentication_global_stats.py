from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Ocsp_Stapling_Requests_to_a10authd: {"description": "Total OCSP Stapling Request", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param Open_socket_failed: {"description": "Total AAM Open Socket Failed", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param Ocsp_Stapling_Responses_from_a10authd: {"description": "Total OCSP Stapling Response", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param Responses: {"description": "Total Authentication Response", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param Created_timer: {"description": "Total AAM Timer Created", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param Misses: {"description": "Total Authentication Request Missed", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param Connect_failed: {"description": "Total AAM Connect Failed", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param Opened_socket: {"description": "Total AAM Socket Opened", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param Connect: {"description": "Total AAM Connection", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param Requests: {"description": "Total Authentication Request", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Total_request: {"description": "Total Request Received by A10 Auth Service", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param Create_timer_failed: {"description": "Total AAM Timer Creation Failed", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Ocsp_Stapling_Requests_to_a10authd = ""
        self.Open_socket_failed = ""
        self.Ocsp_Stapling_Responses_from_a10authd = ""
        self.Responses = ""
        self.Created_timer = ""
        self.Misses = ""
        self.Connect_failed = ""
        self.Opened_socket = ""
        self.Connect = ""
        self.Requests = ""
        self.Total_request = ""
        self.Create_timer_failed = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Global(A10BaseClass):
    
    """Class Description::
    Statistics for the object global.

    Class global supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/global/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "global"
        self.a10_url="/axapi/v3/aam/authentication/global/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


