import random
from string import digits
from string import punctuation
from string import ascii_letters
from tkinter import END
from turtle import end_fill 


perg = str(input("Você precisa de uma senha? Sim ou Não? "))

if perg == 'Sim':
    entrada = int(input('Quantos caracteres você quer que sua senha contenha?'))
    symbols = ascii_letters + digits + punctuation
    secure_random = random.SystemRandom()
    password = "".join(secure_random.choice(symbols)
    for i in range(entrada))
    print("Sua senha é: ", password)
else:
    print('Obrigado por procurar nossos serviços, volte sempre!')
