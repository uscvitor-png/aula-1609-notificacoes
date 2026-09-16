from abc import ABC, abstractmethod


def registrar_envio(func):

    def wrapper(*args, **kwargs):
        print("Iniciando envio da notificação")

        resultado = func(*args, **kwargs)

        print("Envio finalizado")

        return resultado

    return wrapper


class Notificacao(ABC):

    def __init__(self, destinatario, mensagem):
        self.destinatario = destinatario
        self.mensagem = mensagem

    def exibir_dados(self):
        return self.destinatario, self.mensagem

    @abstractmethod
    def enviar(self):
        pass


class NotificacaoEmail(Notificacao):

    @registrar_envio
    def enviar(self):
        return f"E-mail enviado para {self.destinatario}"


class NotificacaoSMS(Notificacao):

    @registrar_envio
    def enviar(self):
        return f"SMS enviado para {self.destinatario}"
    