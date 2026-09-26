# Fluid Stability Analysis

Numerical investigation of hydrodynamic instability in fluid–structure systems using Python.

This project is based on my final-year Mathematics & Statistics research project at the University of Glasgow. It explores how parameters such as wall tension, bending resistance, wall mass and fluid velocity influence the stability of wave modes.

## Methods

- Dispersion relation analysis
- Complex-valued frequency calculations
- Numerical parameter sweeps
- Stability threshold detection
- Scientific visualisation

## Tools

- Python
- NumPy
- SciPy
- Matplotlib

## Project Structure

src/  
&nbsp;&nbsp;&nbsp;&nbsp;dispersion_relation.py

examples/  
&nbsp;&nbsp;&nbsp;&nbsp;wavenumber_analysis.py  
&nbsp;&nbsp;&nbsp;&nbsp;tension_analysis.py  
&nbsp;&nbsp;&nbsp;&nbsp;bending_analysis.py

## Background

The project investigates transitions between stable and unstable modes by examining the real and imaginary components of the dispersion relation.

A non-zero imaginary component of frequency corresponds to exponential growth or decay of a perturbation, allowing stability boundaries to be identified numerically.
