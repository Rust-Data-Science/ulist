EXIT_STATUS=0

echo "Building..."
cd ../ulist && maturin develop|| EXIT_STATUS=$?
echo "\n"

echo "Generating doc..."
cd ../docs && pdoc --html ulist.core || EXIT_STATUS=$?
echo "\n"

echo "Exit status code $EXIT_STATUS!" 
exit $EXIT_STATUS
