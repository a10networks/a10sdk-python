from a10sdk.common.A10BaseClass import A10BaseClass


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param last_server: {"minLength": 1, "maxLength": 63, "type": "string", "format": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.last_server = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DnsMxRecord(A10BaseClass):
    
    """Class Description::
    Operational Status for the object dns-mx-record.

    Class dns-mx-record supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param mx_name: {"description": "Specify Domain Name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/zone/{name}/dns-mx-record/{mx_name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "dns-mx-record"
        self.a10_url="/axapi/v3/gslb/zone/{name}/dns-mx-record/{mx_name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.mx_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


