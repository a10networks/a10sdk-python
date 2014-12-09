from a10sdk.common.A10BaseClass import A10BaseClass


class DeviceGroups(A10BaseClass):
    
    """Class Description::
    configure scaleout device groups.

    Class device-groups supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param device_group_list: {"minItems": 1, "items": {"type": "device-group"}, "uniqueItems": true, "array": [{"required": ["device-group"], "properties": {"device-group": {"description": "scaletout device group", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": false}, "device-id-start": {"optional": true, "type": "number", "format": "number"}, "device-id-end": {"optional": true, "type": "number", "format": "number"}}}], "type": "array", "$ref": "/axapi/v3/acos-scaleout/cluster-config/device-groups/device-group/{device-group}"}
    :param enable: {"default": 0, "optional": true, "partition-visibility": "private", "type": "number", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/acos-scaleout/cluster-config/device-groups`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "device-groups"
        self.a10_url="/axapi/v3/acos-scaleout/cluster-config/device-groups"
        self.DeviceProxy = ""
        self.device_group_list = []
        self.enable = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


