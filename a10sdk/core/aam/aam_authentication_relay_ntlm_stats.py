from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param Encoding_fail: {"description": "Encoding Failure", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "8"}
    :param Http_code_other: {"description": "Other HTTP Response", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "8"}
    :param Success: {"description": "Success", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "8"}
    :param Http_code_200: {"description": "HTTP 200 OK", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "8"}
    :param Http_code_401: {"description": "HTTP 401 Unauthorized", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "8"}
    :param Internal_error: {"description": "Internal Error", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "8"}
    :param Parse_header_fail: {"description": "Parse Header Failure", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "8"}
    :param Request: {"description": "Request", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "8"}
    :param Http_code_400: {"description": "HTTP 400 Bad Request", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "8"}
    :param Failure: {"description": "Failure", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "8"}
    :param Buffer_alloc_fail: {"description": "Buffer Allocation Failure", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "8"}
    :param Http_code_403: {"description": "HTTP 403 Forbidden", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "8"}
    :param Http_code_404: {"description": "HTTP 404 Not Found", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "8"}
    :param Http_code_500: {"description": "HTTP 500 Internal Server Error", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "8"}
    :param Http_code_503: {"description": "HTTP 503 Service Unavailable", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "8"}
    :param Response: {"description": "Response", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "8"}
    :param Insert_header_fail: {"description": "Insert Header Failure", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "8"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.Encoding_fail = ""
        self.Http_code_other = ""
        self.Success = ""
        self.Http_code_200 = ""
        self.Http_code_401 = ""
        self.Internal_error = ""
        self.Parse_header_fail = ""
        self.Request = ""
        self.Http_code_400 = ""
        self.Failure = ""
        self.Buffer_alloc_fail = ""
        self.Http_code_403 = ""
        self.Http_code_404 = ""
        self.Http_code_500 = ""
        self.Http_code_503 = ""
        self.Response = ""
        self.Insert_header_fail = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Ntlm(A10BaseClass):
    
    """Class Description::
    Statistics for the object ntlm.

    Class ntlm supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param name: {"description": "Specify NTLM authentication relay name", "format": "string", "minLength": 1, "oid": "1001", "optional": false, "maxLength": 63, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/aam/authentication/relay/ntlm/{name}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "name"]

        self.b_key = "ntlm"
        self.a10_url="/axapi/v3/aam/authentication/relay/ntlm/{name}/stats"
        self.DeviceProxy = ""
        self.stats = {}
        self.name = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


