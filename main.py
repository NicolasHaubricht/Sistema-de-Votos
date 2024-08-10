# Biblioteca Datetime
from datetime import datetime

# Função que indica a Soma dos Candidatos
def somaDosCanditados (canditato_1, canditato_2, canditato_3):
    print(f'Votos totais do Canditado 1: {len(canditato_1)}')
    print(f'Votos totais do Canditado 2: {len(canditato_2)}')
    print(f'Votos totais do Canditado 3: {len(canditato_3)}')

# Função que Informa o Vencedor
def informarVencedor(canditato_1, canditato_2, canditato_3, quantidadeVotos):
    if len(canditato_1) > len(canditato_2) and len(canditato_1) > len(canditato_3):
        print(f'O vencedor foi o Candidato 1 com uma porcentagem de {(len(canditato_1) / quantidadeVotos) * 100:.2f}% ')

    elif len(canditato_2) > len(canditato_1) and len(canditato_2) > len(canditato_3):
        print(f'O vencedor foi o Candidato 2 com uma porcentagem de {(len(canditato_2) / quantidadeVotos) * 100:.2f}%')

    elif len(canditato_3) > len(canditato_1) and len(canditato_3) > len(canditato_2):
        print(f'O vencedor foi o Candidato 3 com uma porcentagem de {(len(canditato_3) / quantidadeVotos) * 100:.2f}%')

    elif len(canditato_1) == len(canditato_2) or len(canditato_2) == len(canditato_3) or len(canditato_1) == len(canditato_3):
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
canditato_1 = []
canditato_2 = []
canditato_3 = []
nulo = []

# Variaveis
continuar = 'Sim'
quantidadeVotos = 0
votosInvalidos = 0

# Programa Principal
while continuar == 'Sim':
        # Menu de Opções
        opcao = int(input('''
            1 - Votar em Candidato 1
            2 - Votar em Candidato 2
            3 - Votar em Candidato 3
            
            0 - Votar NULO
            
            99 - Encerrar votação
            
            VOTO: '''))

        # Horario que o voto foi computado
        horario = datetime.now().strftime("%H:%M:%S")
        
        # Case
        match opcao:
            case 1:
                canditato_1.append(1)
                print(f'Voto Computado / Horário: {horario}')
            case 2:
                canditato_2.append(1)
                print(f'Voto Computado / Horário: {horario}')
            case 3:
                canditato_3.append(1)
                print(f'Voto Computado / Horário: {horario}')
            case 0:
                nulo.append(1)
                print(f'Voto Computado / Horário: {horario}')
            case 99:
                continuar = "parar"

                # Exibir Resultado
                somaDosCanditados(canditato_1, canditato_2, canditato_3)
                informarVencedor(canditato_1, canditato_2, canditato_3, quantidadeVotos)
                quantidadeVotosInvalidos(votosInvalidos)
                quantidadeVotosNulos(nulo)
            case _:
                print('Digite Uma Opção Válida')
                votosInvalidos += 1
                quantidadeVotos -= 1

        quantidadeVotos += 1