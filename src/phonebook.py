import re

class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def valida_caracteres_especiais(self, valor):
        regex = r"^[a-zA-Z0-9]+$"
        return re.match(regex, valor) is None

    def add(self, name, number):
        CAMPO_VAZIO = 0
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if len(name) == CAMPO_VAZIO or self.valida_caracteres_especiais(name):
            return 'Nome invalido'

        if len(number) == CAMPO_VAZIO:
            return 'Numero invalido'

        # sugestão: validação de nome duplicado
        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        CAMPO_VAZIO = 0
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if len(name) == CAMPO_VAZIO or self.valida_caracteres_especiais(name):
            return 'Nome invalido'

        # sugestão: validação de nome caso não exista no phonebook
        return {name: self.entries[name]}

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return self.entries.keys()

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return self.entries.values()

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries = {}
        return 'phonebook limpado'

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        # sugestão: validar quando search_name for vazio
        result = []

        # sugestão 1: considerar código abaixo e remover a estrutura for
        # return {search_name: self.entries[search_name]}
        for name, number in self.entries.items():
            if search_name in name:
                result.append({name: self.entries[name]})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return sorted(self.entries)

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return reversed(sorted(self.entries))

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        # sugestão: validação de name vazio
        self.entries.pop(name)
        return 'Numero deletado'
