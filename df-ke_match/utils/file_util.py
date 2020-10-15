from hashlib import sha256
import requests


def url_to_filename(url, etag=None):
    url_bytes = url.encode("utf-8")
    url_hash = sha256(url_bytes)
    filename = url_hash.hexdigest()

    if etag:
        etag_bytes = etag.encode("utf-8")
        etag_hash = sha256(etag_bytes)
        filename += "." + etag_hash.hexdigest()

    if url.endswith(".h5"):
        filename += ".h5"

    return filename


if __name__ == '__main__':
    url = "https://cdn.huggingface.co/hfl/chinese-bert-wwm-ext/pytorch_model.bin"
    etag = None
    try:
        response = requests.head(url, allow_redirects=True)
        if response.status_code == 200:
            etag = response.headers.get("ETag")
    except (EnvironmentError, requests.exceptions.Timeout):
        # etag is already None
        pass
    print(url_to_filename(url, etag))
