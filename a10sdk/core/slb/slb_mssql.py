from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "curr_proxy", "total_proxy", "curr_be_enc", "total_be_enc", "curr_fe_enc", "total_fe_enc", "client_fin", "server_fin", "session_err", "queries", "commands", "auth_success", "auth_failure"], "type": "string", "description": "'all': all; 'curr_proxy': Curr Proxy Conns; 'total_proxy': Total Proxy Conns; 'curr_be_enc': Curr BE Encryption Conns; 'total_be_enc': Total BE Encryption Conns; 'curr_fe_enc': Curr FE Encryption Conns; 'total_fe_enc': Total FE Encryption Conns; 'client_fin': Client FIN; 'server_fin': Server FIN; 'session_err': Session err; 'queries': DB Queries; 'commands': DB commands reply; 'auth_success': Authentication Success; 'auth_failure': Authentication Failure; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Mssql(A10BaseClass):
    
    """    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "curr_proxy", "total_proxy", "curr_be_enc", "total_be_enc", "curr_fe_enc", "total_fe_enc", "client_fin", "server_fin", "session_err", "queries", "commands", "auth_success", "auth_failure"], "type": "string", "description": "'all': all; 'curr_proxy': Curr Proxy Conns; 'total_proxy': Total Proxy Conns; 'curr_be_enc': Curr BE Encryption Conns; 'total_be_enc': Total BE Encryption Conns; 'curr_fe_enc': Curr FE Encryption Conns; 'total_fe_enc': Total FE Encryption Conns; 'client_fin': Client FIN; 'server_fin': Server FIN; 'session_err': Session err; 'queries': DB Queries; 'commands': DB commands reply; 'auth_success': Authentication Success; 'auth_failure': Authentication Failure; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Show mssql Statistics.

    Class mssql supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/slb/mssql`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "mssql"
        self.a10_url="/axapi/v3/slb/mssql"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


