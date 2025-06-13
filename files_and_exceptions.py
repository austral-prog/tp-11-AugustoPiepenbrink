def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada línea tiene el formato:
    producto:valor;producto:valor;...
    y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    ventas = {}
    try:
        with open(filename, 'r') as f:
            for linea in f:
                linea = linea.strip()
                if not linea:
                    continue  # saltear líneas en blanco
                items = linea.split(';')
                for item in items:
                    if not item:
                        continue
                    try:
                        producto, valor = item.split(':')
                        valor = float(valor)
                        if producto in ventas:
                            ventas[producto].append(valor)
                        else:
                            ventas[producto] = [valor]
                    except ValueError:
                        continue  # si el item está mal formado, lo salteamos
        return ventas
    except FileNotFoundError:
        raise FileNotFoundError(f"Archivo no encontrado: {filename}")
    

def process_dict(data):
    """Para cada producto, imprimir el total de ventas y el promedio.

    :param data: dict - diccionario a procesar.
    """
    for producto in data:
        montos = data[producto]
        total = sum(montos)
        promedio = total / len(montos)
        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
