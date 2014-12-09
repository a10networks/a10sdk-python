from a10sdk.common.A10BaseClass import A10BaseClass


class IpLists(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param listname: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param hits: {"type": "number", "format": "number"}
    :param errors: {"type": "number", "format": "number"}
    :param last: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param total_entries_in_list: {"type": "number", "format": "number"}
    :param ipaddr: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param filename: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param file_lines: {"type": "number", "format": "number"}
    :param ipaddr_filter: {"type": "number", "format": "number"}
    :param ipmask: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param type: {"enum": ["manual", "file"], "type": "string", "format": "enum"}
    :param group_id: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "ip-lists"
        self.DeviceProxy = ""
        self.listname = ""
        self.hits = ""
        self.errors = ""
        self.last = ""
        self.total_entries_in_list = ""
        self.ipaddr = ""
        self.filename = ""
        self.file_lines = ""
        self.ipaddr_filter = ""
        self.ipmask = ""
        self.A10WW_type = ""
        self.group_id = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param ip_lists: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"listname": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "hits": {"type": "number", "format": "number"}, "errors": {"type": "number", "format": "number"}, "last": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "total-entries-in-list": {"type": "number", "format": "number"}, "optional": true, "ipaddr": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "filename": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "file-lines": {"type": "number", "format": "number"}, "ipaddr-filter": {"type": "number", "format": "number"}, "ipmask": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "type": {"enum": ["manual", "file"], "type": "string", "format": "enum"}, "group-id": {"type": "number", "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.ip_lists = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class IpListInfo(A10BaseClass):
    
    """Class Description::
    Operational Status for the object ip-list-info.

    Class ip-list-info supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/ip-list-info/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "ip-list-info"
        self.a10_url="/axapi/v3/gslb/ip-list-info/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


