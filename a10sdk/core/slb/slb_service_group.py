from a10sdk.common.A10BaseClass import A10BaseClass


class Priorities(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param priority: {"description": "Priority option. Define different action for each priority node. (Priority in the Group)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}
    :param priority_action: {"default": "proceed", "enum": ["drop", "drop-if-exceed-limit", "proceed", "reset", "reset-if-exceed-limit"], "type": "string", "description": "'drop': Drop request when all priority nodes fail; 'drop-if-exceed-limit': Drop request when connection over limit; 'proceed': Proceed to next priority when all priority nodes fail(default); 'reset': Send client reset when all priority nodes fail; 'reset-if-exceed-limit': Send client reset when connection over limit; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "priorities"
        self.DeviceProxy = ""
        self.priority = ""
        self.priority_action = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class ServiceGroup(A10BaseClass):
    
    """Class Description::
    Service Group.

    Class service-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param conn_rate: {"description": "Dynamically enable stateless method by conn-rate (Rate to trigger stateless method(conn/sec))", "format": "number", "type": "number", "maximum": 1000000, "minimum": 1, "optional": true}
    :param reset_on_server_selection_fail: {"default": 0, "optional": true, "type": "number", "description": "Send reset to client if server selection fails", "format": "flag"}
    :param health_check_disable: {"description": "Disable health check", "format": "flag", "default": 0, "optional": true, "not": "health-check", "type": "number"}
    :param protocol: {"description": "'tcp': TCP LB service; 'udp': UDP LB service; ", "format": "enum", "type": "string", "enum": ["tcp", "udp"], "modify-not-allowed": 1, "optional": true}
    :param traffic_replication_mirror: {"default": 0, "optional": true, "type": "number", "description": "Mirror Bi-directional Packet", "format": "flag"}
    :param traffic_replication_mirror_ip_repl: {"default": 0, "optional": true, "type": "number", "description": "Replaces IP with server-IP", "format": "flag"}
    :param reset_priority_affinity: {"default": 0, "optional": true, "type": "number", "description": "Reset", "format": "flag"}
    :param min_active_member: {"description": "Minimum Active Member Per Priority (Minimum Active Member before Action)", "format": "number", "type": "number", "maximum": 63, "minimum": 1, "optional": true}
    :param member_list: {"minItems": 1, "items": {"type": "member"}, "uniqueItems": true, "array": [{"required": ["name", "port"], "properties": {"member-priority": {"description": "Priority of Port in the Group", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": true}, "name": {"description": "Member name", "format": "comp-string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string", "$ref": "/axapi/v3/slb/server"}, "fqdn-name": {"description": "Server hostname - Not applicable if real server is already defined", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}, "member-template": {"description": "Real server port template (Real server port template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/port"}, "host": {"optional": true, "type": "string", "description": "IP Address - Not applicable if real server is already defined", "format": "ipv4-address"}, "member-state": {"description": "'enable': Enable member service port; 'disable': Disable member service port; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}, "server-ipv6-addr": {"optional": true, "type": "string", "description": "IPV6 Address - Not applicable if real server is already defined", "format": "ipv6-address"}, "port": {"description": "Port number", "format": "number", "default": 65534, "optional": false, "maximum": 65534, "minimum": 0, "type": "number", "$ref": "/axapi/v3/slb/server/port"}, "member-stats-data-disable": {"default": 0, "optional": true, "type": "number", "description": "Disable statistical data collection", "format": "flag"}}}], "type": "array", "$ref": "/axapi/v3/slb/service-group/{name}/member/{name}+{port}"}
    :param stats_data_action: {"description": "'stats-data-enable': Enable statistical data collection for service group; 'stats-data-disable': Disable statistical data collection for service group; ", "format": "enum", "default": "stats-data-enable", "type": "string", "enum": ["stats-data-enable", "stats-data-disable"], "optional": true}
    :param traffic_replication_mirror_da_repl: {"default": 0, "optional": true, "type": "number", "description": "Replace Destination MAC", "format": "flag"}
    :param rpt_ext_server: {"default": 0, "optional": true, "type": "number", "description": "Report top 10 fastest/slowest servers", "format": "flag"}
    :param template_port: {"description": "Port template (Port template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/port"}
    :param conn_rate_grace_period: {"description": "Define the grace period during transition (Define the grace period during transition(seconds))", "format": "number", "type": "number", "maximum": 600, "minimum": 1, "optional": true}
    :param l4_session_usage_duration: {"description": "Period that trigger condition consistently happens(seconds)", "format": "number", "type": "number", "maximum": 600, "minimum": 1, "optional": true}
    :param backup_server_event_log: {"default": 0, "optional": true, "type": "number", "description": "Send log info on back up server events", "format": "flag"}
    :param lc_method: {"description": "'least-connection': Least connection on server level; 'service-least-connection': Least connection on service port level; 'weighted-least-connection': Weighted least connection on server level; 'service-weighted-least-connection': Weighted least connection on service port level; ", "format": "enum", "optional": true, "enum": ["least-connection", "service-least-connection", "weighted-least-connection", "service-weighted-least-connection"], "not-list": ["lb-method", "stateless-lb-method"], "type": "string"}
    :param pseudo_round_robin: {"default": 0, "optional": true, "type": "number", "description": "PRR, select the oldest node for sub-select", "format": "flag"}
    :param l4_session_usage_revert_rate: {"description": "Usage to revert to statelful method", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}
    :param template_server: {"description": "Server template (Server template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/server"}
    :param stateless_lb_method: {"description": "'stateless-dst-ip-hash': Stateless load-balancing based on Dst IP and Dst port hash; 'stateless-per-pkt-round-robin': Stateless load-balancing using per-packet round-robin; 'stateless-src-dst-ip-hash': Stateless load-balancing based on IP and port hash for both Src and Dst; 'stateless-src-ip-hash': Stateless load-balancing based on Src IP and Src port hash; 'stateless-src-ip-only-hash': Stateless load-balancing based on only Src IP hash; ", "format": "enum", "optional": true, "enum": ["stateless-dst-ip-hash", "stateless-per-pkt-round-robin", "stateless-src-dst-ip-hash", "stateless-src-ip-hash", "stateless-src-ip-only-hash"], "not-list": ["lb-method", "lc-method"], "type": "string"}
    :param l4_session_revert_duration: {"description": "Period that revert condition consistently happens(seconds)", "format": "number", "type": "number", "maximum": 600, "minimum": 1, "optional": true}
    :param traffic_replication_mirror_sa_da_repl: {"default": 0, "optional": true, "type": "number", "description": "Replace Source MAC and Destination MAC", "format": "flag"}
    :param lb_method: {"description": "'dst-ip-hash': Load-balancing based on only Dst IP and Port hash; 'dst-ip-only-hash': Load-balancing based on only Dst IP hash; 'fastest-response': Fastest response time on service port level; 'least-request': Least request on service port level; 'src-ip-hash': Load-balancing based on only Src IP and Port hash; 'src-ip-only-hash': Load-balancing based on only Src IP hash; 'weighted-rr': Weighted round robin on server level; 'round-robin': Round robin on server level; 'round-robin-strict': Strict mode round robin on server level; ", "format": "enum", "default": "round-robin", "optional": true, "enum": ["dst-ip-hash", "dst-ip-only-hash", "fastest-response", "least-request", "src-ip-hash", "src-ip-only-hash", "weighted-rr", "round-robin", "round-robin-strict"], "not-list": ["lc-method", "stateless-lb-method"], "type": "string"}
    :param stateless_auto_switch: {"default": 0, "optional": true, "type": "number", "description": "Enable auto stateless method", "format": "flag"}
    :param min_active_member_action: {"optional": true, "enum": ["dynamic-priority", "skip-pri-set"], "type": "string", "description": "'dynamic-priority': dynamic change member priority to met the min-active-member requirement; 'skip-pri-set': Skip Current Priority Set If Min not met; ", "format": "enum"}
    :param l4_session_usage: {"description": "Dynamically enable stateless method by session usage (Usage to trigger stateless method)", "format": "number", "type": "number", "maximum": 100, "minimum": 1, "optional": true}
    :param extended_stats: {"default": 0, "optional": true, "type": "number", "description": "Enable extended statistics on service group", "format": "flag"}
    :param conn_rate_revert_duration: {"description": "Period that revert condition consistently happens(seconds)", "format": "number", "type": "number", "maximum": 600, "minimum": 1, "optional": true}
    :param conn_rate_log: {"default": 0, "optional": true, "type": "number", "description": "Send log if transition happens", "format": "flag"}
    :param traffic_replication_mirror_sa_repl: {"default": 0, "optional": true, "type": "number", "description": "Replace Source MAC", "format": "flag"}
    :param report_delay: {"description": "Reporting frequency (in minutes)", "format": "number", "type": "number", "maximum": 7200, "minimum": 1, "optional": true}
    :param name: {"description": "SLB Service Name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}
    :param l4_session_usage_log: {"default": 0, "optional": true, "type": "number", "description": "Send log if transition happens", "format": "flag"}
    :param conn_rate_duration: {"description": "Period that trigger condition consistently happens(seconds)", "format": "number", "type": "number", "maximum": 600, "minimum": 1, "optional": true}
    :param l4_session_usage_grace_period: {"description": "Define the grace period during transition (Define the grace period during transition(seconds))", "format": "number", "type": "number", "maximum": 600, "minimum": 1, "optional": true}
    :param template_policy: {"description": "Policy template (Policy template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/slb/template/policy"}
    :param stateless_lb_method2: {"optional": true, "enum": ["stateless-dst-ip-hash", "stateless-per-pkt-round-robin", "stateless-src-dst-ip-hash", "stateless-src-ip-hash", "stateless-src-ip-only-hash"], "type": "string", "description": "'stateless-dst-ip-hash': Stateless load-balancing based on Dst IP and Dst port hash; 'stateless-per-pkt-round-robin': Stateless load-balancing using per-packet round-robin; 'stateless-src-dst-ip-hash': Stateless load-balancing based on IP and port hash for both Src and Dst; 'stateless-src-ip-hash': Stateless load-balancing based on Src IP and Src port hash; 'stateless-src-ip-only-hash': Stateless load-balancing based on only Src IP hash; ", "format": "enum"}
    :param priorities: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"priority": {"description": "Priority option. Define different action for each priority node. (Priority in the Group)", "minimum": 1, "type": "number", "maximum": 16, "format": "number"}, "priority-action": {"default": "proceed", "enum": ["drop", "drop-if-exceed-limit", "proceed", "reset", "reset-if-exceed-limit"], "type": "string", "description": "'drop': Drop request when all priority nodes fail; 'drop-if-exceed-limit': Drop request when connection over limit; 'proceed': Proceed to next priority when all priority nodes fail(default); 'reset': Send client reset when all priority nodes fail; 'reset-if-exceed-limit': Send client reset when connection over limit; ", "format": "enum"}, "optional": true}}]}
    :param sample_rsp_time: {"default": 0, "optional": true, "type": "number", "description": "sample server response time", "format": "flag"}
    :param top_fastest: {"default": 0, "optional": true, "type": "number", "description": "Report top 10 fastest servers", "format": "flag"}
    :param conn_revert_rate: {"description": "Rate to revert to statelful method (conn/sec)", "format": "number", "type": "number", "maximum": 1000000, "minimum": 1, "optional": true}
    :param priority_affinity: {"default": 0, "optional": true, "type": "number", "description": "Priority affinity. Persist to the same priority if possible.", "format": "flag"}
    :param top_slowest: {"default": 0, "optional": true, "type": "number", "description": "Report top 10 slowest servers", "format": "flag"}
    :param health_check: {"description": "Health Check (Monitor Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "not": "health-check-disable", "type": "string", "$ref": "/axapi/v3/health/monitor"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/service-group/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "service-group"
        self.a10_url="/axapi/v3/slb/service-group/{name}"
        self.DeviceProxy = ""
        self.conn_rate = ""
        self.reset_on_server_selection_fail = ""
        self.health_check_disable = ""
        self.protocol = ""
        self.traffic_replication_mirror = ""
        self.traffic_replication_mirror_ip_repl = ""
        self.reset_priority_affinity = ""
        self.min_active_member = ""
        self.member_list = []
        self.stats_data_action = ""
        self.traffic_replication_mirror_da_repl = ""
        self.rpt_ext_server = ""
        self.template_port = ""
        self.conn_rate_grace_period = ""
        self.l4_session_usage_duration = ""
        self.backup_server_event_log = ""
        self.lc_method = ""
        self.pseudo_round_robin = ""
        self.l4_session_usage_revert_rate = ""
        self.template_server = ""
        self.stateless_lb_method = ""
        self.l4_session_revert_duration = ""
        self.traffic_replication_mirror_sa_da_repl = ""
        self.lb_method = ""
        self.stateless_auto_switch = ""
        self.min_active_member_action = ""
        self.l4_session_usage = ""
        self.extended_stats = ""
        self.conn_rate_revert_duration = ""
        self.conn_rate_log = ""
        self.reset = {}
        self.traffic_replication_mirror_sa_repl = ""
        self.report_delay = ""
        self.name = ""
        self.l4_session_usage_log = ""
        self.conn_rate_duration = ""
        self.l4_session_usage_grace_period = ""
        self.template_policy = ""
        self.stateless_lb_method2 = ""
        self.priorities = []
        self.sample_rsp_time = ""
        self.top_fastest = ""
        self.conn_revert_rate = ""
        self.priority_affinity = ""
        self.top_slowest = ""
        self.health_check = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


