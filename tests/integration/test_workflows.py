"""Integration tests for the complete scoring workflows."""

import pandas as pd
import numpy as np
import sys
import os

# Import test environment setup
test_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, test_dir)

# Add src directory to path
src_dir = os.path.join(os.path.dirname(test_dir), "src")
sys.path.insert(0, src_dir)
