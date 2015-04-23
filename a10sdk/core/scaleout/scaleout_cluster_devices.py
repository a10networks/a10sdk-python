from a10sdk.common.A10BaseClass import A10BaseClass


class ClusterDevices(A10BaseClass):
    
    """Class Description::
    Configure devices in the cluster.

    Class cluster-devices supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param device_id_list: {"minItems": 1, "items": {"type": "device-id"}, "uniqueItems": true, "array": [{"required": ["device-id"], "properties": {"action": {"description": "'enable': enable; 'disable': disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}, "device-id": {"description": "scaleout device id", "format": "number", "type": "number", "maximum": 8, "minimum": 1, "optional": false}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}, "ip": {"optional": true, "type": "string", "format": "ipv4-address"}}}], "type": "array", "$ref": "/axapi/v3/scaleout/{cluster-id}/cluster-devices/device-id/{device-id}"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/scaleout/{cluster_id}/cluster-devices`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "cluster-devices"
        self.a10_url="/axapi/v3/scaleout/{cluster_id}/cluster-devices"
        self.DeviceProxy = ""
        self.device_id_list = []
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


