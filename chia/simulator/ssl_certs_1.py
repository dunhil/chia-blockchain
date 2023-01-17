from __future__ import annotations

from typing import Dict, Tuple

SSL_TEST_PRIVATE_CA_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDKTCCAhGgAwIBAgIUZnoqyaLGQMl08azdwpafGGfEGR0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMB4XDTIyMDMyMzE3MjkyMFoXDTMyMDMy
MDE3MjkyMFowRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8G
A1UECwwYT3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEAmal1SzZpSVae9RShUcN1MjM/B8rJD47K0c49Uxj/YUD7
oGuSKWpYw/nM7aylODTqfJt660KN+Q5AeiZemKZ+YfbiQJ+1YUZazTcjoqOghXFl
E70KM6xyOiTr1SBSS1zf161BHPvTmbBQpkqsUStSZISBKaqU4lhJnBsllei8eFFN
mHEO+bgGQbTnjVWwHS+xgdajMiemK+Cql+pIpaoduTTtNyfwp9m2wF45EUT4DyUu
cU8En3NOOrarkPPG7x+FEANo0/UrqJwozY91Qsv6EPkhFUbBvF8l/p7uNCK0CIBK
yTOoPkeHvEeWX+LZlbICpdJQXIdiZJAqIu56yOPqAQIDAQABoxMwETAPBgNVHRMB
Af8EBTADAQH/MA0GCSqGSIb3DQEBCwUAA4IBAQBiRATAkJaW55BPdZ6TKMYfSFlJ
9lO3K0eS6miuX6HG7OI6DHCBf18fjDLxg7O/HeVxSgI5txB4iEulRBcv35veDti+
R6PuebE1+g0QTMlw0WXlRMg+6bVaV2XwXoWQhhSnDexdQtcDPKd4xC6VGfK3sPjQ
ZSriMmrerVhGL9d1pYBtxolDbk9e/AwrnWKLPUDrR8W5DA+yJ/lL+k5pPrACNR82
cljDU3YA+bE+9LpNtfatPZwceaM7GupXJy9lngwlNAM42XFvWsTjH8Uy7ZJFOi0B
+3rLUOIXxCdpb88qeUGBN6BAUMhItoflSktN813vgKkiV7I0gNoU3XnUqG7w
-----END CERTIFICATE-----
"""

SSL_TEST_PRIVATE_CA_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEAmal1SzZpSVae9RShUcN1MjM/B8rJD47K0c49Uxj/YUD7oGuS
KWpYw/nM7aylODTqfJt660KN+Q5AeiZemKZ+YfbiQJ+1YUZazTcjoqOghXFlE70K
M6xyOiTr1SBSS1zf161BHPvTmbBQpkqsUStSZISBKaqU4lhJnBsllei8eFFNmHEO
+bgGQbTnjVWwHS+xgdajMiemK+Cql+pIpaoduTTtNyfwp9m2wF45EUT4DyUucU8E
n3NOOrarkPPG7x+FEANo0/UrqJwozY91Qsv6EPkhFUbBvF8l/p7uNCK0CIBKyTOo
PkeHvEeWX+LZlbICpdJQXIdiZJAqIu56yOPqAQIDAQABAoIBABWbvuLUw/mMNM5C
GG1nDxQAINz3p06Ixfy7A+Srnz4N5VSpy+QHEHR+rFK/9Hvy9QaQ1rg+o7hiSK7k
tmjBAQTFswtjah5DxoEVP+2fFPOu/ofIDac2mNmUV5Wg9fGjHdc2hfGNeDQklzLL
TXAcp3l7KK6zTjyGLdPF/YMXN2mzzWa5Z/D66q9xXAIZnY0ggj4wJ2oOJvbq5Vec
1/NaXZcKZ6uS8a7AJ94133ItmxeBxJASgy+yF2T1YPOq0lK7OpU4qrG66iHAtB+z
LKao6dXiYZG5uuJ1j30Gk2V/QkT+NJSDnNcliK5pmmjUKHrDi8ow9m+dl7AjQTlj
CBw7AAECgYEAzH17mJR2/eO5MHGhz53QI+R9fcb7DiDT7o3M/rj8VK+sk5o5hqQn
D+5Ryy9H3UVTeXwDIayM23cpEmJFCBZ4cRnz+T11ZZ6P9RMIbfPxO6ooLFciHyHj
MGvOGdH14Mj9asBa8pSthlPNF9zHQ2OuoS4VBclPrmiQFGRfQBcq/FECgYEAwF5T
Rv7z0dttLMo2jaTCroorqD8FApGqK/hGol0PF6ozDXJqC77CBfocfoxK9VAg7Vn9
IRwWQFiIGdHpPuoN0bn4U75X43cUe7eodpck88Sy+KDwurWVPQ6ltO/hDcvxRqAs
rAfCAqG/lRx7Gx08Fmtim3KpRyiV0yvGTH4UlrECgYEAqgouHFJYIAacl4vl4Z54
1V/Keixb1wO1N0jyjV2FdWYfOx2jeDJHyReDLFHEkFp1by+P6xBwkI4luQO+I1uM
C4BpP3e7hySy0DdjawrOLa7weO57kSe8oycB2racnq6DC6Gn/s9i+6/ze0Q67e6V
57FKCeW8PGr2Y/6StdiOBgECgYEAoNo+qE7nccMZNyqfEzGB2JCQkM6hUdSbhsjD
x2ApDpCyv7u8ELYhZv4MdYS56QZnghCNKPJjaMqeg3iSoJj1lTj7/Ipc00bvScP4
ibE4pN0FCgEJShYsBDILPZCXjwHJblThBbg28hxuJjD6f2GirNx+R51JDsdRAJLJ
7Yw/iwECgYEAqNgShZvjTVsFz1hRKTPfJbhJZseqquN+xypJMZyoYJHNF5Urk5YE
ByHQAzAIcMYzsSvqGQbDK22UVP/I3aqcz9JAf1sl6pr+KGRPeIumVOPssKMIhP+x
ivPcyK9bCjrJiirx+TSiRy1698pdp+dDwFhcaHRBFf6FJgxwFHgM9Gw=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUT5GDbvyrLH9Vkb7sFWPi1uFfhnEwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC8vFVDrrbPlVphmwXld9chzAuCt6cUwFYBTxaIW01Ex5Ft
sJvGti6ve5BFx+B+wwA19Y1t6QOOnOn56x0Phm5/NqYidqYCBcrrHK28OH3kBhiO
NZiJi+tybGhxg2kjZldPBmoVA2r9MU1qA0PrRpozYi1mH8W2f/7yCstAHaYxZcjn
T70KkjWc7jMpV2g/6wLUaKJEgryQWqMr1Ru6BR2Q7IVIe688ptO53JRutPj/Fh6t
J9jWyF7b0EwoYc0Un2lRrzYgGQ0gGXGJCax3pWjZAokvVG5PQEPqK9TXqWVj/J+c
aA9jPEQcfivNW0nU8LmKHZyOaG/q39Y1wd9EhfOtAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAvyyCobTP0LbxqcCcNhY+3
/GPpUfYgjZdRy4uRtSLjcY3v604Azyuv07rMlT8qkvyYTuTzGXqpqVN1XJnllklH
psdkdA4uhlzx2ewhZw6usGV8QZEcOl6kMUeZK7TDMRkE10EnH2Qzg7R24coy9cEr
anGHgti6QrTK62aNT7aBGIDmteI3BRXc8Pb3BClDKLPpOC8DwRPD7nmQ/0awF3nN
B7caCwX4NCUuL1/Kbpz5Nt8wZepCcnXwF8BrSsiBFoUI01tGTm4BQVc1mufCmAlX
G8mCVW2JuymC6yia/bAUbvFhowbUrX55/z8SVEKQTLRQK2CglORjOTko0UbUcgN+
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAvLxVQ662z5VaYZsF5XfXIcwLgrenFMBWAU8WiFtNRMeRbbCb
xrYur3uQRcfgfsMANfWNbekDjpzp+esdD4ZufzamInamAgXK6xytvDh95AYYjjWY
iYvrcmxocYNpI2ZXTwZqFQNq/TFNagND60aaM2ItZh/Ftn/+8grLQB2mMWXI50+9
CpI1nO4zKVdoP+sC1GiiRIK8kFqjK9UbugUdkOyFSHuvPKbTudyUbrT4/xYerSfY
1she29BMKGHNFJ9pUa82IBkNIBlxiQmsd6Vo2QKJL1RuT0BD6ivU16llY/yfnGgP
YzxEHH4rzVtJ1PC5ih2cjmhv6t/WNcHfRIXzrQIDAQABAoIBAFnEbf2CJPs4u0M/
W5+Xz2AIz9S9ix+Il5+JwVrbqjWzgg0c+gqabjwS1j0KY1GHaBtCDqGfOYzkPzka
RbkzpGynTn+H1U+S97+55Txn1iDVcWp6PXH2deb3fvm2mhQ3QgGZOG2EMaf5giuR
IAXQj9kusg8nv38dA+KVlbSKJZjKUXVYrlpixfpzz9Z/CuhouRundF/yNBVbSnzR
v70ywjVGykf0YD6y5ZDW3BRAg7lRJ/fF1bK3L/sbLj4BugMs9gjt+cMRcusJdoP6
nWk5Z6Mo5VdZspb351EcpNs1AbTb40MaqNQuNg9jIgs9rZd5ZOMR0a77QufSMzML
qNFBQqECgYEA9AmL1/goSocUEUYRiioMrMkm0OA5/xwrpp8lcOYUVAhL2VD+lFNa
V4htxyUOuE1czQPXSmfioxQrbfHm0uxPMYUDWygdc/zyOlRbvMqmgimNFqRBiGh/
85NuYMSf6AOe7i+hwqZu/ZLDlzA7mEQG0csVLkPphe5HEBu0d5Wu1LUCgYEAxfzM
0xXeyocyuJblLOQxSfnwonG9d8F4hEO42lCEEDh8zVIk23vJ5E72YPwuiRU49Zrp
PoKiM9TjzsmnQIRany7BmNjtuhlvMirwIte0Helc0ks4IpzjymWSl12msOE4Jssl
6cy3xcX+E+JE8rVcrxDu2aAOiBC1fmLLQJlhNhkCgYAzbWuWCMrc4dh9x2lc132y
T/WpIQe31kTwqSsnvqTcDJ+HXYU41tP8DFkuFYYjmtIKtluBZ6EgQtjgI5FEM96A
jgpmBG8oiU62sh5fC8nJNl5wPg89YuBMAW7KX8VfDJxKj6kkLxTGxU4Ip3Z3oSZa
wdRl2pP00IETSPNgHCAq3QKBgFWw1cHirFvB6k0EWkp0tXSMLf9Q9S042n18hixP
Pul6WWHQVM1+JWKgXniZjVadjdqXYq5Agg2m7bZZhv8gicxtwzLxaOrsCTmQZgDe
lUGA+EC4d6JbfyfhkHHdAcF6qP/5Wv53MW7zA8X9X9QgdO38iTQ91yxC9xqtjcT2
3aE5AoGBAJ7clDveQugUC+OoXgru0emb3sXRk8kXDqUTjUlsjU1m4f3D8ZIx7+E6
4xVBExXHddMx9QYiJ5uVkcNB6UxhppqlsJPoKyj8dvDTYeC98Zm/TFl0B/P4iY8D
3w/REN/c8t2oYOpy8/0kgp2szliDeQDxqiijo9LeRRmxvTWYAJMI
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FULLNODE_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUBV+nxo/NCVdtZFyXlpmq8HplFQQwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDXf+htQ1YfVlp2jqHJ+EUmB6bhxE1tYl5i2VaZVanzjYgA
9LDKeRhvUnaOWvLkGQbyzqvnAylXHXSNe9KAZrphoxDP40Ogu4IEGatxkAKafJ0s
KKAB3QwJlnOm2NJNuH9vOirw66ihkpz6Ydg7hmdWCF7bJgG82qwzQvEtIABUxZeq
EMJHLuTlVC5fyuIyggzzU1h+ss3bleM6oqT54yxJPoZYmvy067jeLGiyPg95EP+s
nuxLFhzeW1OZHMGmniDvO0zKGr9chiXKUSgugtT3MHUndociVCmc2OQaqjmWKwGr
O0mU5+lMgP2SojC7wpItyHSfn62YTLQ5VduDd5+fAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBeYWzDc79lXdOi2iopi50n
Hoc+91TiUr9Ubbd8lHWhidHcRYYWo1vFwM3of3eJ4rhAKPgwx9aclkryUEcZ05U9
tzs5OrmYsgnzdoX+zJenx/7NwuMO7Oe+XBAd16/4vGgSU9vPge1Ny4zN+zA1vn2V
zVlSBuGzmJI1ugPOVK9e0XAzJNsG5/pPRB29mbWWrrmFBmHvf33+PJms19aSfKrV
lJXYQV4Q9/xt5ehTPo20HF2r2CDiEjhV+P9QVRnwymuE/Zap+e1v+N+iWJVUB9hR
il4RskorFB1oY+FcNvDlsfO2bl29hGX3nNBQ0o8k1fjvuLz55MUNyGTeeqBGKkU2
-----END CERTIFICATE-----
"""

