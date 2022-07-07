class MeuErroPersonalizado(Exception):

    def __init__(self, message) -> None:
        super().__init__(message)
        self.error_type = 'Esse e meu erro'
        self.message = message
