
from meu_erro import MeuErroPersonalizado


def error_handler_method(error):
    if isinstance(error, MeuErroPersonalizado):
        print("TRatar meu erro personalizado")
        return
    if isinstance(error, ZeroDivisionError):
        print("TRatar dividindo por zero")
        return
    if isinstance(error, ZeroDivisionError):
        print("Tratar caso geral ")
        return
