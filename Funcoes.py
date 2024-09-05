import os

cliente_arquivo = 'Cliente_NoBank.txt'


def cabecalho():
    os.system('cls')
    print('*' * 40)
    print('\nＮｏＢａｎｋ\n')
    print('''Alunos: Eric Amorim; Rafael Almirante Lass
        ''')
    print('*' * 40)
    print()

    print('1. Cadastrar Dados')
    print('2. Listar Dados')
    print('3. Alterar Dados')
    print('4. Excluir Dados')
    print('5. Realizar Backup do Arquivo')
    print('0. Sair')

def voltar_ao_menu():
    input('\n\n\nPressione Enter para retornar ao menu')
    main()

def exibir_subtitulo(titulo):
    os.system('cls')
    print('*' * (len(titulo) + 14))
    print(' ',titulo, '\n')
    print('*' * (len(titulo) + 14))

def exibir_estado_civil(estado):
    '''
    Função responsável por imprimir o estado civil em string
    '''
    if  estado == 1:
        return 'Solteiro'
    if  estado == 2:
        return 'Casado'
    if  estado == 3:
        return 'Separado'
    if  estado == 4:
        return 'Solteiro'
    else:
        return 'Viúvo'

def arquivo_nao_encontrado():
    os.system('cls')
    # Capturar o erro caso o arquivo 'Cliente_NoBank.txt' não seja encontrado
    print("Arquivo de dados não encontrado.") 
    voltar_ao_menu()
    
    
    

def cadastro_cliente():
    '''
    Esta função é responsável por cadastrar e adiconar os dados do cliente no arquivo 'cliente_NoBank.txt' 
    '''
    exibir_subtitulo('Cadastro de dados') #Subtítulo da função imprimida no codigo
    cliente = {} #Variável de um Dicionário
    try:
        cliente['codigo'] = int(input('Digite o código: '))
        cliente['nome'] = input('Digite o nome: ')
        cliente['endereco'] = input('Digite o Endereço: ')
        cliente['bairro'] = input('Digite o bairro: ')
        cliente['cidade'] = input('Digite a  cidade: ')
        cliente['telefone'] = int(input('Digite o  telefone: '))
        cliente['cep'] = int(input('Digite o CEP: '))
    except ValueError:#Erro ao digitar algum caractere não esperado, e retorna para o cadastro
        os.system('cls')
        print('\nAo digitar um número, escreva em Algarismo sem vírgulas e outros tipos de caracteres especiais') 
        input('''

Aperte o enter para retornar ao cadastro''')
        cadastro_cliente()
    except Exception as e:
        print(f'Ocorreu um erro ao cadastrar os clientes, tente novamente. {e}')
        voltar_ao_menu()

    while True:
            try:
                print('''
                Estado Civil:
                    1. Solteiro
                    2. Casado
                    3. Separado
                    4. Divorciado
                    5. Viúvo\n ''')
                cliente['estado_civil'] = int(input())
                if 1 <= cliente['estado_civil'] <= 5:
                    break
                else:
                    exibir_subtitulo('Cadastro de dados')
                    print("Por favor, digite um número de 1 a 5.")

            except ValueError:
                print("Entrada inválida. Digite um número inteiro.")
    cliente = f"{cliente['codigo']},{cliente['nome']},{cliente['endereco']},{cliente['bairro']},{cliente['cidade']},{cliente['telefone']},{cliente['cep']},{cliente['estado_civil']}\n" #Formatação dos dados do cliente em string
    with open(cliente_arquivo, 'a') as arquivo: #Criação do arquivo ou adição de dados na próxima linha
        arquivo.write(cliente) #cliente_arquivo como arquivo, escrevendo a variavel cliente que serve para transformar o dict em uma str
    os.system('cls')
    print('Cliente cadastrado com Sucesso!')
    voltar_ao_menu()
    return
        
