from urllib.parse import urljoin
from utils.request_utils import log_round_trip
import requests


class SessionWithUrlBase(requests.Session):
    def __init__(self, x_test_id=None, base_url=None, *args, **kwargs):
        super(SessionWithUrlBase, self).__init__(*args, **kwargs)
        self.base_url = base_url
        self.x_test_id = x_test_id

    def request(self, method, url, **kwargs):
        modified_url = urljoin(self.base_url, url)
        hooks = {'response': log_round_trip}
        if self.x_test_id:
            self.headers.update({'x-test-id': self.x_test_id})
        return super(SessionWithUrlBase, self).request(method, modified_url, hooks=hooks, **kwargs)
