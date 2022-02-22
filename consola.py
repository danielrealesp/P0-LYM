from parser import Tokenizer, Parser


def show_menu():
    HEADER = '*' * 10 + '\n MENU \n' + '*' * 10
    print(HEADER)
    print("1. Parsing Archivo Propio")
    print("2. Ejecutar Parsing de Prueba (Ejemplo Valido)")
    print("3. Ejecutar Parsing de Prueba (Ejemplo Invalido)")
    print("4. Salir")

def parse_file(ruta):
    with open(ruta) as f:
        program = f.read()
        print("\n PROGRAMA A ANALIZAR: \n")
        print(program)
        tokenizer = Tokenizer(program)
        tokens = tokenizer.tokenize()
        parser = Parser(tokens)
        parser.parse()

def main():
    executing = True
    while executing:
        show_menu()
        selection = int(input("Seleccione la opción que desea ejecutar: "))
        if selection == 1:
            ruta = input("Ingrese la ruta (relativa a este archivo) del archivo con el programa a verificar: ").strip()
            parse_file(ruta)

        elif selection == 2:
            ruta = './ejemplo_valido.txt'
            parse_file(ruta)

        elif selection == 3:
            ruta = './ejemplo_invalido.txt'
            parse_file(ruta)
        
        elif selection == 4:
            executing = False

if __name__ == "__main__":
    main()