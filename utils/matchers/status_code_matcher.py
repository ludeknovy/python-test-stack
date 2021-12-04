from hamcrest.core.base_matcher import BaseMatcher
from requests import Response


class ReturnedStatusCode(BaseMatcher):

    def __init__(self, status_code: int):
        self._status_code = status_code

    def _matches(self, item: Response):
        if not item.status_code:
            return False
        return item.status_code == self._status_code

    def describe_to(self, description):
        description.append_text("status code ")
        description.append_description_of(self._status_code)

    def describe_mismatch(self, item, mismatch_description):
        mismatch_description.append_text("status code ")
        mismatch_description.append_description_of(item.status_code)
        mismatch_description.append_text(" received with body: \n")
        mismatch_description.append_text(item.text[:1000] + (item.text[1000:] and '..'))

    def describe_match(self, item, match_description):
        match_description.append_text("status code ")
        match_description.append_description_of(item.status_code)
        match_description.append_text(" was received with body: \n")
        match_description.append_text(item.text[:1000] + (item.text[1000:] and '..'))


def returned_status_code(status_code: int):
    return ReturnedStatusCode(status_code)
