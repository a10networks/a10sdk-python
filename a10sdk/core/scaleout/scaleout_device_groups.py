from a10sdk.common.A10BaseClass import A10BaseClass


class DeviceGroups(A10BaseClass):
    
    """Class Description::
    configure scaleout device groups.

    Class device-groups supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param device_group_list: {"minItems": 1, "items": {"type": "device-group"}, "uniqueItems": true, "array": [{"required": ["device-group"], "properties": {"device-group": {"description": "scaletout device group", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": false}, "device-id-list": {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"device-id-start": {"type": "number", "format": "number"}, "device-id-end": {"type": "number", "format": "number"}, "optional": true}}]}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/scaleout/{cluster-id}/device-groups/device-group/{device-group}"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/scaleout/{cluster_id}/device-groups`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "device-groups"
        self.a10_url="/axapi/v3/scaleout/{cluster_id}/device-groups"
        self.DeviceProxy = ""
        self.device_group_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