def listar_cliente():
    '''
    Função responsável por exibir todos os clientes cadastrados no NoBank
    '''
    try:
        with open(cliente_arquivo, 'r') as arquivo: #abrindo o arquivo em modo leitura
            linhas = arquivo.readlines() #Lê todas as linhas do arquivo
            if not linhas: #Caso não tenha linha, exibe mensagem e volta ao menu
                exibir_subtitulo('Nenhum cliente cadastrado')
                voltar_ao_menu()
                return
            else:
                exibir_subtitulo('Dados dos cliente da ＮｏＢａｎｋ')
                t1 = 'Código:'
                t2 = 'Nome:'
                t3 = 'Endereço:'
                t4 = 'Bairro:'
                t5 = 'Cidade:'
                t6 = 'Telefone:'
                t7 = 'CEP'
                t8 = 'Estado Civil:'
                print(f'{t1.ljust(7)} | {t2.ljust(15)} | {t3.ljust(30)} | {t4.ljust(20)} | {t5.ljust(15)} | {t6.ljust(11)} | {t7.ljust(9)} | {t8.ljust(10)} ') #titulo dos dados formatados
                for linha in linhas:
                    dados = linha.strip().split(',')
                    codigo_cliente = int(dados[0])
                    nome_cliente = dados[1]
                    endereco_cliente = dados[2]
                    bairro_cliente = dados[3]
                    cidade_cliente = dados[4]
                    telefone_cliente = int(dados[5])
                    cep_cliente = int(dados[6])
                    estado_civil_cliente = int(dados[7])
                    codigo_str = str(codigo_cliente) #alterar int para str, para formartar no print
                    telefone_str = str(telefone_cliente)
                    cep_str = str(cep_cliente)
                    clientes = {'t1':codigo_str, 't2':nome_cliente, 't3':endereco_cliente, 't4':bairro_cliente, 't5':cidade_cliente, 't6':telefone_str, 't7':cep_str,'t8':exibir_estado_civil(estado_civil_cliente) } #Armazenei as variáveis em um dicionário

                    print(f'{clientes['t1'].ljust(7)} | {clientes['t2'].ljust(15)} | {clientes['t3'].ljust(30)} | {clientes['t4'].ljust(20)} | {clientes['t5'].ljust(15)} | {clientes['t6'].ljust(11)} | {clientes['t7'].ljust(9)} | {clientes['t8']}') #print dentro do loop para imprimir todos os clientes
                voltar_ao_menu()
                return
    except FileNotFoundError:
        arquivo_nao_encontrado()

    except Exception as e:
        print('Ocorreu um erro ao listar os clientes', e)

def alterar_dados():
    '''
    Função responsável por alterar os dados do cliente informado caso ele seja encontrado no arquivo
    
    '''
    exibir_subtitulo('Alterar Dados')
    try:
        with open(cliente_arquivo, 'r') as arquivo:  # Modo leitura
            linhas = arquivo.readlines()
            if not linhas:  # Caso não tenha linha exibe mensagem e volta ao menu
                exibir_subtitulo('Nenhum cliente cadastrado')
                voltar_ao_menu()
                return
            else:
                codigo_cliente = int(input('Digite o código do cliente que deseja alterar: '))
                encontrado = False
                novas_linhas = [] #armazena todas as linhas do arquivo
                
                for linha in linhas:
                    dados = linha.strip().split(',')  # Retira os espaços do começo e do final, e divide a linha por ','
                    if int(dados[0]) == codigo_cliente:
                        while True:
                            try:
                                novo_nome = input('Digite o novo nome do cliente: ')
                                novo_endereco = input('Digite o novo endereço: ')
                                novo_bairro = input('Digite o novo bairro: ')
                                nova_cidade = input('Digite a nova cidade: ')
                                novo_telefone = int(input('Digite o novo telefone: '))
                                novo_cep = int(input('digite o novo CEP'))
                                break
                            except ValueError:
                                os.system('cls')
                                print('Certifique-se que escreveu o número corretamente')
                                input('Aperte Enter para recomeçar')
                                
                        while True:
                                try:
                                    print('''
                                        Estado Civil:
                                            1. Solteiro
                                            2. Casado
                                            3. Separado
                                            4. Divorciado
                                            5. Viúvo\n ''')
                                    novo_estado_civil = int(input('Digite o novo estado civil: '))
                                    if 1<= novo_estado_civil <=5:
                                        break
                                    else:
                                        exibir_subtitulo('Cadastro de dados')
                                        print("Por favor, digite um número de 1 a 5.")
                                except ValueError:
                                    os.system('cls')
                                    print("Entrada inválida. Digite um número inteiro.")
                        telefone_str = str(novo_telefone)
                        cep_str = str(novo_cep)
                        
                        clientes = {'t1':codigo_cliente,'t2':novo_nome, 't3':novo_endereco, 't4':novo_bairro, 't5':nova_cidade, 't6':telefone_str, 't7':novo_cep, 't8':novo_estado_civil}
                        
                        linha = f'{clientes['t1']},{clientes['t2']},{clientes['t3']},{clientes['t4']},{clientes['t5']},{clientes['t6']}, {clientes['t7']},{clientes['t8']}\n'
                        os.system('cls')
                        print("Dados do cliente alterados com sucesso!")
                        encontrado = True
                                
                            
                    novas_linhas.append(linha) #adicona a nova string na linha correspondente da antiga
                
                if not encontrado:
                    os.system('cls')
                    print("Nenhum cliente encontrado com o código fornecido.")

        # Abrir o arquivo em modo de escrita após todas as alterações
        with open(cliente_arquivo, 'w') as arquivo:
            arquivo.writelines(novas_linhas) #escreve todas as linhas da lista 

    except ValueError:
        print('Certifique-se que escreveu o número corretamente')
    except FileNotFoundError:
        arquivo_nao_encontrado()
    except Exception as e:
        print(e)
    voltar_ao_menu()

