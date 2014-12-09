from a10sdk.common.A10BaseClass import A10BaseClass


class FileList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param parent: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param file: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "file-list"
        self.DeviceProxy = ""
        self.parent = ""
        self.A10WW_file = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param file_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "parent": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}, "file": {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.file_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnssecDnskey(A10BaseClass):
    
    """Class Description::
    Operational Status for the object dnssec-dnskey.

    Class dnssec-dnskey supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/file/dnssec-dnskey/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dnssec-dnskey"
        self.a10_url="/axapi/v3/file/dnssec-dnskey/oper"
        self.DeviceProxy = ""
        self.oper = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


