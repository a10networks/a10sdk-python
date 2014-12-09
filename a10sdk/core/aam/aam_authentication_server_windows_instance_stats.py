from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Krb_send_req_success: {"description": "Kerberos Request", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Ntlm_auth_success: {"description": "NTLM Authentication Success", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param Ntlm_prepare_req_error: {"description": "NTLM Prepare Request Error", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param Ntlm_other_error: {"description": "NTLM Other Error", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param Ntlm_auth_failure: {"description": "NTLM Authentication Failure", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param Krb_timeout_error: {"description": "Kerberos Timeout", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param Ntlm_session_setup_success: {"description": "NTLM Session Setup Success", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param Krb_other_error: {"description": "Kerberos Other Error", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param Ntlm_proto_nego_failure: {"description": "NTLM Protocol Negotiation Failure", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param Ntlm_session_setup_failure: {"description": "NTLM Session Setup Failure", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param Ntlm_prepare_req_success: {"description": "NTLM Prepare Request Success", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param Krb_get_resp_success: {"description": "Kerberos Response", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param Ntlm_proto_nego_success: {"description": "NTLM Protocol Negotiation Success", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param Ntlm_timeout_error: {"description": "NTLM Timeout", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Krb_send_req_success = ""
        self.Ntlm_auth_success = ""
        self.Ntlm_prepare_req_error = ""
        self.Ntlm_other_error = ""
        self.Ntlm_auth_failure = ""
        self.Krb_timeout_error = ""
        self.Ntlm_session_setup_success = ""
        self.Krb_other_error = ""
        self.Ntlm_proto_nego_failure = ""
        self.Ntlm_session_setup_failure = ""
        self.Ntlm_prepare_req_success = ""
        self.Krb_get_resp_success = ""
        self.Ntlm_proto_nego_success = ""
        self.Ntlm_timeout_error = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Instance(A10BaseClass):
    
    """Class Description::
    Statistics for the object instance.

    Class instance supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify Windows authentication server name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/windows/instance/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "instance"
        self.a10_url="/axapi/v3/aam/authentication/server/windows/instance/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


