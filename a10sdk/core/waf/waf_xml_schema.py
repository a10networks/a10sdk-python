from a10sdk.common.A10BaseClass import A10BaseClass


class XmlSchema(A10BaseClass):
    
    """Class Description::
    Manage XML-Schema files.

    Class xml-schema supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param max_filesize: {"description": "Set maximum XML-Schema file size (Maximum file size in KBytes, default is 32K)", "partition-visibility": "shared", "default": 32, "optional": true, "format": "number", "maximum": 256, "minimum": 16, "type": "number"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/waf/xml-schema`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "xml-schema"
        self.a10_url="/axapi/v3/waf/xml-schema"
        self.DeviceProxy = ""
        self.max_filesize = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


