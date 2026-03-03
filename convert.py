import argparse
import sys

# --- Conversion Data ---
# Format: 'unit': {'type': 'category', 'to_base': function, 'from_base': function}
# We convert everything to a 'base' unit first, then to the target.

CONVERSIONS = {
    # Temperature (Base: Celsius)
    'c': {'type': 'temp', 'to_base': lambda x: x, 'from_base': lambda x: x},
    'f': {'type': 'temp', 'to_base': lambda x: (x - 32) * 5/9, 'from_base': lambda x: (x * 9/5) + 32},
    'k': {'type': 'temp', 'to_base': lambda x: x - 273.15, 'from_base': lambda x: x + 273.15},
    
    # Length (Base: Meters)
    'm': {'type': 'length', 'to_base': lambda x: x, 'from_base': lambda x: x},
    'km': {'type': 'length', 'to_base': lambda x: x * 1000, 'from_base': lambda x: x / 1000},
    'mi': {'type': 'length', 'to_base': lambda x: x * 1609.34, 'from_base': lambda x: x / 1609.34},
    'ft': {'type': 'length', 'to_base': lambda x: x * 0.3048, 'from_base': lambda x: x / 0.3048},
    
    # Weight (Base: Kilograms)
    'kg': {'type': 'weight', 'to_base': lambda x: x, 'from_base': lambda x: x},
    'lb': {'type': 'weight', 'to_base': lambda x: x * 0.453592, 'from_base': lambda x: x / 0.453592},
    'g': {'type': 'weight', 'to_base': lambda x: x / 1000, 'from_base': lambda x: x * 1000},
}

def convert(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    
    # 1. Validation
    if from_unit not in CONVERSIONS:
        return f"Error: Unknown unit '{from_unit}'"
    if to_unit not in CONVERSIONS:
        return f"Error: Unknown unit '{to_unit}'"
    
    # 2. Check Compatibility (Can't convert kg to meters)
    from_type = CONVERSIONS[from_unit]['type']
    to_type = CONVERSIONS[to_unit]['type']
    
    if from_type != to_type:
        return f"Error: Cannot convert {from_type} to {to_type}"
    
    # 3. Perform Conversion
    # Step A: Convert input to Base Unit
    base_value = CONVERSIONS[from_unit]['to_base'](value)
    
    # Step B: Convert Base Unit to Target
    result = CONVERSIONS[to_unit]['from_base'](base_value)
    
    # Clean up result (remove .0 if integer)
    if result.is_integer():
        return int(result)
    return round(result, 4)

def main():
    parser = argparse.ArgumentParser(description="Convert units (Temp, Length, Weight)")
    parser.add_argument("value", type=float, help="The value to convert")
    parser.add_argument("from_unit", type=str, help="Source unit (e.g., kg, mi, c)")
    parser.add_argument("to_unit", type=str, help="Target unit (e.g., lb, km, f)")
    
    args = parser.parse_args()
    
    result = convert(args.value, args.from_unit, args.to_unit)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()