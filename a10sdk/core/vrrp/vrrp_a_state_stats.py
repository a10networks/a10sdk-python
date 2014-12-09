from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param sync_rx_nat_create_sby: {"optional": true, "size": "8", "type": "number", "oid": "74", "format": "counter"}
    :param sync_rx_type_invalid: {"optional": true, "size": "8", "type": "number", "oid": "63", "format": "counter"}
    :param sync_persist_rx_no_such_sg_group: {"optional": true, "size": "8", "type": "number", "oid": "48", "format": "counter"}
    :param sync_rx_conn_exists: {"optional": true, "size": "8", "type": "number", "oid": "56", "format": "counter"}
    :param sync_get_buff_failed_port: {"optional": true, "size": "8", "type": "number", "oid": "72", "format": "counter"}
    :param err_port_counter: {"optional": true, "size": "8", "type": "number", "oid": "21", "format": "counter"}
    :param sync_tx_smp_radius_table_counter: {"optional": true, "size": "2", "type": "number", "oid": "17", "format": "counter"}
    :param err_parid_counter: {"optional": true, "size": "8", "type": "number", "oid": "23", "format": "counter"}
    :param sync_tx_total_info_counter: {"optional": true, "size": "8", "type": "number", "oid": "34", "format": "counter"}
    :param sync_rx_nat_alloc_sby: {"optional": true, "size": "8", "type": "number", "oid": "75", "format": "counter"}
    :param query_tx_min_packed: {"optional": true, "size": "2", "type": "number", "oid": "26", "format": "counter"}
    :param sync_rx_ext_bit_process_error: {"optional": true, "size": "8", "type": "number", "oid": "54", "format": "counter"}
    :param sync_rx_ext_nat_mac: {"optional": true, "size": "8", "type": "number", "oid": "86", "format": "counter"}
    :param sync_rx_lsn_fullcone: {"optional": true, "size": "8", "type": "number", "oid": "88", "format": "counter"}
    :param query_pkt_tx_counter: {"optional": true, "size": "2", "type": "number", "oid": "15", "format": "counter"}
    :param sync_rx_unk_counter: {"optional": true, "size": "8", "type": "number", "oid": "68", "format": "counter"}
    :param dup_id_rcv_counter: {"optional": true, "size": "8", "type": "number", "oid": "19", "format": "counter"}
    :param sync_tx_create_counter: {"optional": true, "size": "2", "type": "number", "oid": "6", "format": "counter"}
    :param sync_persist_rx_len_invalid: {"optional": true, "size": "8", "type": "number", "oid": "40", "format": "counter"}
    :param sync_rx_create_counter: {"optional": true, "size": "2", "type": "number", "oid": "3", "format": "counter"}
    :param err_devid_counter: {"optional": true, "size": "8", "type": "number", "oid": "24", "format": "counter"}
    :param sync_pkt_rcv_counter: {"optional": true, "size": "2", "type": "number", "oid": "2", "format": "counter"}
    :param sync_rx_len_invalid: {"optional": true, "size": "8", "type": "number", "oid": "39", "format": "counter"}
    :param sync_rx_ftp_control: {"optional": true, "size": "8", "type": "number", "oid": "83", "format": "counter"}
    :param sync_rx_persist_create_counter: {"optional": true, "size": "2", "type": "number", "oid": "9", "format": "counter"}
    :param sync_rx_ext_lsn_acl: {"optional": true, "size": "8", "type": "number", "oid": "84", "format": "counter"}
    :param sync_rx_ext_rtsp: {"optional": true, "size": "8", "type": "number", "oid": "80", "format": "counter"}
    :param sync_rx_update_seqnos_counter: {"optional": true, "size": "8", "type": "number", "oid": "67", "format": "counter"}
    :param sync_rx_conn_get_failed: {"optional": true, "size": "8", "type": "number", "oid": "57", "format": "counter"}
    :param sync_tx_persist_del_counter: {"optional": true, "size": "2", "type": "number", "oid": "13", "format": "counter"}
    :param sync_err_lsn_fullcone: {"optional": true, "size": "8", "type": "number", "oid": "89", "format": "counter"}
    :param sync_tx_del_counter: {"optional": true, "size": "2", "type": "number", "oid": "7", "format": "counter"}
    :param sync_tx_persist_update_age_counter: {"optional": true, "size": "2", "type": "number", "oid": "14", "format": "counter"}
    :param sync_persist_rx_vporttype_not_supported: {"optional": true, "size": "8", "type": "number", "oid": "46", "format": "counter"}
    :param sync_rx_dcmsg_counter: {"optional": true, "size": "8", "type": "number", "oid": "65", "format": "counter"}
    :param sync_rx_del_no_such_session: {"optional": true, "size": "8", "type": "number", "oid": "62", "format": "counter"}
    :param sync_tx_lsn_fullcone: {"optional": true, "size": "8", "type": "number", "oid": "87", "format": "counter"}
    :param sync_tx_persist_create_counter: {"optional": true, "size": "2", "type": "number", "oid": "12", "format": "counter"}
    :param sync_rx_smp_radius_table_counter: {"optional": true, "size": "2", "type": "number", "oid": "18", "format": "counter"}
    :param sync_tx_update_seqnos_counter: {"optional": true, "size": "8", "type": "number", "oid": "36", "format": "counter"}
    :param sync_rx_total_info_counter: {"optional": true, "size": "8", "type": "number", "oid": "66", "format": "counter"}
    :param sync_tx_get_buff_failed: {"optional": true, "size": "8", "type": "number", "oid": "33", "format": "counter"}
    :param sync_rx_create_ext_bit_counter: {"optional": true, "size": "8", "type": "number", "oid": "55", "format": "counter"}
    :param sync_rx_no_such_sg_node: {"optional": true, "size": "8", "type": "number", "oid": "61", "format": "counter"}
    :param sync_tx_update_age_counter: {"optional": true, "size": "2", "type": "number", "oid": "8", "format": "counter"}
    :param sync_rx_lsn_create_sby: {"optional": true, "size": "8", "type": "number", "oid": "73", "format": "counter"}
    :param sync_get_buff_failed_rt: {"optional": true, "size": "8", "type": "number", "oid": "71", "format": "counter"}
    :param sync_tx_create_ext_bit_counter: {"optional": true, "size": "8", "type": "number", "oid": "35", "format": "counter"}
    :param sync_tx_max_packed: {"optional": true, "size": "2", "type": "number", "oid": "38", "format": "counter"}
    :param sync_rx_persist_update_age_counter: {"optional": true, "size": "2", "type": "number", "oid": "11", "format": "counter"}
    :param sync_rx_sfw: {"optional": true, "size": "8", "type": "number", "oid": "77", "format": "counter"}
    :param sync_rx_seq_deltas: {"optional": true, "size": "8", "type": "number", "oid": "82", "format": "counter"}
    :param sync_rx_proto_not_supported: {"optional": true, "size": "8", "type": "number", "oid": "58", "format": "counter"}
    :param query_pkt_invalid_idx_counter: {"optional": true, "size": "8", "type": "number", "oid": "27", "format": "counter"}
    :param sync_rx_create_static_sby: {"optional": true, "size": "8", "type": "number", "oid": "78", "format": "counter"}
    :param sync_rx_persist_del_counter: {"optional": true, "size": "2", "type": "number", "oid": "10", "format": "counter"}
    :param sync_rx_update_age_counter: {"optional": true, "size": "2", "type": "number", "oid": "5", "format": "counter"}
    :param query_tx_max_packed: {"optional": true, "size": "2", "type": "number", "oid": "25", "format": "counter"}
    :param sync_persist_rx_ext_bit_process_error: {"optional": true, "size": "8", "type": "number", "oid": "44", "format": "counter"}
    :param query_pkt_rcv_counter: {"optional": true, "size": "2", "type": "number", "oid": "16", "format": "counter"}
    :param sync_rx_zero_info_counter: {"optional": true, "size": "8", "type": "number", "oid": "64", "format": "counter"}
    :param sync_pkt_tx_counter: {"optional": true, "size": "2", "type": "number", "oid": "1", "format": "counter"}
    :param sync_rx_ext_sip_alg: {"optional": true, "size": "8", "type": "number", "oid": "85", "format": "counter"}
    :param sync_rx_reserve_ha: {"optional": true, "size": "8", "type": "number", "oid": "81", "format": "counter"}
    :param vrrp_version_mismatch_counter: {"optional": true, "size": "8", "type": "number", "oid": "20", "format": "counter"}
    :param sync_rx_ext_pptp: {"optional": true, "size": "8", "type": "number", "oid": "79", "format": "counter"}
    :param sync_persist_rx_type_invalid: {"optional": true, "size": "8", "type": "number", "oid": "42", "format": "counter"}
    :param sync_rx_insert_tuple: {"optional": true, "size": "8", "type": "number", "oid": "76", "format": "counter"}
    :param sync_rx_no_such_nat_pool: {"optional": true, "size": "8", "type": "number", "oid": "60", "format": "counter"}
    :param sync_pkt_invalid_idx_counter: {"optional": true, "size": "8", "type": "number", "oid": "32", "format": "counter"}
    :param sync_rx_no_such_rport: {"optional": true, "size": "8", "type": "number", "oid": "52", "format": "counter"}
    :param sync_rx_apptype_not_supported: {"optional": true, "size": "8", "type": "number", "oid": "69", "format": "counter"}
    :param query_rx_zero_info_counter: {"optional": true, "size": "8", "type": "number", "oid": "29", "format": "counter"}
    :param sync_persist_rx_no_such_rport: {"optional": true, "size": "8", "type": "number", "oid": "47", "format": "counter"}
    :param sync_persist_rx_no_such_vport: {"optional": true, "size": "8", "type": "number", "oid": "45", "format": "counter"}
    :param query_tx_get_buff_failed: {"optional": true, "size": "8", "type": "number", "oid": "28", "format": "counter"}
    :param sync_persist_rx_cannot_process_mandatory: {"optional": true, "size": "8", "type": "number", "oid": "43", "format": "counter"}
    :param sync_persist_rx_proto_not_supported: {"optional": true, "size": "8", "type": "number", "oid": "41", "format": "counter"}
    :param sync_persist_rx_conn_get_failed: {"optional": true, "size": "8", "type": "number", "oid": "50", "format": "counter"}
    :param sync_rx_cannot_process_mandatory: {"optional": true, "size": "8", "type": "number", "oid": "53", "format": "counter"}
    :param sync_tx_min_packed: {"optional": true, "size": "2", "type": "number", "oid": "37", "format": "counter"}
    :param query_rx_unk_counter: {"optional": true, "size": "8", "type": "number", "oid": "31", "format": "counter"}
    :param sync_persist_rx_no_sg_group_info: {"optional": true, "size": "8", "type": "number", "oid": "49", "format": "counter"}
    :param sync_rx_no_such_vport: {"optional": true, "size": "8", "type": "number", "oid": "51", "format": "counter"}
    :param set_id_mismatch_counter: {"optional": true, "size": "8", "type": "number", "oid": "22", "format": "counter"}
    :param sync_rx_del_counter: {"optional": true, "size": "2", "type": "number", "oid": "4", "format": "counter"}
    :param query_rx_full_info_counter: {"optional": true, "size": "8", "type": "number", "oid": "30", "format": "counter"}
    :param sync_query_dcmsg_counter: {"optional": true, "size": "8", "type": "number", "oid": "70", "format": "counter"}
    :param sync_rx_no_dst_for_vport_inline: {"optional": true, "size": "8", "type": "number", "oid": "59", "format": "counter"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.sync_rx_nat_create_sby = ""
        self.sync_rx_type_invalid = ""
        self.sync_persist_rx_no_such_sg_group = ""
        self.sync_rx_conn_exists = ""
        self.sync_get_buff_failed_port = ""
        self.err_port_counter = ""
        self.sync_tx_smp_radius_table_counter = ""
        self.err_parid_counter = ""
        self.sync_tx_total_info_counter = ""
        self.sync_rx_nat_alloc_sby = ""
        self.query_tx_min_packed = ""
        self.sync_rx_ext_bit_process_error = ""
        self.sync_rx_ext_nat_mac = ""
        self.sync_rx_lsn_fullcone = ""
        self.query_pkt_tx_counter = ""
        self.sync_rx_unk_counter = ""
        self.dup_id_rcv_counter = ""
        self.sync_tx_create_counter = ""
        self.sync_persist_rx_len_invalid = ""
        self.sync_rx_create_counter = ""
        self.err_devid_counter = ""
        self.sync_pkt_rcv_counter = ""
        self.sync_rx_len_invalid = ""
        self.sync_rx_ftp_control = ""
        self.sync_rx_persist_create_counter = ""
        self.sync_rx_ext_lsn_acl = ""
        self.sync_rx_ext_rtsp = ""
        self.sync_rx_update_seqnos_counter = ""
        self.sync_rx_conn_get_failed = ""
        self.sync_tx_persist_del_counter = ""
        self.sync_err_lsn_fullcone = ""
        self.sync_tx_del_counter = ""
        self.sync_tx_persist_update_age_counter = ""
        self.sync_persist_rx_vporttype_not_supported = ""
        self.sync_rx_dcmsg_counter = ""
        self.sync_rx_del_no_such_session = ""
        self.sync_tx_lsn_fullcone = ""
        self.sync_tx_persist_create_counter = ""
        self.sync_rx_smp_radius_table_counter = ""
        self.sync_tx_update_seqnos_counter = ""
        self.sync_rx_total_info_counter = ""
        self.sync_tx_get_buff_failed = ""
        self.sync_rx_create_ext_bit_counter = ""
        self.sync_rx_no_such_sg_node = ""
        self.sync_tx_update_age_counter = ""
        self.sync_rx_lsn_create_sby = ""
        self.sync_get_buff_failed_rt = ""
        self.sync_tx_create_ext_bit_counter = ""
        self.sync_tx_max_packed = ""
        self.sync_rx_persist_update_age_counter = ""
        self.sync_rx_sfw = ""
        self.sync_rx_seq_deltas = ""
        self.sync_rx_proto_not_supported = ""
        self.query_pkt_invalid_idx_counter = ""
        self.sync_rx_create_static_sby = ""
        self.sync_rx_persist_del_counter = ""
        self.sync_rx_update_age_counter = ""
        self.query_tx_max_packed = ""
        self.sync_persist_rx_ext_bit_process_error = ""
        self.query_pkt_rcv_counter = ""
        self.sync_rx_zero_info_counter = ""
        self.sync_pkt_tx_counter = ""
        self.sync_rx_ext_sip_alg = ""
        self.sync_rx_reserve_ha = ""
        self.vrrp_version_mismatch_counter = ""
        self.sync_rx_ext_pptp = ""
        self.sync_persist_rx_type_invalid = ""
        self.sync_rx_insert_tuple = ""
        self.sync_rx_no_such_nat_pool = ""
        self.sync_pkt_invalid_idx_counter = ""
        self.sync_rx_no_such_rport = ""
        self.sync_rx_apptype_not_supported = ""
        self.query_rx_zero_info_counter = ""
        self.sync_persist_rx_no_such_rport = ""
        self.sync_persist_rx_no_such_vport = ""
        self.query_tx_get_buff_failed = ""
        self.sync_persist_rx_cannot_process_mandatory = ""
        self.sync_persist_rx_proto_not_supported = ""
        self.sync_persist_rx_conn_get_failed = ""
        self.sync_rx_cannot_process_mandatory = ""
        self.sync_tx_min_packed = ""
        self.query_rx_unk_counter = ""
        self.sync_persist_rx_no_sg_group_info = ""
        self.sync_rx_no_such_vport = ""
        self.set_id_mismatch_counter = ""
        self.sync_rx_del_counter = ""
        self.query_rx_full_info_counter = ""
        self.sync_query_dcmsg_counter = ""
        self.sync_rx_no_dst_for_vport_inline = ""

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


