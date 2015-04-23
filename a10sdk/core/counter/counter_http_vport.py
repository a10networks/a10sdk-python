from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "status_200", "status_201", "status_202", "status_203", "status_204", "status_205", "status_206", "status_207", "status_100", "status_101", "status_102", "status_103", "status_300", "status_301", "status_302", "status_303", "status_304", "status_305", "status_306", "status_307", "status_400", "status_401", "status_402", "status_403", "status_404", "status_405", "status_406", "status_407", "status_408", "status_409", "status_410", "status_411", "status_412", "status_413", "status_414", "status_415", "status_416", "status_417", "status_418", "status_422", "status_423", "status_424", "status_425", "status_426", "status_449", "status_450", "status_500", "status_501", "status_502", "status_503", "status_504", "status_504_ax", "status_505", "status_506", "status_507", "status_508", "status_509", "status_510", "status_1xx", "status_2xx", "status_3xx", "status_4xx", "status_5xx", "status_6xx", "status_unknown", "ws_handshake_request", "ws_handshake_success", "ws_client_switch", "ws_server_switch", "REQ_10u", "REQ_20u", "REQ_50u", "REQ_100u", "REQ_200u", "REQ_500u", "REQ_1m", "REQ_2m", "REQ_5m", "REQ_10m", "REQ_20m", "REQ_50m", "REQ_100m", "REQ_200m", "REQ_500m", "REQ_1s", "REQ_2s", "REQ_5s", "REQ_OVER_5s"], "type": "string", "description": "'all': all; 'status_200': Status code 200; 'status_201': Status code 201; 'status_202': Status code 202; 'status_203': Status code 203; 'status_204': Status code 204; 'status_205': Status code 205; 'status_206': Status code 206; 'status_207': Status code 207; 'status_100': Status code 100; 'status_101': Status code 101; 'status_102': Status code 102; 'status_103': Status code 103; 'status_300': Status code 300; 'status_301': Status code 301; 'status_302': Status code 302; 'status_303': Status code 303; 'status_304': Status code 304; 'status_305': Status code 305; 'status_306': Status code 306; 'status_307': Status code 307; 'status_400': Status code 400; 'status_401': Status code 401; 'status_402': Status code 402; 'status_403': Status code 403; 'status_404': Status code 404; 'status_405': Status code 405; 'status_406': Status code 406; 'status_407': Status code 407; 'status_408': Status code 408; 'status_409': Status code 409; 'status_410': Status code 410; 'status_411': Status code 411; 'status_412': Status code 412; 'status_413': Status code 413; 'status_414': Status code 414; 'status_415': Status code 415; 'status_416': Status code 416; 'status_417': Status code 417; 'status_418': Status code 418; 'status_422': Status code 422; 'status_423': Status code 423; 'status_424': Status code 424; 'status_425': Status code 425; 'status_426': Status code 426; 'status_449': Status code 449; 'status_450': Status code 450; 'status_500': Status code 500; 'status_501': Status code 501; 'status_502': Status code 502; 'status_503': Status code 503; 'status_504': Status code 504; 'status_504_ax': Status code 504 AX-gen; 'status_505': Status code 505; 'status_506': Status code 506; 'status_507': Status code 507; 'status_508': Status code 508; 'status_509': Status code 509; 'status_510': Status code 510; 'status_1xx': status code 1XX; 'status_2xx': status code 2XX; 'status_3xx': status code 3XX; 'status_4xx': status code 4XX; 'status_5xx': status code 5XX; 'status_6xx': status code 6XX; 'status_unknown': Status code unknown; 'ws_handshake_request': WS Handshake Req; 'ws_handshake_success': WS Handshake Res; 'ws_client_switch': WS Client Pkts; 'ws_server_switch': WS Server Pkts; 'REQ_10u': Rsp time less than 10u; 'REQ_20u': Rsp time less than 20u; 'REQ_50u': Rsp time less than 50u; 'REQ_100u': Rsp time less than 100u; 'REQ_200u': Rsp time less than 200u; 'REQ_500u': Rsp time less than 500u; 'REQ_1m': Rsp time less than 1m; 'REQ_2m': Rsp time less than 2m; 'REQ_5m': Rsp time less than 5m; 'REQ_10m': Rsp time less than 10m; 'REQ_20m': Rsp time less than 20m; 'REQ_50m': Rsp time less than 5m; 'REQ_100m': Rsp time less than 100m; 'REQ_200m': Rsp time less than 200m; 'REQ_500m': Rsp time less than 500m; 'REQ_1s': Rsp time less than 1s; 'REQ_2s': Rsp time less than 2s; 'REQ_5s': Rsp time less than 5s; 'REQ_OVER_5s': Rsp time greater than equal to 5s; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class Http_Vport(A10BaseClass):
    
    """Class Description::
    http vport counters.

    Class http_vport supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "status_200", "status_201", "status_202", "status_203", "status_204", "status_205", "status_206", "status_207", "status_100", "status_101", "status_102", "status_103", "status_300", "status_301", "status_302", "status_303", "status_304", "status_305", "status_306", "status_307", "status_400", "status_401", "status_402", "status_403", "status_404", "status_405", "status_406", "status_407", "status_408", "status_409", "status_410", "status_411", "status_412", "status_413", "status_414", "status_415", "status_416", "status_417", "status_418", "status_422", "status_423", "status_424", "status_425", "status_426", "status_449", "status_450", "status_500", "status_501", "status_502", "status_503", "status_504", "status_504_ax", "status_505", "status_506", "status_507", "status_508", "status_509", "status_510", "status_1xx", "status_2xx", "status_3xx", "status_4xx", "status_5xx", "status_6xx", "status_unknown", "ws_handshake_request", "ws_handshake_success", "ws_client_switch", "ws_server_switch", "REQ_10u", "REQ_20u", "REQ_50u", "REQ_100u", "REQ_200u", "REQ_500u", "REQ_1m", "REQ_2m", "REQ_5m", "REQ_10m", "REQ_20m", "REQ_50m", "REQ_100m", "REQ_200m", "REQ_500m", "REQ_1s", "REQ_2s", "REQ_5s", "REQ_OVER_5s"], "type": "string", "description": "'all': all; 'status_200': Status code 200; 'status_201': Status code 201; 'status_202': Status code 202; 'status_203': Status code 203; 'status_204': Status code 204; 'status_205': Status code 205; 'status_206': Status code 206; 'status_207': Status code 207; 'status_100': Status code 100; 'status_101': Status code 101; 'status_102': Status code 102; 'status_103': Status code 103; 'status_300': Status code 300; 'status_301': Status code 301; 'status_302': Status code 302; 'status_303': Status code 303; 'status_304': Status code 304; 'status_305': Status code 305; 'status_306': Status code 306; 'status_307': Status code 307; 'status_400': Status code 400; 'status_401': Status code 401; 'status_402': Status code 402; 'status_403': Status code 403; 'status_404': Status code 404; 'status_405': Status code 405; 'status_406': Status code 406; 'status_407': Status code 407; 'status_408': Status code 408; 'status_409': Status code 409; 'status_410': Status code 410; 'status_411': Status code 411; 'status_412': Status code 412; 'status_413': Status code 413; 'status_414': Status code 414; 'status_415': Status code 415; 'status_416': Status code 416; 'status_417': Status code 417; 'status_418': Status code 418; 'status_422': Status code 422; 'status_423': Status code 423; 'status_424': Status code 424; 'status_425': Status code 425; 'status_426': Status code 426; 'status_449': Status code 449; 'status_450': Status code 450; 'status_500': Status code 500; 'status_501': Status code 501; 'status_502': Status code 502; 'status_503': Status code 503; 'status_504': Status code 504; 'status_504_ax': Status code 504 AX-gen; 'status_505': Status code 505; 'status_506': Status code 506; 'status_507': Status code 507; 'status_508': Status code 508; 'status_509': Status code 509; 'status_510': Status code 510; 'status_1xx': status code 1XX; 'status_2xx': status code 2XX; 'status_3xx': status code 3XX; 'status_4xx': status code 4XX; 'status_5xx': status code 5XX; 'status_6xx': status code 6XX; 'status_unknown': Status code unknown; 'ws_handshake_request': WS Handshake Req; 'ws_handshake_success': WS Handshake Res; 'ws_client_switch': WS Client Pkts; 'ws_server_switch': WS Server Pkts; 'REQ_10u': Rsp time less than 10u; 'REQ_20u': Rsp time less than 20u; 'REQ_50u': Rsp time less than 50u; 'REQ_100u': Rsp time less than 100u; 'REQ_200u': Rsp time less than 200u; 'REQ_500u': Rsp time less than 500u; 'REQ_1m': Rsp time less than 1m; 'REQ_2m': Rsp time less than 2m; 'REQ_5m': Rsp time less than 5m; 'REQ_10m': Rsp time less than 10m; 'REQ_20m': Rsp time less than 20m; 'REQ_50m': Rsp time less than 5m; 'REQ_100m': Rsp time less than 100m; 'REQ_200m': Rsp time less than 200m; 'REQ_500m': Rsp time less than 500m; 'REQ_1s': Rsp time less than 1s; 'REQ_2s': Rsp time less than 2s; 'REQ_5s': Rsp time less than 5s; 'REQ_OVER_5s': Rsp time greater than equal to 5s; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/counter/http-vport/{sampling_enable}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "sampling_enable"]

        self.b_key = "http_vport"
        self.a10_url="/axapi/v3/counter/http-vport/{sampling_enable}"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


