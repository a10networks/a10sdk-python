from a10sdk.common.A10BaseClass import A10BaseClass


class OverlayMgmtInfo(A10BaseClass):
    
    """Class Description::
    Overlay management specific data.

    Class overlay-mgmt-info supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param appstring: {"description": "Application string", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param plugin_name: {"description": "Plugin string", "format": "string", "minLength": 1, "optional": false, "maxLength": 128, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/overlay-mgmt-info/{plugin_name}+{appstring}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "plugin_name","appstring"]

        self.b_key = "overlay-mgmt-info"
        self.a10_url="/axapi/v3/overlay-mgmt-info/{plugin_name}+{appstring}"
        self.DeviceProxy = ""
        self.appstring = ""
        self.uuid = ""
        self.plugin_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


