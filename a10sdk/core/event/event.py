from a10sdk.common.A10BaseClass import A10BaseClass


class Event(A10BaseClass):
    
    """Class Description::
    configure event actions.

    Class event supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param partition_list: {"minItems": 1, "items": {"type": "partition"}, "uniqueItems": true, "array": [{"required": ["vnp-events"], "properties": {"vnp-events": {"optional": false, "enum": ["part-create", "part-del"], "type": "string", "description": "'part-create': Create new partition; 'part-del': Delete a partition; ", "format": "enum"}, "logging": {"optional": true, "enum": ["on", "off"], "type": "string", "description": "'on': enable this action; 'off': disable this action; ", "format": "enum"}, "email": {"optional": true, "enum": ["on", "off"], "type": "string", "description": "'on': enable this action; 'off': disable this action; ", "format": "enum"}}}], "type": "array", "$ref": "/axapi/v3/event/partition/{vnp-events}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/event`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "event"
        self.a10_url="/axapi/v3/event"
        self.DeviceProxy = ""
        self.partition_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


