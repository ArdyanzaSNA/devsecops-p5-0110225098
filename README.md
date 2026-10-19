# SecureTask

SecureTask is a simple Python command-line application for managing tasks. It allows users to create, list, and delete tasks, as well as generate a summary report of task statistics.

## Features

- Create tasks with validated titles.
- List all tasks and view their current status.
- Retrieve tasks by ID.
- Delete tasks by ID.
- Generate a task report showing the total number of tasks, completed tasks, and pending tasks.
- Validate task titles to prevent empty titles and titles longer than 100 characters.
- Run automated unit tests for task management and reporting functionality.

## Technology Stack

- **Language:** Python 3.12
- **Testing Framework:** Python `unittest`
- **SAST Tool:** Bandit
- **CI/CD Platform:** GitHub Actions

## Project Structure

```text
devsecops-p5-0110225098/
├── .github/
│   └── workflows/
│       └── devsecops.yml
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── storage.py
│   ├── task_service.py
│   ├── validators.py
│   └── task_report.py
├── tests/
│   └── test_tasks.py
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## Requirements

- Python 3.12 or a compatible Python 3 version.
- Git, to clone the repository.

## How to Run

Clone this repository and open the project directory:

```bash
git clone https://github.com/ArdyanzaSNA/devsecops-p5-0110225098.git
cd devsecops-p5-0110225098
```

Run the application:

```bash
python -m app.main
```

Use the interactive menu to create tasks, list tasks, delete tasks, or view the task report.

**Note:** Tasks are stored in memory and are cleared when the application exits.

## How to Test

Install the development dependencies:

```bash
python -m pip install -r requirements-dev.txt
```

Run the unit tests:

```bash
python -m unittest discover -s tests -v
```

The tests cover task creation, empty-title validation, task listing, deletion, and task report generation.

## DevSecOps Pipeline

GitHub Actions automates build validation, unit testing, and static application security testing.

The workflow is defined in `.github/workflows/devsecops.yml` and is triggered by:

- Push events to the `main` branch.
- Pull requests targeting the `main` branch.

### Pipeline Jobs

**1. Build and Unit Test (`build`)**

- Checks out the repository.
- Sets up Python 3.12.
- Installs development dependencies.
- Compiles Python files.
- Runs automated unit tests.

**2. SAST and Quality Gate (`sast-scan`)**

- Runs only after the `build` job succeeds.
- Uses Bandit to scan Python source code for potential security issues.
- Enforces a Quality Gate that fails if one or more High-severity findings are detected.
- Uploads the Bandit JSON report as a GitHub Actions artifact.

### Quality Gate Policy

The Quality Gate blocks the pipeline when Bandit reports findings with `HIGH` severity. Findings with other severity levels do not fail this specific gate and may still require review.

A successful pipeline means the configured build, unit tests, and Quality Gate have passed. It does not guarantee that the application is completely free of security vulnerabilities.

## Project Objective

This project demonstrates a basic DevSecOps pipeline by integrating automated build validation, unit testing, static security analysis, and a security Quality Gate into a GitHub repository.