def excluir_dados():
    exibir_subtitulo('Excluir Dados')
    try:
        with open(cliente_arquivo, 'r') as arquivo:  # Modo leitura
            linhas = arquivo.readlines()
            
            if not linhas:  # Caso não tenha linha exibe mensagem e volta ao menu
                exibir_subtitulo('Nenhum cliente cadastrado')
                voltar_ao_menu()
                return
            
            codigo_cliente = int(input('Digite o código do cliente que deseja excluir: '))
            encontrado = False
            novas_linhas = []
            
            for linha in linhas:
                dados = linha.strip().split(',')  # Retira os espaços do começo e do final, e divide a linha por ','
                
                if int(dados[0]) == codigo_cliente:
                    print(f'Cliente com código {codigo_cliente} excluído com sucesso!')
                    encontrado = True
                    continue  # Ignora a linha, excluindo ela.
                
                novas_linhas.append(linha)
            
            if not encontrado:
                print("Nenhum cliente encontrado com o código fornecido.")
            
        # Abrir o arquivo em modo de escrita após todas as alterações
        with open(cliente_arquivo, 'w') as arquivo: #Reescreve as linhas ignorando a que foi retirada
            arquivo.writelines(novas_linhas)

    except ValueError:
        print('Certifique-se que escreveu o número corretamente')
    except FileNotFoundError:
        arquivo_nao_encontrado()
    except Exception as e:
        print(e)
    voltar_ao_menu()

def Backup():
    '''
    Esta função é responsável por realizar o backup dos clientes
    '''
    try:
        with open(cliente_arquivo, 'r') as arquivo_origem: #Lê o arquivo
            with open('backup_clientes.txt', 'w') as arquivo_backup: #cria ou reescreve o arquivo 'backup'
                conteudo = arquivo_origem.read() #cria uma variavel que armazena os dados arquivo 'cliente'
                arquivo_backup.write(conteudo) #escreve o conteudo da variável no arquivo 'backup'
            
        
    except FileNotFoundError:
        arquivo_nao_encontrado()
    except Exception as e:
        print("Ocorreu um erro ao realizar o backup:", (e))
    
    os.system('cls')
    print("Backup do arquivo realizado com sucesso!")
    voltar_ao_menu()
    return
    

def opcoes():
    try:
        opcao_escolhida = int(input("\nDigite a opção desejada: "))
        if 0 <= opcao_escolhida <=5:
            match opcao_escolhida:
                case 1:
                    cadastro_cliente()
                case 2:
                    listar_cliente()
                case 3:
                    alterar_dados()
                case 4:
                    excluir_dados()
                case 5:
                    Backup()
                case 0:
                    print("Saindo")
                    
        else:
            os.system('cls')
            print('Digite um número entre 0 à 5')
            voltar_ao_menu()

        
    except ValueError:
        print('Digite em Algarismo de 0 à 5')
        voltar_ao_menu()


    except Exception as e:
        print(e)
        os.system('cls')
        voltar_ao_menu()


def main():
    cabecalho()
    opcoes()

