import asyncio
import json
import aiohttp

url = 'https://snowduck.app/api/1/syncSessionsProto'
auth_data = None
loop = asyncio.get_event_loop()

try:
    with open('auth.json', 'r') as file:
        auth_data = json.loads(file.read())
except:
    raise Exception("Please create the auth.json file using data from Fiddler")


async def persistent_session(app):
    app['PERSISTENT_SESSION'] = session = aiohttp.ClientSession()
    yield
    await session.close()


async def get_product_page(session, timestamp):
    headers = {
        'crc': auth_data['crc'],
        'token': auth_data['token'],
        'userID': auth_data['userID'],
        'LASTUPDATETIMESTAMP': str(timestamp)
    }
    async with session.post(
            url,
            headers=headers, timeout=15) as response:
        response_body = await response.read()
        # print('Hitting Website {}'.format(page))
        return response_body, response, timestamp


def get_results(session, timestamps):
    product_tasks = []
    for timestamp in timestamps:
        task = asyncio.ensure_future(get_product_page(session, timestamp))
        product_tasks.append(task)
    results = loop.run_until_complete(asyncio.gather(*product_tasks, return_exceptions=True))
    return results


def main():
    session = aiohttp.ClientSession()
    results = get_results(session, [0])
    try:
        with open('test_buffer.txt', 'wb') as file:
            file.write(results[0][0])
    except:
        print("Error Saving")

main()
