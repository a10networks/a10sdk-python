from a10sdk.common.A10BaseClass import A10BaseClass


class NewPwdCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param new_password: {"default": 0, "type": "number", "description": "Configure new password text in default change password page", "format": "flag"}
    :param new_size: {"description": "Specify font size", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}
    :param new_font: {"default": 0, "type": "number", "description": "Sepcify font", "format": "flag"}
    :param new_color_name: {"not": "new-color-value", "enum": ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "orange", "purple", "red", "silver", "teal", "white", "yellow"], "type": "string", "description": "'aqua': aqua; 'black': black; 'blue': blue; 'fuchsia': fuchsia; 'gray': gray; 'green': green; 'lime': lime; 'maroon': maroon; 'navy': navy; 'olive': olive; 'orange': orange; 'purple': purple; 'red': red; 'silver': silver; 'teal': teal; 'white': white; 'yellow': yellow; ", "format": "enum"}
    :param new_color: {"default": 0, "type": "number", "description": "Specify font color", "format": "flag"}
    :param new_color_value: {"description": "Specify 6-digit HEX color value", "format": "string", "minLength": 6, "maxLength": 6, "not": "new-color-name", "type": "string"}
    :param new_text: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify new password text (Default: New Password)", "format": "string-rlx"}
    :param new_font_custom: {"description": "Specify custom font", "format": "string-rlx", "minLength": 1, "maxLength": 63, "not": "new-face", "type": "string"}
    :param new_face: {"not": "new-font-custom", "enum": ["Arial", "Courier_New", "Georgia", "Times_New_Roman", "Verdana"], "type": "string", "description": "'Arial': Arial; 'Courier_New': Courier New; 'Georgia': Georgia; 'Times_New_Roman': Times New Roman; 'Verdana': Verdana; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "new-pwd-cfg"
        self.DeviceProxy = ""
        self.new_password = ""
        self.new_size = ""
        self.new_font = ""
        self.new_color_name = ""
        self.new_color = ""
        self.new_color_value = ""
        self.new_text = ""
        self.new_font_custom = ""
        self.new_face = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class TitleCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param title: {"default": 0, "type": "number", "description": "Configure title in default change password page", "format": "flag"}
    :param title_color: {"default": 0, "type": "number", "description": "Specify font color", "format": "flag"}
    :param title_color_name: {"not": "title-color-value", "enum": ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "orange", "purple", "red", "silver", "teal", "white", "yellow"], "type": "string", "description": "'aqua': aqua; 'black': black; 'blue': blue; 'fuchsia': fuchsia; 'gray': gray; 'green': green; 'lime': lime; 'maroon': maroon; 'navy': navy; 'olive': olive; 'orange': orange; 'purple': purple; 'red': red; 'silver': silver; 'teal': teal; 'white': white; 'yellow': yellow; ", "format": "enum"}
    :param title_font_custom: {"description": "Specify custom font", "format": "string-rlx", "minLength": 1, "maxLength": 63, "not": "title-face", "type": "string"}
    :param title_face: {"not": "title-font-custom", "enum": ["Arial", "Courier_New", "Georgia", "Times_New_Roman", "Verdana"], "type": "string", "description": "'Arial': Arial; 'Courier_New': Courier New; 'Georgia': Georgia; 'Times_New_Roman': Times New Roman; 'Verdana': Verdana; ", "format": "enum"}
    :param title_color_value: {"description": "Specify 6-digit HEX color value", "format": "string", "minLength": 6, "maxLength": 6, "not": "title-color-name", "type": "string"}
    :param title_size: {"description": "Specify font size", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}
    :param title_text: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify title (Default: Please Change Your Password)", "format": "string-rlx"}
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


class OldPwdCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param old_face: {"not": "old-font-custom", "enum": ["Arial", "Courier_New", "Georgia", "Times_New_Roman", "Verdana"], "type": "string", "description": "'Arial': Arial; 'Courier_New': Courier New; 'Georgia': Georgia; 'Times_New_Roman': Times New Roman; 'Verdana': Verdana; ", "format": "enum"}
    :param old_color: {"default": 0, "type": "number", "description": "Specify font color", "format": "flag"}
    :param old_color_value: {"description": "Specify 6-digit HEX color value", "format": "string", "minLength": 6, "maxLength": 6, "not": "old-color-name", "type": "string"}
    :param old_password: {"default": 0, "type": "number", "description": "Configure old password text in default change password page", "format": "flag"}
    :param old_color_name: {"not": "old-color-value", "enum": ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "orange", "purple", "red", "silver", "teal", "white", "yellow"], "type": "string", "description": "'aqua': aqua; 'black': black; 'blue': blue; 'fuchsia': fuchsia; 'gray': gray; 'green': green; 'lime': lime; 'maroon': maroon; 'navy': navy; 'olive': olive; 'orange': orange; 'purple': purple; 'red': red; 'silver': silver; 'teal': teal; 'white': white; 'yellow': yellow; ", "format": "enum"}
    :param old_size: {"description": "Specify font size", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}
    :param old_text: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify old password text (Default: Old Password)", "format": "string-rlx"}
    :param old_font_custom: {"description": "Specify custom font", "format": "string-rlx", "minLength": 1, "maxLength": 63, "not": "old-face", "type": "string"}
    :param old_font: {"default": 0, "type": "number", "description": "Sepcify font", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "old-pwd-cfg"
        self.DeviceProxy = ""
        self.old_face = ""
        self.old_color = ""
        self.old_color_value = ""
        self.old_password = ""
        self.old_color_name = ""
        self.old_size = ""
        self.old_text = ""
        self.old_font_custom = ""
        self.old_font = ""

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


class CfmPwdCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param cfm_color_name: {"not": "cfm-color-value", "enum": ["aqua", "black", "blue", "fuchsia", "gray", "green", "lime", "maroon", "navy", "olive", "orange", "purple", "red", "silver", "teal", "white", "yellow"], "type": "string", "description": "'aqua': aqua; 'black': black; 'blue': blue; 'fuchsia': fuchsia; 'gray': gray; 'green': green; 'lime': lime; 'maroon': maroon; 'navy': navy; 'olive': olive; 'orange': orange; 'purple': purple; 'red': red; 'silver': silver; 'teal': teal; 'white': white; 'yellow': yellow; ", "format": "enum"}
    :param cfm_face: {"not": "cfm-font-custom", "enum": ["Arial", "Courier_New", "Georgia", "Times_New_Roman", "Verdana"], "type": "string", "description": "'Arial': Arial; 'Courier_New': Courier New; 'Georgia': Georgia; 'Times_New_Roman': Times New Roman; 'Verdana': Verdana; ", "format": "enum"}
    :param cfm_color_value: {"description": "Specify 6-digit HEX color value", "format": "string", "minLength": 6, "maxLength": 6, "not": "cfm-color-name", "type": "string"}
    :param cfm_font_custom: {"description": "Specify custom font", "format": "string-rlx", "minLength": 1, "maxLength": 63, "not": "cfm-face", "type": "string"}
    :param cfm_size: {"description": "Specify font size", "minimum": 1, "type": "number", "maximum": 7, "format": "number"}
    :param cfm_font: {"default": 0, "type": "number", "description": "Sepcify font", "format": "flag"}
    :param cfm_text: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify confirm password text (Default: Confirm New Password)", "format": "string-rlx"}
    :param confirm_password: {"default": 0, "type": "number", "description": "Configure confirm password text in default change password page", "format": "flag"}
    :param cfm_color: {"default": 0, "type": "number", "description": "Specify font color", "format": "flag"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "cfm-pwd-cfg"
        self.DeviceProxy = ""
        self.cfm_color_name = ""
        self.cfm_face = ""
        self.cfm_color_value = ""
        self.cfm_font_custom = ""
        self.cfm_size = ""
        self.cfm_font = ""
        self.cfm_text = ""
        self.confirm_password = ""
        self.cfm_color = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class UsernameCfg(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param username: {"default": 0, "type": "number", "description": "Configure username text in default change password page", "format": "flag"}
    :param user_font: {"default": 0, "type": "number", "description": "Sepcify font", "format": "flag"}
    :param user_text: {"minLength": 1, "maxLength": 63, "type": "string", "description": "Specify username text (Default: Username)", "format": "string-rlx"}
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


class ChangePassword(A10BaseClass):
    
    """Class Description::
    Change password page configuration.

    Class change-password supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param action_url: {"description": "Specify form action URL in default change password page (Default: /change.fo)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param new_password_var: {"description": "Specify new password variable name in default change password page (Default: cp_new_pwd)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param submit_text: {"description": "Specify submit button text in default change password page (Default: Submit)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param confirm_password_var: {"description": "Specify confirm password variable name in default change password page (Default: cp_cfm_pwd)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param reset_text: {"description": "Specify reset button text in default change password page (Default: Reset)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param username_var: {"description": "Specify username variable name in default change password page (Default: cp_usr)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param old_password_var: {"description": "Specify old password variable name in default change password page (Default: cp_old_pwd)", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/portal/{name}/change-password`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "change-password"
        self.a10_url="/axapi/v3/aam/authentication/portal/{name}/change-password"
        self.DeviceProxy = ""
        self.action_url = ""
        self.new_password_var = ""
        self.new_pwd_cfg = {}
        self.submit_text = ""
        self.uuid = ""
        self.confirm_password_var = ""
        self.title_cfg = {}
        self.reset_text = ""
        self.username_var = ""
        self.old_pwd_cfg = {}
        self.background = {}
        self.old_password_var = ""
        self.cfm_pwd_cfg = {}
        self.username_cfg = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


