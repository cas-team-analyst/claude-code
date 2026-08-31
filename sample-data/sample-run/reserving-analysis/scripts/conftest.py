import sys
import os

# Ensure the scripts/ directory is on sys.path so `from modules import ...` works
# regardless of which directory pytest is invoked from.
sys.path.insert(0, os.path.dirname(__file__))
