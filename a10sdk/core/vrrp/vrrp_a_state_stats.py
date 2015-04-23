from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param sync_tx_create_ext_bit_counter: {"description": "Conn Sync Create with Ext Sent counter", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "8"}
    :param sync_tx_max_packed: {"description": "Min Sync Msg Per Packet", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "2"}
    :param sync_persist_rx_no_such_sg_group: {"description": "Persist Conn Sync No Service Group Found", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "8"}
    :param sync_rx_persist_update_age_counter: {"description": "Conn Sync Update Persist Age Pkts Received counter", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param sync_rx_type_invalid: {"description": "Conn Sync Type Invalid", "format": "counter", "type": "number", "oid": "57", "optional": true, "size": "8"}
    :param sync_rx_ext_rtsp: {"description": "Conn Sync Ext RTSP", "format": "counter", "type": "number", "oid": "74", "optional": true, "size": "8"}
    :param sync_tx_lsn_fullcone: {"description": "Conn Sync Update LSN Fullcone Sent counter", "format": "counter", "type": "number", "oid": "81", "optional": true, "size": "8"}
    :param sync_rx_update_seqnos_counter: {"description": "Conn Sync Update Seq Num Received counter", "format": "counter", "type": "number", "oid": "61", "optional": true, "size": "8"}
    :param sync_rx_create_ext_bit_counter: {"description": "Conn Sync Create with Ext Received counter", "format": "counter", "type": "number", "oid": "49", "optional": true, "size": "8"}
    :param sync_persist_rx_no_such_rport: {"description": "Persist Conn Sync Real Port Not Found", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "8"}
    :param sync_tx_persist_del_counter: {"description": "Conn Sync Delete Persist Session Pkts Sent counter", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param sync_persist_rx_no_such_vport: {"description": "Persist Conn Sync Virt Port Not Found", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "8"}
    :param sync_rx_reserve_ha: {"description": "Conn Sync Reserve HA Conn", "format": "counter", "type": "number", "oid": "75", "optional": true, "size": "8"}
    :param sync_get_buff_failed_rt: {"description": "Conn Sync Get Buff Failure No Route", "format": "counter", "type": "number", "oid": "65", "optional": true, "size": "8"}
    :param sync_rx_conn_exists: {"description": "Conn Sync Create Conn Exists", "format": "counter", "type": "number", "oid": "50", "optional": true, "size": "8"}
    :param sync_err_lsn_fullcone: {"description": "Conn Sync LSN Fullcone Failure", "format": "counter", "type": "number", "oid": "83", "optional": true, "size": "8"}
    :param sync_get_buff_failed_port: {"description": "Conn Sync Get Buff Failure Wrong Port", "format": "counter", "type": "number", "oid": "66", "optional": true, "size": "8"}
    :param query_tx_get_buff_failed: {"description": "Conn Query Get Buff Failure", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "8"}
    :param sync_rx_ext_nat_mac: {"description": "Conn Sync NAT MAC Failure", "format": "counter", "type": "number", "oid": "80", "optional": true, "size": "8"}
    :param sync_pkt_rcv_counter: {"description": "Conn Sync Received counter", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param sync_tx_smp_radius_table_counter: {"description": "Conn Sync Update LSN RADIUS Sent counter", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "2"}
    :param sync_rx_proto_not_supported: {"description": "Conn Sync Protocol Invalid", "format": "counter", "type": "number", "oid": "52", "optional": true, "size": "8"}
    :param sync_tx_persist_update_age_counter: {"description": "Conn Sync Update Persist Age Pkts Sent counter", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "2"}
    :param query_rx_zero_info_counter: {"description": "Conn Query Packet Empty", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "8"}
    :param sync_rx_len_invalid: {"description": "Conn Sync Length Invalid", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "8"}
    :param query_pkt_invalid_idx_counter: {"description": "Conn Query Invalid Interface", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "8"}
    :param sync_rx_create_static_sby: {"description": "Conn Sync Create Static Standby", "format": "counter", "type": "number", "oid": "72", "optional": true, "size": "8"}
    :param sync_persist_rx_cannot_process_mandatory: {"description": "Persist Conn Sync Process Mandatory Invalid", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "8"}
    :param sync_persist_rx_len_invalid: {"description": "Persist Conn Sync Length Invalid", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "8"}
    :param sync_tx_total_info_counter: {"description": "Conn Sync Total Info Pkts Sent counter", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "8"}
    :param sync_pkt_invalid_idx_counter: {"description": "Conn Sync Invalid Interface", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "8"}
    :param sync_rx_nat_alloc_sby: {"description": "Conn Sync NAT Alloc Standby", "format": "counter", "type": "number", "oid": "69", "optional": true, "size": "8"}
    :param sync_rx_persist_del_counter: {"description": "Conn Sync Delete Persist Session Pkts Received counter", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param sync_rx_update_age_counter: {"description": "Conn Sync Update Age Received counter", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param sync_persist_rx_proto_not_supported: {"description": "Persist Conn Sync Protocol Invalid", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "8"}
    :param sync_rx_dcmsg_counter: {"description": "Conn Sync forward CPU", "format": "counter", "type": "number", "oid": "59", "optional": true, "size": "8"}
    :param query_tx_min_packed: {"description": "Min Query Msg Per Packet", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "2"}
    :param sync_tx_min_packed: {"description": "Max Sync Msg Per Packet", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "2"}
    :param sync_persist_rx_conn_get_failed: {"description": "Persist Conn Sync Get Conn Failure", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "8"}
    :param query_tx_max_packed: {"description": "Max Query Msg Per Packet", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "2"}
    :param sync_persist_rx_ext_bit_process_error: {"description": "Persist Conn Sync Proc Ext Bit Failure", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "8"}
    :param sync_rx_seq_deltas: {"description": "Conn Sync Seq Deltas Failure", "format": "counter", "type": "number", "oid": "76", "optional": true, "size": "8"}
    :param query_pkt_rcv_counter: {"description": "Conn Query Received counter", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "2"}
    :param sync_query_dcmsg_counter: {"description": "Conn Sync query forward CPU", "format": "counter", "type": "number", "oid": "64", "optional": true, "size": "8"}
    :param sync_rx_zero_info_counter: {"description": "Conn Sync Packet Empty", "format": "counter", "type": "number", "oid": "58", "optional": true, "size": "8"}
    :param sync_rx_ftp_control: {"description": "Conn Sync FTP Control Failure", "format": "counter", "type": "number", "oid": "77", "optional": true, "size": "8"}
    :param sync_pkt_tx_counter: {"description": "Conn Sync Sent counter", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param sync_rx_ext_sip_alg: {"description": "Conn Sync SIP TCP ALG Failure", "format": "counter", "type": "number", "oid": "79", "optional": true, "size": "8"}
    :param sync_rx_lsn_fullcone: {"description": "Conn Sync Update LSN Fullcone Received counter", "format": "counter", "type": "number", "oid": "82", "optional": true, "size": "8"}
    :param query_pkt_tx_counter: {"description": "Conn Query sent counter", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "2"}
    :param sync_tx_persist_create_counter: {"description": "Conn Sync Create Persist Session Pkts Sent counter", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "2"}
    :param sync_rx_smp_radius_table_counter: {"description": "Conn Sync Update LSN RADIUS Received counter", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "2"}
    :param query_rx_unk_counter: {"description": "Conn Query Unknown Type", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "8"}
    :param sync_rx_total_info_counter: {"description": "Conn Sync Total Info Pkts Received counter", "format": "counter", "type": "number", "oid": "60", "optional": true, "size": "8"}
    :param sync_rx_no_dst_for_vport_inline: {"description": "Conn Sync 'dst' not found for vport inline", "format": "counter", "type": "number", "oid": "53", "optional": true, "size": "8"}
    :param sync_rx_sfw: {"description": "Conn Sync SFW", "format": "counter", "type": "number", "oid": "71", "optional": true, "size": "8"}
    :param sync_rx_unk_counter: {"description": "Conn Sync Unknown Type", "format": "counter", "type": "number", "oid": "62", "optional": true, "size": "8"}
    :param sync_rx_ext_lsn_acl: {"description": "Conn Sync LSN ACL Failure", "format": "counter", "type": "number", "oid": "78", "optional": true, "size": "8"}
    :param sync_tx_create_counter: {"description": "Conn Sync Create Session Sent counter", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param sync_rx_del_no_such_session: {"description": "Conn Sync Del Conn not Found", "format": "counter", "type": "number", "oid": "56", "optional": true, "size": "8"}
    :param sync_tx_get_buff_failed: {"description": "Conn Sync Get Buff Failure", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "8"}
    :param sync_persist_rx_vporttype_not_supported: {"description": "Persist Conn Sync Virt Port Type Invalid", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "8"}
    :param sync_persist_rx_no_sg_group_info: {"description": "Persist Conn Sync No Service Group Info Found", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "8"}
    :param sync_rx_no_such_vport: {"description": "Conn Sync Virt Port Not Found", "format": "counter", "type": "number", "oid": "45", "optional": true, "size": "8"}
    :param sync_rx_create_counter: {"description": "Conn Sync Create Session Received counter", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param sync_rx_conn_get_failed: {"description": "Conn Sync Get Conn Failure", "format": "counter", "type": "number", "oid": "51", "optional": true, "size": "8"}
    :param sync_persist_rx_type_invalid: {"description": "Persist Conn Sync Type Invalid", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "8"}
    :param sync_rx_no_such_rport: {"description": "Conn Sync Real Port Not Found", "format": "counter", "type": "number", "oid": "46", "optional": true, "size": "8"}
    :param sync_rx_nat_create_sby: {"description": "Conn Sync NAT Create Standby", "format": "counter", "type": "number", "oid": "68", "optional": true, "size": "8"}
    :param sync_tx_update_age_counter: {"description": "Conn Sync Update Age Sent counter", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param sync_rx_del_counter: {"description": "Conn Sync Del Session Received counter", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param sync_rx_no_such_nat_pool: {"description": "Conn Sync NAT Pool Error", "format": "counter", "type": "number", "oid": "54", "optional": true, "size": "8"}
    :param sync_tx_del_counter: {"description": "Conn Sync Del Session Sent counter", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param query_rx_full_info_counter: {"description": "Conn Query Packet Full", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "8"}
    :param sync_rx_lsn_create_sby: {"description": "Conn Sync LSN Create Standby", "format": "counter", "type": "number", "oid": "67", "optional": true, "size": "8"}
    :param sync_rx_ext_bit_process_error: {"description": "Conn Sync Proc Ext Bit Failure", "format": "counter", "type": "number", "oid": "48", "optional": true, "size": "8"}
    :param sync_rx_cannot_process_mandatory: {"description": "Conn Sync Process Mandatory Invalid", "format": "counter", "type": "number", "oid": "47", "optional": true, "size": "8"}
    :param sync_rx_insert_tuple: {"description": "Conn Sync Insert Tuple", "format": "counter", "type": "number", "oid": "70", "optional": true, "size": "8"}
    :param sync_tx_update_seqnos_counter: {"description": "Conn Sync Update Seq Num Sent counter", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "8"}
    :param sync_rx_persist_create_counter: {"description": "Conn Sync Create Persist Session Pkts Received counter", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param sync_rx_no_such_sg_node: {"description": "Conn Sync no SG node found", "format": "counter", "type": "number", "oid": "55", "optional": true, "size": "8"}
    :param sync_rx_ext_pptp: {"description": "Conn Sync Ext PPTP", "format": "counter", "type": "number", "oid": "73", "optional": true, "size": "8"}
    :param sync_rx_apptype_not_supported: {"description": "Conn Sync App Type Invalid", "format": "counter", "type": "number", "oid": "63", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.sync_tx_create_ext_bit_counter = ""
        self.sync_tx_max_packed = ""
        self.sync_persist_rx_no_such_sg_group = ""
        self.sync_rx_persist_update_age_counter = ""
        self.sync_rx_type_invalid = ""
        self.sync_rx_ext_rtsp = ""
        self.sync_tx_lsn_fullcone = ""
        self.sync_rx_update_seqnos_counter = ""
        self.sync_rx_create_ext_bit_counter = ""
        self.sync_persist_rx_no_such_rport = ""
        self.sync_tx_persist_del_counter = ""
        self.sync_persist_rx_no_such_vport = ""
        self.sync_rx_reserve_ha = ""
        self.sync_get_buff_failed_rt = ""
        self.sync_rx_conn_exists = ""
        self.sync_err_lsn_fullcone = ""
        self.sync_get_buff_failed_port = ""
        self.query_tx_get_buff_failed = ""
        self.sync_rx_ext_nat_mac = ""
        self.sync_pkt_rcv_counter = ""
        self.sync_tx_smp_radius_table_counter = ""
        self.sync_rx_proto_not_supported = ""
        self.sync_tx_persist_update_age_counter = ""
        self.query_rx_zero_info_counter = ""
        self.sync_rx_len_invalid = ""
        self.query_pkt_invalid_idx_counter = ""
        self.sync_rx_create_static_sby = ""
        self.sync_persist_rx_cannot_process_mandatory = ""
        self.sync_persist_rx_len_invalid = ""
        self.sync_tx_total_info_counter = ""
        self.sync_pkt_invalid_idx_counter = ""
        self.sync_rx_nat_alloc_sby = ""
        self.sync_rx_persist_del_counter = ""
        self.sync_rx_update_age_counter = ""
        self.sync_persist_rx_proto_not_supported = ""
        self.sync_rx_dcmsg_counter = ""
        self.query_tx_min_packed = ""
        self.sync_tx_min_packed = ""
        self.sync_persist_rx_conn_get_failed = ""
        self.query_tx_max_packed = ""
        self.sync_persist_rx_ext_bit_process_error = ""
        self.sync_rx_seq_deltas = ""
        self.query_pkt_rcv_counter = ""
        self.sync_query_dcmsg_counter = ""
        self.sync_rx_zero_info_counter = ""
        self.sync_rx_ftp_control = ""
        self.sync_pkt_tx_counter = ""
        self.sync_rx_ext_sip_alg = ""
        self.sync_rx_lsn_fullcone = ""
        self.query_pkt_tx_counter = ""
        self.sync_tx_persist_create_counter = ""
        self.sync_rx_smp_radius_table_counter = ""
        self.query_rx_unk_counter = ""
        self.sync_rx_total_info_counter = ""
        self.sync_rx_no_dst_for_vport_inline = ""
        self.sync_rx_sfw = ""
        self.sync_rx_unk_counter = ""
        self.sync_rx_ext_lsn_acl = ""
        self.sync_tx_create_counter = ""
        self.sync_rx_del_no_such_session = ""
        self.sync_tx_get_buff_failed = ""
        self.sync_persist_rx_vporttype_not_supported = ""
        self.sync_persist_rx_no_sg_group_info = ""
        self.sync_rx_no_such_vport = ""
        self.sync_rx_create_counter = ""
        self.sync_rx_conn_get_failed = ""
        self.sync_persist_rx_type_invalid = ""
        self.sync_rx_no_such_rport = ""
        self.sync_rx_nat_create_sby = ""
        self.sync_tx_update_age_counter = ""
        self.sync_rx_del_counter = ""
        self.sync_rx_no_such_nat_pool = ""
        self.sync_tx_del_counter = ""
        self.query_rx_full_info_counter = ""
        self.sync_rx_lsn_create_sby = ""
        self.sync_rx_ext_bit_process_error = ""
        self.sync_rx_cannot_process_mandatory = ""
        self.sync_rx_insert_tuple = ""
        self.sync_tx_update_seqnos_counter = ""
        self.sync_rx_persist_create_counter = ""
        self.sync_rx_no_such_sg_node = ""
        self.sync_rx_ext_pptp = ""
        self.sync_rx_apptype_not_supported = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class State(A10BaseClass):
    
    """Class Description::
    Statistics for the object state.

    Class state supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/vrrp-a/state/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "state"
        self.a10_url="/axapi/v3/vrrp-a/state/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


