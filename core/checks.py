import re
import hashlib
import requests

def check_length(password):
    length = len(password)
    if length < 8:
        return "Слабый"
    elif 8 <= length <= 12:
        return 'Средний'
    elif length > 12:
        return 'Сильный'

def check_characters(password):
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'!@#$%^&*(),.?\":{}|<>', password))
    return sum([has_digit, has_lower, has_special, has_upper])

def check_common_password(password, common_passwords):
    return password in common_passwords

def check_pwned_password(password):
    sha1_hash = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_hash[:5], sha1_hash[5:]
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)
    if response.status_code == 200:
        for line in response.text.splitlines():
            if suffix in line:
                count = line.split(':')[1]
                return f"Пароль найден в утечках ({count} раз)"
    return "Без утечек"

def analyze_password(password, common_passwords):
    print('[+] Проверка длины...')
    length_result = check_length(password)
    print(f"[-] Длина: {len(password)} символов -> {length_result}")

    print('[+] Проверка символов...')
    characters_result = check_characters(password)
    print(f'[-] Количество типов символов: {characters_result}/4')

    print('[+] Проверка по списку распространенных паролей...')
    is_common = check_common_password(password, common_passwords)
    print(f"[-] В списке распространенных: {'Да' if is_common else 'Нет'}")

    print('[+] Проверка на утечки...') 
    pwned = check_pwned_password(password)
    print(f"[-] {pwned}")

    final_score = length_result
    if is_common:
        final_score = 'Слабый (находится в списке распространенных паролей)'
    elif length_result == 'Слабый' or characters_result < 2:
        final_score = 'Слабый'
    elif length_result == 'Средний' and characters_result >= 3:
        final_score = "Средний"
    elif length_result == 'Сильный' and characters_result >= 4:
        final_score = 'Сильный'
    print(f"\n[+] Итоговая оценка: {final_score}")
    return final_score