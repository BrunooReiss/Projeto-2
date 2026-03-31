import random
import datetime

def menu():
    nome_arquivo = 'log.txt'
    while True:
        print('Monitor LogPy')
        print('1 - Gerar logs')
        print('2 - Analisar logs')
        print('3 - Gerar e Analisar logs')
        print('4 - sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            try:
                qtd = int(input('Quantidade de logs: '))
                gerarArquivo(nome_arquivo, qtd)
            except:
                print('Quantidade Incorreta')
        elif opcao == '2':
            analisarLog(nome_arquivo)
        elif opcao == '3':
            try:
                qtd = int(input('Quantidade de logs: '))
                gerarArquivo(nome_arquivo, qtd)
                analisarLog(nome_arquivo)
            except:
                print('qtd_incorreta')
        elif opcao == '4':
            print('Até mais')
            break
        else:
            print('Opção errada!!')

def gerarArquivo(nome_arquivo, qtd):
    with open(nome_arquivo, 'w', encoding='UTF-8') as arq:
        for i in range(qtd):
            arq.write(montarLog(i) + '\n')
        print('Logs Gerados')

def montarLog(i):
    data = gerarDataHora(i)
    ip = gerarIp(i)
    recurso = gerarRecurso(i)
    metodo = gerarMetodo(i)
    status = gerarStatus(i)
    tempo = gerarTempo(i)
    agente = gerarAgente(i)
    return f'[{data}] {ip} - {metodo} - {status} - {recurso} - {tempo}ms - 500mb - HTTP/1.1 - {agente} - /home'

def gerarDataHora(i):
    base = datetime.datetime(2026, 3, 30, 22,8,0)
    #ano,mes,dia,hora,minuto,segundo
    data = datetime.timedelta(seconds=i * random.randint(5,20))
    return (base + data).strftime('%d/%m/%Y %H:%M:%S')

def gerarIp(i):
    r = random.randint(1, 6)
    # r = random

    if i >= 20 and i <= 30:
        return '200.0.111.345'
    elif r == 1:
        return '192.168.5.6'
    elif r == 2:
        return '192.168.5.8'
    elif r == 3:
        return '192.168.5.9'
    elif r == 4:
        return '192.168.25.8'
    elif r == 5:
        return '192.168.45.8'
    else:
        return '192.168.65.68'
    

