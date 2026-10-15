
# SecureTask

SecureTask is a simple Python command-line application for managing tasks.

## Features
- Create tasks with validated titles.
- List all tasks.
- Retrieve tasks by ID.
- Delete tasks.
- Run automated unit tests.

## Technology Stack
- Python 3.12
- Python standard library
- unittest for unit testing
- Bandit for Static Application Security Testing (SAST)
- GitHub Actions for CI/CD automation

## Project Structure
- `app/main.py`: Main command-line interface
- `app/task_service.py`: Task business logic
- `app/validators.py`: Input validation
- `app/storage.py`: In-memory task storage
- `tests/test_tasks.py`: Automated unit tests
- `.github/workflows/devsecops.yml`: CI/CD workflow

## Requirements
Python 3.12 or a compatible Python 3 version.

## How to Run
Clone this repository and open the project directory.

Run the application:

```bash
python -m app.main
```

## How to Test
Run the unit tests:

```bash
python -m unittest discover -s tests -v
```

## DevSecOps Pipeline
GitHub Actions runs when code is pushed to the `main` branch or when a pull request targets `main`.

The `build` job compiles Python files and runs unit tests.
After the build succeeds, the `sast-scan` job scans the application source code using Bandit.

The Quality Gate fails if a High-severity security finding is detected.
The SAST report is uploaded as a workflow artifact.

This pipeline automates build validation, testing, and static security analysis.
