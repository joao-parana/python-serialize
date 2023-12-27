import hashlib
import hmac
import pickle
import secrets
from collections.abc import Callable
from typing import Union

import plus

# A função create_signature usa a chave e a mensagem fornecidas para criar
# uma assinatura HMAC usando SHA256. A função verify_signature usa a mesma
# chave e mensagem, junto com a assinatura original, para verificar se a
# assinatura é válida.
#
# Note que a chave deve ser um bytes ou bytearray e a mensagem deve ser bytes.
# Se você estiver trabalhando com strings, você pode convertê-las para bytes
# usando o método encode(), por exemplo, str.encode('utf-8').
#
# É importante lembrar que a segurança da assinatura HMAC depende da segurança
# da chave usada. Portanto, certifique-se de usar uma chave segura e mantê-la
# segura.


def create_signature(key, message):
    """Create a HMAC signature for a message."""
    return hmac.new(key, message, hashlib.sha256).digest()


def verify_signature(key, message, signature):
    """Verify a HMAC signature for a message."""
    return hmac.compare_digest(signature, create_signature(key, message))


def main(key: bytes):
    function_raw: bytes = pickle.dumps(plus.create_plus)
    func_signature: bytes = create_signature(key, function_raw)
    func: Callable[[int | float]] = pickle.loads(function_raw)  # noqa S301
    func_bytes = pickle.dumps(func)
    print(  # noqa T201
        "verify_signature =", verify_signature(key, func_bytes, func_signature)
    )
    print(function_raw)  # noqa T201
    print(func)  # noqa T201
    print(f"{func(3) = }")  # noqa T201
    print(f"{func(3)(2) = }")  # noqa T201


if __name__ == "__main__":
    # Generate a random 256-bit key
    key: bytes = secrets.token_bytes(32)
    main(key)
