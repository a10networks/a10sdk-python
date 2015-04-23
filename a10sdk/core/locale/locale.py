from a10sdk.common.A10BaseClass import A10BaseClass


class Locale(A10BaseClass):
    
    """Class Description::
    Set locale for the CLI startup.

    Class locale supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param value: {"description": "'en_US.UTF-8': English locale for the USA, encoding with UTF-8 (default); 'zh_CN.UTF-8': Chinese locale for PRC, encoding with UTF-8; 'zh_CN.GB18030': Chinese locale for PRC, encoding with GB18030; 'zh_CN.GBK': Chinese locale for PRC, encoding with GBK; 'zh_CN.GB2312': Chinese locale for PRC, encoding with GB2312; 'zh_TW.UTF-8': Chinese locale for Taiwan, encoding with UTF-8; 'zh_TW.BIG5': Chinese locale for Taiwan, encoding with BIG5; 'zh_TW.EUCTW': Chinese locale for Taiwan, encoding with EUC-TW; 'ja_JP.UTF-8': Japanese locale for Japan, encoding with UTF-8; 'ja_JP.EUC-JP': Japanese locale for Japan, encoding with EUC-JP; ", "format": "enum", "default": "en_US.UTF-8", "type": "string", "enum": ["en_US.UTF-8", "zh_CN.UTF-8", "zh_CN.GB18030", "zh_CN.GBK", "zh_CN.GB2312", "zh_TW.UTF-8", "zh_TW.BIG5", "zh_TW.EUCTW", "ja_JP.UTF-8", "ja_JP.EUC-JP"], "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/locale`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "locale"
        self.a10_url="/axapi/v3/locale"
        self.DeviceProxy = ""
        self.test = {}
        self.uuid = ""
        self.value = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


