import pytest

from src.phonebook import Phonebook

class TestPhonebook:

    def test_add_sucesso(self):
        phonebook = Phonebook()
        assert phonebook.add("sarita", "888888") == "Numero adicionado"
        assert phonebook.add("renatão", "777777") == "Numero adicionado"
        assert phonebook.add("raquel", "999999") == "Numero adicionado"

    def test_add_nome_duplicado(self):
        phonebook = Phonebook()
        assert phonebook.add("sarita", "888888") == "Numero adicionado"
        assert phonebook.add("sarita", "888888") == "Nome ja adicionado"

    def test_add_numero_vazio(self):
        phonebook = Phonebook()
        assert phonebook.add("sarita", "") == "Numero invalido"

    def test_add_nome_vazio(self):
        phonebook = Phonebook()
        assert phonebook.add("", "999999") == "Nome invalido"

    @pytest.mark.parametrize("name, number, expected_result", [
        ("renatão!", "999999", "Nome invalido"),
        ("renatão@", "999999", "Nome invalido"),
        ("renatão#", "999999", "Nome invalido"),
        ("renatão$", "999999", "Nome invalido"),
        ("renatão%", "999999", "Nome invalido"),
        ("renatão¨", "999999", "Nome invalido"),
        ("renatão&", "999999", "Nome invalido"),
        ("renatão*", "999999", "Nome invalido"),
        ("renatão(", "999999", "Nome invalido"),
        ("renatão)", "999999", "Nome invalido"),
        ("renatão_", "999999", "Nome invalido"),
        ("renatão+", "999999", "Nome invalido"),
        ("renatão{", "999999", "Nome invalido"),
        ("renatão}", "999999", "Nome invalido"),
        ("renatão[", "999999", "Nome invalido"),
        ("renatão]", "999999", "Nome invalido"),
        ("renatão|", "999999", "Nome invalido"),
        ("renatão\\", "999999", "Nome invalido"),
        ("renatão:", "999999", "Nome invalido"),
        ("renatão;", "999999", "Nome invalido"),
        ("renatão\"", "999999", "Nome invalido"),
        ("renatão<", "999999", "Nome invalido"),
        ("renatão>", "999999", "Nome invalido"),
        ("renatão?", "999999", "Nome invalido"),
        ("renatão/", "999999", "Nome invalido")
    ])
    def test_add_nome_caractere_especial(self, name, number, expected_result):
        phonebook = Phonebook()
        assert phonebook.add(name, number) == expected_result

    def test_lookup_retornar_nome_e_numero(self):
        phonebook = Phonebook()
        phonebook.add("sarita", "999999")

        assert phonebook.lookup("sarita") == {"sarita": "999999"}

    def test_lookup_nome_nao_existe(self):
        phonebook = Phonebook()

        assert phonebook.lookup("sarita") == "Nome nao existe"

    def test_lookup_nome_vazio(self):
        phonebook = Phonebook()

        assert phonebook.lookup("") == "Nome invalido"

    @pytest.mark.parametrize("name, expected_result", [
        ("renatão!", "Nome invalido"),
        ("renatão@", "Nome invalido"),
        ("renatão#", "Nome invalido"),
        ("renatão$", "Nome invalido"),
        ("renatão%", "Nome invalido"),
        ("renatão¨", "Nome invalido"),
        ("renatão&", "Nome invalido"),
        ("renatão*", "Nome invalido"),
        ("renatão(", "Nome invalido"),
        ("renatão)", "Nome invalido"),
        ("renatão_", "Nome invalido"),
        ("renatão+", "Nome invalido"),
        ("renatão{", "Nome invalido"),
        ("renatão}", "Nome invalido"),
        ("renatão[", "Nome invalido"),
        ("renatão]", "Nome invalido"),
        ("renatão|", "Nome invalido"),
        ("renatão\\", "Nome invalido"),
        ("renatão:", "Nome invalido"),
        ("renatão;", "Nome invalido"),
        ("renatão\"", "Nome invalido"),
        ("renatão<", "Nome invalido"),
        ("renatão>", "Nome invalido"),
        ("renatão?", "Nome invalido"),
        ("renatão/", "Nome invalido")
    ])
    def test_lookup_nome_caractere_especial(self, name, expected_result):
        phonebook = Phonebook()
        assert phonebook.lookup(name) == expected_result

    def test_get_names(self):
        phonebook = Phonebook()
        phonebook.add("sarita", "888888")
        phonebook.add("renatão", "777777")
        phonebook.add("raquel", "999999")

        assert 'sarita' in phonebook.get_names()
        assert 'renatão' in phonebook.get_names()
        assert 'raquel' in phonebook.get_names()

    def test_get_numbers(self):
        phonebook = Phonebook()
        phonebook.add("sarita", "888888")
        phonebook.add("renatão", "777777")
        phonebook.add("raquel", "999999")

        assert '888888' in phonebook.get_numbers()
        assert '777777' in phonebook.get_numbers()
        assert '999999' in phonebook.get_numbers()

    def test_phonebook_esta_vazio(self):
        phonebook = Phonebook()
        phonebook.add("sarita", "888888")
        phonebook.add("renatão", "777777")
        phonebook.add("raquel", "999999")

        phonebook.clear()
        assert phonebook.clear() == "phonebook limpado"
        assert len(phonebook.entries) == 0

    def test_search(self):
        phonebook = Phonebook()
        phonebook.add("sarita", "888888")
        phonebook.add("renatão", "777777")
        phonebook.add("raquel", "999999")

        assert phonebook.search("sarita") == [{"sarita": "888888"}]

    def test_search_nome_nao_existe(self):
        phonebook = Phonebook()

        assert phonebook.search("sarita") == []

    def test_search_substrings_nome(self):
        phonebook = Phonebook()
        phonebook.add("sarita", "888888")
        phonebook.add("renatão", "777777")
        phonebook.add("raquel", "999999")

        expected_result = \
            [{'POLICIA': '190'},
             {'sarita': '888888'},
             {'renatão': '777777'},
             {'raquel': '999999'}]

        assert phonebook.search("a") == expected_result

    def test_get_phonebook_sorted(self):
        phonebook = Phonebook()
        phonebook.add("sarita", "888888")
        phonebook.add("renatão", "777777")
        phonebook.add("raquel", "999999")

        phonebook_sorted = phonebook.get_phonebook_sorted()

        assert list(phonebook_sorted) == ["POLICIA", "raquel", "renatão", "sarita"]

    def test_get_phonebook_reverse(self):
        phonebook = Phonebook()
        phonebook.add("sarita", "888888")
        phonebook.add("renatão", "777777")
        phonebook.add("raquel", "999999")

        phonebook_reverse_sorted = phonebook.get_phonebook_reverse()

        assert list(phonebook_reverse_sorted) == ["sarita", "renatão", "raquel", "POLICIA"]

    def test_delete(self):
        phonebook = Phonebook()
        phonebook.add("sarita", "888888")
        phonebook.add("renatão", "777777")
        phonebook.add("raquel", "999999")

        assert phonebook.delete("renatão") == "Numero deletado"
        assert "renatão" not in phonebook.entries

    def test_delete_nome_nao_existe(self):
        phonebook = Phonebook()

        assert phonebook.delete("renatão") == "Nome nao existe"

    @pytest.mark.parametrize("caractere, expected_result", [
        ("!", None),
        ("@", None),
        ("#", None),
        ("$", None),
        ("%", None),
        ("&", None),
        ("*", None),
        ("(", None),
        (")", None),
        ("_", None),
        ("+", None),
        ("-", None),
        ("=", None),
        ("{", None),
        ("}", None),
        ("[", None),
        ("]", None),
        ("|", None),
        ("\\", None),
        (":", None),
        (";", None),
        ("\"", None),
        ("'", None),
        ("<", None),
        (">", None),
        ("?", None),
        ("/", None),
        ("^", None),
        ("~", None),
        ("`", None)
    ])
    def test_valida_caracteres_especiais(self, caractere, expected_result):
        phonebook = Phonebook()
        assert phonebook.valida_caracteres_especiais(caractere)
