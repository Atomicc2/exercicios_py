import math

angle = float(input('Me fale um angulo: '))
sen = math.sin(math.radians(angle))
cos = math.cos(math.radians(angle))
tg = math.tan(math.radians(angle))

print(f'This is a sin {sen:.1f}\nThis is a cossin {cos:.1f}\nThis is a tangent {tg:.1f}.')