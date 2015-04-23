from a10sdk.common.A10BaseClass import A10BaseClass


class ServiceConfig(A10BaseClass):
    
    """Class Description::
    Configure scaleout templates for SLB, CGN and VRRP.

    Class service-config supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param template_list: {"minItems": 1, "items": {"type": "template"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"device-group": {"description": "Device group id", "format": "number", "type": "number", "maximum": 16, "minimum": 1, "optional": true}, "bucket-count": {"description": "Number of traffic buckets", "format": "number", "default": 256, "optional": true, "maximum": 256, "minimum": 1, "type": "number"}, "name": {"description": "Scaleout template Name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}, "uuid": {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/scaleout/{cluster-id}/service-config/template/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/scaleout/{cluster_id}/service-config`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "service-config"
        self.a10_url="/axapi/v3/scaleout/{cluster_id}/service-config"
        self.DeviceProxy = ""
        self.uuid = ""
        self.template_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


