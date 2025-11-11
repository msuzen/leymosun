pip -e uninstall leymosun
python -m build .
pip install -e .[test]
