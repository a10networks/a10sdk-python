from a10sdk.common.A10BaseClass import A10BaseClass


class SourceIp(A10BaseClass):
    
    """Class Description::
    Source IP persistence.

    Class source-ip supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param scan_all_members: {"default": 0, "optional": true, "type": "number", "description": "Persist with SCAN of all members", "format": "flag"}
    :param netmask6: {"description": "IPV6 subnet mask", "format": "number", "default": 128, "optional": true, "maximum": 128, "minimum": 1, "type": "number"}
    :param incl_dst_ip: {"default": 0, "optional": true, "type": "number", "description": "Include destination IP on the persist", "format": "flag"}
    :param name: {"description": "Source IP persistence template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param dont_honor_conn_rules: {"default": 0, "optional": true, "type": "number", "description": "Do not observe connection rate rules", "format": "flag"}
    :param service_group: {"description": "Persist within the same service group", "format": "flag", "default": 0, "optional": true, "not": "server", "type": "number"}
    :param server: {"description": "Persist to the same server, default is port", "format": "flag", "default": 0, "optional": true, "not": "service-group", "type": "number"}
    :param incl_sport: {"default": 0, "optional": true, "type": "number", "description": "Include source port on the persist", "format": "flag"}
    :param netmask: {"default": "255.255.255.255", "optional": true, "type": "string", "description": "IP subnet mask", "format": "ipv4-netmask"}
    :param timeout: {"description": "Persistence timeout (in minutes)", "format": "number", "default": 5, "optional": true, "maximum": 2000, "minimum": 1, "type": "number"}
    :param hash_persist: {"default": 0, "optional": true, "type": "number", "description": "Use hash value of source IP address", "format": "flag"}
    :param enforce_higher_priority: {"default": 0, "optional": true, "type": "number", "description": "Enforce to use high priority node if available", "format": "flag"}
    :param match_type: {"default": 0, "optional": true, "type": "number", "description": "Persistence type", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/persist/source-ip/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "source-ip"
        self.a10_url="/axapi/v3/slb/template/persist/source-ip/{name}"
        self.DeviceProxy = ""
        self.scan_all_members = ""
        self.netmask6 = ""
        self.incl_dst_ip = ""
        self.name = ""
        self.dont_honor_conn_rules = ""
        self.service_group = ""
        self.server = ""
        self.incl_sport = ""
        self.netmask = ""
        self.timeout = ""
        self.hash_persist = ""
        self.enforce_higher_priority = ""
        self.match_type = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


