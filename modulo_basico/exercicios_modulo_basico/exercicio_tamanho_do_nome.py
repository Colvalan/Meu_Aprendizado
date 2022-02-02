nome = input('Qual é o seu primeiro nome?: ')
tamanho = len(nome)

if not nome.isalpha():
    print('Não use numeros no seu nome!')
elif tamanho <= 4:
    print('Seu nome é bem curto hein!')
elif tamanho == 5 or tamanho == 6:
    print('Seu nome é de um tamanho normal!')
else:
    print('Seu nome é maior que o normal!')

"""
    Considerações Finais.
    
    Meu programa atingiu o mesmo resultado do programa do professor, porém no meu programa
pude tratar melhor os dados que foram inseridos pelo usuário.
    
    Isso previniu que o usuário digitasse um nome contendo números e fiz isso utilizando o comando
var.isalpha() que verifica se o valor da variável contém apenas caracteres alfabéticos.
    
    Caso o usuário tenha informado um nome contendo números, o programa informava "Não use numeros no seu nome!"
    
    O código do professor ficou muito similar ao meu e é o que segue:
    
 nome = input('Digite seu nome: ')
 tamanho = len(nome)

 if tamanho <= 4:
     print('Seu nome é curto.')
 elif tamanho <= 6:
     print('Seu nome é normal.')
 else:
     print('Seu nome é muito grande.')

"""