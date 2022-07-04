import hashlib
import scrypt
import hmac

SALT_BYTES = 128
BUF_LEN = 64

# Sequencia de bytes definidos manualmente para que as Keys sejam as mesmas com os mesmos inputs
SALT = b'S\\\xe9\x13z\x97K\xaa\xad\x1b\x05d\xf8\xd3\xfa\xce\x18\x16E\x96\ns\xc1\x18\x97\xb7Ny\xf9tx\x92\x7f\x81+I\x04xj\x8e\x8d\xf8P\xc5\x96%\x157\xae\xc5\xa0\xbf\n\xec\x11c\xb2\xa6\xc2&\x08\x86\x01^J\x16\x1c\xd8K\nVL\x9f\xc6\xa0\x99\xa7\x03\xeai\x9f\xac\x88\x9f\xab\xd6\xd0\x93M\xce5\x17\x16\xc5t\x0cu\x97\xfa\xbf\xa9\x11t8\xbc\xdfx\xe3T\x88\xa4\x0eB\xa5\xff\x13B\xd2S\xfe.\x1b\xbb\xbfP\xb8\x7fQ'


# Três inputs necessários
def passGen(fullName, personalPassword, siteDomain):
    password = fullName + personalPassword

# userKey é definido a partir do nome completo e a senha pessoal
    userKey = scrypt.hash(
        password=password, salt=SALT, buflen=BUF_LEN)

# Por fim, gera-se siteKey
    siteDomain = siteDomain.encode()
    siteKey = hmac.new(userKey, siteDomain, hashlib.sha256).hexdigest().upper()

    return siteKey

# Ainda é necessário passar siteKey por um encriptador que, baseado em um template,
# gere senhas seguras, com numeros, letras maiusculas e minusculas e caracteres especiais
