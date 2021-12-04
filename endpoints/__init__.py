from requests import Response
from utils.session_with_url import SessionWithUrlBase
import os


class BaseEndpoint(object):

    def __init__(self, client=None, x_test_id=None, **kwargs):
        self._client = client or SessionWithUrlBase(base_url=self.__get_base_url(), x_test_id=x_test_id)

    def __get_base_url(self):
        return os.environ.get("BASE_URL", "http://localhost")

    def get(self, url: str, **kwargs) -> Response:
        return self._client.get(url, **kwargs)

    def post(self, url: str, **kwargs) -> Response:
        return self._client.post(url, **kwargs)

    def put(self, url: str, **kwargs) -> Response:
        return self._client.put(url, **kwargs)

    def delete(self, url: str, **kwargs) -> Response:
        return self._client.delete(url, **kwargs)

    def request(self, **kwargs):
        return self._client.request(**kwargs)
