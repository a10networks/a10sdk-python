from a10sdk.common.A10BaseClass import A10BaseClass


class Scaleout(A10BaseClass):
    
    """Class Description::
    Configure Scaleout.

    Class scaleout supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param cluster_id: {"description": "Scaleout cluster-id", "format": "number", "type": "number", "maximum": 64, "minimum": 1, "optional": false}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param follow_vcs: {"default": 0, "optional": true, "type": "number", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/scaleout/{cluster_id}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "cluster_id"]

        self.b_key = "scaleout"
        self.a10_url="/axapi/v3/scaleout/{cluster_id}"
        self.DeviceProxy = ""
        self.local_device = {}
        self.cluster_id = ""
        self.uuid = ""
        self.cluster_devices = {}
        self.follow_vcs = ""
        self.device_groups = {}
        self.service_config = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


