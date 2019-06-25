from tornado import gen, httpclient, ioloop


async def get_content_from_url(url):
    response = await httpclient.AsyncHTTPClient().fetch(url).body.decode()
    print(response)


# def remove_
# def remove
import asyncio


async def main():
    await asyncio.wait([get_content_from_url('www.baidu.com')])


if __name__ == "__main__":
    loop=asyncio.get_event_loop()
    loop.run_until_complete(main())
