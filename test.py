import re
soz=input('so\'z kiriting  : ')
if re.match('^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$',soz):
    print('Qabul Qilindi')
else:
    print('Qabul qilinmadi')