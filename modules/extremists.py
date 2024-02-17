from asyncio import run
from re import search

class Extremist:

    types_text = [
        'иноагентом',
        'экстремистской организацией',
        'экстремистским и террористическим лицом',
        'террорестической организацией',
        'запрещена'
    ]

    def __init__(self, *names: str, types: list[int]):
        self.name = names[0]
        self.var = [name.lower() for name in names]
        self.types = types

    async def get_text(self):
        list_type = ', '.join([Extremist.types_text[type_] for type_ in self.types]) + '\n'
        return f'{self.name} - признан {list_type}'
    
    async def find(self, text: str | None):
        if text is None:
            return False
        text = text.lower()
        for name in self.var:
            if search(r'(^|[^а-яА-ЯёЁa-zA-Z]){}($|[^а-яА-ЯёЁa-zA-Z])'.format(name), text):
                return True
        return False
    
list_extremists = [
    Extremist('ИГ', 'игил', types=[3, 4]),
    Extremist('ФБК', types=[0, 1, 4]),
    Extremist('Навальный', types=[2])
]

# if __name__ == '__main__':
#     obj = Extremist('ИГ', 'игил', types=[3, 4])
#     print(run(obj.find('и иги\nиг илм')))