# TODO: import sys; detect venv with sys.prefix != sys.base_prefix
# TODO: print executable, YES/NO, and sys.prefix
# TODO: try importing arcade; print its path or NOT INSTALLED
import sys

in_venv = sys.prefix != sys.base_prefix

print("Python running this script:", sys.executable)
print("Inside a .venv?           :", "YES" if in_venv else "NO")
print("Its home folder           :", sys.prefix)

try:
    import arcade
    print("arcade found at           :", arcade.__file__)
except ModuleNotFoundError:
    print("arcade found at           : NOT INSTALLED for this Python")