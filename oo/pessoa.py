class Pessoa:
    def comprimentar(self):
        return(f'Ola Mundo {id(self)}')

if __name__ == '__main__':
    p=Pessoa()
    print(p.comprimentar())
    print(id(p))