from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "slave_recv_err", "slave_send_err", "slave_recv_bytes", "slave_sent_bytes", "slave_n_recv", "slave_n_sent", "slave_msg_inval", "slave_keepalive", "slave_cfg_upd", "slave_cfg_upd_fail", "slave_cfg_upd_fail", "slave_cfg_upd_fail", "slave_cfg_upd_fail", "slave_cfg_upd_fail"], "type": "string", "description": "'all': all; 'slave_recv_err': vBlade Receive Errors counter of aVCS election; 'slave_send_err': vBlade Send Errors counter of aVCS election; 'slave_recv_bytes': vBlade Received Bytes counter of aVCS election; 'slave_sent_bytes': vBlade Sent Bytes counter of aVCS election; 'slave_n_recv': vBlade Received Messages counter of aVCS election; 'slave_n_sent': vBlade Sent Messages counter of aVCS election; 'slave_msg_inval': vBlade Invalid Messages counter of aVCS election; 'slave_keepalive': vBlade Received Keepalives counter of aVCS election; 'slave_cfg_upd': vBlade Received Configuration Updates counter of aVCS election; 'slave_cfg_upd_fail': vBlade Local Configuration Update Errors (1) counter of aVCS election; 'slave_cfg_upd_fail': vBlade Remote Configuration Update Errors counter of aVCS election; 'slave_cfg_upd_fail': vBlade Local Configuration Update Errors (2) counter of aVCS election; 'slave_cfg_upd_fail': vBlade Configuration Update Notif Errors counter of aVCS election; 'slave_cfg_upd_fail': vBlade Configuration Update Result Errors counter of aVCS election; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Stat(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "slave_recv_err", "slave_send_err", "slave_recv_bytes", "slave_sent_bytes", "slave_n_recv", "slave_n_sent", "slave_msg_inval", "slave_keepalive", "slave_cfg_upd", "slave_cfg_upd_fail", "slave_cfg_upd_fail", "slave_cfg_upd_fail", "slave_cfg_upd_fail", "slave_cfg_upd_fail"], "type": "string", "description": "'all': all; 'slave_recv_err': vBlade Receive Errors counter of aVCS election; 'slave_send_err': vBlade Send Errors counter of aVCS election; 'slave_recv_bytes': vBlade Received Bytes counter of aVCS election; 'slave_sent_bytes': vBlade Sent Bytes counter of aVCS election; 'slave_n_recv': vBlade Received Messages counter of aVCS election; 'slave_n_sent': vBlade Sent Messages counter of aVCS election; 'slave_msg_inval': vBlade Invalid Messages counter of aVCS election; 'slave_keepalive': vBlade Received Keepalives counter of aVCS election; 'slave_cfg_upd': vBlade Received Configuration Updates counter of aVCS election; 'slave_cfg_upd_fail': vBlade Local Configuration Update Errors (1) counter of aVCS election; 'slave_cfg_upd_fail': vBlade Remote Configuration Update Errors counter of aVCS election; 'slave_cfg_upd_fail': vBlade Local Configuration Update Errors (2) counter of aVCS election; 'slave_cfg_upd_fail': vBlade Configuration Update Notif Errors counter of aVCS election; 'slave_cfg_upd_fail': vBlade Configuration Update Result Errors counter of aVCS election; ", "format": "enum"}}}]}
    :param vblade_id: {"description": "vBlade-id", "format": "number", "type": "number", "maximum": 8, "minimum": 1, "optional": false}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show aVCS vBlade box statistics information.

    Class stat supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs-vblades/stat/{vblade_id}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "vblade_id"]

        self.b_key = "stat"
        self.a10_url="/axapi/v3/vcs-vblades/stat/{vblade_id}"
        self.DeviceProxy = ""
        self.sampling_enable = []
        self.vblade_id = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


