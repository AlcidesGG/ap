import os

restaurantes = ['MDV','The Best']

def exibir_nome_do_programa():
 print("""Sabor MDV
""")
def exibir_opcoes():
 print('1. Cadastrar restaurante')
 print('2. Listar restaurante')
 print('3. Ativar restaurante')
 print('4. Sair')

def finaliza_app():
   exibir_subtitulo('Finalizar App')

def voltar_ao_menu_principal():
      input('\n Digite a tecla "Enter" para voltar ao menu principal')
      main()

def opcao_invalida():
      print('Opção inválida!\n')
      voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('clear') #os.system('clear')
    print(texto)
    print()

def cadastrar_novo_restaurante():
   exibir_subtitulo('Cadastro do novo restaurante:')
   nome_do_restaurante = input('Digite o nome do novo restaurante')
   restaurantes.append(nome_do_restaurante)
   print(f'O restaurante {nome_do_restaurante} foi cadastro com sucesso!')

def escolher_opcao():
 try:
   opcao_escolhida = int(input('Escolha uma opção: '))

   if opcao_escolhida == 1:
     print('Cadastrar restaurante')
   elif opcao_escolhida == 2:
     print('Listar restaurantes')
   elif opcao_escolhida == 3:
     print('Ativar restaurantes')
   elif opcao_escolhida == 4:
      finaliza_app()
   else:
       opcao_invalida()
 except:
       opcao_invalida()

def main():
       os.system('clear')
       exibir_nome_do_programa()
       exibir_opcoes()
       escolher_opcao()

       if __name__ == '__main__':
           main()