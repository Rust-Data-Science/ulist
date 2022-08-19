. ./check_version.sh

EXIT_STATUS=0

check_version || EXIT_STATUS=$?

echo "Running clippy..."
cargo clippy --manifest-path ../ulist/Cargo.toml -- -D warnings|| EXIT_STATUS=$?
echo "\n"

echo "Running unit tests..."
pytest ../tests|| EXIT_STATUS=$?
echo "\n"

echo "Running flake8..."
flake8 ../tests|| EXIT_STATUS=$?
flake8 ../ulist/python|| EXIT_STATUS=$?
echo "\n"

echo "Running mypy..."
mypy ../tests|| EXIT_STATUS=$?
mypy ../ulist/python|| EXIT_STATUS=$?
echo "\n"

echo "Exit status code $EXIT_STATUS!" 
exit $EXIT_STATUS
