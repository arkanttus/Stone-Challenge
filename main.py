from data import get_shopping_list, get_email_list
from utils import calculate


def main():
    shopping_list = get_shopping_list()
    email_list = get_email_list()

    result = calculate(shopping_list, email_list)
    print(result)


if __name__ == '__main__':
    main()