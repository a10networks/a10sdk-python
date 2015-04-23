from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param slave_recv_bytes: {"description": "vBlade Received Bytes counter of aVCS election", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param slave_cfg_upd: {"description": "vBlade Received Configuration Updates counter of aVCS election", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param slave_msg_inval: {"description": "vBlade Invalid Messages counter of aVCS election", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param slave_n_recv: {"description": "vBlade Received Messages counter of aVCS election", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param slave_keepalive: {"description": "vBlade Received Keepalives counter of aVCS election", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param slave_recv_err: {"description": "vBlade Receive Errors counter of aVCS election", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param slave_cfg_upd_fail: {"description": "vBlade Configuration Update Result Errors counter of aVCS election", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param slave_send_err: {"description": "vBlade Send Errors counter of aVCS election", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param slave_n_sent: {"description": "vBlade Sent Messages counter of aVCS election", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param slave_sent_bytes: {"description": "vBlade Sent Bytes counter of aVCS election", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.slave_recv_bytes = ""
        self.slave_cfg_upd = ""
        self.slave_msg_inval = ""
        self.slave_n_recv = ""
        self.slave_keepalive = ""
        self.slave_recv_err = ""
        self.slave_cfg_upd_fail = ""
        self.slave_send_err = ""
        self.slave_n_sent = ""
        self.slave_sent_bytes = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Stat(A10BaseClass):
    
    """Class Description::
    Statistics for the object stat.

    Class stat supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vblade_id: {"description": "vBlade-id", "format": "number", "optional": false, "oid": "1001", "maximum": 8, "minimum": 1, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs-vblades/stat/{vblade_id}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "vblade_id"]

        self.b_key = "stat"
        self.a10_url="/axapi/v3/vcs-vblades/stat/{vblade_id}/stats"
        self.DeviceProxy = ""
        self.vblade_id = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


