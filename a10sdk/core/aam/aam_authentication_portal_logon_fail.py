from a10sdk.common.A10BaseClass import A10BaseClass


class FailMsgCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param fail_font_custom: {"description": "Specify custom font", "format": "string-rlx", "minLength": 1, "maxLength": 63, "not": "fail-face", "type": "string"}
    :param fail_color: {"default": 0, "type": "number", "description": "Specify font color", "format": "flag"}
    :param fail_size: {"description": "Specify font size", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}
    :param fail_msg: {"default": 0, "type": "number", "description": "Configure logon failure message in default logon fail page", "format": "flag"}
    :param fail_text: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify logon failure message (Default: Login Failed!!)", "format": "string-rlx"}
    :param fail_color_value: {"description": "Specify 6-digit HEX color value", "format": "string", "minLength": 6, "maxLength": 6, "not": "fail-color-name", "type": "string"}
    :param fail_font: {"default": 0, "type": "number", "description": "Sepcify font", "format": "flag"}
    :param fail_color_name: {"not": "fail-color-value", "enum": ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "orange", "purple", "red", "silver", "teal", "white", "yellow"], "type": "string", "description": "'aqua': aqua; 'black': black; 'blue': blue; 'fuchsia': fuchsia; 'gray': gray; 'green': green; 'lime': lime; 'maroon': maroon; 'navy': navy; 'olive': olive; 'orange': orange; 'purple': purple; 'red': red; 'silver': silver; 'teal': teal; 'white': white; 'yellow': yellow; ", "format": "enum"}
    :param fail_face: {"not": "fail-font-custom", "enum": ["Arial", "Courier_New", "Georgia", "Times_New_Roman", "Verdana"], "type": "string", "description": "'Arial': Arial; 'Courier_New': Courier New; 'Georgia': Georgia; 'Times_New_Roman': Times New Roman; 'Verdana': Verdana; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "fail-msg-cfg"
        self.DeviceProxy = ""
        self.fail_font_custom = ""
        self.fail_color = ""
        self.fail_size = ""
        self.fail_msg = ""
        self.fail_text = ""
        self.fail_color_value = ""
        self.fail_font = ""
        self.fail_color_name = ""
        self.fail_face = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TitleCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param title: {"default": 0, "type": "number", "description": "Configure title in default logon fail page", "format": "flag"}
    :param title_color: {"default": 0, "type": "number", "description": "Specify font color", "format": "flag"}
    :param title_color_name: {"not": "title-color-value", "enum": ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "orange", "purple", "red", "silver", "teal", "white", "yellow"], "type": "string", "description": "'aqua': aqua; 'black': black; 'blue': blue; 'fuchsia': fuchsia; 'gray': gray; 'green': green; 'lime': lime; 'maroon': maroon; 'navy': navy; 'olive': olive; 'orange': orange; 'purple': purple; 'red': red; 'silver': silver; 'teal': teal; 'white': white; 'yellow': yellow; ", "format": "enum"}
    :param title_font_custom: {"description": "Specify custom font", "format": "string-rlx", "minLength": 1, "maxLength": 63, "not": "title-face", "type": "string"}
    :param title_face: {"not": "title-font-custom", "enum": ["Arial", "Courier_New", "Georgia", "Times_New_Roman", "Verdana"], "type": "string", "description": "'Arial': Arial; 'Courier_New': Courier New; 'Georgia': Georgia; 'Times_New_Roman': Times New Roman; 'Verdana': Verdana; ", "format": "enum"}
    :param title_color_value: {"description": "Specify 6-digit HEX color value", "format": "string", "minLength": 6, "maxLength": 6, "not": "title-color-name", "type": "string"}
    :param title_size: {"description": "Specify font size", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}
    :param title_text: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify title (Default: Try Too Many Times)", "format": "string-rlx"}
    :param title_font: {"default": 0, "type": "number", "description": "Sepcify font", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "title-cfg"
        self.DeviceProxy = ""
        self.title = ""
        self.title_color = ""
        self.title_color_name = ""
        self.title_font_custom = ""
        self.title_face = ""
        self.title_color_value = ""
        self.title_size = ""
        self.title_text = ""
        self.title_font = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Background(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param bgfile: {"description": "Specify background image filename", "format": "string-rlx", "minLength": 1, "maxLength": 63, "not": "bgcolor", "type": "string"}
    :param bgstyle: {"enum": ["tile", "stretch", "fit"], "type": "string", "description": "'tile': Tile; 'stretch': Stretch; 'fit': Fit; ", "format": "enum"}
    :param bgcolor_value: {"description": "Specify 6-digit HEX color value", "format": "string", "minLength": 6, "maxLength": 6, "not": "bgcolor-name", "type": "string"}
    :param bgcolor_name: {"not": "bgcolor-value", "enum": ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "orange", "purple", "red", "silver", "teal", "white", "yellow"], "type": "string", "description": "'aqua': aqua; 'black': black; 'blue': blue; 'fuchsia': fuchsia; 'gray': gray; 'green': green; 'lime': lime; 'maroon': maroon; 'navy': navy; 'olive': olive; 'orange': orange; 'purple': purple; 'red': red; 'silver': silver; 'teal': teal; 'white': white; 'yellow': yellow; ", "format": "enum"}
    :param bgcolor: {"default": 0, "not": "bgfile", "type": "number", "description": "Specify background color", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "background"
        self.DeviceProxy = ""
        self.bgfile = ""
        self.bgstyle = ""
        self.bgcolor_value = ""
        self.bgcolor_name = ""
        self.bgcolor = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class LogonFail(A10BaseClass):
    
    """Class Description::
    Logon fail page configuration.

    Class logon-fail supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/portal/{name}/logon-fail`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "logon-fail"
        self.a10_url="/axapi/v3/aam/authentication/portal/{name}/logon-fail"
        self.DeviceProxy = ""
        self.fail_msg_cfg = {}
        self.title_cfg = {}
        self.background = {}
        self.uuid = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


