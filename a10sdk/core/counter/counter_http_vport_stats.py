from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param REQ_50u: {"description": "Rsp time less than 50u", "format": "counter", "type": "number", "oid": "72", "optional": true, "size": "2"}
    :param ws_server_switch: {"description": "WS Server Pkts", "format": "counter", "type": "number", "oid": "69", "optional": true, "size": "2"}
    :param REQ_50m: {"description": "Rsp time less than 5m", "format": "counter", "type": "number", "oid": "81", "optional": true, "size": "2"}
    :param status_450: {"description": "Status code 450", "format": "counter", "type": "number", "oid": "46", "optional": true, "size": "2"}
    :param REQ_500m: {"description": "Rsp time less than 500m", "format": "counter", "type": "number", "oid": "84", "optional": true, "size": "2"}
    :param status_510: {"description": "Status code 510", "format": "counter", "type": "number", "oid": "58", "optional": true, "size": "2"}
    :param ws_handshake_request: {"description": "WS Handshake Req", "format": "counter", "type": "number", "oid": "66", "optional": true, "size": "2"}
    :param status_207: {"description": "Status code 207", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param status_206: {"description": "Status code 206", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param status_205: {"description": "Status code 205", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param status_204: {"description": "Status code 204", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param status_203: {"description": "Status code 203", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param status_202: {"description": "Status code 202", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param status_201: {"description": "Status code 201", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param status_200: {"description": "Status code 200", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param ws_client_switch: {"description": "WS Client Pkts", "format": "counter", "type": "number", "oid": "68", "optional": true, "size": "2"}
    :param status_406: {"description": "Status code 406", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "2"}
    :param REQ_20u: {"description": "Rsp time less than 20u", "format": "counter", "type": "number", "oid": "71", "optional": true, "size": "2"}
    :param status_4xx: {"description": "status code 4XX", "format": "counter", "type": "number", "oid": "62", "optional": true, "size": "2"}
    :param status_3xx: {"description": "status code 3XX", "format": "counter", "type": "number", "oid": "61", "optional": true, "size": "2"}
    :param REQ_200u: {"description": "Rsp time less than 200u", "format": "counter", "type": "number", "oid": "74", "optional": true, "size": "2"}
    :param REQ_100m: {"description": "Rsp time less than 100m", "format": "counter", "type": "number", "oid": "82", "optional": true, "size": "2"}
    :param REQ_5m: {"description": "Rsp time less than 5m", "format": "counter", "type": "number", "oid": "78", "optional": true, "size": "2"}
    :param REQ_100u: {"description": "Rsp time less than 100u", "format": "counter", "type": "number", "oid": "73", "optional": true, "size": "2"}
    :param REQ_5s: {"description": "Rsp time less than 5s", "format": "counter", "type": "number", "oid": "87", "optional": true, "size": "2"}
    :param REQ_20m: {"description": "Rsp time less than 20m", "format": "counter", "type": "number", "oid": "80", "optional": true, "size": "2"}
    :param REQ_500u: {"description": "Rsp time less than 500u", "format": "counter", "type": "number", "oid": "75", "optional": true, "size": "2"}
    :param REQ_2s: {"description": "Rsp time less than 2s", "format": "counter", "type": "number", "oid": "86", "optional": true, "size": "2"}
    :param REQ_200m: {"description": "Rsp time less than 200m", "format": "counter", "type": "number", "oid": "83", "optional": true, "size": "2"}
    :param status_307: {"description": "Status code 307", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "2"}
    :param status_304: {"description": "Status code 304", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "2"}
    :param status_305: {"description": "Status code 305", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "2"}
    :param status_302: {"description": "Status code 302", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "2"}
    :param status_303: {"description": "Status code 303", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "2"}
    :param status_300: {"description": "Status code 300", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param status_301: {"description": "Status code 301", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "2"}
    :param REQ_10u: {"description": "Rsp time less than 10u", "format": "counter", "type": "number", "oid": "70", "optional": true, "size": "2"}
    :param REQ_10m: {"description": "Rsp time less than 10m", "format": "counter", "type": "number", "oid": "79", "optional": true, "size": "2"}
    :param status_306: {"description": "Status code 306", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "2"}
    :param status_412: {"description": "Status code 412", "format": "counter", "type": "number", "oid": "33", "optional": true, "size": "2"}
    :param status_413: {"description": "Status code 413", "format": "counter", "type": "number", "oid": "34", "optional": true, "size": "2"}
    :param status_410: {"description": "Status code 410", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "2"}
    :param status_411: {"description": "Status code 411", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "2"}
    :param status_416: {"description": "Status code 416", "format": "counter", "type": "number", "oid": "37", "optional": true, "size": "2"}
    :param status_417: {"description": "Status code 417", "format": "counter", "type": "number", "oid": "38", "optional": true, "size": "2"}
    :param status_414: {"description": "Status code 414", "format": "counter", "type": "number", "oid": "35", "optional": true, "size": "2"}
    :param status_415: {"description": "Status code 415", "format": "counter", "type": "number", "oid": "36", "optional": true, "size": "2"}
    :param status_418: {"description": "Status code 418", "format": "counter", "type": "number", "oid": "39", "optional": true, "size": "2"}
    :param status_unknown: {"description": "Status code unknown", "format": "counter", "type": "number", "oid": "65", "optional": true, "size": "2"}
    :param status_100: {"description": "Status code 100", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param status_101: {"description": "Status code 101", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param status_102: {"description": "Status code 102", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param status_103: {"description": "Status code 103", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "2"}
    :param REQ_2m: {"description": "Rsp time less than 2m", "format": "counter", "type": "number", "oid": "77", "optional": true, "size": "2"}
    :param ws_handshake_success: {"description": "WS Handshake Res", "format": "counter", "type": "number", "oid": "67", "optional": true, "size": "2"}
    :param status_504_ax: {"description": "Status code 504 AX-gen", "format": "counter", "type": "number", "oid": "52", "optional": true, "size": "2"}
    :param status_6xx: {"description": "status code 6XX", "format": "counter", "type": "number", "oid": "64", "optional": true, "size": "2"}
    :param status_5xx: {"description": "status code 5XX", "format": "counter", "type": "number", "oid": "63", "optional": true, "size": "2"}
    :param status_401: {"description": "Status code 401", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "2"}
    :param status_400: {"description": "Status code 400", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "2"}
    :param status_403: {"description": "Status code 403", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "2"}
    :param status_402: {"description": "Status code 402", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "2"}
    :param status_405: {"description": "Status code 405", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "2"}
    :param status_404: {"description": "Status code 404", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "2"}
    :param status_407: {"description": "Status code 407", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "2"}
    :param status_2xx: {"description": "status code 2XX", "format": "counter", "type": "number", "oid": "60", "optional": true, "size": "2"}
    :param status_409: {"description": "Status code 409", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "2"}
    :param status_408: {"description": "Status code 408", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "2"}
    :param REQ_1m: {"description": "Rsp time less than 1m", "format": "counter", "type": "number", "oid": "76", "optional": true, "size": "2"}
    :param REQ_1s: {"description": "Rsp time less than 1s", "format": "counter", "type": "number", "oid": "85", "optional": true, "size": "2"}
    :param status_1xx: {"description": "status code 1XX", "format": "counter", "type": "number", "oid": "59", "optional": true, "size": "2"}
    :param status_423: {"description": "Status code 423", "format": "counter", "type": "number", "oid": "41", "optional": true, "size": "2"}
    :param status_422: {"description": "Status code 422", "format": "counter", "type": "number", "oid": "40", "optional": true, "size": "2"}
    :param status_426: {"description": "Status code 426", "format": "counter", "type": "number", "oid": "44", "optional": true, "size": "2"}
    :param status_425: {"description": "Status code 425", "format": "counter", "type": "number", "oid": "43", "optional": true, "size": "2"}
    :param status_424: {"description": "Status code 424", "format": "counter", "type": "number", "oid": "42", "optional": true, "size": "2"}
    :param status_508: {"description": "Status code 508", "format": "counter", "type": "number", "oid": "56", "optional": true, "size": "2"}
    :param status_509: {"description": "Status code 509", "format": "counter", "type": "number", "oid": "57", "optional": true, "size": "2"}
    :param REQ_OVER_5s: {"description": "Rsp time greater than equal to 5s", "format": "counter", "type": "number", "oid": "88", "optional": true, "size": "2"}
    :param status_500: {"description": "Status code 500", "format": "counter", "type": "number", "oid": "47", "optional": true, "size": "2"}
    :param status_501: {"description": "Status code 501", "format": "counter", "type": "number", "oid": "48", "optional": true, "size": "2"}
    :param status_502: {"description": "Status code 502", "format": "counter", "type": "number", "oid": "49", "optional": true, "size": "2"}
    :param status_503: {"description": "Status code 503", "format": "counter", "type": "number", "oid": "50", "optional": true, "size": "2"}
    :param status_504: {"description": "Status code 504", "format": "counter", "type": "number", "oid": "51", "optional": true, "size": "2"}
    :param status_505: {"description": "Status code 505", "format": "counter", "type": "number", "oid": "53", "optional": true, "size": "2"}
    :param status_506: {"description": "Status code 506", "format": "counter", "type": "number", "oid": "54", "optional": true, "size": "2"}
    :param status_507: {"description": "Status code 507", "format": "counter", "type": "number", "oid": "55", "optional": true, "size": "2"}
    :param status_449: {"description": "Status code 449", "format": "counter", "type": "number", "oid": "45", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.REQ_50u = ""
        self.ws_server_switch = ""
        self.REQ_50m = ""
        self.status_450 = ""
        self.REQ_500m = ""
        self.status_510 = ""
        self.ws_handshake_request = ""
        self.status_207 = ""
        self.status_206 = ""
        self.status_205 = ""
        self.status_204 = ""
        self.status_203 = ""
        self.status_202 = ""
        self.status_201 = ""
        self.status_200 = ""
        self.ws_client_switch = ""
        self.status_406 = ""
        self.REQ_20u = ""
        self.status_4xx = ""
        self.status_3xx = ""
        self.REQ_200u = ""
        self.REQ_100m = ""
        self.REQ_5m = ""
        self.REQ_100u = ""
        self.REQ_5s = ""
        self.REQ_20m = ""
        self.REQ_500u = ""
        self.REQ_2s = ""
        self.REQ_200m = ""
        self.status_307 = ""
        self.status_304 = ""
        self.status_305 = ""
        self.status_302 = ""
        self.status_303 = ""
        self.status_300 = ""
        self.status_301 = ""
        self.REQ_10u = ""
        self.REQ_10m = ""
        self.status_306 = ""
        self.status_412 = ""
        self.status_413 = ""
        self.status_410 = ""
        self.status_411 = ""
        self.status_416 = ""
        self.status_417 = ""
        self.status_414 = ""
        self.status_415 = ""
        self.status_418 = ""
        self.status_unknown = ""
        self.status_100 = ""
        self.status_101 = ""
        self.status_102 = ""
        self.status_103 = ""
        self.REQ_2m = ""
        self.ws_handshake_success = ""
        self.status_504_ax = ""
        self.status_6xx = ""
        self.status_5xx = ""
        self.status_401 = ""
        self.status_400 = ""
        self.status_403 = ""
        self.status_402 = ""
        self.status_405 = ""
        self.status_404 = ""
        self.status_407 = ""
        self.status_2xx = ""
        self.status_409 = ""
        self.status_408 = ""
        self.REQ_1m = ""
        self.REQ_1s = ""
        self.status_1xx = ""
        self.status_423 = ""
        self.status_422 = ""
        self.status_426 = ""
        self.status_425 = ""
        self.status_424 = ""
        self.status_508 = ""
        self.status_509 = ""
        self.REQ_OVER_5s = ""
        self.status_500 = ""
        self.status_501 = ""
        self.status_502 = ""
        self.status_503 = ""
        self.status_504 = ""
        self.status_505 = ""
        self.status_506 = ""
        self.status_507 = ""
        self.status_449 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Http_Vport(A10BaseClass):
    
    """Class Description::
    Statistics for the object http_vport.

    Class http_vport supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/counter/http-vport/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "http_vport"
        self.a10_url="/axapi/v3/counter/http-vport/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


