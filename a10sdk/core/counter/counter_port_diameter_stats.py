from a10sdk.common.A10BaseClass import A10BaseClass


class Stats(A10BaseClass):
    
    """This class does not support CRUD Operations please use parent.

    :param svrsel_fail: {"description": "Number of server selection failed", "format": "counter", "type": "number", "oid": "4", "optional": true, "size": "2"}
    :param curr: {"description": "Current", "format": "counter", "type": "number", "oid": "2", "optional": true, "size": "2"}
    :param acr_out: {"description": "Number of ACRs out", "format": "counter", "type": "number", "oid": "11", "optional": true, "size": "2"}
    :param dwr_in: {"description": "Number of DWRs in", "format": "counter", "type": "number", "oid": "20", "optional": true, "size": "2"}
    :param num: {"description": "Number", "format": "counter", "type": "number", "oid": "1", "optional": true, "size": "2"}
    :param no_route: {"description": "Number of no routes", "format": "counter", "type": "number", "oid": "5", "optional": true, "size": "2"}
    :param server_fail: {"description": "Number of server failures", "format": "counter", "type": "number", "oid": "8", "optional": true, "size": "2"}
    :param user_session: {"description": "Number of user sessions", "format": "counter", "type": "number", "oid": "10", "optional": true, "size": "2"}
    :param aca_out: {"description": "Number of ACAs out", "format": "counter", "type": "number", "oid": "13", "optional": true, "size": "2"}
    :param sta_in: {"description": "Number of STAs in", "format": "counter", "type": "number", "oid": "26", "optional": true, "size": "2"}
    :param total: {"description": "Total", "format": "counter", "type": "number", "oid": "3", "optional": true, "size": "2"}
    :param dwa_in: {"description": "Number of DWAs in", "format": "counter", "type": "number", "oid": "22", "optional": true, "size": "2"}
    :param dwa_out: {"description": "Number of DWAs out", "format": "counter", "type": "number", "oid": "21", "optional": true, "size": "2"}
    :param asa_in: {"description": "Number of ASAs in", "format": "counter", "type": "number", "oid": "30", "optional": true, "size": "2"}
    :param asr_out: {"description": "Number of ASRs out", "format": "counter", "type": "number", "oid": "27", "optional": true, "size": "2"}
    :param aca_in: {"description": "Number of ACAs in", "format": "counter", "type": "number", "oid": "14", "optional": true, "size": "2"}
    :param dwr_out: {"description": "Number of DWRs out", "format": "counter", "type": "number", "oid": "19", "optional": true, "size": "2"}
    :param other_out: {"description": "Number of other messages out", "format": "counter", "type": "number", "oid": "31", "optional": true, "size": "2"}
    :param cea_out: {"description": "Number of CEAs out", "format": "counter", "type": "number", "oid": "15", "optional": true, "size": "2"}
    :param asr_in: {"description": "Number of ASRs in", "format": "counter", "type": "number", "oid": "28", "optional": true, "size": "2"}
    :param cer_in: {"description": "Number of CERs in", "format": "counter", "type": "number", "oid": "18", "optional": true, "size": "2"}
    :param str_in: {"description": "Number of STRs in", "format": "counter", "type": "number", "oid": "24", "optional": true, "size": "2"}
    :param sta_out: {"description": "Number of STAs out", "format": "counter", "type": "number", "oid": "25", "optional": true, "size": "2"}
    :param snat_fail: {"description": "Number of snat failures", "format": "counter", "type": "number", "oid": "6", "optional": true, "size": "2"}
    :param client_fail: {"description": "Number of client failures", "format": "counter", "type": "number", "oid": "7", "optional": true, "size": "2"}
    :param cer_out: {"description": "Number of CERs out", "format": "counter", "type": "number", "oid": "17", "optional": true, "size": "2"}
    :param str_out: {"description": "Number of STRs out", "format": "counter", "type": "number", "oid": "23", "optional": true, "size": "2"}
    :param cea_in: {"description": "Number of CEAs in", "format": "counter", "type": "number", "oid": "16", "optional": true, "size": "2"}
    :param asa_out: {"description": "Number of ASAs out", "format": "counter", "type": "number", "oid": "29", "optional": true, "size": "2"}
    :param no_sess: {"description": "Number of no sessions", "format": "counter", "type": "number", "oid": "9", "optional": true, "size": "2"}
    :param other_in: {"description": "Number of other messages in", "format": "counter", "type": "number", "oid": "32", "optional": true, "size": "2"}
    :param acr_in: {"description": "Number of ACRs in", "format": "counter", "type": "number", "oid": "12", "optional": true, "size": "2"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        
        self.b_key = "stats"
        self.DeviceProxy = ""
        self.svrsel_fail = ""
        self.curr = ""
        self.acr_out = ""
        self.dwr_in = ""
        self.num = ""
        self.no_route = ""
        self.server_fail = ""
        self.user_session = ""
        self.aca_out = ""
        self.sta_in = ""
        self.total = ""
        self.dwa_in = ""
        self.dwa_out = ""
        self.asa_in = ""
        self.asr_out = ""
        self.aca_in = ""
        self.dwr_out = ""
        self.other_out = ""
        self.cea_out = ""
        self.asr_in = ""
        self.cer_in = ""
        self.str_in = ""
        self.sta_out = ""
        self.snat_fail = ""
        self.client_fail = ""
        self.cer_out = ""
        self.str_out = ""
        self.cea_in = ""
        self.asa_out = ""
        self.no_sess = ""
        self.other_in = ""
        self.acr_in = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


class PortDiameter(A10BaseClass):
    
    """Class Description::
    Statistics for the object port-diameter.

    Class port-diameter supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/counter/port-diameter/{sampling_enable}/stats`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required = [ "sampling_enable"]

        self.b_key = "port-diameter"
        self.a10_url="/axapi/v3/counter/port-diameter/{sampling_enable}/stats"
        self.DeviceProxy = ""
        self.stats = {}

        for keys, value in kwargs.items():
            setattr(self,keys, value)


