from a10sdk.common.A10BaseClass import A10BaseClass


class Partition(A10BaseClass):
    
    """Class Description::
    module partition.

    Class partition supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param vnp_events: {"optional": false, "enum": ["part-create", "part-del"], "type": "string", "description": "'part-create': Create new partition; 'part-del': Delete a partition; ", "format": "enum"}
    :param logging: {"optional": true, "enum": ["on", "off"], "type": "string", "description": "'on': enable this action; 'off': disable this action; ", "format": "enum"}
    :param email: {"optional": true, "enum": ["on", "off"], "type": "string", "description": "'on': enable this action; 'off': disable this action; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/event/partition/{vnp_events}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "vnp_events"]

        self.b_key = "partition"
        self.a10_url="/axapi/v3/event/partition/{vnp_events}"
        self.DeviceProxy = ""
        self.vnp_events = ""
        self.logging = ""
        self.email = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


