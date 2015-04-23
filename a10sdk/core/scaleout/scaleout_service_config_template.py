from a10sdk.common.A10BaseClass import A10BaseClass


class Template(A10BaseClass):
    
    """Class Description::
    Scaleout template.

    Class template supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param device_group: {"description": "Device group id", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": true}
    :param bucket_count: {"description": "Number of traffic buckets", "format": "number", "default": 256, "optional": true, "maximum": 256, "minimum": 1, "type": "number"}
    :param name: {"description": "Scaleout template Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/scaleout/{cluster_id}/service-config/template/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "template"
        self.a10_url="/axapi/v3/scaleout/{cluster_id}/service-config/template/{name}"
        self.DeviceProxy = ""
        self.device_group = ""
        self.bucket_count = ""
        self.name = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


