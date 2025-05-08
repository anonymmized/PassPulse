import os
import sys
import click
import argparse
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'core')))

from core.checks import check_length, check_characters, check_common_password, check_pwned_password, analyze_password
from core.utils import load_passwords, export_json, export_csv

COMMON_PASSWORDS_DIR = "data/passwords"

def parse_args():
    parser = argparse.ArgumentParser(description="Проверка сложности пароля")
    parser.add_argument('-p', '--password', help='Ручной ввод пароля')
    parser.add_argument('-f', '--file', help="Пароль читается из файла")
    parser.add_argument('-l', '--length', action="store_true", help="Проверка длины")
    parser.add_argument('-c', '--characters', action='store_true', help='Проверка типов символов')
    parser.add_argument('-pw', '--pwned', action="store_true", help="Проверка через HIBP API")
    parser.add_argument('-ld', '--loaded', action="store_true", help="Список загруженных файлов")
    parser.add_argument('-cp', '--cmnpassword', action='store_true', help="Проверка по списку паролей")
    parser.add_argument('-af', '--addfile', help='Добавить список из файла')
    parser.add_argument('-ej', '--exportjson', action="store_true", help='Экспорт в JSON')
    parser.add_argument('-ecsv', '--exportcsv', action="store_true", help="Экспорт в CSV")
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_args()

    if args.loaded:
        os.system(f'ls {COMMON_PASSWORDS_DIR}')
        print('\n' + '='*50)

    if not os.path.exists(COMMON_PASSWORDS_DIR) or not os.listdir(COMMON_PASSWORDS_DIR):
        print("[!] Списки паролей не найдены.")
        print("[*] Запустите './scripts/download_lists.sh'")
        sys.exit(1)

    if args.file:
        try:
            with open(args.file, 'r') as f:
                password = f.read().strip()
        except Exception as e:
            print(f"[!] Ошибка чтения файла: {e}")
            sys.exit(1)
    elif args.password:
        password = args.password
    else:
        password = click.prompt('Введите пароль', hide_input=True)

    run_length_check = args.length
    run_char_check = args.characters
    run_pwned_check = args.pwned

    if any([run_char_check, run_length_check, run_pwned_check]):
        if run_char_check:
            print(f"[+] Проверка символов: {check_characters(password)}/4")
        if run_length_check:
            print(f"[+] Проверка длины: {len(password)} → {check_length(password)}")
        if run_pwned_check:
            pwned_result = check_pwned_password(password)
            print(f"[+] {pwned_result}")
        sys.exit(0)

    if args.addfile:
        common_passwords = load_passwords(args.addfile)
    else:
        common_passwords = load_passwords()

    final_result = analyze_password(password, common_passwords)

    if args.exportjson:
        export_json(password, final_result)
    elif args.exportcsv:
        export_csv(password, final_result)