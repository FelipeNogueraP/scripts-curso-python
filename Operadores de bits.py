flag_register = 0x1234
flag_register = 11111111111111111111111111110111

# comprobar estado de bit
x & 1 = x
x & 0 = 0

# Mascara de bit

the_mask = 8

# secuencia de instrucciones

if flag_register & the_mask:
    x = 1
else:
    x = 0
# reiniciar el bit
flag_register = flag_register & ~the_mask
flag_register &= ~the_mask

# establecer el bit
x | 1 = 1
x | 0 = x

# configurar el bit
flag_register = flag_register | the_mask
flag_register |= the_mask

# negar el bit
x ^ 1 = ~x
x ^ 0 = x

flag_register = flag_register ^ the_mask
flag_register ^= the_mask
