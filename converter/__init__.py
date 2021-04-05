from ._2lib import *
from .libgen_search import *

async def download_from_2lib(url):
    isbn_codes = await get_isbn_from(url)
    assert isbn_codes, "Could not resolve ISBN values."
    
    return await download_uris_from_isbn(isbn_codes.pop(0))