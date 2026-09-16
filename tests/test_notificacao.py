import pytest

from notificacao import Notificacao
from notificacao import NotificacaoEmail
from notificacao import NotificacaoSMS


def test_email():
    email = NotificacaoEmail(
        "cliente@email.com",
        "Olá, cliente!"
    )

    resultado = email.enviar()

    assert resultado == "E-mail enviado para cliente@email.com"


def test_sms():
    sms = NotificacaoSMS(
        "11999999999",
        "Olá!"
    )

    resultado = sms.enviar()

    assert resultado == "SMS enviado para 11999999999"


def test_exibir_dados():
    email = NotificacaoEmail(
        "cliente@email.com",
        "Olá!"
    )

    resultado = email.exibir_dados()

    assert resultado == ("cliente@email.com", "Olá!")


def test_notificacao_abstrata():
    with pytest.raises(TypeError):
        Notificacao(
            "cliente@email.com",
            "Olá!"
        )