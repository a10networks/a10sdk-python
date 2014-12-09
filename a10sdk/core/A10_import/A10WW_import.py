from a10sdk.common.A10BaseClass import A10BaseClass


class Import(A10BaseClass):
    
    """    :param geo_location: {"description": "Geo-location CSV File", "partition-visibility": "shared", "minLength": 1, "format": "string", "optional": true, "maxLength": 63, "type": "string"}
    :param ssl_cert_key: {"optional": true, "enum": ["bulk"], "type": "string", "description": "'bulk': import an archive file; ", "format": "enum"}
    :param bw_list: {"description": "Black white List File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param auth_portal: {"description": "Portal file for http authentication", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param aflex: {"description": "aFleX Script Source File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param overwrite: {"default": 0, "optional": true, "type": "number", "description": "Overwrite existing file", "format": "flag"}
    :param pfx_password: {"description": "The password for certificate file (pfx type only)", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "type": "string"}
    :param class_list: {"description": "Class List File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param policy: {"description": "WAF policy File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param auth_portal_image: {"description": "Image file for default portal", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param csr_generate: {"default": 0, "optional": true, "type": "number", "description": "Generate CSR file", "format": "flag"}
    :param ssl_crl: {"description": "SSL Crl File", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param remote_file: {"not": "store-name", "optional": true, "type": "string", "description": "profile name for remote url", "format": "url"}
    :param dnssec_ds: {"description": "DNSSEC DS file for child zone", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param local_uri_file: {"description": "Local URI files for http response", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param wsdl: {"description": "Web Service Definition Language File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param ssl_key: {"description": "SSL Key File(enter bulk when import an archive file)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param geo_location_class_list: {"description": "Geo-location Class-list file", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param use_mgmt_port: {"default": 0, "optional": true, "type": "number", "description": "Use management port as source port", "format": "flag"}
    :param license: {"description": "License File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param store_name: {"description": "Import store name", "format": "string", "minLength": 1, "optional": true, "maxLength": 128, "not": "remote-file", "type": "string"}
    :param ca_cert: {"description": "CA Cert File(enter bulk when import an archive file)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param lw_4o6: {"description": "LW-4over6 Binding Table File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param xml_schema: {"description": "XML-Schema File", "format": "string", "minLength": 1, "optional": true, "maxLength": 63, "type": "string"}
    :param certificate_type: {"optional": true, "enum": ["pem", "der", "pfx", "p7b"], "type": "string", "description": "'pem': pem; 'der': der; 'pfx': pfx; 'p7b': p7b; ", "format": "enum"}
    :param ssl_cert: {"description": "SSL Cert File(enter bulk when import an archive file)", "format": "string", "minLength": 1, "optional": true, "maxLength": 255, "type": "string"}
    :param dnssec_dnskey: {"description": "DNSSEC DNSKEY(KSK) file for child zone", "format": "string", "minLength": 1, "optional": true, "maxLength": 127, "type": "string"}
    :param DeviceProxy: The device proxy for REST operations and session handling. Refer to `common/device_proxy.py`

Class Description::
    Get files from remote site.

    Class import supports CRUD Operations and inherits from `common/A10BaseClass`.
    This class is the `"PARENT"` class for this module.`

    

    URL for this object::
    `https://<Hostname|Ip address>//axapi/v3/import`.

    

    
    """
    def __init__(self, **kwargs):
        self.ERROR_MSG = ""
        self.required=[]
        self.b_key = "import"
        self.a10_url="/axapi/v3/import"
        self.DeviceProxy = ""
        self.geo_location = ""
        self.ssl_cert_key = ""
        self.bw_list = ""
        self.health_external = {}
        self.auth_portal = ""
        self.aflex = ""
        self.overwrite = ""
        self.pfx_password = ""
        self.class_list = ""
        self.health_postfile = {}
        self.policy = ""
        self.store = {}
        self.auth_portal_image = ""
        self.csr_generate = ""
        self.ssl_crl = ""
        self.remote_file = ""
        self.dnssec_ds = ""
        self.local_uri_file = ""
        self.wsdl = ""
        self.ssl_key = ""
        self.geo_location_class_list = ""
        self.use_mgmt_port = ""
        self.A10WW_license = ""
        self.store_name = ""
        self.ca_cert = ""
        self.lw_4o6 = ""
        self.xml_schema = ""
        self.certificate_type = ""
        self.auth_saml_idp = {}
        self.ssl_cert = ""
        self.dnssec_dnskey = ""

        for keys, value in kwargs.items():
            setattr(self,keys, value)


