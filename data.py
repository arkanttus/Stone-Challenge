from typing import List


class Item:
    '''Representa o modelo de um Item.

    Attributes:
        name: O nome do Item.
        price: O preço unitário do Item.
    '''
    def __init__ (self, name: str, price: int):
        self.name = name
        self.price = price


class ItemShopping:
    '''Representa o modelo de um Item dentro de uma lista de compras.

    Attributes:
        item: Um objeto do tipo Item.
        quantity: A quantidade de itens do mesmo tipo.
    '''
    def __init__ (self, item: Item, quantity: int):
        self.item = item
        self.quantity = quantity


def get_shopping_list() -> List[ItemShopping]:
    '''Cada elemento da lista representa um ItemShopping.
    '''
    
    return [
        ItemShopping(
            item=Item(name='Graphics Card', price=135686),
            quantity=2
        ),
        ItemShopping(
            item=Item(name='Processor', price=85602),
            quantity=4
        ),
        ItemShopping(
            item=Item(name='Motherboard', price=50000),
            quantity=1
        ),
        ItemShopping(
            item=Item(name='Fan Cooler', price=5025),
            quantity=5
        ),
        ItemShopping(
            item=Item(name='Pen Drive 4Gb', price=1199),
            quantity=3
        )
    ]


def get_email_list() -> List[str]:
    '''Cada elemento da lista é uma string, que representa um e-mail, que por sua vez representa uma pessoa.
    '''

    return [
        'yasuo@troll.com',
        'zed@confia.com',
        'kat@feeder.com',
        'lee@sin.com',
        'teemo@jg.com'
    ]