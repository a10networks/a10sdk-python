from a10sdk.common.A10BaseClass import A10BaseClass


class SamplingEnable(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param counters1: {"enum": ["all", "num", "curr", "total", "svrsel_fail", "no_route", "snat_fail", "client_fail", "server_fail", "no_sess", "user_session", "acr_out", "acr_in", "aca_out", "aca_in", "cea_out", "cea_in", "cer_out", "cer_in", "dwr_out", "dwr_in", "dwa_out", "dwa_in", "str_out", "str_in", "sta_out", "sta_in", "asr_out", "asr_in", "asa_out", "asa_in", "other_out", "other_in"], "type": "string", "description": "'all': all; 'num': Number; 'curr': Current; 'total': Total; 'svrsel_fail': Number of server selection failed; 'no_route': Number of no routes; 'snat_fail': Number of snat failures; 'client_fail': Number of client failures; 'server_fail': Number of server failures; 'no_sess': Number of no sessions; 'user_session': Number of user sessions; 'acr_out': Number of ACRs out; 'acr_in': Number of ACRs in; 'aca_out': Number of ACAs out; 'aca_in': Number of ACAs in; 'cea_out': Number of CEAs out; 'cea_in': Number of CEAs in; 'cer_out': Number of CERs out; 'cer_in': Number of CERs in; 'dwr_out': Number of DWRs out; 'dwr_in': Number of DWRs in; 'dwa_out': Number of DWAs out; 'dwa_in': Number of DWAs in; 'str_out': Number of STRs out; 'str_in': Number of STRs in; 'sta_out': Number of STAs out; 'sta_in': Number of STAs in; 'asr_out': Number of ASRs out; 'asr_in': Number of ASRs in; 'asa_out': Number of ASAs out; 'asa_in': Number of ASAs in; 'other_out': Number of other messages out; 'other_in': Number of other messages in; ", "format": "enum"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "sampling-enable"
        self.DeviceProxy = ""
        self.counters1 = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PortDiameter(A10BaseClass):
    
    """Class Description::
    port diameter counters.

    Class port-diameter supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param sampling_enable: {"minItems": 1, "items": {"type": "object"}, "uniqueItems": true, "type": "array", "array": [{"properties": {"optional": true, "counters1": {"enum": ["all", "num", "curr", "total", "svrsel_fail", "no_route", "snat_fail", "client_fail", "server_fail", "no_sess", "user_session", "acr_out", "acr_in", "aca_out", "aca_in", "cea_out", "cea_in", "cer_out", "cer_in", "dwr_out", "dwr_in", "dwa_out", "dwa_in", "str_out", "str_in", "sta_out", "sta_in", "asr_out", "asr_in", "asa_out", "asa_in", "other_out", "other_in"], "type": "string", "description": "'all': all; 'num': Number; 'curr': Current; 'total': Total; 'svrsel_fail': Number of server selection failed; 'no_route': Number of no routes; 'snat_fail': Number of snat failures; 'client_fail': Number of client failures; 'server_fail': Number of server failures; 'no_sess': Number of no sessions; 'user_session': Number of user sessions; 'acr_out': Number of ACRs out; 'acr_in': Number of ACRs in; 'aca_out': Number of ACAs out; 'aca_in': Number of ACAs in; 'cea_out': Number of CEAs out; 'cea_in': Number of CEAs in; 'cer_out': Number of CERs out; 'cer_in': Number of CERs in; 'dwr_out': Number of DWRs out; 'dwr_in': Number of DWRs in; 'dwa_out': Number of DWAs out; 'dwa_in': Number of DWAs in; 'str_out': Number of STRs out; 'str_in': Number of STRs in; 'sta_out': Number of STAs out; 'sta_in': Number of STAs in; 'asr_out': Number of ASRs out; 'asr_in': Number of ASRs in; 'asa_out': Number of ASAs out; 'asa_in': Number of ASAs in; 'other_out': Number of other messages out; 'other_in': Number of other messages in; ", "format": "enum"}}}]}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/counter/port-diameter/{sampling_enable}`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "sampling_enable"]

        self.b_key = "port-diameter"
        self.a10_url="/axapi/v3/counter/port-diameter/{sampling_enable}"
        self.DeviceProxy = ""
        self.sampling_enable = []

        for keys, value in kwargs.items():
            setattr(self,keys, value)


