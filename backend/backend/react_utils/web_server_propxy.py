from http.client import HTTPResponse
from typing import Collection, Tuple, Mapping, Optional, Union
from urllib.error import HTTPError
from urllib.request import urlopen

from django.http import HttpResponse, StreamingHttpResponse
from django.template.backends.django import DjangoTemplates


def web_server_proxy(request, context, templates: DjangoTemplates,
                     upstream: str = 'http://frontend:3000', path: str = None):
    if path and not path.startswith('/'):
        path = f'/{path}'
    upstream_url = f'{upstream}{path or request.path}'
    try:
        response: Union[HTTPResponse, HTTPError] = urlopen(upstream_url)
        headers = _read_headers(response.getheaders())
    except HTTPError as res:
        headers = _read_headers(res.headers.items())
        response = res
    content_type = headers['Content-Type'].lower()
    if content_type == 'text/html; charset=utf-8':
        response_text = _read_response(response)
        response_text = response_text.decode()
        return HttpResponse(
            templates.from_string(response_text).render(context, request),
            status=response.status,
            reason=response.reason,
            headers=headers,
        )
    return StreamingHttpResponse(
        _iter_response(response),
        status=response.status,
        reason=response.reason,
        headers=headers,
    )


_blacklist_headers = {'Connection', 'Content-Security-Policy', 'Content-Length'}


def _read_headers(headers: Collection[Tuple[str, str]]) -> Optional[Mapping[str, str]]:
    if headers is None:
        return None
    return {k: v for k, v in headers if k not in _blacklist_headers}


def _read_response(response):
    content = response.read()
    response.close()
    return content


def _iter_response(response, chunk_size=65536):
    try:
        while True:
            data = response.read(chunk_size)
            if not data:
                break
            yield data
    finally:
        response.close()
