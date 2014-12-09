from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param select_client_conn: {"description": "Client conn selection", "format": "counter", "type": "number", "oid": "63", "optional": true, "size": "2"}
    :param select_client_fail: {"description": "Select failed", "format": "counter", "type": "number", "oid": "67", "optional": true, "size": "2"}
    :param msg_proxy_server_incomplete: {"description": "Incomplete", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "2"}
    :param select_client_by_conn: {"description": "Select by conn", "format": "counter", "type": "number", "oid": "66", "optional": true, "size": "2"}
    :param AX_response_directly: {"description": "Number of packet which AX responds directly", "format": "counter", "type": "number", "oid": "62", "optional": true, "size": "2"}
    :param select_client_by_req: {"description": "Select by request", "format": "counter", "type": "number", "oid": "64", "optional": true, "size": "2"}
    :param select_server_by_req: {"description": "Select by request", "format": "counter", "type": "number", "oid": "69", "optional": true, "size": "2"}
    :param select_server_by_conn: {"description": "Select server conn by client conn", "format": "counter", "type": "number", "oid": "71", "optional": true, "size": "2"}
    :param msg_proxy_client_send_success: {"description": "Sent to server", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param msg_proxy_client_drop: {"description": "AX responds directly", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param msg_proxy_total: {"description": "Total SMPP Proxy", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param select_server_from_list: {"description": "Select by roundbin", "format": "counter", "type": "number", "oid": "70", "optional": true, "size": "2"}
    :param msg_proxy_current: {"description": "Curr SMPP Proxy", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param msg_proxy_client_fail: {"description": "Number of SMPP messages received from client but failed to forward to server", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param msg_proxy_create_server_conn: {"description": "Server conn created", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "2"}
    :param msg_proxy_server_send_success: {"description": "Sent to client", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "2"}
    :param msg_proxy_server_fail: {"description": "Number of SMPP messages received from server but failed to forward to client", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "2"}
    :param select_client_from_list: {"description": "Select by roundbin", "format": "counter", "type": "number", "oid": "65", "optional": true, "size": "2"}
    :param msg_proxy_client_incomplete: {"description": "Incomplete", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param msg_proxy_server_drop: {"description": "Number of the packet AX drop", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "2"}
    :param select_server_fail: {"description": "Fail to select server conn", "format": "counter", "type": "number", "oid": "72", "optional": true, "size": "2"}
    :param msg_proxy_start_server_conn: {"description": "Number of server connection created successfully", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "2"}
    :param msg_proxy_fail_start_server_conn: {"description": "Number of server connection created failed", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "2"}
    :param select_server_conn: {"description": "Server conn selection", "format": "counter", "type": "number", "oid": "68", "optional": true, "size": "2"}
    :param msg_proxy_server_recv: {"description": "Server message rcvd", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "2"}
    :param msg_proxy_client_connection: {"description": "Connecting server", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param msg_proxy_client_recv: {"description": "Client message rcvd", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.select_client_conn = ""
        self.select_client_fail = ""
        self.msg_proxy_server_incomplete = ""
        self.select_client_by_conn = ""
        self.AX_response_directly = ""
        self.select_client_by_req = ""
        self.select_server_by_req = ""
        self.select_server_by_conn = ""
        self.msg_proxy_client_send_success = ""
        self.msg_proxy_client_drop = ""
        self.msg_proxy_total = ""
        self.select_server_from_list = ""
        self.msg_proxy_current = ""
        self.msg_proxy_client_fail = ""
        self.msg_proxy_create_server_conn = ""
        self.msg_proxy_server_send_success = ""
        self.msg_proxy_server_fail = ""
        self.select_client_from_list = ""
        self.msg_proxy_client_incomplete = ""
        self.msg_proxy_server_drop = ""
        self.select_server_fail = ""
        self.msg_proxy_start_server_conn = ""
        self.msg_proxy_fail_start_server_conn = ""
        self.select_server_conn = ""
        self.msg_proxy_server_recv = ""
        self.msg_proxy_client_connection = ""
        self.msg_proxy_client_recv = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Smpp(A10BaseClass):
    
    """Class Description::
    Statistics for the object smpp.

    Class smpp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/smpp/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "smpp"
        self.a10_url="/axapi/v3/slb/smpp/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


