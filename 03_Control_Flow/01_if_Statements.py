age = 19
film_showing = True

if age >= 18 and film_showing:
    print('You are allowed to buy a ticket for this film.')
    print('Enjoy the film!')
elif age == 17:
    print('Come back next year')
else:
    print('No dice')


print('This will always print')

certificate = 'U'.upper() # U, PG, 12, 12A, 15, 18
# check the certificate
# Print corresponding info about the film

if certificate == 'U':
    print('Suitable for all ages')
elif certificate == 'PG':
    print('PARENTAL GUIDANCE SUGGESTED. SOME MATERIAL MAY NOT BE SUITABLE FOR CHILDREN'.lower().capitalize())
elif certificate in ('12', '12A'):
    print('Suitable for aged 12 and above')
elif certificate == '15':
    print('Suitable for aged 15 and above')
elif certificate == '18':
    print('Suitable for Adults')
else:
    print('Unknown rating')