SSL_TEST_FULLNODE_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEA13/obUNWH1Zado6hyfhFJgem4cRNbWJeYtlWmVWp842IAPSw
ynkYb1J2jlry5BkG8s6r5wMpVx10jXvSgGa6YaMQz+NDoLuCBBmrcZACmnydLCig
Ad0MCZZzptjSTbh/bzoq8OuooZKc+mHYO4ZnVghe2yYBvNqsM0LxLSAAVMWXqhDC
Ry7k5VQuX8riMoIM81NYfrLN25XjOqKk+eMsST6GWJr8tOu43ixosj4PeRD/rJ7s
SxYc3ltTmRzBpp4g7ztMyhq/XIYlylEoLoLU9zB1J3aHIlQpnNjkGqo5lisBqztJ
lOfpTID9kqIwu8KSLch0n5+tmEy0OVXbg3efnwIDAQABAoIBADq0WF+zcTmWL4yO
bFp1rHigqwBjlmgO3QF2jVW19Vconf0Mq0Bs3pAs2akL85DZlH/+duu2e8OEfaSx
L3XVBj7kygantVuK2O8/AuorvdnRyosmAfif+9B80MKJ3DhZ4zUsllgNCmIBa4v1
rY8BnRLdsuFmKCEHPNO2D7coOY7dyIc+MHF249nKyPYMjfeyKyALqF5EcQPL/2Kp
lSaR6dJoQyMo/f+IvF3r2UCfLMWWpK2MDuLpSvAISy+GF4OtL4wBZ+R3BG8p2dw2
tesFIVLfKYafpZiVQz6Pa1CIQvp150EFtilZwSbJByK5qyubKTOT1u4V+ANF4gii
Sfh9FxECgYEA/gjYjm28swTPlh+7s4BUSbWZMJ5FgYjFuGHaRKQbqD8kyfEIMie9
Pu2iOaS5Ym+0Z/cI7mqmepQdfkL5NfkosHZVA0KR4P1QhrfcnXbIinfYDlPaG4Ee
syWkDYIJDawTWDMQvBnGlyAi3eO7nUJoWke5ozHg9VxRWe1NWDNqFtcCgYEA2Sq8
3DK0H16YMztn7aKIWMS/17E11F8hZaSWiRXTNgdnTcye64Y+wLzfQaw/nLFw+rSO
qHjcTK333l90l0gKflJBePORhEZ7/5p/o3xOCdsRKH8itH+21aq/K+p4XmvodgVd
tnY93QcRid6U7e/ZDW3od6pjMLllJNUkKjJtTHkCgYA3p4x6N8R9m/I2u6ENxHGy
7FwxcJtds69No/KD00hT5fGTZIEdK+OkI7/EzTfoPvzRQifsw+TROh30CYw7rOij
MGmTm0QGfLjlquZkgR+SZospKGnCWNl2+iok43ZEToy2aAmkjCkb9uhsoHX8EA54
qPocrNLSLnWMNBcb2bfGZQKBgGuUwm6LJ7QKlnd6zGdqhwUCos7lWPdWESNbP7+1
ciZn0IM4BNpEbL3qUucjv3eOZ5uq6qkHBott+0bMHuP6qkgd05VphAL1L+RV0zlY
EQjM31kicjzcr+R1a7MDupF7/3LIAb6sIMVoBQY5n6mnke0XL3xoii7PCQ4QEJRe
2spxAoGBAIWBbVLqYSzFZzzmxhPdGi8tNLgj3idkVAO+Ovuwf4RLiulatJcebI5A
HAuJZY7XMzGKsrTX0ZY/j5uYuParAy0kzyBpXlh4FvxswFC+R2GiAMXXJCqXL2N9
tbM0dgomIxudh/4gfrCUid4mNEtYALqorXhMwJLPDaGZ1KbyytSw
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUXxPjAJgu/kDoq+EOobX/wSYZjW4wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMFoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCzYrIdaNeAReJVfaMXpHtY1JgjpAAP3XipZfrmRj0SY4pS
zHfEDSZByX7LLwde8B2ivQHDDmmIgDhL9TZ3pZlYmk2Vq0BQHJMciaI/fzF1+FNQ
imkccmvsC+LXft3SMG61ldFszMkVWGOLdflBzBudGa7z034czq3/Ucj2mE4jEsPI
OxnFH06DBadMDtGfaiyFPvEc1Ywr+LdJQ24LVrih1IZ2dmQtS40n2K77UUsvUs3s
jNx27qISfUI/tspa8DnKujuY/9x9AIzo5ldq8N20Ccns6kXxSewsxX1vH2uNH9RP
ReReTFsZU3z8xicFx8SBE4VcRXXTTsqm974QMYJlAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQA52jQ4+CoZILaTRP3mFYpg
1OmD/bwzBsHbDZhB1co6d6lWel07fj3uNekBigyHgnciMGvXm2wSJIxEvsMoXIPh
yyBjdLb8IwaZRldnLPewUuTuA6WQx6eNwA+qEn6vT9tBVLMO0pRNXy1201c7oeCj
QCJQzn+tZweNdGuX06xgPX5q196gFS+BZDw/sn3ctQ/xCXC6gno21NRqyM2VdSCM
UIzCBQLoL9DVvpmC0atV9BO7LTvOYlEuCF58IXpBBi7P+3i1Q2z4SLamsKKcU1Pp
dJkK0lA+FfIYEGsUV09ddxGXRghU7YV0kU4iPMRs/ckin95kPiUOQx4lLo3N6u8+
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAs2KyHWjXgEXiVX2jF6R7WNSYI6QAD914qWX65kY9EmOKUsx3
xA0mQcl+yy8HXvAdor0Bww5piIA4S/U2d6WZWJpNlatAUByTHImiP38xdfhTUIpp
HHJr7Avi137d0jButZXRbMzJFVhji3X5QcwbnRmu89N+HM6t/1HI9phOIxLDyDsZ
xR9OgwWnTA7Rn2oshT7xHNWMK/i3SUNuC1a4odSGdnZkLUuNJ9iu+1FLL1LN7Izc
du6iEn1CP7bKWvA5yro7mP/cfQCM6OZXavDdtAnJ7OpF8UnsLMV9bx9rjR/UT0Xk
XkxbGVN8/MYnBcfEgROFXEV1007Kpve+EDGCZQIDAQABAoIBAE9OfQx/g3bUbqH5
L5eOQnIdWz22jch105ig23He77UniMneV7y3S4ieOo49tnaElbWS9ip0Prf4Z+s8
992hus/vOAnJcl94opllR/PmmclcBgl/h8Tp2Ui8YIeBMTRx8SAaokIFr4jeUPQh
Lhem0zZ7Wlu1zvWRcl+EmuJap4DdVu3jpbddccJ00nfuw+GDgynhbJjRBmrS+2f+
a49qfH2HSoxDEHeAJuLap4b7svvyGl1G685aDGgx/mqsHxPJXiavFYQaVY1MBUiq
NMx8NUZtxFahZIsj4ScuzOx6mVhDudMlqtfBZ0c4ae0OImWqWDRyx6kJOA++5RNE
0gLxuukCgYEA5qoghL0ZLJk8UIyBI1/XECK1DP0cbOVTPSOuYBu+9ur36BhS9XPG
Ut4M3YAYLccfvV9wqolZz3811kT1E0vqWHNgyZ7I2VWP68rW1+k+F7vZld0ThXrm
T8QbH8IFGjGwPEJ/BE2OYp6r6wAaAQ2Lr8r08b0XegZLbYX+eoX9c9MCgYEAxxax
0G6uqy67z/b5/OrP6S3/XSIGEYwCrAqHikDBX22QeTop5Medzf3MFHmxS7VOYZ0X
Tuo5oieSE5DHY8Ih6DJ1hc+8LyP2aVd144A0f5SIQFJxfIxMJCp2w/9rKgyYlwRs
RqsdJ75a3jBpo7NhwbQhr4+xKdxTUWBKNBRtpecCgYEA2tIyHzq1ExYbnd5s8/4L
rAcA8t17heLX4HxlBE/ODbhCji/lI209i4eTdN38EhGBDsnnvCCozqvDiw3H4RJ3
soliHGNB7su4yNuYjSN8AE/4zq73wf0hWDKV+L660Gqq4b/Dd3WLygr01O83vB/5
kD9dt6bHCr/F9pTTIbDTDHkCgYEAqbXE2gKfzrjFzN+h9mFL3mAhgQiR179cP7+y
Dr5omKpTL6PPNoCbGo+wufuKkRj6uecpiVHM01ecBCW0cmt4b/EjkW+l4SFs2ht+
GPKezeqVww8EQsFt3p58I1PFzFB0ereAfTU8Yza3SxRF2Q/+0xp0ZK2+vgpc08+b
MY4Ach0CgYBM1qpAPFDx1fkIUc6uCr5+CJmN52djuNh5PQkBuoN4S9c98lKWXi+q
eVrsNKfDS5+92E2O4iKgWd9aCRzqxxq/0mIgT+3QLUj84SyXxlrkrV0QiU3xMrnQ
L/CjF5cbKXcixbuIlTfKwoqpRj/igThAKNtBGLKZqw0eV6uISbbDNw==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_WALLET_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUIlcBc0KB9zljlWlercBlXSmz7i8wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDFXFmZ+JAM+10oeWht8WutI9nkQRV2oMtCwmdJYerOQXEx
NGNAsUZAYQi7pUi3WFfKIOXcr+hwCFdCaoXG8A07kpAXnKlFYO8agYCwcyiYGx1Z
raB2UtUik/6j1/N6bluG4uMljojWRIAK5umAVALAmEHj4Qu0QSsv2Bi9cjqlPn80
/mM0iMqXhuQ3u+ae3t8yxbI8pQ2Zt6WJV1q9idiu6JB1ZBkm1VSO2m80rVIia4JS
nK5y/psDK5xzhi2NMp6WrCAc9ll0uNEysW2c+1ZZ5K5Sx6aEuOJadDGmZwxaHBdg
EUxrKtCTFRppHmgsr/pBwwXtI1g6rHY/Zm/8SRsDAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAn8BB5RX1ZvKsKEY+UMEEZ
7u/yoXiocrxFsRyHGgjaB3Lh4ArMsFM6I3xIbeKjojidci2d5IxWACM4V4A2MQoG
FTiX192lg0a0VgutjcylGfXQuQuC4vQux+WaShksDTYn+CKl4vSDaZIkGi6j/MNb
lqgULuMUuilLJyNPqGobz/b1jE2N6uqMD6YUJHakD4ph/oVKOcxyvlcV9jGIdOgd
UlEk/zn3PPC6CadBQ3diEm9LYoLi3QPcsLYIFRSt2YcmdvMSl/9+uLAlP2Ja7RQr
8KPvq4WWGh7S/9tblPBrPeab+Zw405qBc3RfAYuLvk4+DXA0iXIBO5yNSDpXzN3U
-----END CERTIFICATE-----
"""

SSL_TEST_WALLET_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAxVxZmfiQDPtdKHlobfFrrSPZ5EEVdqDLQsJnSWHqzkFxMTRj
QLFGQGEIu6VIt1hXyiDl3K/ocAhXQmqFxvANO5KQF5ypRWDvGoGAsHMomBsdWa2g
dlLVIpP+o9fzem5bhuLjJY6I1kSACubpgFQCwJhB4+ELtEErL9gYvXI6pT5/NP5j
NIjKl4bkN7vmnt7fMsWyPKUNmbeliVdavYnYruiQdWQZJtVUjtpvNK1SImuCUpyu
cv6bAyucc4YtjTKelqwgHPZZdLjRMrFtnPtWWeSuUsemhLjiWnQxpmcMWhwXYBFM
ayrQkxUaaR5oLK/6QcMF7SNYOqx2P2Zv/EkbAwIDAQABAoIBAQCNG2cwz+fmcD39
9zf0C31qEEz0hpga9gH93FLOw8SG7YFJpeQk19qbowUEbLtd4zr5WKYgMGEm4L/K
y7CUOQOtCTAewbLA2Pp7YAYrolpuzkwg1yP4FWcvztJsQLVjXs3v1f6D1rH9SIKn
yMtAJlDFdNb/X+LnYQTIs1+U67wEcjONZqCEjVedUvQr1ciraOKIwPRuMZK4rSjC
dJbIeD4LOyafv3SKVptaWfP24tGBLHCYcTbMDnyDNfdRvLtUK9d/9u/Wgmrjm6mP
bemtc7gnhvZ6nWySVSvzpo8V+VtVJL5ypsUcs8csOfZJpzuRput2BOYC2ffSv96q
1aHdEWfpAoGBAP/sbXcDOa9G8DmiE27FTTuOB5//ZPooJI1xTa7dnt5xNGzisGWN
ZX4U5JxgaVXR3uE8PlSdTQP5wgJV8b5bFRY3cnpAt4EgH7FcktvxeQUzDjzn/IsX
B1xO+facsl7Ssk84QWciS1w+oHteVEmZGYbHrUyk5HBbBSvnmE+LS3TPAoGBAMVr
cZRRW7cjnxPLiIEb/YJwUtmz7rFx2TFp3f1tT7Q4F3cFpYtS9phTG62NlLSmnttE
okmRkZI4PKmSvinnUe8sRrvgIlF7Xn1p3q891BiFmw+bj305qUAbwXV0mdFkxk6r
IqmWsGo6Xe8tKDnP9h7gQShqTKXnfV4B6xyj9SuNAoGBAJPvG7uOzrpl3BjEek0u
mZ1SVVAENl9v8ukb1Ja/HsVgVLiYNPUOzdsawqcuB9WG0joKM9F/d/RTW/UzruCl
D8Re2rqWTDzEz+0bIP0oURdTUuicBNx1vFh8gnsuSuELE+09DHlMVpmEzgliFoDQ
kfPZ2nASZMYZpxyg6+cXEs/7AoGAfNfpR4X7neDk5Du94we0VRx7CDkFJSl91AXC
4FSUJr+h9x6XBXg9gS5tPl9ePq9vnfHVPvjTOchedE3b+9vQsJMrV/vxN93wbxbY
P7G1wpwa5s/U+bfRFD15JbHK4+P6lB0dGmm0vjiS1oGUAptEZVojWk9+kRvG6AAG
kmIM1LECgYB7Gfaz9h0a7mbyiiMd7gXjYV760/7sgoJhmeg353FrKGxfRyowndXu
O8I4aDwSbCqtLu/Q2XOZoW+jchmvHqs/Kg9PWait7lb8bWcAxhcuC0d76OpCyp5y
S/qbLTKwRiskQR68jBd7K4TM0vYLiyc3GUEhaCUXGHPNoKtvZQyVXg==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUH4ybLZJDdYBBZEXa7rRC0r1WLYUwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQCr67MRDiKgPiH15yQ6ZJeEcghZEoYXb98sCwHKTk7cDMp+
9Q92IP761jOmqXn1BTXNZQc62a1kZ0yIBUdqCxH5R3+BGF31fDwK0VPQhSh7Np85
iv3SHlrJBmNF+JX6A+aiKf0f6Zaq0pK1NiTaY7mfXMynSVdxJwwTgqQR0qfvqXEm
XWBeARhXpUelIyUexXHrGpXumAWY4wn1YEW+SpcGNXElidd/HLbJ/OHkCExd0nge
yKDQBabCAiIb6fm0wmL6HcD++mqsEt9II8U1qoUPfpUWxFpUSWBoZWcATqrPIPYu
LeHPvl3ZctQCuTthWHvum1zRK3G8YUXcTWwWsNBHAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAb3eNfxvPPv3QjmDEIcOhv
fyGS8orMzygz0eCtX0ODKsIWEBZw7bSym6fhEYvkltSf41KkeBInjDJnqiCJ2Yef
VvXcGLyHw/klmkafcvcVCoa95TNTuKb9ElJbdIuoQ3EWk4uQEK0ARH4K+mXA5lzh
RVbG9EWvmdYXaG9BrnX9Hr/lCEPXynGtbgKvglpFn8mAWz2ru44BsrkiZgMFBpPF
R6VJV3SRCTib0nsYXkLXyRgG5JcH/VPpFfyS+sLi/98AIG2mTWXTpj4dT5f9epTr
Cn00kytB4+9ZUvCMUrg0BciQkCz6lr46gcOwbMpzoxXWnK+cwPcr9zu+LLEs1NiZ
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEAq+uzEQ4ioD4h9eckOmSXhHIIWRKGF2/fLAsByk5O3AzKfvUP
diD++tYzpql59QU1zWUHOtmtZGdMiAVHagsR+Ud/gRhd9Xw8CtFT0IUoezafOYr9
0h5ayQZjRfiV+gPmoin9H+mWqtKStTYk2mO5n1zMp0lXcScME4KkEdKn76lxJl1g
XgEYV6VHpSMlHsVx6xqV7pgFmOMJ9WBFvkqXBjVxJYnXfxy2yfzh5AhMXdJ4Hsig
0AWmwgIiG+n5tMJi+h3A/vpqrBLfSCPFNaqFD36VFsRaVElgaGVnAE6qzyD2Li3h
z75d2XLUArk7YVh77ptc0StxvGFF3E1sFrDQRwIDAQABAoIBAHmFHQmNKESEJpUe
UKlFuSPRRr1PLqEaXnFPRnCtcWhxUiDzL36cTB8ZkWDYom/iwujv5HBgtQMnUR1E
Pfpi4M2HEEU76A5BRl+PHuNhe/+72EhgSpFfC2TUsw8ea0RRxZAShe0su2b7eN/F
6b7EhsxyV+ZXHQvKQer4iOhgMnxf68BuYpL4eyYfPlKFlSN1YcBCpuh+BPBuVdqV
JSHBumr4SBHFrG/Gn+IpzAJ3EyB7idTYn3jzr/iXqtwjhSI+9Hmh8rs4ctBElrxO
of57t3uPO2Z12cQtMN29kJTplXud6AJBacM1AWlY3jbUcAYlqQtyFGNlWwqjUdP+
zXyAtoECgYEA3EXfLDNnulR4so5Ab6rYhxRmb2c+5He7BNc1fCri5U/bE7GPh0Ew
uHDLa3mc3XrHEwd6B1DpnzpiV8a7Lb9U32xPYoX73753a5RaLxr/yrZZZyuirtTE
vKdyOVufoOzD53XDvlUtkDwYLywFKpiIVp++wsf7BeKuuJ7oHpPuwfcCgYEAx84n
7sr6MsKizGMELYtjIQ24pHdzDQW6Uk3U2BU2glvzNJ0KIOgdYN3nQ/4LBhENgRL1
+mtDgQ/+NF9Q4DgpriAQCp8Kth4hosgHOZZ9mbPwMvL40XxXOtk1POHWN8SXWdU1
tHw69yMk4vS1IgjGsG6QvNfoNlscNjzW7/GD0DECgYAjmadYHXbGRqC7OwJvCc21
BzcHCki/5Bn1zlJ2nvfM1/swU6I+2epl5NT7qcwQf6dtC+hNBma7tVPvm87kteeh
tH+gDMeIgeALIw7wTgzJVm9cnVDNsNWbJ/TuEEDcYWfIIOBiAqI6jXvbI+Ix4DUo
yuip0mhfqyNR81zQlFgiQQKBgEs3KUM0d/Fp4d0tHSKECWIlBzAqo03wrQ5UrF5X
xfhW4vwYbfqrRnvzrR6kYMP84WeImr6VaIkKWzid9RUjL1WUTlWhP2gFecYMpOOh
6lBVM4QKgW5i73eA0xDDN2AxCoTPxXLXHV9xhG5HjnRsd1dtl+DvKkRkEf+88XDM
K0HRAoGAIOufId2qbyFGxWld5DpWTb2RPt7ghbxYK6SNXk5mzKOdKA6c5La9evDF
btn0mfIQf/4qftgACHTYcx/IYtOHzl83rLvuP0YE7+8ErU8TCUta1lAOIBqm/WO2
RjFbl5GxJxthIxT0CK3BEj8rSuwk9pXsnawEPN9/Ca0BuseIy5o=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_FARMER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUQv7oQqnVOgMJxwGj1o9mVlDjSV8wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDWc6RPgLnigv9641Ig8ro/KxVnUM3ORHs2hgp9Cj4lljnn
3Pl1IOlZu4pI8nQ0MGNVaiRTH5iqi1PmxfngFSsCAKjLFjty/Av2HpFiuYXQPxrC
suMPbF+KTpxi0QyxM/04inX9sZZpAPXbRtJ7XuFq71jB1mHvvyq/7/0mzTMwdUnX
LRfTMSN8TKVc+x0nGaQynIQbFxW2UcWLShaeNpfk0++2MeHOqrJo1LRta3uN8MBT
tdd7ISMv85gbwBajJ833BeE5/hxbDuohWnN6NOko+lKf+iaiVZG6LIqg4YLO8nEC
3eCtPSqZDeMcojF2TpfAs7RYy/uPTnrurq1I3M1VAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBQPItY6FjeAmX7cpd0BPdo
lWYb1yYOUVdVkHV5S160tGhLCcipZF511IOvjH+UUh/YVRUPyAhb+tCURTxWMAmz
xKiMESk5uJWoxWKZYOTkEE1SzTHdOLIO4gVz+z5ewovgSHOQ6R95AtCCeFNf+G8K
JZux2BbxkHZTiUK21UiarheTIOvdwn4W3NaGnDaxgIQncptLlLUSHKcc5FbLNhU9
4dlPe/VMglwI6R7euYFBdcJCpAnyhkeGGiEGZMPgu7oG8AY/PnbiAq4EFQa5rwB9
KtZGtuEvHhChxuCJrdhS3arkhq7qNPQc2iYRUeAnzK+CqVMMP+j9SqJA47YEoLKN
-----END CERTIFICATE-----
"""

