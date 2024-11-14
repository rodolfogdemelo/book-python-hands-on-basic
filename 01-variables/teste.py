class Aluno():
    def __init__(self, nome, curso):
        self.nome = nome
        self.curso = curso


code = input('Type your code')

match code:
    case 'bills':
        print('Bills code')
    case 'sales':
        print('Sales code')
    case default:
        print('Wrong selection')