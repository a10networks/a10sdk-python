from a10sdk.common.A10BaseClass import A10BaseClass


class WebCategoryLicense(A10BaseClass):
    
    """    :param action: {"optional": true, "enum": ["import"], "type": "string", "description": "'import': import; ", "format": "enum"}
    :param file_handle: {"description": "Full path of the uploaded file", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param file: {"description": "Web-Category license local file name", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param size: {"description": "License file size in byte", "format": "number", "type": "number", "maximum": 2147483647, "minimum": 0, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    License file to enable web-category feature activation.

    Class web-category-license supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/file/web-category-license`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "web-category-license"
        self.a10_url="/axapi/v3/file/web-category-license"
        self.DeviceProxy = ""
        self.action = ""
        self.file_handle = ""
        self.A10WW_file = ""
        self.size = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