SSL_TEST_FARMER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA1nOkT4C54oL/euNSIPK6PysVZ1DNzkR7NoYKfQo+JZY559z5
dSDpWbuKSPJ0NDBjVWokUx+YqotT5sX54BUrAgCoyxY7cvwL9h6RYrmF0D8awrLj
D2xfik6cYtEMsTP9OIp1/bGWaQD120bSe17hau9YwdZh778qv+/9Js0zMHVJ1y0X
0zEjfEylXPsdJxmkMpyEGxcVtlHFi0oWnjaX5NPvtjHhzqqyaNS0bWt7jfDAU7XX
eyEjL/OYG8AWoyfN9wXhOf4cWw7qIVpzejTpKPpSn/omolWRuiyKoOGCzvJxAt3g
rT0qmQ3jHKIxdk6XwLO0WMv7j0567q6tSNzNVQIDAQABAoIBACsYXiKj6bb9QD3/
xJdeb9MV4105vcH/vQr98Mmj7006XTSdEXxaOsqPh4CVSIjcWHnntJkHtnQ/P4MW
sdo4JsZmP4VgWF4JDJZPGkROp/drVwNdU4fb7W8r0P2CqRxLKE3edUugDmvXh5Cj
MNUeAgqtQpbhcBjvv7WGksbjYbAQ43UH8/zDFpSDmMbPjUHOnKoCZSFC3IfCoUPg
8U55AWBQVQnqP5E0R38PpAeTmHr80HFBPppYteCH7/OATr8/7ffv7Vd10/bVL1DP
Lqa8YZdNP2UOtKCDnbxq4CLFm9gQ2jIwhjL5c6YDVvXeOWiN5PKybhgU0yX3mQZa
UMFL/RkCgYEA+9l7oRtXt4Me1AkSLSstQlyGaMEEnYAwf6iU/HBu9dH7ZAadte2g
an9sciJUlODvcj3fK8rIewgJFY/wzdZPuCQv3fQGghrM9gXMgz8NiU1hK0AK/XI2
zUwVJpiFXjemRly41Ss5UG1H3tHQObl6QyEeAzpJZrNENALFL6exwQ8CgYEA2fxi
BRGr3yHq9t/RsClpPlSHuE1IM1l8G1hXxrkROo83dILEsvIcHInntoJ03SPJI9NT
0Oa/XQ/Q/21xPOmjYl+b3jKBn9Yaad0l/mwoG1M+NXEniZ2/Fok3EGqu0hoaPpJ/
ipCtnNWurA8BaSnQJD/2Fu0UnZdexlHlsr32A1sCgYBZpHSjyJa1RB+R+1ST7T1j
1Ikm+iUJZppcpgW5wM9OAhrH5K74FYe2wHo6Ocv/Xfz8ndc0wC4R1K9fFGfy7Chd
88tx5iz23FE99JxxztyjlX5Tpa0Dv0aQVldk8H7wJUCy5MgJYCQ7Y1pkjivekA1b
nYsQPQvpWT+af63uI3NaswKBgQCKMry98/cf7nP1ce6RnZ9weczVpoFItMm+2GJF
xZzLoHKK9kDYJjB2U2PIzKpkbMSfZuIzhab6zAU3et4YvRLtUioSU7jkaauzRBZL
V6yRrlO5M/TaBV1ZX0K+sLQG1a+fzeb4JUM8NCiaQqUlU/H2mWpeHI4+XvIiD1ft
2wr2EwKBgQDMM22ppSf22Cv9aw7VQW2OJHI3+22LyL7SCqQDqKGPnnDlyKtLz/sK
iQozbZbSmVHFbz0DJMNMpIWm7irD44cdpnDxxO5KDd1FJjH2Ha/RiPA6QAiJkiOT
oAFJ/tFPZF+faEhscTBdGU4yS6frDVDGJpyFgqAvTxi7H7PRrfRP6Q==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_HARVESTER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUCg9lMTGr9/8DyLNEaafobyIYAS0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQC7v3qmcCjmcREbWhZbtKpeZEwUPVkFpHg9yd0YQW0ZACZf
BZsJn5S9fkpfpJ9E758wRqvntAoKUwh0yntqjSNVEF+IwPs8eVV85yJLjZWzRlYN
FyZnr4ihtKAleDkXnSwDKKuWI3tm68GCmGlvzRvv8gR9/8Wut01JB4LjUslzaL5B
dM36gzjWGSxUD1A0gdG6leCMbJkRV6VQDLKMzMqfkrkleNZMfarrh4y2odaxGSlt
YGvIkeJg4R/vhUdWWnSCSZk8EtPZTC2ic/dMh0TZTw6zsaq0kkSf17a9HQ7exjgj
AMzTl4/O2mPQ1/j6t3nLqxXAMKRmQwe0RhW47fCzAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBSd5/DP0a3Pi7gQeYounMW
9qa/ZCn2JyIlCSKPiQ2lRJeFLzXzG/e1hEiNtSBWS0oMi5HtyhsBSbmPeEp4Enl4
Ri7UR4OhyEOddOAI98IEPtditV7YVczQi0h8a3/518yxvqVcUUOmIsABIvNWWtB+
jov5sHygh2gQ9LK/9SXWxguvI4U0AiFteJvLKSFqqcUWbNXQn09fJNyM8Cx6mnTG
5pba3FCnr39CdRgzn21Zp+plodI6xu2T/VmvkBcU4jFVY/i36LJkJ0EBjcaUiE3h
/1+POQXMivBuERizoRvtIx/xmsfKaFSp26iBW0I/AkQjCAJiVS+RF4DfaHLzg8jT
-----END CERTIFICATE-----
"""

SSL_TEST_HARVESTER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAu796pnAo5nERG1oWW7SqXmRMFD1ZBaR4PcndGEFtGQAmXwWb
CZ+UvX5KX6SfRO+fMEar57QKClMIdMp7ao0jVRBfiMD7PHlVfOciS42Vs0ZWDRcm
Z6+IobSgJXg5F50sAyirliN7ZuvBgphpb80b7/IEff/FrrdNSQeC41LJc2i+QXTN
+oM41hksVA9QNIHRupXgjGyZEVelUAyyjMzKn5K5JXjWTH2q64eMtqHWsRkpbWBr
yJHiYOEf74VHVlp0gkmZPBLT2UwtonP3TIdE2U8Os7GqtJJEn9e2vR0O3sY4IwDM
05ePztpj0Nf4+rd5y6sVwDCkZkMHtEYVuO3wswIDAQABAoIBAEZ5IXjIMRIO7vTt
Y+cYcbrsuwH95SSRD/FhjHRGWsU/oSeZ2xBJrnNSrGgqSv59U6uzW2Ol2P73G/16
48ijIdgURUf36FZS1RwFRoJFqyOYC0Tuo6PX59mLC3IFJqkOfi7RXVcGCpQfeoui
2jD1NL9kgPsqvvFOLNx0zVS3Bpci3L+HgQHRgSBJVjCuLnB+CF5nlb8abzh4gv5n
zE7vyx+sZNJW+qk3TN8yM7D144YxKXZpzzK0tQCjmf2m8P2L4vuJLhuoi43kFgfm
fgWUNFSfNrtSkVcYh9VEiaN0ZtpZbDgfNOixXIDq5N0whK3HoJSM0osST/C2Cz9V
uyXAwUECgYEA8FUVMek74XOXKWDrvC6wenyKXQ0xnHJy3qAvH5amO6LvnXWLr0Ex
ZbDz+BSzHBbjyY26m1z48BUS3GRY52mROVTlWJT+RMzdjEDWZdxjbCqrlCvx6mfI
ZmnAJJ2oAw2ndw8a/2vtoVAzayxz62LUOY2m1HwotXh8/RS9/0UcoXUCgYEAx/zQ
KSp6WB2MrwK+r5fLlmJtNVZEvqajjcD8g/1EggFN5QD5a/mLeoaYYREOu/mmWeJH
GSK2FnSCeiTYzcVbao3BD7u9pt/6s+ev/QpiBAxCnyKAQ7zTiVEvzvruEhLi6TBq
3rjvjzsOz0PYgNTzK01x/ZU8BIr5czcKRJ78HIcCgYEAvkiPRHpHCAUOLRvo6ZEJ
96D9qBkXK6hOHMg1J0yPB27FSyVTWIpEgyBsugIhod7Zsa5+jh45l1UIHulwnqCt
8/essssc2vpde3umhPXO3kiWmvWET7SmLbgTAqq06N35tsGF/a/FcNBgNb33depE
3+Cws1IupSflxjeTCzb8KTUCgYAqFvI0h8UiAG4Yc0pwqFDnwKVdYV+shGPNtL0w
hkBB4EZlmRPlfqq1SdiOLUndlAhHyJDQIHcUOMcxL8oVXKEFxvnH9upOUbtw26U1
a1b/pRjsZxV5rCcVMmoOdM9gLGtnSpJjd6arjXFre8r4KllXVsBT73GnPxyK/B2E
HbXPxwKBgAkjgd/D6v8LLneuqLOYvuEwcecCuOrkkVl6S24y/Gn7hS4awojpraoj
lZk1ZlWJwEj3KYp8toy7Wpz5bvVmZT6nVDudP2uMy3BrifIK5zZ/mKZZ4JmU7WSV
R5+9lwCKYXUDvK7dVBY6M8oh8WD5F6tHAX1EV/b/PEnqRpaqsjGi
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUZZmj3NMn41MJf/JZnA19S7GWBEcwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDiAHh3GaeWWIKsNlwDE6s8EfKs8AKvq7ThxFGtTAbZs1MT
ckyg/7/phaihOVXmpdl9Lhul9nUxr3pFkW3pDuCXWeF/QB4pJqbbDUdOl1fu1g6z
8H3hLIKK8+yKm8SliLKGlYlm0lrCh+bR1gn46ACImMxs2PiLJydaG6TH/rnQZo8k
8S8unwpjrI09dwnwdhTGG6F3789bEHyZbwzmitHRrzYUKDviazaWvyspDNg6CJ9x
+ufdVyY3vTAVsQZaGyTZMqxE/3cLtT3CHCGZaMddlVmicEIkgKh4vCYV//6suVbW
cQnzBXYCbAC0jp+TaHFoLztoB++ODJbQ02kI6xylAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCMUxFYqgEUN06caqVcTTZ5
rW3V8oRETxkCZ5okxRnKKJk6L9YhdkiL4Mjsbn+9ZwmWwEZJjlqOGUC8uZZgrRjr
fqyftmYjvRVMZNZoh1wqp3kcEDXPLOqM7ixpK/D/ScOZc8G0EpiTykj4lmgF8/7t
11fCyv6vHYLqsDFNC3BJ8g8E09Zej2bEBwTXp6g52J/YCuJ2xpu9g8mOF2xs3ECv
M74JEGlF0eNjuAQ+R5J5DaNwojHDoVYMYT5X/KaPxmLLl6b6n7ZvKuCZHs1CoLFn
1Jg1JGLOczrHvHnRPr4zLqffdnq/SFQP1MLFs+QUORLpHved+PPZJogSbRn7HzGQ
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA4gB4dxmnlliCrDZcAxOrPBHyrPACr6u04cRRrUwG2bNTE3JM
oP+/6YWooTlV5qXZfS4bpfZ1Ma96RZFt6Q7gl1nhf0AeKSam2w1HTpdX7tYOs/B9
4SyCivPsipvEpYiyhpWJZtJawofm0dYJ+OgAiJjMbNj4iycnWhukx/650GaPJPEv
Lp8KY6yNPXcJ8HYUxhuhd+/PWxB8mW8M5orR0a82FCg74ms2lr8rKQzYOgifcfrn
3VcmN70wFbEGWhsk2TKsRP93C7U9whwhmWjHXZVZonBCJICoeLwmFf/+rLlW1nEJ
8wV2AmwAtI6fk2hxaC87aAfvjgyW0NNpCOscpQIDAQABAoIBADgCidhqgUAfe3MW
ncMdcsiWYiA980x6L3/sWZmrR99YM/ST1S3pdDR5rYsXXJSm8bm2XZ/J7s17gcAQ
BL9Hsp2P5vTUfSURsTSEm/F8TIyifE5YAbp2f3vUbAEGDbxAno4ALWdQJrIjYC8M
7rfDN66iv7cSJrbF41jPlQ0DsiVVbkmUVQmb40o5iymROxj1as8ovDFqPC2mPIux
94gpKNf0FcwN/WPhz6uqHdkD26E5lIKSHy4G0Ko0uBWyITYPDQnp+57IRsm5goz9
8FzzKKlQOOh/MP4jondCjNbQXUMND2E/MUZoa/WH5JOthkrGnrupayQ9WSPWjmDd
Ru+DMxkCgYEA98ESR2Qaxu+LvdjLTl4c/G+I6/6pKmKpAhomWS1s5a4oz5llJZeM
3bGxQJYM5Zk9f5lhBgHtM30N4W5sX7aKgixeK+rITqneX0jE9eyH/WisI4WHOwxw
EXWuWhOK5MkctZPuruzCkaLAvhxtsmOQKhrSO5oCsBes0VK/dlglRJcCgYEA6YYQ
Suam/OckqmYlbu+N1km4AtRO6O+qbkRsDT88vH1Z/PAIIbS0XYlzhfc/jStZtUOE
k5UmEVqMeDHHHHg/ejczbNPVaTm0oWfWYH6D1UQdaQsI+AFDfYbuVc69ik9idnpb
+8yUHyI7ikjowKvf0f/4rgHmZX4B7Ga5gtVupCMCgYEA6fp/zcZfd4MhYSDOGGvP
SiP3lpDBqFLWtDKIBu5ciqkox65hlNgEZBZ9hLZw5aEMMGZk9+x33Il8w2qqlNXr
BzbplOY9V/UbGre5s1s3rv3cnAtuBDkh2YtfJpiQMrMwFtfnsXHN6wZequxkOPXI
X8tGwp0XbsBdKK7SPOzP/W8CgYEAxUSNCtjhg462+IMlaBtRVA4eNbWnmzqqXE/M
fzxGUGwL0pHqLJ78Jm/weOCufNB8DZWlrw41hD9bnkVej/w8kz+CX5JrG2K15gtT
m1wEfen2dj/uKaLXoniTaUUl9GqvIKqofYMKNWqzpVOF2wzWHA4Bwuyz9lSFx2/X
kmA+AMUCgYB4x8hb035umUb+lh3EyS06edJPZdrHV3teJAZ25RAU76OQzGzfndCS
VhgssI9LPWYXaO1vS7u9jSg56f6zNPHtpngSOZc9uySdSIIKM7pbucYmJB0Jrdhb
3HmdkTpb6wlZD/69AF6++09b3iFk67xsQCSSST1jW/66ZqLBkp57fw==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_TIMELORD_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUCo4bPbI2+6ucwAKVWOVvza/5Ve0wDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDTrCQBeTfXl3xKstyCxQpGelFNEagDRZLaJe/dPLN9FiBq
N25JmL0mMiJfSSI1HQQoMMM0ayilEU8epeqWkWLi+Pw2aR7nuayPzlqfY411pOVy
I0lZWi/M+w+ytyHA+/ORZHqSUf3Zccs8PouexC7bU4ScLHo6X7bOSiLfezNsqPAc
RngI9C1rPLrzQQHUd1m2aQOhvMmbXfawaofZzSRZT/Ipdhm6TsTy4325XM8BtoXm
CQtEUyM8xgmOkQF/4m/N51/+7Jnchcb3pBP1RujmibOwH4fAlDwu6A5kwe1oFMaq
ql15KdElfkRvzbVDdyAVjUnW2j0WZ3WnumM0uTSbAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBGVJ1SnI7UT7M9BSt6Sfnu
noJa96HgjVJTwMBkGIP7phGY8sm2B9OSVlaVUC6tZkJaXSPDqejdHRFleFrMn+yS
eY3apM70u+GHRIjozf6FtQQ8D9AWY3sL1eDVfoNh/w6UPaLtt0GtvLXhR9gCvPgH
WKNJ7/5hSsJHRVKBRZtuLwrU4nIwrdvcFHh9btAeNU+ZQ9BPx+jD7G0b3MC4aePg
M/mUQkCBShhQPFIuPO5B5hYmyqvSfKfRCCXz3yObo0/DmEk1XlWu5fUStUXMoBRl
JQ8AxL5aH9GLLkdhMqzInZiiEgFEEEF9OjeA0FpwG7qmRMwL0d6Mp/VfyMV3CwqT
-----END CERTIFICATE-----
"""

