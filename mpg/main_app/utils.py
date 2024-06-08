import re
import datetime
def valid_phone_number(phone):
    cleaned_phone = re.sub(r"\D", '', phone)

    if len(cleaned_phone) < 10 or len(cleaned_phone) > 15:
        return "Invalid phone number"

    if cleaned_phone[0] == '8':
        cleaned_phone = '7' + cleaned_phone[1:]
    elif len(cleaned_phone) == 10:
        cleaned_phone = '7' + cleaned_phone

    main_number = cleaned_phone[-10:]
    extra_parts = cleaned_phone[:-10]

    formatted_number = f"{main_number[:3]} {main_number[3:6]}-{main_number[6:8]}-{main_number[8:]}"

    if extra_parts:
        formatted_phone = f"+{extra_parts} ({formatted_number[:3]}) {formatted_number[4:]}"
    else:
        formatted_phone = f"+1 ({formatted_number[:3]}) {formatted_number[4:]}"

    return formatted_phone

def age_type(birth_date):
    try:
        birth_date = datetime.datetime.strptime(birth_date, '%d.%m.%Y').date()
    except ValueError:
        return "Invalid date format. Please use DD.MM.YYYY."

    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    if age < 0:
        return "Invalid date of birth"
    elif age <= 2:
        return ('infant', 'Ребенок (0-2 лет)')
    elif age <= 12:
        return ('child', 'Ребенок (2-12 лет)')
    else:
        return ('adult', 'Взрослый')

