# Error Propagation (Fehlerfortpflanzung)

## Overview

This project implements **error propagation** calculations, a fundamental concept in experimental physics and engineering. It provides tools to calculate how uncertainties in measured quantities propagate through mathematical operations and formulas.

## What It Does

The script calculates the uncertainty (error) in results when input measurements have known uncertainties. Using error propagation rules, it determines how errors combine when performing:

- **Basic arithmetic operations** (addition, subtraction, multiplication, division)
- **Mathematical functions** (power, exponential, logarithm, trigonometric)
- **Complex formulas** with multiple variables

## How It Works

### Core Principles

The script uses the **Taylor series expansion method** (first-order approximation) to calculate error propagation:

- For a function `f(x, y, z, ...)`, the uncertainty is calculated using partial derivatives
- Error formula: `δf = √[(∂f/∂x · δx)² + (∂f/∂y · δy)² + ...]`

### Key Features

- **Automatic differentiation** for computing partial derivatives
- **Support for multiple variables** with independent uncertainties
- **Clear output** showing calculated values and uncertainties
- **Flexible input** for custom formulas and measurement data

## Usage

1. Define your measured values
2. Specify the formula or mathematical operation in the given function
3. Run the script to calculate the resulting uncertainty
4. Review the computed results and propagated error

## Project Structure

```
c:\Users\simon\PythonProject\Fehlerfortpflanzunh\
├── README.md
├── error_propagation.py    # Main implementation
├── main.py                  # Entry point
└── pyproject.toml           # Project configuration
```

## Requirements

- Python 3.7+
- NumPy (for numerical operations)
- SciPy (for scientific functions)

## License

This project is free to use, but take care, everything is WIP.
