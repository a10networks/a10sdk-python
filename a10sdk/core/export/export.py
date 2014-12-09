from a10sdk.common.A10BaseClass import A10BaseClass


class Export(A10BaseClass):
    
    """    :param geo_location: {"description": "Geo-location CSV File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param ssl_cert_key: {"description": "Local SSL Key/Certificate file name", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param bw_list: {"description": "Black white List File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param merged_pcap: {"default": 0, "optional": true, "type": "number", "description": "Export the merged pcap file when there are multiple Export sessions", "format": "flag"}
    :param syslog: {"description": "Syslog file", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param auth_portal: {"description": "Portal file for http authentication", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param aflex: {"description": "aFleX Script Source File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param fixed_nat: {"description": "Fixed NAT Port Mapping File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param saml_idp_name: {"description": "SAML metadata of identity provider", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param class_list: {"description": "Class List File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param debug_monitor: {"description": "Debug Monitor Output", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param policy: {"description": "WAF policy File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param running_config: {"default": 0, "optional": true, "type": "number", "description": "Running Config", "format": "flag"}
    :param auth_portal_image: {"description": "Image file for default portal", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param ssl_crl: {"description": "SSL Crl File", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param remote_file: {"not": "store-name", "optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param dnssec_ds: {"description": "DNSSEC DS file for child zone", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param profile: {"description": "Startup-config Profile", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param local_uri_file: {"description": "Local URI files for http response", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param wsdl: {"description": "Web Services Definition Language File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param ssl_key: {"description": "SSL Key File(enter bulk when import an archive file)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param externalfilename: {"description": "Export the External Program from the System", "format": "string", "minLength": 1, "optional": true, "maxLength": 31, "type": "string"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param store_name: {"description": "Export store name", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "not": "remote-file", "type": "string"}
    :param axdebug: {"description": "AX Debug Packet File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param lw_4o6: {"description": "LW-4over6 Binding Table File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param xml_schema: {"description": "XML-Schema File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param startup_config: {"default": 0, "optional": true, "type": "number", "description": "Startup Config", "format": "flag"}
    :param ssl_cert: {"description": "SSL Cert File(enter bulk when import an archive file)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param dnssec_dnskey: {"description": "DNSSEC DNSKEY(KSK) file for child zone", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Put files to remote site.

    Class export supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/export`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "export"
        self.a10_url="/axapi/v3/export"
        self.DeviceProxy = ""
        self.geo_location = ""
        self.ssl_cert_key = ""
        self.bw_list = ""
        self.merged_pcap = ""
        self.syslog = ""
        self.auth_portal = ""
        self.aflex = ""
        self.fixed_nat = ""
        self.saml_idp_name = ""
        self.class_list = ""
        self.debug_monitor = ""
        self.policy = ""
        self.running_config = ""
        self.auth_portal_image = ""
        self.ssl_crl = ""
        self.remote_file = ""
        self.dnssec_ds = ""
        self.profile = ""
        self.local_uri_file = ""
        self.wsdl = ""
        self.ssl_key = ""
        self.store = {}
        self.externalfilename = ""
        self.use_mgmt_port = ""
        self.store_name = ""
        self.axdebug = ""
        self.lw_4o6 = ""
        self.xml_schema = ""
        self.startup_config = ""
        self.ssl_cert = ""
        self.dnssec_dnskey = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


