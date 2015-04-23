from a10sdk.common.A10BaseClass import A10BaseClass


class DeviceIdList(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param device_id_start: {"type": "number", "format": "number"}
    :param device_id_end: {"type": "number", "format": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "device-id-list"
        self.DeviceProxy = ""
        self.device_id_start = ""
        self.device_id_end = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class DeviceGroup(A10BaseClass):
    
    """Class Description::
    configure scaleout device groups.

    Class device-group supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param device_group: {"description": "scaletout device group", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": false}
    :param device_id_list: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"device-id-start": {"type": "number", "format": "number"}, "device-id-end": {"type": "number", "format": "number"}, "optional": true}}]}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/scaleout/{cluster_id}/device-groups/device-group/{device_group}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "device_group"]

        self.b_key = "device-group"
        self.a10_url="/axapi/v3/scaleout/{cluster_id}/device-groups/device-group/{device_group}"
        self.DeviceProxy = ""
        self.device_group = ""
        self.device_id_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


