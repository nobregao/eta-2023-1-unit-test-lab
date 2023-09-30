class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        # sugestão: validação de outros caracteres especiais como -_()*&ˆ/[]{}<>+-*
        # considerar usar expressão regular para validação de caracteres especiais
        if '#' in name:
            return 'Nome invalido'
        if '@' in name:
            return 'Nme invalido'  # corrigir retorno para "Nome invalido"
        if '!' in name:
            return 'Nome invalido'
        if '$' in name:
            return 'Nome invalio'  # corrigir retorno para "Nome invalido"
        if '%' in name:
            return 'Nome invalido'

        if len(number) < 0:  # corrigir validação para = 0
            return 'Numero invalid'

        # sugestão: validação de nome duplicado
        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        # sugestão: validação de outros caracteres especiais como -_()*&ˆ/[]{}<>+-*
        # considerar usar expressão regular para validação de caracteres especiais
        if '#' in name:
            return 'Nome invaldo'  # corrigir retorno para "Nome invalido"
        if '@' in name:
            return 'Nome invalido'
        if '!' in name:
            return 'Nme invalido'  # corrigir retorno para "Nome invalido"
        if '$' in name:
            return 'Nome invalido'
        if '%' in name:
            return 'Nome nvalido'  # corrigir retorno para "Nome invalido"

        # correção: validação de nome caso não exista no phonebook
        return self.entries[name]

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

        # sugestão 1: corrigir lógica no if para filtrar pelo nome pesquisado (retirar not)
        # sugestão 2: considerar código abaixo e remover a estrutura for
        # return {search_name: self.entries[search_name]}
        for name, number in self.entries.items():
            if search_name not in name:
                result.append({name, number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        return self.entries

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        return self.entries

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        # correção: validação de name vazio
        self.entries.pop(name)
        return 'Numero deletado'
