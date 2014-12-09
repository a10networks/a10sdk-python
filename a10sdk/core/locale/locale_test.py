from a10sdk.common.A10BaseClass import A10BaseClass


class Test(A10BaseClass):
    
    """    :param locale: {"optional": true, "enum": ["zh_CN", "zh_TW", "ja_JP"], "type": "string", "description": "'zh_CN': Chinese locale for PRC; 'zh_TW': Chinese locale for Taiwan; 'ja_JP': Japanese locale for Japan; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    To test current terminal encodings for specific locale.

    Class test supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/locale/test`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "test"
        self.a10_url="/axapi/v3/locale/test"
        self.DeviceProxy = ""
        self.locale = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