SSL_TEST_TIMELORD_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpgIBAAKCAQEA06wkAXk315d8SrLcgsUKRnpRTRGoA0WS2iXv3TyzfRYgajdu
SZi9JjIiX0kiNR0EKDDDNGsopRFPHqXqlpFi4vj8Nmke57msj85an2ONdaTlciNJ
WVovzPsPsrchwPvzkWR6klH92XHLPD6LnsQu21OEnCx6Ol+2zkoi33szbKjwHEZ4
CPQtazy680EB1HdZtmkDobzJm132sGqH2c0kWU/yKXYZuk7E8uN9uVzPAbaF5gkL
RFMjPMYJjpEBf+Jvzedf/uyZ3IXG96QT9Ubo5omzsB+HwJQ8LugOZMHtaBTGqqpd
eSnRJX5Eb821Q3cgFY1J1to9Fmd1p7pjNLk0mwIDAQABAoIBAQClwrZnmP/MC0tA
TBU3KwrC6mLkkaEa/s7jmrXecPy2Ri+YPlRVuhDV6ojUSbdKFLD+sEENuaUYrxdg
jtnIk4325LjN+0BCgzrJWvXIv/M1X6521X9JQ8EPKsS+VX9PW38AKsl58E90ixJ2
2RwJduSiySKeEo6dS/siTRhGHnrE6ZFG9QsMTKhsLU0WfQFY3h9NzmAv5hN5eOta
vVofMnOLRPeAEpvw0SzmnHf/oBs0cV/JTez/G1LB/xtG6QX2ko/DbjjtlKPr8kT+
Jz8i2pJvh3IA4ZxJYa7PiBxLszKvDgiOvbI/P6yKAwbeB0O1YWeiEdzQwujdEpzy
0+tNlE1RAoGBAP1qNZvUBJDGCVFKLKN+MU31K63nzGETV4kDsurvxMSxhSeOJILb
aSx62dCWKyU/mrqE+uUrpAoV37Tp2rzyDeqyOSBoW/d7shsYk0Y+/oYQp3t4DB7J
g8CQdL3ihgUvONwBUcG7MW7/RyXP29Na2eASlkkRdLPlP+jG9Wlzt1qHAoGBANXU
69QRx/4g/LyYCinkgeHqNqu4VORbyd5bnfCXkPwDppV317rJuMOJjye8IQngX6G0
fOdFXaxGWHE+w26bGI5gRvuPrG44NnD6xLfp2fFa+iUaW8qtY9z9qLK5w6RK7rGf
oMV/cxofWpSrEVQu4ZojswpgBQH+hxo+c6280bZNAoGBAOLrgVepcfEltGA7WF+K
d6IEQXm3UFc5F7BURJmF3J/5CnASI3Wd/b7bv0G9xqLTIr2UqIogGwMA9VIt+jYp
VfbsYqU3berds+35gp9rd0Ubkq3IIKpM7pK3iCIkvrfTwkmXUNt2wVxQcShVydWn
y+OPIU4KuIMCbMkHp+gmu2/vAoGBAMWw2m7wGYQbn04FCrB8cJAa53yPKP0O121a
KoT6u7Ii9eoOKEaqpMUy8kT8K1dkN0XbBfcTLG1PhAj+y9QAVA2deUKuK+6izcJa
NXELJNF9GPMgkWiqMT9ozISgNf44wME7IXo2QIYQIsB7/8NirHTDOI4JA9g6J1He
Fziy7vepAoGBAOqr2nikLpb8vBozfHmXcTx72cRHOm53L9u3UwUwnyQML0JwDNe1
xrmKS/sKZgVk+TcjEIakfLn04wmk2ZmEPA/n2z9Xc17DQlstlC10Mg6eIga/Aw/s
ocV3tE/6LBAtsPRjqR4U7JK4so6w64zHc6vbG25YBZunSnuegy73OM/3
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_CRAWLER_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUZXUt4iAbkAXAUd0mDEZSMXmcl3YwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDxVh9zMP+GF0XYDAqC3vehKpK2gTXSZTdgQWn0YMOkKQFZ
NNHHkWAtePO5p7wSbysSUnurh9GlYtsK4kDnkj1eVBCWfVyPM/0cfkbhIcv5Jpkr
qKABv+6b3v1mikl+erJ2SE3GEWY7wThZuPvNh8kDAYs7MuN766jQ59wSIxvCPlpp
cObzbz21dHRrxDl8zCzNOk2z41sY12sGvtR1fWTIByqxnNy7mfa15/uEtY5qVaVz
uQBm+gYV+lRoW3sHBJz9TEH92s+VnSpZj/hHbL8kpN8y0zichH9vG17E78LcCfCR
B6fd/Civ8mZZNhH1cCGlm26w8y7qM2PnEwvsVJ/xAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQAyQKtGaSz4s/U85m3zSqTm
fykoZVo9+BhqPEK3bqiA/wQ4RnQushPEuaLqdD/qI9l6h6jKgnx3hyJ0Ht8CYo4r
KAEhRVSoImdqW8TpFIOG2vNgK09HuI0ahwT3NfmXz8uI87IkzHco+QS/i7AMvU7V
vjyFXSjWWQYmnzb7gWw/LEcpqScMB6/4UOam3G/xznMiFCmUDn9CEh/VNFaE6YK5
9VcfE2mcOftm8/jstoOgz5a/XduxJGObE/esMf2XeLLvfhIJV5yL+AkyVUrgESeB
/SVfSH0gcu98o+jp3fT8zKF6Q53D4Uyf28HUY261pvvvZFnshprKR3Tzfjo+LcpW
-----END CERTIFICATE-----
"""

SSL_TEST_CRAWLER_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEA8VYfczD/hhdF2AwKgt73oSqStoE10mU3YEFp9GDDpCkBWTTR
x5FgLXjzuae8Em8rElJ7q4fRpWLbCuJA55I9XlQQln1cjzP9HH5G4SHL+SaZK6ig
Ab/um979ZopJfnqydkhNxhFmO8E4Wbj7zYfJAwGLOzLje+uo0OfcEiMbwj5aaXDm
8289tXR0a8Q5fMwszTpNs+NbGNdrBr7UdX1kyAcqsZzcu5n2tef7hLWOalWlc7kA
ZvoGFfpUaFt7BwSc/UxB/drPlZ0qWY/4R2y/JKTfMtM4nIR/bxtexO/C3AnwkQen
3fwor/JmWTYR9XAhpZtusPMu6jNj5xML7FSf8QIDAQABAoIBAGjyLZz2+rcB2dJ4
cf21HfQMwl3w1EnYz/rgl0W46nqxhi+Xo33oPu2nQj1CrqtJgm5mRfcyib0kvuH9
v4Gz+1HQtqHqg9yWHARO+V2fR8bhvQvaOTJpl0Za8tCrZAhHLOH40TFHkbB8dpe1
tHINESFog3ZLy9awhOnLWczdTY3qnVLl/SuK7hK8WTjthl5ZBIXiv+gvXs77eahl
Daa9q3KQRwlaDpjrkHiM8H3T645TREhatMBvpExO89bnMHPNTiLh5UF9SBrjF7RR
xJwfYrgKmf/GPSeWvb4+RBGUwCHCmuFHibyqJ/VLT/pKeTzQWLKPxavrgmEIJyqN
9R47Xu0CgYEA+Jx6iKhdJM3Egp6k1mLOLQ2m+yjTU5D39/DjIhdEu/fI8zBGSwwO
JtAGj9qUpNG0m74wqd3y8++LIxJmTjSqG9Z1jxT/sri4UvT3bqZy6Ry4/iwk+KZr
8IOYLzNmdxDhazSTa3UeHouvNmeLwmzCCNCQkHAN2jKsdjJiIe3ZkL8CgYEA+IJL
diWOyBcMtcIH+bCaU80OYRiMOatexktBHu07r1eCETlXJPn3ifmcrM9JXhCKqlVc
9ZLunPq0NwqHdNGVTBtU2gau0DhomrXr7y4WGOdiB27cV1FsuU9PmpvL18/8AWxZ
jEqmd3LuXphYdHWhn9N79Yxwdl7YKHAUXYB3S08CgYEA1VIfaiddVPkixxmtQy+g
zdPLFfOf8TKRMzSFEHl6xvcEfHdNuZNsiS0ylDjwFsTB/mkhhIAnudwvPTbKhgx2
clCAqvdPuGD7+GKt9Unpi9DTg3UJfDoAoG2qJcYrA7t+UOjaHfhukbM18q7Co1+C
1uFvSiB8ImAcz4bH4WkfqC0CgYBz3WwJneFAcV6/r8PAKxMJV2YI50UZ7ki184hd
PwbA7e/6z91NpC5B6lueRtdSQCwm1r4M0YDnOAymTQZy9PTDE0swjEUdV++Nkpx6
W+Z5nggapxmcrJ4gmFXpJBKagKJil3345yVONAvnluhHBEFjH1uAVQZqajYmRHt6
TNdSCQKBgQDB8Q+Vmqt34P/5gipoYFHdBaipLGupamJ1CBX1KoqtmMEWDgSxhGI4
Xhtm4AC2f6xwlo3S9R74QipeDyU0gN1LfGMdX8nsWUP2gcy6b1m1kSHI/e4AzJ4l
aDkjJwkopaytAEq/SVAhqNPHdtH0ihLkBOoi1xkl9u1tNpMwZHv0NA==
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_DAEMON_PRIVATE_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUQBjubkcEz8Ame+evhVR/P+08N7IwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQClp3iVfH6FLpZut6UdSrfkIfqED7h0aj8rkUi934BDFQiP
I87MuuAl7N3Nj3U3my+vppp3se0kt4cro79KStORGGuKm6EftkWJj9PIx/UKU0jv
PmtU2T7jzmohwM0RFwXSUUpAnInGUptSNlngbDJSQo92KYqCnCCw2Kllh8tSnaqn
/cVeBeOQ6ippM6YwJGs4rVMzS0v93aUvTXsKHaqq+wLe7Jcbiy2iAZT2HWZcuIt/
uhWDTRiDMxFsSl53O2dtG5tlvxS+kjZ0YOZbhJMcddHBNg0fX6oPeEzMB0DMs7Nj
3Q4CDrPXYIaLryMccGDljrF8xZ1+rlOLar1A8pufAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQCKnK69Hada53vK4LIQS8mk
PqMiGLkrNsdqo+8/zm31wWQaL+XfWEzdEWfpSy4nPAKN8PriBafoRJynxUzNKNfP
YwzSpdwh49I/hQXgTg43Ps/Ud8eMAOwZ8hQFjtpxwMN5KMCNUZ2WkN7gyHN4eCFL
Vi52fq0zSvKIgCiB/G5oauC+4oesD3KhNFNdGDM+u4cZowfJP0ytetW9YRppUDyL
Di8vN8lRfLQmt/yvEF0Qgxuz1w/4D090mSHNwkiQFvu1+A21PEkk/FGsOqaEXyjN
a/hVuQii73GQQJgDCbeBECbmNz32rXYhzm0/Gg2QQ3B592qNnyDfU0Jxsq/IJtcU
-----END CERTIFICATE-----
"""

