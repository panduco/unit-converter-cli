# 📏 Unit Converter CLI

A simple, strict command-line tool to convert units of Temperature, Length, and Weight.

![Python](https://img.shields.io/badge/Python-3.6%2B-blue) ![License](https://img.shields.io/badge/License-MIT-yellow)

## ✨ Features

- **Multiple Categories:** Supports Temperature, Length, and Weight.
- **Smart Validation:** Prevents impossible conversions (e.g., converting kg to meters).
- **Precise:** Handles floating-point math accurately.

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/unit-converter-cli.git
   cd unit-converter-cli
   ```

## 💻 Usage

```bash
python convert.py <value> <from_unit> <to_unit>
```

### Supported Units

| Category | Units |
|----------|-------|
| **Temperature** | `c` (Celsius), `f` (Fahrenheit), `k` (Kelvin) |
| **Length** | `m` (Meters), `km` (Kilometers), `mi` (Miles), `ft` (Feet) |
| **Weight** | `kg` (Kilograms), `lb` (Pounds), `g` (Grams) |

### Examples

**Convert 100 Celsius to Fahrenheit:**
```bash
python convert.py 100 c f
# Output: Result: 212
```

**Convert 10 Miles to Kilometers:**
```bash
python convert.py 10 mi km
# Output: Result: 16.0934
```

**Convert 50 Kilograms to Pounds:**
```bash
python convert.py 50 kg lb
# Output: Result: 110.231
```

## 📜 License

This project is licensed under the MIT License.