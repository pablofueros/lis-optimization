# 📈 Longest Increasing Subsequence Optimization

This repository contains various implementations and optimizations of the Longest Increasing Subsequence (LIS) problem in both Python and Rust. It includes performance comparisons and analysis tools to understand the efficiency of different approaches.

## 🎯 Problem Description

The Longest Increasing Subsequence problem is a classic algorithmic challenge: given a sequence of numbers, find a subsequence (not necessarily contiguous) where all elements are in strictly increasing order, and this subsequence is as long as possible.

## 🛠️ Implementations

### Python Implementations

- `lis_bruteforce.py`: Brute force approach (exponential time)
- `lis_bruteforce_numpy.py`: NumPy-optimized brute force
- `lis_dp_n2.py`: Dynamic Programming O(n²) solution
- `lis_nlogn.py`: Optimized O(n log n) solution using patience sorting
- `lis_recursive.py`: Basic recursive implementation
- `lis_recursive_np.py`: NumPy-optimized recursive version
- `lis_recursive_opt_1.py`: First optimization of recursive approach
- `lis_recursive_opt_2.py`: Second optimization of recursive approach

### Rust Implementations

- `lis_bruteforce.rs`: Brute force approach in Rust
- `lis_dp_n2.rs`: O(n²) Dynamic Programming solution
- `lis_nlogn.rs`: O(n log n) optimized solution
- `lis_recursive.rs`: Recursive implementation

## 📊 Analysis Tools

The project includes comprehensive analysis tools:

- `analysis.py`: Jupyter/Marimo notebook for visualizing and comparing performance
- `generator.py`: Test data generation utilities
- `utils.py`: Common utilities and helper functions

## 🔧 Requirements

### Python
uv: https://docs.astral.sh/uv/

### Rust
rust-script: https://rust-script.org/

## 📁 Project Structure

```
.
├── analysis.py           # Performance analysis notebook
├── data/                # Test sequences of various sizes
├── python/              # Python implementations
├── results/             # Performance test results
└── rust/                # Rust implementations
```

## 🚀 Performance

Performance results and comparisons can be found in the `results/` directory. The analysis notebook provides visualizations and detailed comparisons between different implementations.

## 📄 License

This project is open source. Feel free to use, modify, and distribute as needed.