SSL_TEST_DAEMON_PRIVATE_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEpQIBAAKCAQEApad4lXx+hS6WbrelHUq35CH6hA+4dGo/K5FIvd+AQxUIjyPO
zLrgJezdzY91N5svr6aad7HtJLeHK6O/SkrTkRhripuhH7ZFiY/TyMf1ClNI7z5r
VNk+485qIcDNERcF0lFKQJyJxlKbUjZZ4GwyUkKPdimKgpwgsNipZYfLUp2qp/3F
XgXjkOoqaTOmMCRrOK1TM0tL/d2lL017Ch2qqvsC3uyXG4stogGU9h1mXLiLf7oV
g00YgzMRbEpedztnbRubZb8UvpI2dGDmW4STHHXRwTYNH1+qD3hMzAdAzLOzY90O
Ag6z12CGi68jHHBg5Y6xfMWdfq5Ti2q9QPKbnwIDAQABAoIBAQCYEW7uu4Rhumy6
YreedjLtqAuTI+NOayJmWk6OjxftfOeIj3SOGJcf+Zt70s/mJf3Wn3h5nMp3xEq/
0ugNyTcCoYpHiaqVs/uN1oyyam0V93KivYhGMdA7zAc9yQH3SE09zwX83jbT6o1P
ITnMfUaMoTGVZXkTgUO5VIvc+pW51iyZ3mD8eH4MmkV/GoeOBkD7T1TMrTiMpeDD
K18lhmmEeMMqp7lhZ781pnfu9WzHeY6b37kap24EGBgDUDNtTdhu2bN2ejW4g+VH
0CzZcYJ02jwY1UE9fxfN/GXkfdQ5vPDy8xdo7mE3N0oMqfD+I5MZdZqG8xDKnofg
qSNv2LWxAoGBANcmVHsmAMvt0FXQ1j3GD/wJk5y/ty+UEqfVq7bmdpFYSxS4CKO2
mTlRgc+7NEYz5x/2y/7Pji4l7wICBymbgvx+Gdr60HEF/RO6wdYgZNmRcR5doHc0
RBt+8F3YCryN2AonA0abpa/mRu3QNNZNr8Vobw5v3khrhB7eSZAtkRL9AoGBAMUb
Vk1DDTElgPMzeXjjWD2UOBpLgNJBK9Ku6eGu870eOD3/oN0MwYt6WroEEpkC3EU5
Q2ATqei5Tg0I4tldlT7bA/RY3bhY17rkN83v2Sp09xAn5TvVRMaIV9m1GsSRkuCq
hgKMAoZJwjuAaEsoAa5IoyFmu2/gFICTOEF4iNHLAoGAN1lpCnVwZwY7PpiHRUUa
/6AHFaBMpDTXx820a01G24V3a1EdB+EF8jUBzEtA236myxZWzKrgzQZ9Qmr7JL0Z
KZPXWvqDfVApF1ZIX6ndyAseqs0zZvdPPjOd6saVnIRxO8tlkFiie2omfS+/KBK8
UXDYgUJOURs31ikhi7HtTJECgYEAneKX7quXFZcFA8pnsv3o4OqpRebU+ZZalBio
H68UbpiWVJM/N9HP9vm7UuWQQCCacJi972fQ4ioM60QC8jqUIhUtxbypXdFMfNfy
G3PUcL3gaYCLjrH2tVDhjfITzwEMtgnh7ohYPVk3zJG++PTC4+grQ8YWvjawNY23
sjnq3qECgYEAsrKp9xPdTpG6Y4LhhBF1O7fP2IT/8aIWMNCPoTTbhkhULlYoRXf4
hKpYRnpWkntdGqej0bq1IBt89j3LF8KLAG4d0zhyEQlFucWifd76srOPw60j86AO
Ix29DNjD9RATOzpDEvgp7R7H4/bazcqcpo/Pz0kE3/UwuCi+ebFyt+E=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_INTRODUCER_PUBLIC_CRT = b"""-----BEGIN CERTIFICATE-----
MIIDLDCCAhSgAwIBAgIUbJaDX38rnF2BylBTXCWNjn1E4kkwDQYJKoZIhvcNAQEL
BQAwRDENMAsGA1UECgwEQ2hpYTEQMA4GA1UEAwwHQ2hpYSBDQTEhMB8GA1UECwwY
T3JnYW5pYyBGYXJtaW5nIERpdmlzaW9uMCAXDTIyMDMyMjEwMjkyMVoYDzIxMDAw
ODAyMDAwMDAwWjBBMQ0wCwYDVQQDDARDaGlhMQ0wCwYDVQQKDARDaGlhMSEwHwYD
VQQLDBhPcmdhbmljIEZhcm1pbmcgRGl2aXNpb24wggEiMA0GCSqGSIb3DQEBAQUA
A4IBDwAwggEKAoIBAQDfTXQTHHDgCbBC8m1oybg5od+wH7Pfh4duI9m/I1JZLZoz
74GaQZlDG2bTHwwa3ccXDF5N3BbVG5BWGhFKquy37Od5mB88pDLngazumte0DaRC
MvM542TUwBVwLruT2jNDIPtXFZ5b7XMZh+dyLXHbvP9wyEUUBKcSi5kRgp02OYJC
g053dKazEAFtmOHoPNlCWlqqjfpMAXsbiFUBCoXmqYcyRBnNpzV1ET0nZC9W6Don
racpKDIvCGQPvZ6PL1iP/SLGx2n8QQ6y+MwRO+f4A+5dabTJHgLBQ6s3nL8ijPUU
V8jLUAkP4Yzrg127RqfHRolf644d3RqMyxGabOlPAgMBAAGjFzAVMBMGA1UdEQQM
MAqCCGNoaWEubmV0MA0GCSqGSIb3DQEBCwUAA4IBAQBKXvslWP38FdHCrH4uZq6C
r38iUHhM83Bd5PWOWpJLSepoDuAuV6FaLsDVqjQxI8M1sv6uLfBbfsCBZY6e61QM
vWI8vzDiCaUicntxozI02gSedAOyecUksADYkoL0xTPWlWHoD3EwASbwTC9Giip6
0A3Aja5mgDxB6vwRjhXs2hX0ERTJ0kmXG4As2gPhuqoXYKo5E2y+z8PkvEkjEeUx
laMTDrnaYZjfk1Vq5qED49CwAZljaIghe+Bad84JtEOckAEUteoCtsG7Th2/nQ9t
Qs81jLixhO1sYJmhoYxM8kwtv8/hC18u9qvKxZfqZfa178G3eePvbYNeS3LRlhg6
-----END CERTIFICATE-----
"""

