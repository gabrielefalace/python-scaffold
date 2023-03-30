# Generic Python Scaffold
A python scaffold for whatever project


# Installation

1. cd to the directory where requirements.txt is located
2. activate your virtualenv 
   * create the virtualenv with `python -m venv .` in the root folder
   * activate the virtualenv with `source bin/activate`
3. run: `pip3 install -r requirements.txt` in your shell
4. to exit the virtualenv `deactivate`

# Running tests
1. Running **tests** `python3 -m pytest test/test_main.py`
2. Running **doctests** `python3 -m doctest -v src/main.py`
3. Running tests with **coverage** `coverage run -m pytest test/test_main.py`
   * To see the coverage report, simply run: `coverage report`
4. Running **mutation test**, from root folder:
   * Init: `cosmic-ray init cosmic-ray-config.toml cosmic-ray-data.sqlite`
   * Baseline: `cosmic-ray --verbosity=INFO baseline cosmic-ray-config.toml`
   * Run Mutations: `cosmic-ray exec cosmic-ray-config.toml cosmic-ray-data.sqlite`
5. See mutation tests results: `cr-report cosmic-ray-data.sqlite --show-pending`
