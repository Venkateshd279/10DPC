# 10DPC

## Virtual Environment

Note: use `python3` on macOS if `python` points to Python 2.

macOS (bash / zsh)

Create:
```bash
python3 -m venv venv
```
Activate:
```bash
source venv/bin/activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
Deactivate:
```bash
deactivate
```

Windows (PowerShell / CMD)

Create:
```powershell
python -m venv venv
```
Activate (PowerShell):
```powershell
venv\Scripts\Activate.ps1
```
Activate (CMD):
```cmd
venv\Scripts\activate.bat
```
Install dependencies:
```powershell
pip install -r requirements.txt
```
Deactivate:
```powershell
deactivate
```

Remove (optional):
```bash
rm -rf venv    # macOS
rmdir /s /q venv  # Windows
```

## Quick Concepts (short)

- **Variables & Types:** int, float, str, bool — variables store values.
- **Collections:** list (ordered, changeable), tuple (ordered, fixed), set (unique, unordered), dict (key:value pairs).
- **Control flow:** `if` / `elif` / `else`, `for`, `while`.
- **Functions:** use `def` to create reusable blocks.
- **Modules:** reusable `.py` files; packages are folders with `__init__.py`.

See full, easy-to-recall notes: [defintion.md](defintion.md)
Runnable examples live in the `Python/` folder (e.g. `Python/data_type.py`).
