## WindowsApp File
## This file is used to implement code used to run scripts for Windows

from exception import Exceptions
from windows import FileSystem

def Main():
   # Obtém o primeiro número
   print("=" * 80)
   print(">> ENTRADA DO USUÁRIO <<")
   print("=" * 80)
   N1 = int(input("Insira o primeiro número: "))
   print("=" * 80)
   print("\n")


   # Obtém o segundo número

   # Informa o usuário sobre as operações disponíveis
   print("=" * 80)
   print("Operações disponíveis")
   print("=" * 80)
   print(">> [+]: Soma")
   print(">> [-]: Subrtração")
   print(">> [*]: Multiplicação")
   print(">> [/]: Divisão")

   # Obtém a operação
   print("=" * 80)
   print(">> ENTRADA DO USUÁRIO <<")
   print("=" * 80)
   Result = str(input("Insira uma operação: "))
   print("=" * 80)
   print("\n")

   # Obtém o segundo número
   print("=" * 80)
   print(">> ENTRADA DO USUÁRIO <<")
   print("=" * 80)
   N2 = int(input("Insira o segundo número: "))
   print("=" * 80)

   # Executa o código condizente com a operação escolhida pelo usuário
   if Result == "+":
       Result = N1 + N2
   elif Result == "-":
       Result = N1 - N2
   elif Result == "*":
       Result = N1 * N2
   elif Result == "/":
       Result = N1 / N2
   else:
       Result = "Indisponível"
       print("Não foi possível realizar o cálculo. Verifique a operação.")

   # Imprime o resultado
   print("[Resultado]:", Result)
   print("=" * 80)


Main()
