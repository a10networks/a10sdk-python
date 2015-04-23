from a10sdk.common.A10BaseClass import A10BaseClass


class MetricList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param type: {"type": "string", "format": "string"}
    :param order: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "metric-list"
        self.DeviceProxy = ""
        self.A10WW_type = ""
        self.order = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Oper(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param metric_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "type": {"type": "string", "format": "string"}, "order": {"type": "number", "format": "number"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "oper"
        self.DeviceProxy = ""
        self.metric_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Policy(A10BaseClass):
    
    """Class Description::
    Operational Status for the object policy.

    Class policy supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify policy name", "format": "string", "default": "default", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/gslb/policy/{name}/oper`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "policy"
        self.a10_url="/axapi/v3/gslb/policy/{name}/oper"
        self.DeviceProxy = ""
        self.oper = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


