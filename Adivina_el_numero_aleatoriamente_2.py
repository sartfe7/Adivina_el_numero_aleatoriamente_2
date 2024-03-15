import random

def adivinar_numero():
    numero_a_adivinar = random.randint(10, 20)
    intentos_restantes = 3

    print("Bienvenido al juego de adivinanza de números entre 10 y 20.")
    print("Tienes 3 intentos para adivinar el número secreto.")

    while intentos_restantes > 0:
        intento = int(input("Ingresa tu número: "))
        
        if intento == numero_a_adivinar:
            print("¡Felicidades! ¡Has adivinado el número secreto!")
            return
        elif intento < numero_a_adivinar:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")
        
        intentos_restantes -= 1
        print(f"Te quedan {intentos_restantes} intentos.")

    print("Lo siento, has agotado tus intentos. El número secreto era:", numero_a_adivinar)

if __name__ == "__main__":
    adivinar_numero()


