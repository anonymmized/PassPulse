# PassPulse 🔐
A lightweight CLI tool to assess password strength, check against common password lists, and verify if a password exists in known data breaches via the [Have I Been Pwned](https://haveibeenpwned.com/Passwords) API.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](https://opensource.org/licenses/MIT)

## 🧩 Features
- **Password Strength Analysis**: Checks length, character diversity, and complexity
- **Local Database Checks**: Verifies passwords against multiple leaked password lists
- **Pwned Passwords API**: Integrates with [HIBP](https://haveibeenpwned.com/API/v3#PwnedPasswords) API for real-time breach checks
- **Privacy-Focused**: No data stored or transmitted
- **Cross-Platform**: Works on macOS, Linux, and Windows (via WSL)

## 🛠️ Requirements
- Python 3.x
- Git
- Internet connection for API checks
- `curl` or `wget` for list downloads

## 📦 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourname/passpulse.git
   cd passpulse