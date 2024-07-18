# json_repair

This is a Python package for repairing JSON string.

# Test code when pull request

```bash
python -m unittest discover -s tests -v
```

# Uploaded to PyPI
```bash
python setup.py sdist bdist_wheel
twine upload  --skip-existing dist/*
```