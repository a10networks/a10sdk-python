from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param server_fin: {"description": "Server FIN", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param curr_be_enc: {"description": "Curr BE Encryption Conns", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param total_be_enc: {"description": "Total BE Encryption Conns", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param auth_success: {"description": "Authentication Success", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "2"}
    :param total_proxy: {"description": "Total Proxy Conns", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param curr_proxy: {"description": "Curr Proxy Conns", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param commands: {"description": "DB commands reply", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param client_fin: {"description": "Client FIN", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param curr_fe_enc: {"description": "Curr FE Encryption Conns", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param queries: {"description": "DB Queries", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param session_err: {"description": "Session err", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param auth_failure: {"description": "Authentication Failure", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param total_fe_enc: {"description": "Total FE Encryption Conns", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.server_fin = ""
        self.curr_be_enc = ""
        self.total_be_enc = ""
        self.auth_success = ""
        self.total_proxy = ""
        self.curr_proxy = ""
        self.commands = ""
        self.client_fin = ""
        self.curr_fe_enc = ""
        self.queries = ""
        self.session_err = ""
        self.auth_failure = ""
        self.total_fe_enc = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Mssql(A10BaseClass):
    
    """Class Description::
    Statistics for the object mssql.

    Class mssql supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/mssql/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "mssql"
        self.a10_url="/axapi/v3/slb/mssql/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


