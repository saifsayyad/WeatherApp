from groundwork import GwBasePattern
from weatherapp.applications.configuration import YAHOO_APP_ID, YAHOO_END_POINT, CLIENT_ID, CLIENT_SECRET
import time
import uuid
import urllib
import json
import hmac
import hashlib
from base64 import b64encode


class YahooApiPattern(GwBasePattern):
    method = 'GET'
    concat = '&'
    query = {'location': 'nasik', 'format': 'json', 'u': 'c'}

    def set_query_params(self, **kwargs):
        """
        Update query.
        supported params are:

            * location -> name of location
            * u -> 'c'/'f'
            * lat -> latitude
            * lon -> longitude
            * format -> xml/json
            * woeid -> woeid number

        """
        query_params = {}
        for k, v in kwargs.items():
            if v != '':
                query_params[k] = v

        self.query.update(query_params)

    def get_oauth_header(self):
        """
        Create and return ``OAuth`` header
        """

        oauth = {
            'oauth_consumer_key': CLIENT_ID,
            'oauth_nonce': uuid.uuid4().hex,
            'oauth_signature_method': 'HMAC-SHA1',
            'oauth_timestamp': str(int(time.time())),
            'oauth_version': '1.0'
        }

        merged_params = self.query.copy()
        merged_params.update(oauth)
        sorted_params = [k + '=' + urllib.parse.quote(merged_params[k], safe='') for k in sorted(merged_params.keys())]
        signature_base_str = self.method + self.concat + urllib.parse.quote(YAHOO_END_POINT,
                                                                            safe='') + self.concat + urllib.parse.quote(
            self.concat.join(sorted_params), safe='')

        composite_key = urllib.parse.quote(CLIENT_SECRET, safe='') + self.concat
        oauth_signature = b64encode(
            hmac.new(composite_key.encode('utf-8'), signature_base_str.encode('utf-8'), hashlib.sha1).digest())

        oauth['oauth_signature'] = oauth_signature.decode('utf-8')
        auth_header = 'OAuth ' + ', '.join(['{}="{}"'.format(k, v) for k, v in oauth.items()])

        return auth_header

    def get_weathter_info(self):
        """
        Fetches data from Yahoo endpoint, packs it in python ``dict`` and returns the ``dict``
        :return:
        """

        url = YAHOO_END_POINT + '?' + urllib.parse.urlencode(self.query)

        request = urllib.request.Request(url)
        request.headers['Authorization'] = self.get_oauth_header()
        request.headers['X-Yahoo-App-Id'] = YAHOO_APP_ID

        response = json.loads(
            urllib.request.urlopen(request).read().decode())  # Converting the bytes data to python dict

        return response


class YahooApiException(Exception):
    pass
