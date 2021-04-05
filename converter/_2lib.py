import aiohttp
import lxml.html as htmlparser

async def get_isbn_from(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            content = await response.text()

    element = htmlparser.fromstring(content)
    
    return [e.text for e in element.xpath('//div[@class="bookProperty property_isbn 10"]/div[@class="property_value"] | //div[@class="bookProperty property_isbn 13"]/div[@class="property_value"]')]