from a10sdk.common.A10BaseClass import A10BaseClass


class Techreport(A10BaseClass):
    
    """Class Description::
    Configure show tech.

    Class techreport supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param priority_partition_list: {"minItems": 1, "items": {"type": "priority-partition"}, "uniqueItems": true, "array": [{"required": ["part-name"], "properties": {"part-name": {"description": "Name of partition always want to show in showtech (shared is always shown by default)", "format": "string", "minLength": 1, "optional": false, "maxLength": 14, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/techreport/priority-partition/{part-name}"}
    :param disable: {"default": 0, "optional": true, "type": "number", "description": "Disable the polling techreport", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/techreport`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "techreport"
        self.a10_url="/axapi/v3/techreport"
        self.DeviceProxy = ""
        self.priority_partition_list = []
        self.disable = ""
        self.uuid = ""
        self.interval = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


