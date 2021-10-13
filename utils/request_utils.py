import logging
import textwrap

# logger setup in conftest.py
logger = logging.getLogger('test-logger')


def format_round_trip(response):
    result = textwrap.dedent('''
                ---------------- request ----------------
                {req.method} {req.url}
                {reqhdrs}

                {req.body}
                ---------------- response ----------------
                {res.status_code} {res.reason} {res.url}
                {reshdrs}

                {res.text}
            ''').format(
        req=response.request,
        res=response,
        reqhdrs=_format_headers(response.request.headers),
        reshdrs=_format_headers(response.headers)
    )
    return result


def _format_headers(d):
    return '\n'.join(f'{k}: {v}' for k, v in d.items())


def log_round_trip(response, *args, **kwargs):
    logger.debug(f'{format_round_trip(response)}')


def schemathesis_case_kwargs_update(kwargs):
    del kwargs['url']
    del kwargs['method']
    return kwargs
