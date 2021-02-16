from typing import List, Dict
from data import get_shopping_list, get_email_list, ItemShopping


def divide_between_users(amount: int, email_list: List[str]) -> Dict[str, int]:
    '''Divide o valor total da lista de compras entre os usuários presentes na lista de e-mails. A divisão procura ser a
    mais igualitária possível. Custo da função: O(n) | n = Tamanho da lista email_list

    Args:
        amount: Um valor inteiro que representa o valor total da lista de compras. Exemplo: 100
        email_list: Uma lista de strings, onde cada string representa um email.

    Returns:
        Um dict, onde cada chave do dict é uma string que representa um e-mail presente em email_list, e o valor de 
        cada chave é um inteiro que representa o valor associado a esse usuário, após a divisão.
    '''

    total_emails = len(email_list)
    
    if total_emails == 0:
        print('Erro: Lista de e-mails vazia! Favor fornecer uma lista de e-mails válida.')
        exit()

    divide, rest = divmod(amount, total_emails)
    
    result = {}
    for i in range(total_emails):
        '''Para cada email na lista, é criado uma chave no dict result e atribuido o valor da divisão.
        O resto da divisão é dividido entre os n primeiros usuarios, sendo n = rest | rest < total_emails
        '''
        result[email_list[i]] = divide + (i < rest)
    
    return result


def validate_item_shopping(item_shopping: ItemShopping) -> bool:
    '''Valida se os valores de preço e quantidade são positivos.
    '''

    if item_shopping.item.price < 0 or item_shopping.quantity < 0:
        print('Erro: Os valores de preço e quantidade de cada item devem ser positivos! Favor fornecer uma lista de compras válida.')
        return False

    return True


def amount_shopping_list(shopping_list: List[ItemShopping]) -> int:
    '''Calcula o valor total da lista de compras. Custo da função: O(n) | n = Tamanho da lista shopping_list

    Args:
        shopping_list: Uma lista de dicts, onde cada dict representa um item.

    Returns:
        Um valor inteiro correspondente ao valor total da lista de compras.
    '''

    if len(shopping_list) == 0:
        print('Erro: Lista de compras vazia! Favor fornecer uma lista de compras válida.')
        exit()

    amount = 0
    for item_shopping in shopping_list:
        if not validate_item_shopping(item_shopping):
            exit()

        amount += item_shopping.item.price * item_shopping.quantity
    
    return amount
    

def calculate(shopping_list: List[ItemShopping], email_list: List[str]) -> Dict[str, int]:
    '''Função auxiliar que chama outras funções para calcular o valor total da lista de compras e divide entre 
    os usuários presentes na lista de emails. 
    
    Custo da função: O(n + m) | n = Tamanho da lista shopping_list, m = Tamanho da lista email_list

    Args:
        shopping_list: Uma lista de dicts, onde cada dict representa um item.
        email_list: Uma lista de strings, onde cada string representa um email.

    Returns:
        Um dict, onde cada chave do dict é uma string que representa um e-mail presente em email_list, e o valor de 
        cada chave é um inteiro que representa o valor associado a esse usuário, após a divisão.
    '''

    amount = amount_shopping_list(shopping_list)
    
    return divide_between_users(amount, email_list)
