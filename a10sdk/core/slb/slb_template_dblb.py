from a10sdk.common.A10BaseClass import A10BaseClass


class Dblb(A10BaseClass):
    
    """Class Description::
    DBLB template.

    Class dblb supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param server_version: {"optional": true, "enum": ["MSSQL2008", "MSSQL2012", "MySQL"], "type": "string", "description": "'MSSQL2008': MSSQL server 2008 or 2008 R2; 'MSSQL2012': MSSQL server 2012; 'MySQL': MySQL server (any version); ", "format": "enum"}
    :param name: {"description": "DBLB template name", "format": "string", "minLength": 1, "optional": false, "maxLength": 63, "type": "string"}
    :param class_list: {"description": "Specify user/password string class list (Class list name)", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string", "$ref": "/axapi/v3/class-list"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/template/dblb/{name}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "dblb"
        self.a10_url="/axapi/v3/slb/template/dblb/{name}"
        self.DeviceProxy = ""
        self.server_version = ""
        self.name = ""
        self.calc_sha1 = {}
        self.class_list = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


