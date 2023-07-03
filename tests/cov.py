import pytest

pytest.main([
    "-x",
    "pytest --cov-report html  --cov-report term-missing --cov=ulist",
    "tests/"]
)
