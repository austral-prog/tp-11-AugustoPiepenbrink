def read_file_to_dict(filename):
    """Lee un archivo de ventas donde cada venta es producto:valor_de_venta;... y agrupa los valores por producto en una lista.

    :param filename: str - nombre del archivo a leer.
    :return: dict - diccionario con listas de montos por producto.
    :raises: FileNotFoundError - si el archivo no existe.
    """
    ventas = {}
    try:
        with open(filename, 'r') as f:
            linea = f.readline().strip()
            if not linea:
                return ventas

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
                    continue  # Si hay un item mal formado, lo salteamos
        return ventas
    except FileNotFoundError:
        raise FileNotFoundError(f"Archivo no encontrado: {filename}")

def process_dict(data):
    """Para cada producto, imprime el total de ventas y el promedio, en el orden natural del diccionario.

    :param data: dict - diccionario a procesar.
    :return: None
    """
    for producto in data:
        montos = data[producto]
        total = sum(montos)
