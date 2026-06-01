import sys
import os

# Add the scripts directory to sys.path so `from modules import ...` works
# when pytest is invoked from the repo root.
SCRIPTS_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "skills", "reserving-analysis", "scripts")
)
sys.path.insert(0, SCRIPTS_DIR)
