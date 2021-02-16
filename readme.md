A solução foi dividida em 3 arquivos, com o intuito de facilitar a leitura e entendimento do código. Não foram utilizados
try-except e nem lançamento de exceções, a fim de tornar o código mais simples e limpo.

- Como testar a solução:

1. Tenha instalado em sua máquina o Python 3.8 64-bit ou uma versão superior;

2. Em seu terminal, navegue até o diretorio onde se encontra o arquivo main.py;

3. Em um S.O Linux, execute:
python3 main.py

4. Em um S.O Windows, execute:
python main.py


- Como modificar os dados de teste:

1. Abra o arquivo data.py;
2. Dentro da função get_shopping_list é retornado uma lista de objetos ItemShopping, que possui os atributos 
item e quantity;
3. O atributo item é um objeto Item, e nele é possível alterar o nome e preço unitário do Item;
4. Altere o atributo quantity para um inteiro que representa quantos objetos do mesmo Item estão na lista de compras;
5. Salve o arquivo data.py e execute a função main.py, conforme explicado no tópico "Como testar a solução".
