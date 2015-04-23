from a10sdk.common.A10BaseClass import A10BaseClass


class Common(A10BaseClass):
    
    """Class Description::
    SLB related commands.

    Class common supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param stats_data_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable global slb data statistics", "format": "flag"}
    :param compress_block_size: {"description": "Set compression block size (Compression block size in bytes)", "format": "number", "type": "number", "maximum": 131008, "minimum": 6000, "optional": true}
    :param dns_cache_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable DNS cache", "format": "flag"}
    :param msl_time: {"description": "Configure maximum session life, default is 2 seconds (1-40 seconds, default is 2 seconds)", "format": "number", "default": 2, "optional": true, "maximum": 40, "minimum": 1, "type": "number"}
    :param graceful_shutdown_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable graceful shutdown", "format": "flag"}
    :param buff_thresh_hw_buff: {"description": "Set hardware buffer threshold", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 1, "optional": true}
    :param hw_syn_rr: {"description": "Configure hardware SYN round robin (range 1-500000)", "format": "number", "type": "number", "maximum": 500000, "minimum": 1, "optional": true}
    :param entity: {"optional": true, "enum": ["server", "virtual-server"], "type": "string", "description": "'server': Graceful shutdown server/port only; 'virtual-server': Graceful shutdown virtual server/port only; ", "format": "enum"}
    :param rate_limit_logging: {"default": 0, "optional": true, "type": "number", "description": "Configure rate limit logging", "format": "flag"}
    :param scale_out: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB scale out", "format": "flag"}
    :param graceful_shutdown: {"description": "1-65535, in unit of seconds", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}
    :param exclude_destination: {"optional": true, "enum": ["local", "remote"], "type": "string", "description": "'local': Maximum local rate; 'remote': Maximum remote rate;  (Maximum rates)", "format": "enum"}
    :param fast_path_disable: {"default": 0, "optional": true, "type": "number", "description": "Disable fast path in SLB processing", "format": "flag"}
    :param drop_icmp_to_vip_when_vip_down: {"default": 0, "optional": true, "type": "number", "description": "Drop ICMP to VIP when VIP down", "format": "flag"}
    :param buff_thresh: {"default": 0, "optional": true, "type": "number", "description": "Set buffer threshold", "format": "flag"}
    :param hw_compression: {"default": 0, "optional": true, "type": "number", "description": "Use hardware compression", "format": "flag"}
    :param extended_stats: {"default": 0, "optional": true, "type": "number", "description": "Enable global slb extended statistics", "format": "flag"}
    :param buff_thresh_sys_buff_low: {"description": "Set low water mark of system buffer", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param after_disable: {"default": 0, "optional": true, "type": "number", "description": "Graceful shutdown after disable server/port and/or virtual server/port", "format": "flag"}
    :param max_local_rate: {"description": "Set maximum local rate", "format": "number", "default": 32, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param dns_cache_age: {"description": "Set DNS cache entry age, default is 300 seconds (1-1000000 seconds, default is 300 seconds)", "format": "number", "type": "number", "maximum": 1000000, "minimum": 1, "optional": true}
    :param max_http_header_count: {"description": "Set maximum number of HTTP headers allowed", "partition-visibility": "shared", "default": 90, "optional": true, "format": "number", "maximum": 255, "minimum": 90, "type": "number"}
    :param l2l3_trunk_lb_disable: {"description": "Disable L2/L3 trunk LB", "partition-visibility": "shared", "default": 0, "type": "number", "format": "flag", "optional": true}
    :param sort_res: {"default": 0, "optional": true, "type": "number", "description": "Enable SLB sorting of resource names", "format": "flag"}
    :param snat_gwy_for_l3: {"default": 0, "optional": true, "type": "number", "description": "Use source NAT gateway for L3 traffic", "format": "flag"}
    :param buff_thresh_relieve_thresh: {"description": "Relieve threshold", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param dsr_health_check_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable dsr-health-check (direct server return health check)", "format": "flag"}
    :param dns_vip_stateless: {"description": "Enable DNS VIP stateless mode", "format": "flag", "default": 0, "type": "number", "optional": true, "plat-neg-list": ["non-fpga", "soft-ax"]}
    :param dns_cache_entry_size: {"description": "Set DNS cache entry size, default is 256 bytes (1-4096 bytes, default is 256 bytes)", "format": "number", "default": 256, "optional": true, "maximum": 4096, "minimum": 1, "type": "number"}
    :param buff_thresh_sys_buff_high: {"description": "Set high water mark of system buffer", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param max_buff_queued_per_conn: {"description": "Set per connection buffer threshold (Buffer value range 128-4096)", "partition-visibility": "shared", "optional": true, "format": "number", "maximum": 4096, "minimum": 128, "type": "number"}
    :param max_remote_rate: {"description": "Set maximum remote rate", "format": "number", "default": 15000, "optional": true, "maximum": 1000000, "minimum": 1, "type": "number"}
    :param ttl_threshold: {"description": "Only cache DNS response with longer TTL", "format": "number", "type": "number", "maximum": 10000000, "minimum": 1, "optional": true}
    :param response_type: {"optional": true, "enum": ["single-answer", "round-robin"], "type": "string", "description": "'single-answer': Only cache DNS response with single answer; 'round-robin': Round robin; ", "format": "enum"}
    :param enable_l7_req_acct: {"default": 0, "optional": true, "type": "number", "description": "Enable L7 request accounting", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param snat_on_vip: {"default": 0, "optional": true, "type": "number", "description": "Enable source NAT traffic against VIP", "format": "flag"}
    :param disable_server_auto_reselect: {"default": 0, "optional": true, "type": "number", "description": "Disable auto reselection of server", "format": "flag"}
    :param interval: {"description": "Specify the healthcheck interval, default is 5 seconds (Interval Value, in seconds (default 5))", "format": "number", "type": "number", "maximum": 180, "minimum": 1, "optional": true}
    :param gateway_health_check: {"default": 0, "optional": true, "type": "number", "description": "Enable gateway health check", "format": "flag"}
    :param mss_table: {"description": "Set MSS table (128-750, default is 536)", "partition-visibility": "shared", "default": 536, "optional": true, "format": "number", "maximum": 750, "minimum": 128, "type": "number"}
    :param timeout: {"description": "Specify the healthcheck timeout value, default is 15 seconds (Timeout Value, in seconds (default 15))", "format": "number", "default": 15, "optional": true, "maximum": 60, "minimum": 1, "type": "number"}
    :param use_mss_tab: {"default": 0, "optional": true, "type": "number", "description": "Use MSS based on internal table for SLB processing", "format": "flag"}
    :param reset_stale_session: {"default": 0, "optional": true, "type": "number", "description": "Send reset if session in delete queue receives a SYN packet", "format": "flag"}
    :param no_auto_up_on_aflex: {"default": 0, "optional": true, "type": "number", "description": "Don't automatically mark vport up when aFleX is bound", "format": "flag"}
    :param software: {"default": 0, "optional": true, "type": "number", "description": "Software", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/common`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "common"
        self.a10_url="/axapi/v3/slb/common"
        self.DeviceProxy = ""
        self.stats_data_disable = ""
        self.compress_block_size = ""
        self.dns_cache_enable = ""
        self.msl_time = ""
        self.graceful_shutdown_enable = ""
        self.buff_thresh_hw_buff = ""
        self.hw_syn_rr = ""
        self.entity = ""
        self.rate_limit_logging = ""
        self.scale_out = ""
        self.graceful_shutdown = ""
        self.exclude_destination = ""
        self.fast_path_disable = ""
        self.drop_icmp_to_vip_when_vip_down = ""
        self.buff_thresh = ""
        self.hw_compression = ""
        self.extended_stats = ""
        self.buff_thresh_sys_buff_low = ""
        self.after_disable = ""
        self.max_local_rate = ""
        self.dns_cache_age = ""
        self.max_http_header_count = ""
        self.l2l3_trunk_lb_disable = ""
        self.sort_res = ""
        self.snat_gwy_for_l3 = ""
        self.buff_thresh_relieve_thresh = ""
        self.dsr_health_check_enable = ""
        self.dns_vip_stateless = ""
        self.dns_cache_entry_size = ""
        self.buff_thresh_sys_buff_high = ""
        self.max_buff_queued_per_conn = ""
        self.max_remote_rate = ""
        self.ttl_threshold = ""
        self.response_type = ""
        self.enable_l7_req_acct = ""
        self.uuid = ""
        self.snat_on_vip = ""
        self.disable_server_auto_reselect = ""
        self.interval = ""
        self.gateway_health_check = ""
        self.conn_rate_limit = {}
        self.mss_table = ""
        self.timeout = ""
        self.use_mss_tab = ""
        self.reset_stale_session = ""
        self.no_auto_up_on_aflex = ""
        self.software = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


