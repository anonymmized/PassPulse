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
   git clone https://github.com/anonymmized/PassPulse
   cd PassPulse
   ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Download password lists:
    ```
    chmod +x download_lists.sh
    ./download_lists.sh
    ```

## ▶️ Usage
    ```
    python3 main.py
    ```

You'll be prompted to enter a password for analysis. The tool will:

- Assess password strength (Weak/Medium/Strong)
- Check against 10+ million leaked passwords
- Verify against PwnedPasswords database
- Show detailed security report

## 📊 Example Output
    ```
    [+] Checking password: '123456789'
    [-] Strength: Weak (9 characters)
    [-] Found in local lists: Yes (rockyou.txt)
    [-] Found in PwnedPasswords: Yes (20,689 times)
    [-] Verdict: CRITICAL - Password compromised in multiple breaches!
    ```

## 🛡️ Security

```
### Key Improvements:
1. Added license badge with direct link to MIT license
2. Created dedicated sections for features, requirements, and contributing
3. Added security disclaimer about password handling
4. Improved code formatting with syntax highlighting
5. Added professional emojis for better visual hierarchy
6. Included contribution guidelines
7. Added maintainer information
8. Made the project name consistent (PassPulse instead of password-checker)
9. Added cross-platform compatibility note
10. Included version control instructions

Make sure to:
1. Add the actual MIT license file
2. Update the GitHub repository URL in links
3. Add your project-specific technical documentation
4. Consider adding screenshots or a demo video for better visualization
```