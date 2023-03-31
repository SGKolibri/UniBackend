"""
Script responsável por fazer as requisições.

Aviso: antes de executar esse código, certifique que 'main.py' esteja rodando em outro terminal.

"""

import requests
# Atualize BASE com a url correta caso a mesma se altere quando 'main.py' for executada.
BASE = "http://127.0.0.1:5000/"

# Exemplo de como criar um novo personagem.
"""
 'data' é uma array que armazena os objetos (personagens).
 Todos argumentos/parâmentros são obrigatórios.
"""
data = [
    {
    # Define o nome do personagem (limite: 50 caracteres).
    "name":"Batman",
    # Define a descrição do personagem (limite: 100 caracteres).
    "description":"Super-herói de Gotham City",
    # Define o link da imagem do personagem (limite: 200 caracteres).
    "image_link":"https://t.ctcdn.com.br/Bhc_yILZ7vL4OL5F2CVRclZydwg=/720x405/smart/filters:format(webp)/i567711.jpeg",
    # Define o programa do personagem (limite: 50 caracteres).
    "program":"Liga da Justiça",
    # Define o animador do personagem (limite: 50 caracteres).     
    "animator":"WarnerBros."
    }
    ]

"""
Para fazer requisições: requests.ação(BASE+ "character/id")
ações são: put(), get(), patch(), delete()

Exemplos a seguir.

"""
# Para adicionar o personagem de data para a database: 'request.put()'
# Nesse caso, adicionamos data[0], personagem Batman, à database.
print("Put é chamado e o personagem é adicionado à database:")
response = requests.put(BASE + "characters/0", data[0])
print(response.json())
# Pressione Enter no terminal para prosseguir.
input()


# Para atualizar um parâmetro de um personagem: requests.patch(BASE + "character/id", {"arg":"new_arg"})
print("Patch é chamado e o personagem é atualizado:\n",
      "Nesse exemplo, name do personagem é mudado para 'Cavaleiro das Trevas'.")
response = requests.patch(BASE + "characters/0", {"name":"Cavaleiro das Trevas"})
input()


# Para visualizar um personagem já existente da db: requests.get(BASE + "character/id")
print("Get é chamado para verificar se o personagem foi atualizado:")
response = requests.get(BASE + "characters/0")
print(response.json())
print("Atualizado com sucesso. :)")

input()


# Para deletar um personagem já existente da db: requests.delete(BASE + "character/id")
print("Delete é chamado e o personagem é deletado da database, response 204:")
response = requests.delete(BASE + "characters/0")
print(response)

input()


# Para verificar se character de id 0 foi deletado:
print("Chama o personagem para confirmar se ele foi deletado:")
response = requests.get(BASE + "characters/0")
print(response.json())
print("Deletado com sucesso. :)")

"""
    Adicionar diversos personagens à database de uma só vez também é possível,
    basta adicionar novos personagens ao array 'data' e executar um loop com
    a função put() para adicioná-los.
    Exemplo:

    for i in range(len(data)):
        response = requests.put(BASE + "characters/"+str(i), data[i])
        print(response.json())

"""