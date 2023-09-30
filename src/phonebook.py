import re

class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    # MELHORIA: criamos a função para validar caracteres especiais usando expressão regular
    def valida_caracteres_especiais(self, valor):
        regex = r"^[a-zA-Z0-9áéíóúâêîôûãõàèìòùäëïöüçñÁÉÍÓÚÂÊÎÔÛÃÕÀÈÌÒÙÄËÏÖÜÇÑ]+$"
        return re.match(regex, valor) is None

    def add(self, name, number):
        CAMPO_VAZIO = 0
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado' or 'Nome ja adicionado'
        """
        # MELHORIA: trocamos os Ifs para usar apenas um onde valida o campo nome.
        # nome inválido caso esteja vazio ou contenha caracteres especiais
        # BUG: Corrigir retorno quando existiam mais de um If.
        if len(name) == CAMPO_VAZIO or self.valida_caracteres_especiais(name):
            return 'Nome invalido'

        # BUG: na validação de vazio para campo numero
        if len(number) == CAMPO_VAZIO:
            return 'Numero invalido'

        # MELHORIA: validação de nome duplicado
        if name in self.entries.keys():
            return 'Nome ja adicionado'

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    def lookup(self, name):
        CAMPO_VAZIO = 0
        """
        :param name: name of person in string
        :return: return number of person with name or 'Nome nao existe'
        """
        # MELHORIA: trocamos os Ifs para usar apenas um onde valida o campo nome.
        # nome inválido caso esteja vazio ou contenha caracteres especiais
        # BUG: Corrigir retorno quando existiam mais de um If.
        if len(name) == CAMPO_VAZIO or self.valida_caracteres_especiais(name):
            return 'Nome invalido'

        # MELHORIA: validação de nome caso não exista no phonebook
        if name not in self.entries.keys():
            return 'Nome nao existe'

        # BUG: corrigimos o retorno da função para retornar o nome com o número
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
        :return: return list with results of search or 'Nome nao existe'
        """
        result = []

        # sugestão 1: considerar código abaixo e remover a estrutura for
        # return {search_name: self.entries[search_name]}
        for name, number in self.entries.items():
            # BUG: corrigimos a validação do If para comparar com o name passado por parâmetro
            # MELHORIA: equiparamos os dois valores para caixa baixa para ajudar na pesquisa
            if search_name.lower() in name.lower():
                # BUG: corrigimos o objeto adicionado no array.
                result.append({name: self.entries[name]})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        # BUG: corrigimos ordenando o phonebook com a função sorted
        return sorted(self.entries)

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        # BUG: corrigimos ordenando o phonebook com a função sorted e ordenando de forma inversa com a função reversed
        return reversed(sorted(self.entries))

    def delete(self, name):
        CAMPO_VAZIO = 0
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado' or 'Nome invalido' or 'Nome nao existe'
        """
        # MELHORIA: validação de name vazio
        if len(name) == CAMPO_VAZIO:
            return 'Nome invalido'

        # MELHORIA: validação de name não exista no phonebook
        if name not in self.entries.keys():
            return 'Nome nao existe'

        self.entries.pop(name)
        return 'Numero deletado'
