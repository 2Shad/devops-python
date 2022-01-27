# # import random
# # print(random.random())

# from random import random, randint
# from math import ceil, floor, pi

# print(random())
# print(pi)
# print(ceil(pi))
# print(floor(pi))

# print(randint(1, 100))


# # import os

# # work_dir = os.getcwd()
# # print(work_dir)
# # print(os.getgid())

# from my_functions.os_functions import return_os_info, return_user_id, return_new_vegas

# print(return_os_info())

# # PIP -> PIP Installs Packages
import requests

r = requests.get('https://www.bbc.co.uk')
print(r, type(r))

print(r.status_code)
# print(r.content)

