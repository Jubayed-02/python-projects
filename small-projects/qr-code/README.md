# QR code generator

A simple Python script that generates a styled QR code with circular modules using the [`qrcode`](https://pypi.org/project/qrcode/) library and Pillow.

## Features

- Auto-sized QR code (`version=None`)
- High error correction (`ERROR_CORRECT_H`) — recovers up to ~30% of damaged data
- Circular module design (dots instead of squares)
- Customizable foreground and background colors
- Saves output as `qr.png`

## Module needs to be installed

```bash
pip install "qrcode[pil]"
```

## How to Run

1. Download or clone this project.
2. Open a terminal in the project folder.
3. Run the game:

```bash
python main.py
```

## 📦 Requirements

- Python 3.7+
- [`qrcode`](https://pypi.org/project/qrcode/)
- [`pillow`](https://pypi.org/project/pillow/)
