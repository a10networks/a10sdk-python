__author__ = 'mthompson'
import base64
import httplib
import json
import mimetypes
import random
import string
import urllib
import urlparse


class DeviceProxy():
    def __init__(self, host, port, username, password, use_https=True, keep_alive=False):
        self.username = username
        self.password = password
        self.host = host
        self.port = port
        #self.lastPayload = "No Data"
        #self.lastResult = "No Data"
        self.keep_alive = keep_alive
        self.use_https = use_https
        self.logon()

    def get_connection(self):
        if self.use_https:
            return httplib.HTTPSConnection(self.host, port=self.port)
        else:
            return httplib.HTTPConnection(self.host, port=self.port)

    def logon(self):
        headers = {'Content-type': 'application/json'}
        conn = self.get_connection()
        conn.request("POST", "/axapi/v3/auth",
                     json.dumps({'credentials': {"username": self.username, "password": self.password}}), headers)
        self.password = ''
        try:
            response = json.loads(conn.getresponse().read())
            if "authresponse" in response:
                self.session_id = str(response['authresponse']['signature'])
                self.headers = {'Content-type': 'application/json', 'Authorization': "A10 %s" % self.session_id}
            else:
                self.session_id = "AUTHENTICATION FAILED"
                self.headers = {'Content-type': 'application/json', 'Authorization': "A10 %s" % self.session_id}

        except:
            return None

    def logoff(self):
        logoff_uri = "/axapi/v3/logoff"
        conn = self.get_connection()
        conn.request("POST", logoff_uri, "", self.headers)
        response = conn.getresponse().read()
        return response

    def request_handler(self, method, obj, response):
        response_payload = response.read()
        obj.__setattr__("DEBUG_Response", response_payload)
        obj.__setattr__("_HTTP_RESPONSE", response)
        if response.status == 401:
            if self.keep_alive:
                self.logon()
                if method == "GET":
                    return self.GET(obj)
                elif method == "GET_MP":
                    return self.multi_part_get(obj)
                elif method == "MPP":
                    return self.post_multipart(obj)
                elif method == "FD":
                    return self.file_delete(obj)
                elif method == "POST":
                    return self.POST(obj)
                elif method == "PUT":
                    return self.PUT(obj)
                elif method == "DELETE":
                    return self.DELETE(obj)
            else:
                return "Session Timeout"

        if len(response_payload) == 0:
            return None

        return response_payload

    def GET(self, obj, query_params=None):
        # Replace the a10_url with just the base path, stripping out any previous querystring
        parse_result = urlparse.urlparse(obj.a10_url)
        obj.a10_url = parse_result.path
        obj.a10_url = self.url_encoder(obj.a10_url)
        if query_params:
            obj.a10_url += '?' + urlparse.unquote(urllib.urlencode(query_params))

        print "URL:", obj.a10_url
        conn = self.get_connection()
        conn.request("GET", obj.a10_url, "", self.headers)
        response = conn.getresponse()
        conn.close()
        obj.__setattr__("DEBUG_CONNECTION", conn.__dict__)
        obj.__setattr__("DEBUG_Payload", "")
        obj.__setattr__("DEBUG_Response", response)
        obj.__setattr__("DEBUG_URL", obj.a10_url)
        obj.__setattr__("DEBUG_headers", self.headers)
        return self.request_handler("GET", obj, response)


    # TODO: Due to Bug 175975, add zero_length kwarg to optionally send zero-length POST. Remove code once bug resolved
    def POST(self, obj, zero_length=False):
        obj.a10_url = self.url_encoder(obj.a10_url)
        conn = self.get_connection()

        if zero_length:
            payload = None
        else:
            payload = obj.__json__(obj)
            if payload:
                payload = json.dumps(payload)

        conn.request("POST", self.url_encoder(obj.a10_url), payload, self.headers)
        response = conn.getresponse()
        obj.__setattr__("DEBUG_CONNECTION", conn.__dict__)
        conn.close()
        obj.__setattr__("DEBUG_Payload", payload)
        obj.__setattr__("DEBUG_Response", response)
        obj.__setattr__("DEBUG_URL", obj.a10_url)
        obj.__setattr__("DEBUG_headers", self.headers)
        return self.request_handler("POST", obj, response)

    def PUT(self, obj, payload_empty_string=False):
        obj.a10_url = self.url_encoder(obj.a10_url)
        conn = self.get_connection()
        if payload_empty_string:
            payload = ''
        else:
            json_output = obj.__json__(obj)
            if json_output:
                payload = json.dumps(obj.__json__(obj))
            else:
                payload = ''
        conn.request("PUT", self.url_encoder(obj.a10_url), payload, self.headers)
        response = conn.getresponse()
        conn.close()
        obj.__setattr__("DEBUG_CONNECTION", conn.__dict__)
        obj.__setattr__("DEBUG_Payload", payload)
        obj.__setattr__("DEBUG_Response", response)
        obj.__setattr__("DEBUG_URL", obj.a10_url)
        obj.__setattr__("DEBUG_headers", self.headers)
        return self.request_handler("PUT", obj, response)

    def POST_ALL(self, caller, obj_list):
        formatted_key = caller.b_key
        json_key = formatted_key + '-list'
        json_data = []
        for obj in obj_list:
            if obj.__json__(obj).get(formatted_key):
                json_data.append(obj.__json__(obj).get(formatted_key))
        json_packet = {}
        json_packet[json_key] = json_data
        payload = json.dumps(json_packet)
        conn = self.get_connection()
        conn.request("POST", self.url_encoder(caller.a10_url), payload, self.headers)
        response = conn.getresponse()
        conn.close()
        caller.__setattr__("DEBUG_CONNECTION", conn.__dict__)
        caller.__setattr__("DEBUG_Payload", payload)
        caller.__setattr__("DEBUG_Response", response)
        caller.__setattr__("DEBUG_URL", caller.a10_url)
        caller.__setattr__("DEBUG_headers", self.headers)
        return self.request_handler("POST", caller, response)

    def PUT_ALL(self, caller, obj_list):
        formatted_key = caller.b_key
        json_key = formatted_key + '-list'
        json_data = []
        for obj in obj_list:
            if obj.__json__(obj).get(formatted_key):
                json_data.append(obj.__json__(obj).get(formatted_key))
        json_packet = {}
        json_packet[json_key] = json_data
        payload = json.dumps(json_packet)
        conn = self.get_connection()
        conn.request("PUT", self.url_encoder(caller.a10_url), payload, self.headers)
        response = conn.getresponse()
        conn.close()
        caller.__setattr__("DEBUG_CONNECTION", conn.__dict__)
        caller.__setattr__("DEBUG_Payload", payload)
        caller.__setattr__("DEBUG_Response", response)
        caller.__setattr__("DEBUG_URL", caller.a10_url)
        caller.__setattr__("DEBUG_headers", self.headers)
        return self.request_handler("PUT", caller, response)


    def DELETE(self, obj):
        obj.a10_url = self.url_encoder(obj.a10_url)
        conn = self.get_connection()
        payload = None
        conn.request("DELETE", self.url_encoder(obj.a10_url), "", self.headers)
        response = conn.getresponse()
        conn.close()
        obj.__setattr__("DEBUG_CONNECTION", conn.__dict__)
        obj.__setattr__("DEBUG_Payload", "")
        obj.__setattr__("DEBUG_Response", response)
        obj.__setattr__("DEBUG_URL", obj.a10_url)
        obj.__setattr__("DEBUG_headers", self.headers)
        return self.request_handler("DELETE", obj, response)


    def url_encoder(self, url):
        url = url.replace(" ", "%20")
        return url


    def post_multipart(self, obj):
        """
        Post fields and files to an http host as multipart/form-data.
        fields is a sequence of (name, value) elements for regular form fields.
        files is a sequence of (name, filename, value) elements for data to be uploaded as files
        Return the server's response page.
        """
        content_type, body = self.encode_multipart_formdata(obj.fields,
                                                            obj.files)
        conn = self.get_connection()
        conn.putrequest('POST', self.url_encoder(obj.a10_url))
        conn.putheader('content-type', content_type)
        conn.putheader('Authorization', "A10 %s" % self.session_id)
        conn.putheader('content-length', str(len(body)))
        conn.endheaders()
        conn.send(body)
        response = conn.getresponse()
        conn.close()
        return self.request_handler('MPP', obj, response)


    def encode_multipart_formdata(self, fields, files):
        """
        fields is a sequence of (name, value) elements for regular form fields.
        files is a sequence of (name, filename, value) elements for data to be uploaded as files
        Return (content_type, body) ready for httplib.HTTP instance
        """
        boundkey = "".join([random.SystemRandom().choice(string
                                                         .digits +
                                                         string.letters)
                            for i in range(16)])
        BOUNDARY = "----------" + boundkey
        CRLF = '\r\n'
        L = []

        for (key, value) in fields:
            L.append('--' + BOUNDARY)
            L.append('Content-Disposition: form-data; name="%s"' % key)
            L.append('Content-Type: application/json')
            L.append('')
            if isinstance(value, dict):
                value = json.dumps(value)
            L.append(value)
            L.append('')

        for (key, filename, value) in files:
            L.append('--' + BOUNDARY)
            L.append(
                'Content-Disposition: form-data; name="%s"; filename="%s"' % (
                    key, filename))
            L.append('Content-Type: %s' % self.get_content_type(filename))
            #L.append('Content-transfer-encoding: Base64')
            L.append('')
            #L.append(base64.b64encode(value))
            L.append(value)

        L.append('--' + BOUNDARY + '--')
        L.append('')
        body = CRLF.join(L)
        content_type = 'multipart/form-data; boundary=%s' % BOUNDARY
        return content_type, body


    def get_content_type(self, filename):
        return mimetypes.guess_type(filename)[0] or 'text/plain'


    def multi_part_get(self, obj, query_params=None):
        # Replace the a10_url with just the base path, stripping out any previous querystring
        conn = self.get_connection()
        conn.request("GET", obj.a10_url, "", self.headers)
        response = conn.getresponse()
        conn.close()
        return self.request_handler("GET_MP", obj, response)

    def file_delete(self, obj):
        obj.a10_url = self.url_encoder(obj.a10_url)
        conn = httplib.HTTPSConnection(self.host, port=self.port)
        payload = None
        conn.request("DELETE", self.url_encoder(obj.a10_url), "", self.headers)
        response = conn.getresponse()
        conn.close()
        obj.__setattr__("DEBUG_CONNECTION", conn.__dict__)
        obj.__setattr__("DEBUG_Payload", "")
        obj.__setattr__("DEBUG_Response", response)
        obj.__setattr__("DEBUG_URL", obj.a10_url)
        obj.__setattr__("DEBUG_headers", self.headers)
        return self.request_handler("FD", obj, response)
