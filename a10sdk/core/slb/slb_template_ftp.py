from a10sdk.common.A10BaseClass import A10BaseClass


class Ftp(A10BaseClass):
    
    """Class Description::
    FTP template.

    Class ftp supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param to: {"description": "End range of FTP Active mode port", "format": "number", "type": "number", "maximum": 65534, "minimum": 1, "optional": true}
    :param active_mode_port: {"default": 0, "optional": true, "type": "number", "description": "Non-Standard FTP Active mode port", "format": "flag"}
    :param active_mode_port_val: {"description": "Non-Standard FTP Active mode port", "format": "number", "optional": true, "maximum": 65534, "minimum": 1, "not": "any", "type": "number"}
    :param any: {"description": "Allow any FTP Active mode port", "format": "flag", "default": 0, "optional": true, "not": "active-mode-port-val", "type": "number"}
    :param name: {"description": "FTP template name", "format": "string-rlx", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/ftp/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "ftp"
        self.a10_url="/axapi/v3/slb/template/ftp/{name}"
        self.DeviceProxy = ""
        self.uuid = ""
        self.to = ""
        self.active_mode_port = ""
        self.active_mode_port_val = ""
        self.A10WW_any = ""
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


