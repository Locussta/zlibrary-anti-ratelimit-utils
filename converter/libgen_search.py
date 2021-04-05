import aiohttp
import lxml.html as htmlparser

import re

BASE = "https://libgen.is/search.php?req=%(isbn)s&open=0&res=100&view=simple&phrase=0&column=identifier"
PARTIAL_URL = re.compile(r'http:\/\/(?:\S+\.)?library\.lol\/main\/[^/]+')

async def from_partial_uri(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()

    element = htmlparser.fromstring(content)
    
    return [{e.text: e.get('href')} for e in element.xpath('//div[@id="download"]/*//a')]


async def get_download_uri(html_text):
    """
    Generate download links of the first search result.
    """
    element = htmlparser.fromstring(html_text)
    for element in element.xpath('//td/a[@href]'):
        if PARTIAL_URL.match(element.get('href', '')):
            return await from_partial_uri(element.get('href'))
    

async def download_uris_from_isbn(isbn_no: int):
    async with aiohttp.ClientSession() as session:
        async with session.get(BASE % {'isbn': isbn_no}) as response:
            return await get_download_uri(await response.text())