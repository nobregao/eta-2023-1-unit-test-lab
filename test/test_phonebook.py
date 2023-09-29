from src.phonebook import Phonebook

class TestPhonebook:

    def test_add_sucesso(self):
        phonebook = Phonebook()
        assert phonebook.add("sarita", "888888") == "Numero adicionado"
        assert phonebook.add("renatão", "777777") == "Numero adicionado"
        assert phonebook.add("raquel", "999999") == "Numero adicionado"

    def test_add_numero_vazio(self):
        phonebook = Phonebook()
        assert phonebook.add("sarita", "") == "Numero invalido"

    def test_add_nome_vazio(self):
        phonebook = Phonebook()
        assert phonebook.add("", "999999") == "Nome invalido"

    def test_add_nome_caractere_especial(self):
        phonebook = Phonebook()
        assert phonebook.add("renatão#", "999999") == "Nome invalido"
        assert phonebook.add("rena@tão", "999999") == "Nome invalido"
        assert phonebook.add("!renatão", "999999") == "Nome invalido"
        assert phonebook.add("rena$tão", "999999") == "Nome invalido"
        assert phonebook.add("renatão%", "999999") == "Nome invalido"

    def test_lookup_retornar_nome_e_numero(self):
        phonebook = Phonebook()
        phonebook.add("sarita", "999999")

        assert phonebook.lookup("sarita") == {"sarita": "999999"}

    def test_lookup_retornar_nome_e_numero(self):
        phonebook = Phonebook()
        assert phonebook.lookup("sarita") == "Nome "
