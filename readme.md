ZLibrary / 2Library Anti Ratelimit
---

This project is a tool that completely obliterates [ZLibrary / 2Library](https://z-lib.org/)'s ratelimit.

If you've tried to download books from the associated website, you might see quite an annoying message regarding the fact that you can only download 5 or 10 books freely from the website per day.

Using this algorithm, that issue is no more and moreover, you get 4 high speed download urls to download from which also happens to completely remove the 1 MBPS limit ZLibrary puts in their website.

**Use case**

Yep, there are conditions when this script can be completely useless. This is when the link to the book does not consist of an ISBN 10 or an ISBN 13 code. 
Usually, every book has an ISBN number and the most appropriate way to deal with this issue when it occurs is to search for another page relating to the same page that consists an ISBN number.

**How it works?**

Well, it's not a surprise that [ZLibrary / 2Library](https://z-lib.org/) is basically just a mirror of [Library Genesis](http://libgen.is). 
The different between the two (as far as I can see) is that, one has a nice search algorithm and SSL and the other doesn't while the other has amazing download urls and no intentions to capitalize upon pirated books.

Hence, this program here scrapes out the ISBN codes using XPATH and converts that code to a high speed download url.

The download that come from this are directly hosted from Cloudflare or IPFS.io, making them incredibly fast and reliable. 
The urls are also static, that means, there is no need of regeneration of the urls.

**How to use?**

Check out `example.py`, it showcases a working code consisting a replace-able URL.

**Disclaimer**

Downloading pirated books might be illegal in your country.

The aim of this project is to prove the usefulness of automation and not directly piracy.

Requirements
---

This code is an asynchronous code and hence, it requires packages such as `aiohttp`. Similarly, a light-weight html parser `lxml` is also required.