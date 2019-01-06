import responses
# import requests
import unittest

from grafana_api.grafana_face import GrafanaFace
# from grafana_api.grafana_api import TokenAuth


class TestGrafanaAdminAPI(unittest.TestCase):
    def test_settings_with_token(self):
        with responses.RequestsMock() as rsps:
            rsps.add(rsps.GET, 'https://grafana/api/admin/settings',
                          json={
                              "email": "user@mygraf.com",
                              "name": "admin",
                              "login": "admin",
                              "theme": "light",
                              "orgId": 1,
                              "isGrafanaAdmin": True
                          }, status=200)

            cli = GrafanaFace(('admin', 'admin'), host='grafana',
                              url_path_prefix='', protocol='https')
            r = cli.users.find_user('test@test.com')

            print(r)

# class TestGrafanaAPI(unittest.TestCase):
    # def test_grafana_api(self):
    #     with responses.RequestsMock() as rsps:
    #         rsps.add(rsps.GET, 'https://grafana/api/users/lookup?loginOrEmail=test@test.com',
    #                       json={
    #                           "email": "user@mygraf.com",
    #                           "name": "admin",
    #                           "login": "admin",
    #                           "theme": "light",
    #                           "orgId": 1,
    #                           "isGrafanaAdmin": True
    #                       }, status=200)
    #
    #         cli = GrafanaFace(('admin', 'admin'), host='grafana',
    #                           url_path_prefix='', protocol='https')
    #         r = cli.users.find_user('test@test.com')
    #
    #         print(r)

        # assert resp.json() == {"error": "not found"}
        #
        # assert len(responses.calls) == 1
        # assert responses.calls[0].request.url == 'http://twitter.com/api/1/foobar'
        # assert responses.calls[0].response.text == '{"error": "not found"}'


#   def test_grafana_api_no_verify(self):
#       cli = GrafanaFace(('admin', 'admin'), host='localhost',
#                         url_path_prefix='', protocol='https', verify=False)
#       cli.api.s.get = Mock(name='get')
#       cli.api.s.get.return_value = MockResponse({
# "email": "user@mygraf.com",
# "name": "admin",
# "login": "admin",
# "theme": "light",
# "orgId": 1,
# "isGrafanaAdmin": True}, 200)
#
#       basicAuth = requests.auth.HTTPBasicAuth('admin', 'admin')
#       cli.users.find_user('test@test.com')
#       cli.api.s.get.assert_called_once_with('https://localhost/api/users/lookup?loginOrEmail=test@test.com', auth=basicAuth, headers=None, json=None, verify=False)
#
#   def test_grafana_api_basic_auth(self):
#       cli = GrafanaFace(('admin', 'admin'), host='localhost',
#                         url_path_prefix='', protocol='https')
#       self.assertTrue(isinstance(cli.api.auth, requests.auth.HTTPBasicAuth))
#
#   def test_grafana_api_token_auth(self):
#       cli = GrafanaFace('alongtoken012345etc', host='localhost',
#                         url_path_prefix='', protocol='https')
#       self.assertTrue(isinstance(cli.api.auth, TokenAuth))
#
#
#   def test_grafana_api_basic_auth(self):
#       cli = GrafanaFace(('admin', 'admin'), host='localhost',
#                         url_path_prefix='', protocol='https')
#       self.assertTrue(isinstance(cli.api.auth, requests.auth.HTTPBasicAuth))
#
#   def test_grafana_api_token_auth(self):
#       cli = GrafanaFace('alongtoken012345etc', host='localhost',
#                         url_path_prefix='', protocol='https')
#       self.assertTrue(isinstance(cli.api.auth, TokenAuth))


if __name__ == '__main__':
    unittest.main()
