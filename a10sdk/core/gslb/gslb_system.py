from a10sdk.common.A10BaseClass import A10BaseClass


class GslbLoadFileList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param geo_location_load_filename: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify file to be loaded", "format": "string-rlx"}
    :param template_name: {"description": "CSV template to load this file", "format": "string", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/gslb/template/csv"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "gslb-load-file-list"
        self.DeviceProxy = ""
        self.geo_location_load_filename = ""
        self.template_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class System(A10BaseClass):
    
    """Class Description::
    GSLB system options.

    Class system supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param gslb_service_ip: {"default": 0, "optional": true, "type": "number", "description": "GSLB Service-IP", "format": "flag"}
    :param gslb_site: {"default": 0, "optional": true, "type": "number", "description": "GSLB Site", "format": "flag"}
    :param ip_ttl: {"description": "TTL of IP packets, default is 0 (IP TTL value, default is 0)", "format": "number", "default": 0, "optional": true, "maximum": 255, "minimum": 0, "type": "number"}
    :param gslb_group: {"default": 0, "optional": true, "type": "number", "description": "GSLB Group", "format": "flag"}
    :param slb_device: {"default": 0, "optional": true, "type": "number", "description": "SLB Device", "format": "flag"}
    :param hostname: {"default": 0, "optional": true, "type": "number", "description": "System's Network Name", "format": "flag"}
    :param module: {"default": 0, "optional": true, "type": "number", "description": "Specify Auto Map Module", "format": "flag"}
    :param age_interval: {"description": "Interval to age runtime statistics. 0: never age, default is 10 (Time, unit: sec, default is 10)", "format": "number", "default": 10, "optional": true, "maximum": 120, "minimum": 0, "type": "number"}
    :param geo_location_iana: {"default": 1, "optional": true, "type": "number", "description": "Load built-in IANA table", "format": "flag"}
    :param ttl: {"description": "Specify Auto Map TTL (TTL, default is 300)", "format": "number", "default": 300, "optional": true, "maximum": 65535, "minimum": 1, "type": "number"}
    :param slb_server: {"default": 0, "optional": true, "type": "number", "description": "SLB Server", "format": "flag"}
    :param slb_virtual_server: {"default": 0, "optional": true, "type": "number", "description": "SLB Virtual Server", "format": "flag"}
    :param gslb_load_file_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "geo-location-load-filename": {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify file to be loaded", "format": "string-rlx"}, "template-name": {"description": "CSV template to load this file", "format": "string", "minLength": 1, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/gslb/template/csv"}}}]}
    :param wait: {"description": "Disable GSLB until timeout if system is not ready (Time, unit: sec, default is 0)", "format": "number", "default": 0, "optional": true, "maximum": 16384, "minimum": 0, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/system`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "system"
        self.a10_url="/axapi/v3/gslb/system"
        self.DeviceProxy = ""
        self.gslb_service_ip = ""
        self.gslb_site = ""
        self.ip_ttl = ""
        self.gslb_group = ""
        self.slb_device = ""
        self.hostname = ""
        self.module = ""
        self.age_interval = ""
        self.geo_location_iana = ""
        self.ttl = ""
        self.slb_server = ""
        self.slb_virtual_server = ""
        self.gslb_load_file_list = []
        self.wait = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


