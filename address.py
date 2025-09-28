import brazilcep
from brazilcep.exceptions import CEPNotFound, InvalidCEP

def address():
    # function to receive postal code.
    try:
        zip_code = input("cep ")
        data = brazilcep.get_address_from_cep(zip_code)
        print(data)
    except CEPNotFound:
        print(f"Cep não encontrado")
    except InvalidCEP:
        print("Cep inválido.")


address()
