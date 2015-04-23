from a10sdk.common.A10BaseClass import A10BaseClass


class LocalDevice(A10BaseClass):
    
    """Class Description::
    Local device configuration.

    Class local-device supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param priority: {"optional": true, "minimum": 1, "type": "number", "maximum": 255, "format": "number"}
    :param id: {"format": "number", "type": "number", "maximum": 8, "minimum": 1, "modify-not-allowed": 1, "optional": true}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/scaleout/{cluster_id}/local-device`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "local-device"
        self.a10_url="/axapi/v3/scaleout/{cluster_id}/local-device"
        self.DeviceProxy = ""
        self.priority = ""
        self.A10WW_id = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