SSL_TEST_INTRODUCER_PUBLIC_KEY = b"""-----BEGIN RSA PRIVATE KEY-----
MIIEogIBAAKCAQEA3010Exxw4AmwQvJtaMm4OaHfsB+z34eHbiPZvyNSWS2aM++B
mkGZQxtm0x8MGt3HFwxeTdwW1RuQVhoRSqrst+zneZgfPKQy54Gs7prXtA2kQjLz
OeNk1MAVcC67k9ozQyD7VxWeW+1zGYfnci1x27z/cMhFFASnEouZEYKdNjmCQoNO
d3SmsxABbZjh6DzZQlpaqo36TAF7G4hVAQqF5qmHMkQZzac1dRE9J2QvVug6J62n
KSgyLwhkD72ejy9Yj/0ixsdp/EEOsvjMETvn+APuXWm0yR4CwUOrN5y/Ioz1FFfI
y1AJD+GM64Ndu0anx0aJX+uOHd0ajMsRmmzpTwIDAQABAoIBAD13nJQGKCwDfrlu
8h7+J+/1VxWsJF9Ld0QiKjYrCufxXZkePJaxp/aI/GzxBuv+UGdPyEW2Z7KRu9F3
q3raQf7+/1jBPxf6OujvESM9DFNLzgNK8xjkN0U4+q2+r3OrhKDd21HFaan0WtKU
TmlniQfrpoTtG9a+0R6RvrjLM2tRNW/562bPR+tUmo9CHGXIwPWEb3r7sD+8UTf1
yS/xwq5HWLancjiOfEbNk5hweXI+d2x8Jb8vPM4Dm4frdfFWIt5Mek37aSE/Dn7f
9DxKfYp3wrKX378P9S60gV8qqOTEMQlBQoDOkPJxcokGYtba4Mln6ApASqV6Ocna
yQoREEECgYEA/FMVleoa1Yt/YX4UDco4Bwyh3CNflnJvTMRadKBb7ql1OvK/dSWb
WnTIc/Nmi5yAvfhUCQtzw2jdnOH1be7JQ+MkfYVgpeKanAtXGxMldgv80FtQFXQY
qipGnibAHjOWniomutV1WW6bGBiA8RUdcxh+cVCd7oRiflp6NjnopssCgYEA4o4l
eINvoccBC4DD5ZoHczaqda5qgz9zvh3c6qCOFdHHyCH/zlH75LBzGNAH1IFqacB/
nfSJsMV657Xp0uZi16YoVPVCHCFA9bFNo2w5ubaYeFdSPQi8ZwbJgmYtAPvyDoWT
UHT81RQ+GSyRaWVey39RcHcsoay1ilCs/6LmMw0CgYA0Bc1Fg2bU8FXq+9uWnELA
8VHN2V0z35Qi97jOouFRa47IAJSIyqAlHj7V6TETR8kjYbexxbKwb0aBufSoHbtR
S9uSJZWvnfDSi2QCKQhoNkCBlNIGGlGbg+vbX5HsqCY9peMmUixHrA4+AY9UJU5V
FI+9PSnSq2jDNFROKdJV0QKBgH9KSndZseD9hPLHmElqr4DmWAPiyWmQvyE0eilB
qFNOGKezopxzp8mn8iMgzyVwyS89vvYqrSoq6pFBvmyGkUaEzuhdHJXdgTgKNIr7
hbt4glYrCcPNIr3oLFQdwG9rH2dVWZ28/UljJDjUt6a2E/rWQBWmf+ceuKlMBsdi
6WAJAoGANzWzy3eDpkIWgDZJ2+kCiwSAYYmcyh0YhZENiomHdv5SCxAZzpomHI7V
kZlHSzGYnaHaUqRW1TVXN1PgYxI4HKdGlY5kKQlw0aVhUEPwJNF2HhxAltLsFiqe
RrjJMJLNHQwsrOGfhn+JCUlprbuThjUekSqNtOpNh3qqwEAtC9A=
-----END RSA PRIVATE KEY-----
"""

