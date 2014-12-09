from a10sdk.common.A10BaseClass import A10BaseClass


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


class FailMsgCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param fail_font_custom: {"description": "Specify custom font", "format": "string-rlx", "minLength": 1, "maxLength": 63, "not": "fail-face", "type": "string"}
    :param fail_color: {"default": 0, "type": "number", "description": "Specify font color", "format": "flag"}
    :param fail_size: {"description": "Specify font size", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}
    :param fail_msg: {"default": 0, "type": "number", "description": "Configure login failure message in default logon page", "format": "flag"}
    :param fail_text: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify login failure message (Default: Invalid username or password. Please try again.)", "format": "string-rlx"}
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


class PasswordCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param pass_color_value: {"description": "Specify 6-digit HEX color value", "format": "string", "minLength": 6, "maxLength": 6, "not": "pass-color-name", "type": "string"}
    :param pass_color: {"default": 0, "type": "number", "description": "Specify font color", "format": "flag"}
    :param pass_color_name: {"not": "pass-color-value", "enum": ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "orange", "purple", "red", "silver", "teal", "white", "yellow"], "type": "string", "description": "'aqua': aqua; 'black': black; 'blue': blue; 'fuchsia': fuchsia; 'gray': gray; 'green': green; 'lime': lime; 'maroon': maroon; 'navy': navy; 'olive': olive; 'orange': orange; 'purple': purple; 'red': red; 'silver': silver; 'teal': teal; 'white': white; 'yellow': yellow; ", "format": "enum"}
    :param pass_face: {"not": "pass-font-custom", "enum": ["Arial", "Courier_New", "Georgia", "Times_New_Roman", "Verdana"], "type": "string", "description": "'Arial': Arial; 'Courier_New': Courier New; 'Georgia': Georgia; 'Times_New_Roman': Times New Roman; 'Verdana': Verdana; ", "format": "enum"}
    :param pass_font_custom: {"description": "Specify custom font", "format": "string-rlx", "minLength": 1, "maxLength": 63, "not": "pass-face", "type": "string"}
    :param pass_size: {"description": "Specify font size", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}
    :param pass_text: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify password text (Default: Password)", "format": "string-rlx"}
    :param pass_font: {"default": 0, "type": "number", "description": "Sepcify font", "format": "flag"}
    :param password: {"default": 0, "type": "number", "description": "Configure password text in default logon page", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "password-cfg"
        self.DeviceProxy = ""
        self.pass_color_value = ""
        self.pass_color = ""
        self.pass_color_name = ""
        self.pass_face = ""
        self.pass_font_custom = ""
        self.pass_size = ""
        self.pass_text = ""
        self.pass_font = ""
        self.password = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class UsernameCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param username: {"default": 0, "type": "number", "description": "Configure username text in default logon page", "format": "flag"}
    :param user_font: {"default": 0, "type": "number", "description": "Sepcify font", "format": "flag"}
    :param user_text: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify username text (Default: User Name)", "format": "string-rlx"}
    :param user_size: {"description": "Specify font size", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}
    :param user_color_value: {"description": "Specify 6-digit HEX color value", "format": "string", "minLength": 6, "maxLength": 6, "not": "user-color-name", "type": "string"}
    :param user_font_custom: {"description": "Specify custom font", "format": "string-rlx", "minLength": 1, "maxLength": 63, "not": "user-face", "type": "string"}
    :param user_color: {"default": 0, "type": "number", "description": "Specify font color", "format": "flag"}
    :param user_face: {"not": "user-font-custom", "enum": ["Arial", "Courier_New", "Georgia", "Times_New_Roman", "Verdana"], "type": "string", "description": "'Arial': Arial; 'Courier_New': Courier New; 'Georgia': Georgia; 'Times_New_Roman': Times New Roman; 'Verdana': Verdana; ", "format": "enum"}
    :param user_color_name: {"not": "user-color-value", "enum": ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "orange", "purple", "red", "silver", "teal", "white", "yellow"], "type": "string", "description": "'aqua': aqua; 'black': black; 'blue': blue; 'fuchsia': fuchsia; 'gray': gray; 'green': green; 'lime': lime; 'maroon': maroon; 'navy': navy; 'olive': olive; 'orange': orange; 'purple': purple; 'red': red; 'silver': silver; 'teal': teal; 'white': white; 'yellow': yellow; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "username-cfg"
        self.DeviceProxy = ""
        self.username = ""
        self.user_font = ""
        self.user_text = ""
        self.user_size = ""
        self.user_color_value = ""
        self.user_font_custom = ""
        self.user_color = ""
        self.user_face = ""
        self.user_color_name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Logon(A10BaseClass):
    
    """Class Description::
    Logon page configuration.

    Class logon supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param action_url: {"description": "Specify form action URL in default logon page (Default: /logon.fo)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param password_var: {"description": "Specify password variable name in default logon page (Default: pwd)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param username_var: {"description": "Specify username variable name in default logon page (Default: user)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param submit_text: {"description": "Specify submit button text in default logon page (Default: Log In)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/portal/{name}/logon`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "logon"
        self.a10_url="/axapi/v3/aam/authentication/portal/{name}/logon"
        self.DeviceProxy = ""
        self.action_url = ""
        self.password_var = ""
        self.username_var = ""
        self.submit_text = ""
        self.background = {}
        self.fail_msg_cfg = {}
        self.password_cfg = {}
        self.username_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


