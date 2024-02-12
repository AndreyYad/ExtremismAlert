from json import load

async def get_data():
    with open('json/data.json') as file:
        data = load(file)
        return data['']