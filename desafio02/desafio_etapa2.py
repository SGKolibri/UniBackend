class Character:
    def __init__(self, nome, descricao, image_link, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.image_link = image_link
        self.programa = programa
        self.animador = animador

    def __str__(self):
        return f"Nome: {self.nome}. \nDescrição: {self.descricao}. \nImagem: {self.image_link}. \nPrograma: {self.programa}. \nAnimador: {self.animador}."

#Exemplo de uso
batman = Character("Batman", "Super-herói de Gotham City", "https://upload.wikimedia.org/wikipedia/pt/8/8d/Batman_por_Jim_Lee.jpg", "Liga da Justiça", "Warner Bros")
print(batman)
