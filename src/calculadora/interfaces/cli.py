from pathlib import Path
from typing import Annotated

import typer

from calculadora.adaptadores.json_adapter import JSONAdapter, MatrizInvalidaError
from calculadora.aplicacion import Aplicacion

app = typer.Typer(help="Calculadora de matrices con entrada JSON")


@app.command()
def calcular(
    operacion: Annotated[
        str,
        typer.Argument(help="Operación: suma, multiplicacion, determinante o inversa"),
    ],
    archivo: Annotated[
        Path,
        typer.Argument(
            help="Ruta del archivo JSON",
            exists=True,
            dir_okay=False,
            readable=True,
        ),
    ],
) -> None:
    """Ejecuta una operación usando las matrices de un archivo JSON."""
    adaptador = JSONAdapter()
    aplicacion = Aplicacion()

    try:
        texto_json = archivo.read_text(encoding="utf-8")
        entrada = adaptador.deserializar_entrada(texto_json)

        if "matrixB" not in entrada:
            raise MatrizInvalidaError("La entrada debe contener 'matrixA' y 'matrixB'")

        matrices = [entrada["matrixA"], entrada["matrixB"]]

        resultado = aplicacion.ejecutar(operacion, matrices)
        typer.echo(adaptador.serializar_resultado(resultado))

    except (MatrizInvalidaError, ValueError, IndexError, OSError) as error:
        typer.echo(f"Error: {error}", err=True)
        raise typer.Exit(code=1) from error
