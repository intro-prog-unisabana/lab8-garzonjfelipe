"""Laboratorio 8 - Problema 1.

Implementa una CLI que calcule carga por punto de soporte.
"""
import sys

try:
    total_load = float(sys.argv[1])
    num_supports = float(sys.argv[2])

    if num_supports == 0:
        print("Error: Cannot divide by zero! Supports must be greater than zero.")
    else:
        result = total_load / num_supports
        print(f"Load per support point: {result:.2f} N")

except (IndexError, ValueError):
    print("Error: Invalid input! Enter numeric values only.")