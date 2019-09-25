if __name__ == "__main__":
    with open("lista_labsschool_python.csv") as file:
        for line in file:
            nome, email = line.split(',')
            print(f"O endereço de e-mail de {nome} é {email.rstrip()}.")