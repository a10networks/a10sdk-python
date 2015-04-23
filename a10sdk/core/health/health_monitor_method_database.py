from a10sdk.common.A10BaseClass import A10BaseClass


class Database(A10BaseClass):
    
    """Class Description::
    DATABASE type.

    Class database supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param db_send: {"description": "Specify the SQL query", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param db_password: {"default": 0, "optional": true, "type": "number", "description": "Specify the user password", "format": "flag"}
    :param db_receive_integer: {"description": "Specify the response integer", "format": "number", "optional": true, "maximum": 2147483647, "minimum": 0, "not": "db-receive", "type": "number"}
    :param database: {"default": 0, "optional": true, "type": "number", "description": "DATABASE type", "format": "flag"}
    :param db_receive: {"description": "Specify the response string", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "not": "db-receive-integer", "type": "string"}
    :param db_row_integer: {"description": "Specify the row number for receiving", "format": "number", "type": "number", "maximum": 10, "minimum": 1, "optional": true}
    :param database_name: {"optional": true, "enum": ["mssql", "mysql", "oracle", "postgresql"], "type": "string", "description": "'mssql': Specify MSSQL database; 'mysql': Specify MySQL database; 'oracle': Specify Oracle database; 'postgresql': Specify PostgreSQL database; ", "format": "enum"}
    :param db_password_str: {"description": "Configure password", "format": "password", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param db_encrypted: {"optional": true, "type": "encrypted", "description": "Do NOT use this option manually. (This is an A10 reserved keyword.) (The ENCRYPTED password string)", "format": "encrypted"}
    :param db_column: {"description": "Specify the column number for receiving", "format": "number", "type": "number", "maximum": 10, "minimum": 1, "optional": true}
    :param db_name: {"description": "Specify the database name", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param db_column_integer: {"description": "Specify the column number for receiving", "format": "number", "type": "number", "maximum": 10, "minimum": 1, "optional": true}
    :param db_username: {"description": "Specify the username", "format": "string-rlx", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param uuid: {"description": "uuid of the object", "format": "string", "minLength": 1, "modify-not-allowed": 1, "optional": true, "maxLength": 64, "type": "string"}
    :param db_row: {"description": "Specify the row number for receiving", "format": "number", "type": "number", "maximum": 10, "minimum": 1, "optional": true}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/health/monitor/{name}/method/database`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "database"
        self.a10_url="/axapi/v3/health/monitor/{name}/method/database"
        self.DeviceProxy = ""
        self.db_send = ""
        self.db_password = ""
        self.db_receive_integer = ""
        self.database = ""
        self.db_receive = ""
        self.db_row_integer = ""
        self.database_name = ""
        self.db_password_str = ""
        self.db_encrypted = ""
        self.db_column = ""
        self.db_name = ""
        self.db_column_integer = ""
        self.db_username = ""
        self.uuid = ""
        self.db_row = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


