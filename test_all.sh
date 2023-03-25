# Run DocTests
python3 -m doctest -v src/main.py

# Run regular tests with coverage
coverage run -m pytest test/test_main.py
coverage report

# Run mutation tests
cosmic-ray init cosmic-ray-config.toml cosmic-ray-data.sqlite
cosmic-ray exec cosmic-ray-config.toml cosmic-ray-data.sqlite

