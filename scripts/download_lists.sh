#!/bin/bash

REPO_URL="https://github.com/berandal666/Passwords.git"
PASSWORDS_DIR="passwords"

if ! command -v git &> /dev/null; then
    echo "[!] Git не установлен. Установите его перед продолжением."
    exit 1
fi

mkdir -p "$PASSWORDS_DIR"

if [ -d "$PASSWORDS_DIR/.git" ]; then
    echo "[*] Репозиторий уже существует. Обновляю его..."
    (cd "$PASSWORDS_DIR" && git pull origin master)
    if [ $? -eq 0 ]; then
        echo "[+] Репозиторий успешно обновлен"
    else
        echo "[!] Не удалось обновить репозиторий"
        exit 1
    fi
else
    echo "[+] Клонирую репозиторий из $REPO_URL в $PASSWORDS_DIR..."
    git clone "$REPO_URL" "$PASSWORDS_DIR"
    if [ $? -eq 0 ]; then
        echo "[+] Репозиторий успешно загружен"
    else
        echo "[!] Ошибка при клонировании репозитория"
        exit 1
    fi
fi

if [ "$(ls -A "$PASSWORDS_DIR")" ]; then
    echo "[+] Списки паролей сохранены в: $PASSWORDS_DIR"
else
    echo "[!] Репозиторий загружен, но файлы не найдены"
    exit 1
fi