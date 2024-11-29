"""
Proxy requests to avoid SSRF
"""

import logging
import time

import httpx

from configs import mlchain_config

SSRF_DEFAULT_MAX_RETRIES = mlchain_config.SSRF_DEFAULT_MAX_RETRIES

proxy_mounts = (
    {
        "http://": httpx.HTTPTransport(proxy=mlchain_config.SSRF_PROXY_HTTP_URL),
        "https://": httpx.HTTPTransport(proxy=mlchain_config.SSRF_PROXY_HTTPS_URL),
    }
    if mlchain_config.SSRF_PROXY_HTTP_URL and mlchain_config.SSRF_PROXY_HTTPS_URL
    else None
)

BACKOFF_FACTOR = 0.5
STATUS_FORCELIST = [429, 500, 502, 503, 504]


def make_request(method, url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    if "allow_redirects" in kwargs:
        allow_redirects = kwargs.pop("allow_redirects")
        if "follow_redirects" not in kwargs:
            kwargs["follow_redirects"] = allow_redirects

    if "timeout" not in kwargs:
        kwargs["timeout"] = httpx.Timeout(
            timeout=mlchain_config.SSRF_DEFAULT_TIME_OUT,
            connect=mlchain_config.SSRF_DEFAULT_CONNECT_TIME_OUT,
            read=mlchain_config.SSRF_DEFAULT_READ_TIME_OUT,
            write=mlchain_config.SSRF_DEFAULT_WRITE_TIME_OUT,
        )

    retries = 0
    stream = kwargs.pop("stream", False)
    while retries <= max_retries:
        try:
            if mlchain_config.SSRF_PROXY_ALL_URL:
                with httpx.Client(proxy=mlchain_config.SSRF_PROXY_ALL_URL) as client:
                    response = client.request(method=method, url=url, **kwargs)
            elif proxy_mounts:
                with httpx.Client(mounts=proxy_mounts) as client:
                    response = client.request(method=method, url=url, **kwargs)
            else:
                with httpx.Client() as client:
                    response = client.request(method=method, url=url, **kwargs)

            if response.status_code not in STATUS_FORCELIST:
                if stream:
                    return response.iter_bytes()
                return response
            else:
                logging.warning(f"Received status code {response.status_code} for URL {url} which is in the force list")

        except httpx.RequestError as e:
            logging.warning(f"Request to URL {url} failed on attempt {retries + 1}: {e}")

        retries += 1
        if retries <= max_retries:
            time.sleep(BACKOFF_FACTOR * (2 ** (retries - 1)))

    raise Exception(f"Reached maximum retries ({max_retries}) for URL {url}")


def get(url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    return make_request("GET", url, max_retries=max_retries, **kwargs)


def post(url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    return make_request("POST", url, max_retries=max_retries, **kwargs)


def put(url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    return make_request("PUT", url, max_retries=max_retries, **kwargs)


def patch(url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    return make_request("PATCH", url, max_retries=max_retries, **kwargs)


def delete(url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    return make_request("DELETE", url, max_retries=max_retries, **kwargs)


def head(url, max_retries=SSRF_DEFAULT_MAX_RETRIES, **kwargs):
    return make_request("HEAD", url, max_retries=max_retries, **kwargs)
