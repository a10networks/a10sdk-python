from a10sdk.common.A10BaseClass import A10BaseClass


class DeviceId(A10BaseClass):
    
    """Class Description::
    configure Scaleout devices.

    Class device-id supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param action: {"description": "'enable': enable; 'disable': disable; ", "format": "enum", "default": "enable", "type": "string", "enum": ["enable", "disable"], "optional": true}
    :param device_id: {"description": "scaleout device id", "format": "number", "type": "number", "maximum": 8, "minimum": 1, "optional": false}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param ip: {"optional": true, "type": "string", "format": "ipv4-address"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/scaleout/{cluster_id}/cluster-devices/device-id/{device_id}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "device_id"]

        self.b_key = "device-id"
        self.a10_url="/axapi/v3/scaleout/{cluster_id}/cluster-devices/device-id/{device_id}"
        self.DeviceProxy = ""
        self.action = ""
        self.device_id = ""
        self.uuid = ""
        self.ip = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


