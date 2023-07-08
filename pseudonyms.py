"""This program generates random combinations of Arabic names and adjectives to create great names. 
It uses a predefined list of Arabic names and adjectives to select random combinations. 
The user is prompted to try again to generate more names until they choose to quit.
"""

import sys
import random



print('Welcom to the great name game \n')


arabic_names = (
    'أحمد', 'محمد', 'فاطمة', 'علي', 'نور', 'عمر', 'عائشة', 'حسن', 'أمينة', 'عبدالله',
    'مريم', 'إبراهيم', 'سارة', 'خالد', 'زينب', 'مصطفى', 'ليلى', 'عبدالرحمن', 'فاضل', 'سمية',
    'محسن', 'نادية', 'عبدالملك', 'سعاد', 'عبدالعزيز', 'أماني', 'عبداللطيف', 'هند', 'يوسف',
    'رقية', 'صلاح', 'فاطمة', 'جمال', 'حبيبة', 'معتصم', 'جميلة', 'مجدي', 'عائدة', 'ناجي',
    'عفاف', 'رمضان', 'سميرة', 'أحمد', 'سمر', 'حكيم', 'صباح', 'مجد', 'سعيدة', 'سيد', 'صالحة',
    'رشيد', 'فاطمة', 'حازم'
)

arabic_adjectives = (
    'جميل', 'ذكي', 'سعيد', 'عظيم', 'حكيم', 'صادق', 'مدهش', 'رائع', 'عميق', 'شجاع',
    'طيب', 'حلو', 'سريع', 'طويل', 'صغير', 'غني', 'فقير', 'بسيط', 'عاطفي', 'واضح',
    'ممتع', 'فعال', 'عادل', 'مليء', 'صحي', 'قوي', 'مرح', 'صامت', 'ساحر', 'متفائل',
    'نشيط', 'سهل', 'صبور', 'حر', 'متسامح', 'مبدع', 'حذر', 'متقدم', 'خجول', 'صادق',
    'محظوظ', 'مستقر', 'عابر', 'حاد', 'متواضع', 'سلمي', 'مستعد', 'محبوب', 'حنون', 'واعي'
)



print('Here is your first great name: ')
while True:
    nameName = random.choice(arabic_names)
    adj = random.choice(arabic_adjectives)

    print(f"\033[91m {nameName} {adj} \033[0m", file=sys.stderr)
    print('\n')

    try_again = input("Try again? (Press Enter else n to quite) \n")

    if try_again.lower() == 'n':
        break

input("Press Enter to exit")
