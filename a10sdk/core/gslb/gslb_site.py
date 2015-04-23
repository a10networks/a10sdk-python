from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "hits"], "type": "string", "description": "'all': all; 'hits': Number of times the site was selected; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class MultipleGeoLocations(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param geo_location: {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify the geographic location of the GSLB site (Specify geo-location for this site)", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "multiple-geo-locations"
        self.DeviceProxy = ""
        self.geo_location = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Site(A10BaseClass):
    
    """Class Description::
    Specify a GSLB site.

    Class site supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param ip_server_list: {"minItems": 1, "items": {"type": "ip-server"}, "uniqueItems": true, "array": [{"required": ["ip-server-name"], "properties": {"ip-server-name": {"description": "Specify the real server name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/gslb/service-ip"}, "sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hits"], "type": "string", "description": "'all': all; 'hits': Number of times the IP was selected; ", "format": "enum"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/ip-server/{ip-server-name}"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param weight: {"description": "Specify a weight for the GSLB site (Weight, default is 1)", "format": "number", "default": 1, "optional": true, "maximum": 100, "minimum": 1, "type": "number"}
    :param site_name: {"description": "Specify GSLB site name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param slb_dev_list: {"minItems": 1, "items": {"type": "slb-dev"}, "uniqueItems": true, "array": [{"required": ["device-name"], "properties": {"client-ip": {"optional": true, "type": "string", "description": "Specify client IP address", "format": "ipv4-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "vip-server": {"type": "object", "properties": {"vip-server-v4-list": {"minItems": 1, "items": {"type": "vip-server-v4"}, "uniqueItems": true, "array": [{"required": ["ipv4"], "properties": {"sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "dev_vip_hits"], "type": "string", "description": "'all': all; 'dev_vip_hits': Number of times the service-ip was selected; ", "format": "enum"}}}]}, "ipv4": {"optional": false, "type": "string", "description": "Specify IP address", "format": "ipv4-address"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}/vip-server/vip-server-v4/{ipv4}"}, "vip-server-v6-list": {"minItems": 1, "items": {"type": "vip-server-v6"}, "uniqueItems": true, "array": [{"required": ["ipv6"], "properties": {"sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "dev_vip_hits"], "type": "string", "description": "'all': all; 'dev_vip_hits': Number of times the service-ip was selected; ", "format": "enum"}}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ipv6": {"optional": false, "type": "string", "description": "Specify IP address (IPv6 address)", "format": "ipv6-address"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}/vip-server/vip-server-v6/{ipv6}"}, "vip-server-name-list": {"minItems": 1, "items": {"type": "vip-server-name"}, "uniqueItems": true, "array": [{"required": ["vip-name"], "properties": {"sampling-enable": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "dev_vip_hits"], "type": "string", "description": "'all': all; 'dev_vip_hits': Number of times the service-ip was selected; ", "format": "enum"}}}]}, "vip-name": {"description": "Specify a VIP name for the SLB device", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/gslb/service-ip"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}/vip-server/vip-server-name/{vip-name}"}}, "$ref": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}/vip-server"}, "device-name": {"description": "Specify SLB device name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "proto-aging-fast": {"default": 1, "optional": true, "type": "number", "description": "Fast GSLB Protocol aging", "format": "flag"}, "proto-compatible": {"default": 0, "optional": true, "type": "number", "description": "Run GSLB Protocol in compatible mode", "format": "flag"}, "auto-map": {"default": 1, "optional": true, "type": "number", "description": "Enable DNS Auto Mapping", "format": "flag"}, "proto-aging-time": {"description": "Specify GSLB Protocol aging time, default is 60", "format": "number", "default": 60, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}, "rdt-value": {"description": "Specify Round-delay-time", "format": "number", "type": "number", "maximum": 65535, "minimum": 1, "optional": true}, "admin-preference": {"description": "Specify administrative preference (Specify admin-preference value,default is 100)", "format": "number", "default": 100, "optional": true, "maximum": 255, "minimum": 0, "type": "number"}, "ip-address": {"optional": true, "type": "string", "description": "IP address", "format": "ipv4-address"}, "auto-detect": {"description": "'ip': Service IP only; 'port': Service Port only; 'ip-and-port': Both service IP and service port; 'disabled': disable auto-detect; ", "format": "enum", "default": "ip-and-port", "type": "string", "enum": ["ip", "port", "ip-and-port", "disabled"], "optional": true}, "health-check-action": {"description": "'health-check': Enable health Check; 'health-check-disable': Disable health check; ", "format": "enum", "default": "health-check", "type": "string", "enum": ["health-check", "health-check-disable"], "optional": true}, "max-client": {"description": "Specify maximum number of clients, default is 32768", "format": "number", "default": 32768, "optional": true, "maximum": 2147483647, "minimum": 1, "type": "number"}, "gateway-ip-addr": {"optional": true, "type": "string", "description": "IP address", "format": "ipv4-address"}}}], "type": "array", "$ref": "/axapi/v3/gslb/site/{site-name}/slb-dev/{device-name}"}
    :param bw_cost: {"default": 0, "optional": true, "type": "number", "description": "Specify cost of band-width", "format": "flag"}
    :param auto_map: {"default": 1, "optional": true, "type": "number", "description": "Enable DNS Auto Mapping", "format": "flag"}
    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "hits"], "type": "string", "description": "'all': all; 'hits': Number of times the site was selected; ", "format": "enum"}}}]}
    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable all servers in the GSLB site", "format": "flag"}
    :param limit: {"description": "Specify the limit for bandwidth, default is unlimited", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param template: {"description": "Specify template to collect site information (Specify template name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param threshold: {"description": "Specify the threshold for limit", "format": "number", "default": 0, "optional": true, "maximum": 100, "minimum": 0, "type": "number"}
    :param multiple_geo_locations: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"geo-location": {"minLength": 1, "maxLength": 127, "type": "string", "description": "Specify the geographic location of the GSLB site (Specify geo-location for this site)", "format": "string"}, "optional": true}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/site/{site_name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "site_name"]

        self.b_key = "site"
        self.a10_url="/axapi/v3/gslb/site/{site_name}"
        self.DeviceProxy = ""
        self.ip_server_list = []
        self.uuid = ""
        self.weight = ""
        self.site_name = ""
        self.slb_dev_list = []
        self.bw_cost = ""
        self.auto_map = ""
        self.sampling_enable = []
        self.disable = ""
        self.limit = ""
        self.template = ""
        self.threshold = ""
        self.multiple_geo_locations = []
        self.easy_rdt = {}
        self.active_rdt = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


