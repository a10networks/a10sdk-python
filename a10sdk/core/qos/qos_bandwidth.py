from a10sdk.common.A10BaseClass import A10BaseClass


class Bandwidth(A10BaseClass):
    
    """Class Description::
    QoS bandwidth setting.

    Class bandwidth supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param enable: {"default": 0, "optional": true, "type": "number", "description": "enable bandwidth/shape control", "format": "flag"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/qos/bandwidth`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "bandwidth"
        self.a10_url="/axapi/v3/qos/bandwidth"
        self.DeviceProxy = ""
        self.enable = ""
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


