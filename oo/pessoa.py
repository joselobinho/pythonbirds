class Pessoa:
    def __init__(self,*filhos, nome=None,idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos=list(filhos)

    def comprimentar(self): # Metodo

        print('O nome da pessoa e: ',self.nome,self.idade)
        return(f'Ola Mundo {id(self)}')

if __name__ == '__main__':
    a=['Lobinho','Jose de Almeida']
    renzo = Pessoa(*a,nome='Renzo')
    luciano = Pessoa("Marcia", "marcia zigolis", nome='Renzo')
#    luciano=Pessoa(renzo, nome='luciana')

    print(renzo.filhos)
    print(luciano.filhos)
#    print(p.nome)
#    p.nome="Marcia Zigolis"
#    print(p.nome)
#    print(p.comprimentar())
#    print(id(p))
#    p.nome="Jose de Almeida Lobinho"
 #   print(p.nome)