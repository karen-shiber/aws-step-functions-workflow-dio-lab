import json

def handler(event, context):
    """
    Função Lambda de exemplo usada no laboratório.
    - event: dados de entrada vindos da Step Function
    - retorna: resultado processado
    """
    if "input" not in event:
        return {
            "valido": False,
            "motivo": "Campo 'input' ausente"
        }

    dado = event["input"]

    # processamento fake
    resultado = dado.upper()

    return {
        "valido": True,
        "processado": resultado,
        "status": "OK"
    }