SSL_TEST_PRIVATE_CA_CERT_AND_KEY_1: Tuple[bytes, bytes] = (SSL_TEST_PRIVATE_CA_CRT, SSL_TEST_PRIVATE_CA_KEY)

SSL_TEST_NODE_CERTS_AND_KEYS_1: Dict[str, Dict[str, Dict[str, bytes]]] = {
    "full_node": {
        "private": {"crt": SSL_TEST_FULLNODE_PRIVATE_CRT, "key": SSL_TEST_FULLNODE_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FULLNODE_PUBLIC_CRT, "key": SSL_TEST_FULLNODE_PUBLIC_KEY},
    },
    "wallet": {
        "private": {"crt": SSL_TEST_WALLET_PRIVATE_CRT, "key": SSL_TEST_WALLET_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_WALLET_PUBLIC_CRT, "key": SSL_TEST_WALLET_PUBLIC_KEY},
    },
    "farmer": {
        "private": {"crt": SSL_TEST_FARMER_PRIVATE_CRT, "key": SSL_TEST_FARMER_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_FARMER_PUBLIC_CRT, "key": SSL_TEST_FARMER_PUBLIC_KEY},
    },
    "harvester": {
        "private": {"crt": SSL_TEST_HARVESTER_PRIVATE_CRT, "key": SSL_TEST_HARVESTER_PRIVATE_KEY},
    },
    "timelord": {
        "private": {"crt": SSL_TEST_TIMELORD_PRIVATE_CRT, "key": SSL_TEST_TIMELORD_PRIVATE_KEY},
        "public": {"crt": SSL_TEST_TIMELORD_PUBLIC_CRT, "key": SSL_TEST_TIMELORD_PUBLIC_KEY},
    },
    "crawler": {
        "private": {"crt": SSL_TEST_CRAWLER_PRIVATE_CRT, "key": SSL_TEST_CRAWLER_PRIVATE_KEY},
    },
    "daemon": {
        "private": {"crt": SSL_TEST_DAEMON_PRIVATE_CRT, "key": SSL_TEST_DAEMON_PRIVATE_KEY},
    },
    "introducer": {
        "public": {"crt": SSL_TEST_INTRODUCER_PUBLIC_CRT, "key": SSL_TEST_INTRODUCER_PUBLIC_KEY},
    },
}
