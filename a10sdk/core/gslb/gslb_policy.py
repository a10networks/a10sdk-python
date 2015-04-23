from a10sdk.common.A10BaseClass import A10BaseClass


class Policy(A10BaseClass):
    
    """Class Description::
    Policy for GSLB zone, service or geo-location.

    Class policy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param weighted_ip_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable Select Service-IP by weighted preference", "format": "flag"}
    :param alias_admin_preference: {"default": 0, "optional": true, "type": "number", "description": "Select alias name having maximum admin preference", "format": "flag"}
    :param admin_ip_top_only: {"description": "Return highest priority server only", "format": "flag", "default": 0, "optional": true, "not": "ordered-ip-top-only", "type": "number"}
    :param least_response: {"default": 0, "optional": true, "type": "number", "description": "Least response selection", "format": "flag"}
    :param bw_cost_fail_break: {"default": 0, "optional": true, "type": "number", "description": "Break when exceed limit", "format": "flag"}
    :param metric_fail_break: {"default": 0, "optional": true, "type": "number", "description": "Break if no valid Service-IP", "format": "flag"}
    :param weighted_ip: {"default": 0, "optional": true, "type": "number", "description": "Select Service-IP by weighted preference", "format": "flag"}
    :param round_robin: {"default": 1, "optional": true, "type": "number", "description": "Round robin selection, enabled by default", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param metric_type: {"optional": true, "enum": ["health-check", "weighted-ip", "weighted-site", "capacity", "active-servers", "active-rdt", "geographic", "connection-load", "num-session", "admin-preference", "bw-cost", "least-response", "admin-ip"], "type": "string", "format": "enum-list"}
    :param num_session_tolerance: {"description": "The difference between the available sessions, default is 10 (Tolerance)", "format": "number", "default": 10, "optional": true, "maximum": 100, "minimum": 0, "type": "number"}
    :param metric_order: {"default": 0, "optional": true, "type": "number", "description": "Specify order of metric", "format": "flag"}
    :param weighted_ip_total_hits: {"default": 0, "optional": true, "type": "number", "description": "Weighted by total hits", "format": "flag"}
    :param weighted_site_total_hits: {"default": 0, "optional": true, "type": "number", "description": "Weighted by total hits", "format": "flag"}
    :param ordered_ip_top_only: {"description": "Return highest priority server only", "format": "flag", "default": 0, "optional": true, "not": "admin-ip-top-only", "type": "number"}
    :param weighted_site_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable Select Service-IP by weighted site preference", "format": "flag"}
    :param bw_cost: {"default": 0, "optional": true, "type": "number", "description": "Select site with minimum bandwidth cost", "format": "flag"}
    :param metric_force_check: {"default": 0, "optional": true, "type": "number", "description": "Always check Service-IP for all enabled metrics", "format": "flag"}
    :param admin_ip_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable admin ip", "format": "flag"}
    :param geo_location_list: {"minItems": 1, "items": {"type": "geo-location"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"ip-multiple-fields": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ip-addr2-sub": {"type": "string", "description": "Specify IP address range", "format": "ipv4-address"}, "optional": true, "ip-sub": {"type": "string", "description": "Specify IP information", "format": "ipv4-address"}, "ip-mask-sub": {"type": "string", "description": "Specify IP/mask format (Specify IP address mask)", "format": "ipv4-netmask-brief"}}}]}, "name": {"description": "Specify geo-location name, section range is (1-15)", "format": "string", "minLength": 1, "optional": false, "maxLength": 127, "type": "string"}, "ipv6-multiple-fields": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"ipv6-mask-sub": {"description": "Specify IPv6/mask format (Specify IP address mask)", "minimum": 0, "type": "number", "maximum": 128, "format": "number"}, "ipv6-sub": {"type": "string", "description": "Specify IPv6 information", "format": "ipv6-address"}, "optional": true, "ipv6-addr2-sub": {"type": "string", "description": "Specify IPv6 address range", "format": "ipv6-address"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/policy/{name}/geo-location/{name}"}
    :param weighted_alias: {"default": 0, "optional": true, "type": "number", "description": "Select alias name by weighted preference", "format": "flag"}
    :param bw_cost_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable bw cost", "format": "flag"}
    :param num_session_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable Select Service-IP for device having maximum number of available sessions", "format": "flag"}
    :param name: {"description": "Specify policy name", "format": "string", "default": "default", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param active_servers_enable: {"default": 0, "optional": true, "type": "number", "description": "Enable Select Service-IP with the highest number of active servers", "format": "flag"}
    :param active_servers_fail_break: {"default": 0, "optional": true, "type": "number", "description": "Break when no active server", "format": "flag"}
    :param ip_list: {"description": "Specify IP List (IP List Name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/gslb/ip-list"}
    :param admin_preference: {"default": 0, "optional": true, "type": "number", "description": "Select Service-IP for the device having maximum admin preference", "format": "flag"}
    :param weighted_site: {"default": 0, "optional": true, "type": "number", "description": "Select Service-IP by weighted site preference", "format": "flag"}
    :param geographic: {"default": 1, "optional": true, "type": "number", "description": "Select Service-IP by geographic", "format": "flag"}
    :param health_check: {"default": 1, "optional": true, "type": "number", "description": "Select Service-IP by health status", "format": "flag"}
    :param active_servers: {"default": 0, "optional": true, "type": "number", "description": "Select Service-IP with the highest number of active servers", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/policy/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "policy"
        self.a10_url="/axapi/v3/gslb/policy/{name}"
        self.DeviceProxy = ""
        self.weighted_ip_enable = ""
        self.alias_admin_preference = ""
        self.admin_ip_top_only = ""
        self.least_response = ""
        self.auto_map = {}
        self.bw_cost_fail_break = ""
        self.metric_fail_break = ""
        self.edns = {}
        self.weighted_ip = ""
        self.active_rdt = {}
        self.round_robin = ""
        self.capacity = {}
        self.uuid = ""
        self.metric_type = ""
        self.num_session_tolerance = ""
        self.geo_location_match = {}
        self.metric_order = ""
        self.dns = {}
        self.weighted_ip_total_hits = ""
        self.weighted_site_total_hits = ""
        self.ordered_ip_top_only = ""
        self.weighted_site_enable = ""
        self.bw_cost = ""
        self.metric_force_check = ""
        self.admin_ip_enable = ""
        self.geo_location_list = []
        self.weighted_alias = ""
        self.bw_cost_enable = ""
        self.num_session_enable = ""
        self.name = ""
        self.active_servers_enable = ""
        self.active_servers_fail_break = ""
        self.connection_load = {}
        self.ip_list = ""
        self.admin_preference = ""
        self.weighted_site = ""
        self.geographic = ""
        self.health_check = ""
        self.active_servers = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


