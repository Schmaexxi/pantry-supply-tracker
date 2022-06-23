echo "Checking with black"
black --check .

echo "Checking with flake8"
flake8 --max-line-length=88 .

echo "Checking with mypy"
mypy --strict ./pantry_supply_tracker
