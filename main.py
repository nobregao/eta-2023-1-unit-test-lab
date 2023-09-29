from src.phonebook import Phonebook

phonebook = Phonebook()

# TODO: estudar código phonebook
# TODO: escrever testes unitários para phonebook



phonebook.add("sarita", "888888") # passou
phonebook.add("renatão", "123456789") # passou
phonebook.add("raquel", "999999") # passou

# print(phonebook.add("renatão", "")) # passou CORRIGIR
# print(phonebook.add("", "123456789")) # passou CORRIGIR
# print(phonebook.add("renatão#", "123456789")) # passou
# print(phonebook.add("ren@atão", "123456789")) # passou CORRIGIR retorno
# print(phonebook.add("renatão!", "123456789")) # passou
# print(phonebook.add("renatão$", "123456789")) # passou CORRIGIR retorno
# print(phonebook.add("renatão%", "123456789")) # passou

# print(phonebook.add("renatão", "11111111"))
# print(phonebook.add("renatão", "22222222"))
# passou CORRIGIR validacão de duplicidade de nomes
# sugestão: validação de outros caracteres especiais como -_()*&ˆ/[]{}<>+-*


# print(phonebook.lookup("renatão")) # passou CORRIGIR retorno com numero

print(phonebook.lookup("raquel")) # não passou, erro quando nome não existe
# print(phonebook.lookup("")) # não passou, erro quando nome está vazio

# print(phonebook.lookup("renatão#")) # passou CORRIGIR retorno
# print(phonebook.lookup("renatão@")) # passou
# print(phonebook.lookup("renatão!")) # passou CORRIGIR retorno
# print(phonebook.lookup("renatão$")) # passou
# print(phonebook.lookup("renatão%")) # passou CORRIGIR retorno

# sugestão: validação de outros caracteres especiais como -_()*&ˆ/[]{}<>+-*

# print(phonebook.get_names()) # passou

# print(phonebook.get_numbers()) # passou

# print(phonebook.clear()) # passou

# print(phonebook.search("")) # passou CORRIGIR validação pra nome vazio
# print(phonebook.search("renatão")) # NÃO PASSOU, não retorna o numero do nome pesquisado

# print(phonebook.get_phonebook_sorted()) # NÃO PASSOU, não ordena por nome
# print(phonebook.get_phonebook_reverse()) # NÃO PASSOU, não está com ordem decrescente

# print(phonebook.delete("")) # não passou, deu erro
# print(phonebook.delete("ren")) # não passou, deu erro

# print(phonebook.delete("renatão")) # passou
