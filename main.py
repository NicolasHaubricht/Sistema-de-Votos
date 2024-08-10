# Biblioteca Datetime
from datetime import datetime

# Função que indica a Soma dos Candidatos
def somaDosCanditados (hugo, ze, luiz):
    print(f'Votos totais do Canditado Huguinho: {len(hugo)}')
    print(f'Votos totais do Canditado Zezinho: {len(ze)}')
    print(f'Votos totais do Canditado Luizinho: {len(luiz)}')

# Função que Informa o Vencedor
def informarVencedor(hugo, ze, luiz, quantidadeVotos):
    if len(hugo) > len(ze) and len(hugo) > len(luiz):
        print(f'O vencedor foi o candidato Huguinho com uma porcentagem de {(len(hugo) / quantidadeVotos) * 100:.2f}% ')

    elif len(ze) > len(hugo) and len(ze) > len(luiz):
        print(f'O vencedor foi o candidato Zezinho com uma porcentagem de {(len(ze) / quantidadeVotos) * 100:.2f}%')

    elif len(luiz) > len(hugo) and len(luiz) > len(ze):
        print(f'O vencedor foi o candidato Luizinho com uma porcentagem de {(len(luiz) / quantidadeVotos) * 100:.2f}%')

    elif len(luiz) == len(hugo) or len(luiz) == len(ze) or len(hugo) == len(ze):
        print(f'Acontecerá Segundo Turno')
    else:
        print(f'Não houve vencedor')

# Função que Informa a Quantidade de Votos Invalidos
def quantidadeVotosInvalidos (votosInvalidos):
    print(f'Quantidade Votos Invalidos: {votosInvalidos}')

# Função que Informa a Quantidade de Votos Nulos
def quantidadeVotosNulos (nulo):
    print(f'Votos totais Nulo: {len(nulo)}')

# Listas
hugo = []
ze = []
luiz = []
nulo = []

# Variaveis
continuar = 'Sim'
quantidadeVotos = 0
votosInvalidos = 0

# Programa Principal
while continuar == 'Sim':
        # Menu de Opções
        opcao = str(input('''
            H - Votar em Huguinho
            Z - Votar em Zezinho
            L - Votar em Luizinho
            
            N - Votar NULO
            
            S - Encerrar votação
            
            VOTO: ''')).upper()

        # Horario que o voto foi computado
        horario = datetime.now().strftime("%H:%M:%S")
        
        # Case
        match opcao:
            case 'H':
                hugo.append(1)
                print(f'Voto Computado / Horário: {horario}')
            case 'Z':
                ze.append(1)
                print(f'Voto Computado / Horário: {horario}')
            case 'L':
                luiz.append(1)
                print(f'Voto Computado / Horário: {horario}')
            case 'N':
                nulo.append(1)
                print(f'Voto Computado / Horário: {horario}')
            case 'S':
                continuar = "parar"

                # Exibir Resultado
                somaDosCanditados(hugo, ze, luiz)
                informarVencedor(hugo, ze, luiz, quantidadeVotos)
                quantidadeVotosInvalidos(votosInvalidos)
                quantidadeVotosNulos(nulo)
            case _:
                print('Digite Uma Opção Válida')
                votosInvalidos += 1
                quantidadeVotos -= 1
                
        quantidadeVotos += 1