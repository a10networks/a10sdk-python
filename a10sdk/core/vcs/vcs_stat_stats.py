from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param elect_master_discard_challenger: {"description": "vMaster discard challenger counter of aVCS election", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "8"}
    :param elect_pdu_master_sent: {"description": "Sent vMaster-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param elect_pdu_cluster_mismatch: {"description": "PDU Chassis-ID mismatch counter of aVCS election", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "8"}
    :param daemon_sent_bytes: {"description": "bytes of aVCS daemon sent", "format": "counter", "type": "number", "oid": "70", "optional": true, "size": "8"}
    :param daemon_send_err: {"description": "counter of aVCS daemon sent error", "format": "counter", "type": "number", "oid": "68", "optional": true, "size": "8"}
    :param elect_pdu_slave_recv: {"description": "Received vBlade-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param master_slave_start: {"description": "vMaster vBlades Started counter of aVCS election", "format": "counter", "type": "number", "oid": "48", "optional": true, "size": "8"}
    :param elect_enter_master_cand_stat: {"description": "Enter MC counter of aVCS election", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "8"}
    :param daemon_n_elec_start: {"description": "times of aVCS election start", "format": "counter", "type": "number", "oid": "65", "optional": true, "size": "8"}
    :param elect_pdu_unknown_sent: {"description": "Sent Unknown-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param elect_recv_byte: {"description": "Receive bytes counter of aVCS election", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param elect_mc_dup_masterr: {"description": "MC duplicate vMaster-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param master_slave_start_err: {"description": "vMaster Start vBlade Errors counter of aVCS election", "format": "counter", "type": "number", "oid": "47", "optional": true, "size": "8"}
    :param elect_pdu_slave_sent: {"description": "Sent vBlade-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param master_cfg_upd: {"description": "Received vMaster Configuration Updates counter of aVCS election", "format": "counter", "type": "number", "oid": "50", "optional": true, "size": "8"}
    :param elect_leave_master_take_over: {"description": "Leave MTO counter of aVCS election", "format": "counter", "type": "number", "oid": "46", "optional": true, "size": "8"}
    :param master_slave_stop: {"description": "vMaster vBlades stopped counter of aVCS election", "format": "counter", "type": "number", "oid": "49", "optional": true, "size": "8"}
    :param daemon_n_recv: {"description": "counter of aVCS daemon receive", "format": "counter", "type": "number", "oid": "71", "optional": true, "size": "8"}
    :param elect_mc_discard_master: {"description": "MC discarded vMaster-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "8"}
    :param daemon_recv_err: {"description": "counter of aVCS daemon receive error", "format": "counter", "type": "number", "oid": "67", "optional": true, "size": "8"}
    :param elect_leave_master_cand: {"description": "Leave MC counter of aVCS election", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "8"}
    :param slave_cfg_upd: {"description": "vBlade Received Configuration Updates counter of aVCS election", "format": "counter", "type": "number", "oid": "63", "optional": true, "size": "8"}
    :param master_cfg_upd_r_fail: {"description": "vMaster Remote Configuration Update Errors counter of aVCS election", "format": "counter", "type": "number", "oid": "52", "optional": true, "size": "8"}
    :param slave_msg_inval: {"description": "vBlade Invalid Messages counter of aVCS election", "format": "counter", "type": "number", "oid": "61", "optional": true, "size": "8"}
    :param elect_pdu_dev_id_collision: {"description": "PDU Device-ID collision counter of aVCS election", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "8"}
    :param slave_send_err: {"description": "vBlade Send Errors counter of aVCS election", "format": "counter", "type": "number", "oid": "56", "optional": true, "size": "8"}
    :param elect_mc_reset_timer_by_mto: {"description": "MC timers reset by MTO-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param elect_pdu_master_take_over_sent: {"description": "Sent MTO-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param elect_master_discard_neighbour: {"description": "vMaster discard neighbour counter of aVCS election", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "8"}
    :param elect_slave_dup_master: {"description": "vBlade duplicate vMaster-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param slave_keepalive: {"description": "vBlade Received Keepalives counter of aVCS election", "format": "counter", "type": "number", "oid": "62", "optional": true, "size": "8"}
    :param elect_send_err: {"description": "Send error counter of aVCS election", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param elect_pdu_master_cand_sent: {"description": "Sent MC-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param elect_slave_dup_challenger: {"description": "vBlade duplicate challenger counter of aVCS election", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param daemon_n_elec_stop: {"description": "times of aVCS election stop", "format": "counter", "type": "number", "oid": "66", "optional": true, "size": "8"}
    :param slave_sent_bytes: {"description": "vBlade Sent Bytes counter of aVCS election", "format": "counter", "type": "number", "oid": "58", "optional": true, "size": "8"}
    :param slave_recv_bytes: {"description": "vBlade Received Bytes counter of aVCS election", "format": "counter", "type": "number", "oid": "57", "optional": true, "size": "8"}
    :param daemon_msg_inval: {"description": "counter of aVCS daemon invalid message", "format": "counter", "type": "number", "oid": "73", "optional": true, "size": "8"}
    :param elect_pdu_hw_mismatch: {"description": "PDU HW mismatch counter of aVCS election", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param elect_slave_discard_challenger: {"description": "vBlade discard challenger counter of aVCS election", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param elect_master_replace_challenger: {"description": "vMaster replace challenger counter of aVCS election", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "8"}
    :param elect_master_too_many_neighbour: {"description": "vMaster too many neighbours counter of aVCS election", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "8"}
    :param elect_pdu_master_cand_recv: {"description": "Received MC-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param elect_leave_master: {"description": "Leave vMaster counter of aVCS election", "format": "counter", "type": "number", "oid": "45", "optional": true, "size": "8"}
    :param slave_recv_err: {"description": "vBlade Receive Errors counter of aVCS election", "format": "counter", "type": "number", "oid": "55", "optional": true, "size": "8"}
    :param elect_enter_master: {"description": "Enter vMaster counter of aVCS election", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "8"}
    :param elect_mc_replace_master: {"description": "MC replaced vMaster-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param elect_master_dup_challenger: {"description": "vMaster duplicate challenger counter of aVCS election", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "8"}
    :param elect_recv_err: {"description": "Receive error counter of aVCS election", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param elect_slave_too_many_neighbour: {"description": "vBlade too many neighbours counter of aVCS election", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param elect_enter_slave: {"description": "Enter vBlade counter of aVCS election", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "8"}
    :param daemon_n_sent: {"description": "counter of aVCS daemon sent", "format": "counter", "type": "number", "oid": "72", "optional": true, "size": "8"}
    :param master_cfg_upd_l_fail: {"description": "vMaster Local Configuration Update Errors counter of aVCS election", "format": "counter", "type": "number", "oid": "51", "optional": true, "size": "8"}
    :param slave_n_sent: {"description": "vBlade Sent Messages counter of aVCS election", "format": "counter", "type": "number", "oid": "60", "optional": true, "size": "8"}
    :param elect_slave_replace_challenger: {"description": "vBlade replace challenger counter of aVCS election", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param elect_master_dup_neighbour: {"description": "vMaster duplicate neighbours counter of aVCS election", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "8"}
    :param elect_mc_reset_timer_by_mc: {"description": "MC timers reset by MC-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param elect_send_byte: {"description": "Send bytes counter of aVCS election", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param slave_cfg_upd_fail: {"description": "vBlade Configuration Update Failures counter of aVCS election", "format": "counter", "type": "number", "oid": "64", "optional": true, "size": "8"}
    :param daemon_msg_handle_failure: {"description": "counter of aVCS daemon message handle failure", "format": "counter", "type": "number", "oid": "74", "optional": true, "size": "8"}
    :param elect_slave_dup_neighbour: {"description": "send vBlade duplicate neighbours of aVCS election", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "8"}
    :param elect_pdu_unknown_recv: {"description": "Received Unknown-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param elect_slave_discard_neighbour: {"description": "vBlade discard neighbour counter of aVCS election", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param master_cfg_upd_notif_err: {"description": "vMaster Configuration Update Notif Errors counter of aVCS election", "format": "counter", "type": "number", "oid": "53", "optional": true, "size": "8"}
    :param elect_pdu_master_recv: {"description": "Received vMaster-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param elect_master_new_challenger: {"description": "vMaster new challenger counter of aVCS election", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "8"}
    :param daemon_recv_bytes: {"description": "bytes of aVCS daemon receive", "format": "counter", "type": "number", "oid": "69", "optional": true, "size": "8"}
    :param master_cfg_upd_result_err: {"description": "vMaster Configuration Update Result Errors counter of aVCS election", "format": "counter", "type": "number", "oid": "54", "optional": true, "size": "8"}
    :param elect_leave_slave: {"description": "Leave vBlade counter of aVCS election", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "8"}
    :param slave_n_recv: {"description": "vBlade Received Messages counter of aVCS election", "format": "counter", "type": "number", "oid": "59", "optional": true, "size": "8"}
    :param elect_enter_master_take_over: {"description": "Enter MTO counter of aVCS election", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "8"}
    :param elect_pdu_master_take_over_recv: {"description": "Received MTO-PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param elect_pdu_inval: {"description": "Invalid PDU counter of aVCS election", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.elect_master_discard_challenger = ""
        self.elect_pdu_master_sent = ""
        self.elect_pdu_cluster_mismatch = ""
        self.daemon_sent_bytes = ""
        self.daemon_send_err = ""
        self.elect_pdu_slave_recv = ""
        self.master_slave_start = ""
        self.elect_enter_master_cand_stat = ""
        self.daemon_n_elec_start = ""
        self.elect_pdu_unknown_sent = ""
        self.elect_recv_byte = ""
        self.elect_mc_dup_masterr = ""
        self.master_slave_start_err = ""
        self.elect_pdu_slave_sent = ""
        self.master_cfg_upd = ""
        self.elect_leave_master_take_over = ""
        self.master_slave_stop = ""
        self.daemon_n_recv = ""
        self.elect_mc_discard_master = ""
        self.daemon_recv_err = ""
        self.elect_leave_master_cand = ""
        self.slave_cfg_upd = ""
        self.master_cfg_upd_r_fail = ""
        self.slave_msg_inval = ""
        self.elect_pdu_dev_id_collision = ""
        self.slave_send_err = ""
        self.elect_mc_reset_timer_by_mto = ""
        self.elect_pdu_master_take_over_sent = ""
        self.elect_master_discard_neighbour = ""
        self.elect_slave_dup_master = ""
        self.slave_keepalive = ""
        self.elect_send_err = ""
        self.elect_pdu_master_cand_sent = ""
        self.elect_slave_dup_challenger = ""
        self.daemon_n_elec_stop = ""
        self.slave_sent_bytes = ""
        self.slave_recv_bytes = ""
        self.daemon_msg_inval = ""
        self.elect_pdu_hw_mismatch = ""
        self.elect_slave_discard_challenger = ""
        self.elect_master_replace_challenger = ""
        self.elect_master_too_many_neighbour = ""
        self.elect_pdu_master_cand_recv = ""
        self.elect_leave_master = ""
        self.slave_recv_err = ""
        self.elect_enter_master = ""
        self.elect_mc_replace_master = ""
        self.elect_master_dup_challenger = ""
        self.elect_recv_err = ""
        self.elect_slave_too_many_neighbour = ""
        self.elect_enter_slave = ""
        self.daemon_n_sent = ""
        self.master_cfg_upd_l_fail = ""
        self.slave_n_sent = ""
        self.elect_slave_replace_challenger = ""
        self.elect_master_dup_neighbour = ""
        self.elect_mc_reset_timer_by_mc = ""
        self.elect_send_byte = ""
        self.slave_cfg_upd_fail = ""
        self.daemon_msg_handle_failure = ""
        self.elect_slave_dup_neighbour = ""
        self.elect_pdu_unknown_recv = ""
        self.elect_slave_discard_neighbour = ""
        self.master_cfg_upd_notif_err = ""
        self.elect_pdu_master_recv = ""
        self.elect_master_new_challenger = ""
        self.daemon_recv_bytes = ""
        self.master_cfg_upd_result_err = ""
        self.elect_leave_slave = ""
        self.slave_n_recv = ""
        self.elect_enter_master_take_over = ""
        self.elect_pdu_master_take_over_recv = ""
        self.elect_pdu_inval = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Stat(A10BaseClass):
    
    """Class Description::
    Statistics for the object stat.

    Class stat supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vcs/stat/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "stat"
        self.a10_url="/axapi/v3/vcs/stat/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


