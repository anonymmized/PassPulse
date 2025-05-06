import os
import json
import csv

def load_passwords(passwords_dir="data/passwords"):
    passwords = set()
    if not os.path.exists(passwords_dir):
        print(f"[!] Каталог {passwords_dir} не найден")
        return passwords
    
    for filename in os.listdir(passwords_dir):
        filepath = os.path.join(passwords_dir, filename)
        if os.path.isfile(filepath):
            try:
                with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                    passwords.update(line.strip() for line in f if line.strip())
            except Exception as e:
                print(f"[!] Ошибка чтения файла {filename}: {e}")
    print(f"[+] Загружено {len(passwords)} уникальных паролей из списков")
    return passwords

def export_json(password, result):
    with open("data/report.json", "w", encoding="utf-8") as f:
        json.dump({
            "password": password,
            "length": len(password),
            "strength": result
        }, f, indent=2, ensure_ascii=False)
    return "[*] Данные сохранены в data/report.json"

def export_csv(password, result):
    with open("data/report.csv", "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Password", "Length", "Strength"])
        writer.writerow([password, len(password), result])
    return "[*] Данные сохранены в data/report.csv"