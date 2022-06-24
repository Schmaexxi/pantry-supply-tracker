echo "Checking with black"
black --check .

echo "Checking with flake8"
flake8 --max-line-length=100 ./src/pantry_supply_tracker

echo "Checking with mypy"
mypy --strict ./src/pantry_supply_tracker
