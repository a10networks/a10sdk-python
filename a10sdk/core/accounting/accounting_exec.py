from a10sdk.common.A10BaseClass import A10BaseClass


class Exec(A10BaseClass):
    
    """Class Description::
    Configuration for EXEC <shell> accounting.

    Class exec supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param accounting_exec_type: {"optional": true, "enum": ["start-stop", "stop-only"], "type": "string", "description": "'start-stop': Record start and stop without waiting; 'stop-only': Record stop when service terminates; ", "format": "enum"}
    :param accounting_exec_method: {"optional": true, "enum": ["tacplus", "radius"], "type": "string", "description": "'tacplus': Use TACACS+ servers for accounting; 'radius': Use radius servers for accounting; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/accounting/exec`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "exec"
        self.a10_url="/axapi/v3/accounting/exec"
        self.DeviceProxy = ""
        self.accounting_exec_type = ""
        self.accounting_exec_method = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


