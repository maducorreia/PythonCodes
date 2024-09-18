peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em m: "))
imc = peso / (altura * altura)
if imc <= 18.5:
    print("Você está abaixo do peso")
elif 18.6 <= imc <= 24.9:
    print("Você está no peso ideal. Parabéns!")
elif 25.0 <= imc <= 29.9:
    print("Você está um pouco acima do peso")
elif 30.0 <= imc <= 34.9:
    print("Você está com Obesidade grau 1")
elif 35.0 <= imc <= 39.9:
    print("Você está com Obesidade grau 2")
elif imc >= 40:
    print("Você está com Obesidade grau 3")
