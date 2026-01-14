# Contributing to Industrial and Logistics Optimization Samples

Thank you for your interest in contributing! This document provides guidelines for contributing to this repository.

## How to Contribute

### Reporting Issues

- Use the GitHub issue tracker to report bugs or suggest features
- Check if the issue already exists before creating a new one
- Provide clear descriptions and reproducible examples when possible

### Submitting Changes

1. **Fork the repository** and create your branch from `main`
2. **Add your sample** in a new directory under `samples/`
3. **Write clear code** with comments explaining the optimization approach
4. **Include a README** in your sample directory explaining:
   - The problem being solved
   - How to run the example
   - Expected output
   - References and resources
5. **Test your code** to ensure it runs correctly
6. **Update the main README** to include your new sample
7. **Submit a pull request** with a clear description of your changes

## Sample Guidelines

### Structure

Each sample should be in its own directory:
```
samples/your_sample_name/
├── README.md           # Documentation for the sample
├── solver.py          # Main implementation
├── requirements.txt   # Sample-specific dependencies (if any)
└── example_data/      # Sample data files (if applicable)
```

### Code Quality

- Use clear, descriptive variable names
- Add comments explaining the optimization model
- Follow PEP 8 style guidelines for Python code
- Include docstrings for functions and classes
- Keep implementations focused and educational

### Documentation

- Explain the problem clearly
- Document assumptions and constraints
- Provide references to academic papers or resources
- Include usage examples
- Show expected output

## Optimization Topics

We welcome samples covering various optimization problems:
- **Routing**: VRP, TSP, multi-depot routing
- **Scheduling**: Job shop, flow shop, project scheduling
- **Allocation**: Resource allocation, assignment problems
- **Network**: Flow problems, shortest path, network design
- **Inventory**: Lot sizing, stock optimization
- **Facility**: Location problems, layout optimization
- **Production**: Planning, capacity planning
- **Supply Chain**: Distribution, logistics network design

## Questions?

Feel free to open an issue for questions or clarifications.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
