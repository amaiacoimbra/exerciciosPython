from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
sen = sin(radians(an))
print('O ângulo de {} tem o SENO de {:.2f}'.format(an, sen))
con = cos(radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, con))
tan = tan(radians(an))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(an, tan))

