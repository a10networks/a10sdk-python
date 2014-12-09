from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param NTLM_Authentication_failure: {"description": "Total NTLM Authentication Failure", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param Kerberos_request_send: {"description": "Total Kerberos Request", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param NTLM_session_setup_failed: {"description": "Total NTLM Session Setup Failure", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param NTLM_proto_negotiation_success: {"description": "Total NTLM Protocol Negotiation Success", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param Kerberos_response_get: {"description": "Total Kerberos Response", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param NTLM_proto_negotiation_failure: {"description": "Total NTLM Protocol Negotiation Failure", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param NTLM_session_setup_success: {"description": "Total NTLM Session Setup Success", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param NTLM_Authentication_success: {"description": "Total NTLM Authentication Success", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param Kerberos_other_error: {"description": "Total Kerberos Other Error", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param Kerberos_timeout_error: {"description": "Total Kerberos Timeout", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.NTLM_Authentication_failure = ""
        self.Kerberos_request_send = ""
        self.NTLM_session_setup_failed = ""
        self.NTLM_proto_negotiation_success = ""
        self.Kerberos_response_get = ""
        self.NTLM_proto_negotiation_failure = ""
        self.NTLM_session_setup_success = ""
        self.NTLM_Authentication_success = ""
        self.Kerberos_other_error = ""
        self.Kerberos_timeout_error = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Windows(A10BaseClass):
    
    """Class Description::
    Statistics for the object windows.

    Class windows supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param instance_list: {"minItems": 1, "items": {"type": "instance"}, "uniqueItems": true, "array": [{"required": ["name"], "properties": {"stats": {"type": "object", "properties": {"Krb_send_req_success": {"description": "Kerberos Request", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}, "Ntlm_auth_success": {"description": "NTLM Authentication Success", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}, "Ntlm_prepare_req_error": {"description": "NTLM Prepare Request Error", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}, "Ntlm_other_error": {"description": "NTLM Other Error", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}, "Ntlm_auth_failure": {"description": "NTLM Authentication Failure", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}, "Krb_timeout_error": {"description": "Kerberos Timeout", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}, "Ntlm_session_setup_success": {"description": "NTLM Session Setup Success", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}, "Krb_other_error": {"description": "Kerberos Other Error", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}, "Ntlm_proto_nego_failure": {"description": "NTLM Protocol Negotiation Failure", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}, "Ntlm_session_setup_failure": {"description": "NTLM Session Setup Failure", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}, "Ntlm_prepare_req_success": {"description": "NTLM Prepare Request Success", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}, "Krb_get_resp_success": {"description": "Kerberos Response", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}, "Ntlm_proto_nego_success": {"description": "NTLM Protocol Negotiation Success", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}, "Ntlm_timeout_error": {"description": "NTLM Timeout", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}}}, "name": {"description": "Specify Windows authentication server name", "format": "string-rlx", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}}}], "type": "array", "$ref": "/axapi/v3/aam/authentication/server/windows/instance/{name}"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/server/windows/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "windows"
        self.a10_url="/axapi/v3/aam/authentication/server/windows/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.instance_list = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


