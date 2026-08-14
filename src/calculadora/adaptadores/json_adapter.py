import json


class MatrizInvalidaError(ValueError):
    """Error lanzado cuando un JSON no representa una matriz válida."""


class JSONAdapter:
    """Traduce entre representaciones JSON y las estructuras de datos internas
    que usan las operaciones de la calculadora (diccionarios con rows, cols y data).
    """

    def deserializar_matriz(self, texto_json: str) -> dict:
        """Convierte un string JSON en una matriz validada.

        Args:
            texto_json: Cadena de texto en formato JSON que representa una matriz.
                Debe tener las claves "rows", "cols" y "data".

        Returns:
            Diccionario con las claves "rows", "cols" y "data", listo para
            ser usado por las operaciones de la calculadora.

        Raises:
            MatrizInvalidaError: Si el texto no es JSON válido, si faltan
                claves requeridas, si los tipos no son los esperados, o si
                las dimensiones declaradas no coinciden con los datos.
        """
        try:
            matriz = json.loads(texto_json)
        except json.JSONDecodeError as error:
            raise MatrizInvalidaError(f"El texto no es JSON válido: {error}") from error

        self._validar_estructura(matriz)
        return matriz

    def serializar_resultado(self, resultado) -> str:
        """Convierte el resultado de una operación en un string JSON.

        Args:
            resultado: Resultado de una operación. Puede ser un diccionario
                con una matriz (rows, cols, data) o un valor numérico
                (por ejemplo, el determinante).

        Returns:
            Cadena de texto en formato JSON, con indentación legible.
        """
        return json.dumps(resultado, indent=2, ensure_ascii=False)

    def _validar_estructura(self, matriz) -> None:
        """Valida que un objeto tenga la estructura esperada de una matriz.

        Args:
            matriz: Objeto obtenido de deserializar el JSON de entrada.

        Raises:
            MatrizInvalidaError: Si la estructura no cumple lo esperado.
        """
        if not isinstance(matriz, dict):
            raise MatrizInvalidaError("La matriz debe ser un objeto JSON")

        claves_faltantes = {"rows", "cols", "data"} - matriz.keys()
        if claves_faltantes:
            raise MatrizInvalidaError(
                f"Faltan las claves requeridas: {', '.join(sorted(claves_faltantes))}"
            )

        rows, cols, data = matriz["rows"], matriz["cols"], matriz["data"]

        if not isinstance(rows, int) or not isinstance(cols, int):
            raise MatrizInvalidaError("'rows' y 'cols' deben ser números enteros")

        if rows <= 0 or cols <= 0:
            raise MatrizInvalidaError("'rows' y 'cols' deben ser mayores a cero")

        if not isinstance(data, list) or len(data) != rows:
            raise MatrizInvalidaError(f"'data' debe tener exactamente {rows} filas")

        for indice_fila, fila in enumerate(data):
            if not isinstance(fila, list) or len(fila) != cols:
                raise MatrizInvalidaError(
                    f"La fila {indice_fila} debe tener exactamente {cols} columnas"
                )
            for indice_col, valor in enumerate(fila):
                if not isinstance(valor, (int, float)) or isinstance(valor, bool):
                    raise MatrizInvalidaError(
                        f"El valor en ({indice_fila}, {indice_col}) debe ser numérico"
                    )
