# Machine Problem II: Brute Force Review and Implementation

[![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B.svg)](https://streamlit.io)
[![GitHub](https://img.shields.io/badge/View%20on-GitHub-green.svg)](https://github.com/JpCurada/g6-mp2-desalgo)

## Table of Contents
- [Overview](#overview)
- [Group Members](#group-members)
- [Project Goals](#project-goals)
- [Environment Setup](#environment-setup)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview
This project involves the review and implementation of various brute force algorithms as part of Machine Problem 2 in the Design and Analysis of Algorithms course. The application is built using Python 3.11 and Streamlit, providing an interactive interface for exploring algorithmic concepts.

## Group Members
- CURADA, John Paul M.
- ZARAGOZA, Marie Criz 
- LUCERO, Ken Audie S.
- FAELDONIA, Elias Von Isaac R. 
- OJA, Ma. Izabelle L.
- RACELIS, Michael Richmond V.
- CANSINO, Florence Lee F.
- RAMILO, Gian G.
- MAGTANONG, Gabriel Andre E.

## Project Goals
- Implement and analyze brute force algorithms such as Selection Sort, Bubble Sort, Sequential Search, Traveling Salesman Problem, and Knapsack Problem.
- Provide a user-friendly interface for visualizing algorithm behavior and performance.
- Explore optimization techniques and their impact on algorithm efficiency.

## Environment Setup

### Installing Python
1. Open Windows PowerShell and execute:
   ```
   winget install -e --id Python.Python.3.11
   ```
2. During installation, ensure you check the `Add to PATH` option for a smooth workflow.
3. Verify installation by opening command prompt and running:
   ```
   python --version
   ```

### Installing Package Manager
We'll use UV as our package manager:

1. Open Windows PowerShell and run:
   ```
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

## Usage
1. Clone the repository:
   ```
   git clone https://github.com/JpCurada/g6-mp2-desalgo.git
   cd g6-mp2-desalgo
   ```
2. Install dependencies:
   ```
   uv install
   ```
3. Run the Streamlit application:
   ```
   streamlit run src/streamlit_app.py
   ```
4. Open your web browser and navigate to `http://localhost:8501` to explore the application.

## Contributing
We welcome contributions! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```
   git commit -m "Description of changes"
   ```
4. Push to your branch:
   ```
   git push origin feature-name
   ```
5. Open a pull request and describe your changes.











