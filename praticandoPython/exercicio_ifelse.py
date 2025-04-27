def exec1():
    '''Função para saber qual fruta vendeu mais'''
    quantidade_maca =  int(input('Digite a quant. de maças vendidas: '))
    quantidade_banana =  int(input('Digite a quant. de banana vendidas: '))

    if quantidade_banana > quantidade_maca:
        print('As bananas tiveram mais vendas')
    elif quantidade_maca > quantidade_banana:
        print('As maças tiveram mais vendas')
    else:
        print('Teve empate')
#exec1()
#-------------------------------------------------------------------------
def exec2():
    '''Função que soma os dias de um projeto'''
    tempo_ativA = int(input('Informe os dias para a atividade A: '))
    tempo_ativB = int(input('Informe os dias para a atividade B: '))
    tempo_ativC = int(input('Informe os dias para a atividade C: '))

    if tempo_ativA < 0 or tempo_ativB<0 or tempo_ativC<0:
        print('Erro> Os dias não podem ser negativos.')
    
    media = tempo_ativA + tempo_ativB + tempo_ativC
    print(f'O tempo total do projeto é {media} dias')

#exec2()
#-------------------------------------------------------------------------
def exec3():
    '''Função de monitoramento de temperatura'''
    temperatura = float(input('Digite a temperatura atual: '))
    if temperatura > 25:
        print('Alerta, Temperatura acima do limite permitido.')
    else:
        print('temperatura Ok')
#exec3()
#-------------------------------------------------------------------------
def exec4():
    '''Função que calcula IMC'''
    print('Calculo IMC\n')
    
    peso = float(input('Digite seu peso(kg): '))
    altura = float(input('Digite sua altura(m): '))
    
    mediaIMC = peso/(altura*2)
    print(f'Seu IMC é: {mediaIMC}\n')    
    
    if mediaIMC < 18.5:
        print('Você está abaixo do peso')
    elif mediaIMC < 25:
        print('Você está com peso normal')
    else:
        print('Você está acima do peso')    
     
#exec4()
#-------------------------------------------------------------------------
def exec5():
    '''Função para monitorar o orçamento'''
    limite = 3.000
    orcamento = float(input('Digite o total de despesas do mês (R$): '))
    
    if orcamento > limite:
        print('Atenção! Você ultrapassou o limite do orçamento.')
    else:
        print('Esta dentro do limite')
#exec5()
#-------------------------------------------------------------------------
def exec6():
    '''Função de liberação de acesso por hora'''
    hora_permitida_inicial = 8
    hora_permitida_final = 18

    hora_atual = int(input('Digite a hora atual (formato 24 horas): '))

    if hora_permitida_inicial <= hora_atual < hora_permitida_final:
        print('Acesso permitido')
    else:
        print('Acesso negado')

#exec6()
#-------------------------------------------------------------------------
def exec7():
    '''Calculo de media, 3 notas '''
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    nota3 = float(input('Digite a terceira nota: '))

    media = (nota1+nota2+nota3)/3
    print(f'Média: {media}')

    if media < 5:
        print('Reprovado')
    elif media < 7:
        print('Recuperação')
    else:
        print('Aprovado')
#exec7()
#-------------------------------------------------------------------------
def exec8():
    '''Calculo de pedagio'''
    dist_pedagio = float(input('Digite a distancia percorrida (em km): '))

    text= 'Valor do pedágio: R$ '

    if dist_pedagio < 100:
        text += '10,00'
    elif dist_pedagio < 200:
        text += '20,00'
    else:
        text += '30,00'
    
    print(text)

#exec8()
#-------------------------------------------------------------------------
def exec9():
    ''' Verifica se o numero é par ou impar'''
    numero_par_impar = int(input('Digite um numero inteiro: '))
    if numero_par_impar%2 == 0:
        print('O número é par.')
    else:
        print('O número é impar.')
                 
#exec9()
#-------------------------------------------------------------------------
def exec10():
    '''Verifica se o valor do emprestimo condiz com a renda mensal'''
    renda_mensal = float(input('Digite o valor da sua renda mensal: '))
    parcela_desejada = float(input('Digite o valor da parcela desejada: '))

    percentual_ideal = renda_mensal*0.3

    if renda_mensal > 2000 and parcela_desejada <= percentual_ideal:
        print('Emprestimo aprovado')
    elif renda_mensal <= 2000:
        print('Emprestimo reprovado: renda baixa')
    else:
        print("Emprestimo reprovado: parcela acima de 30% da renda")
      
#exec10()
