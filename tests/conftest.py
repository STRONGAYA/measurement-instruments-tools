"""Test fixtures and configuration for the STRONG AYA instruments test suite."""

import pytest
import pandas as pd
import numpy as np
import sys
import os

# Add current directory to path and import test environment setup
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Import test environment setup
import test_env  # noqa: F401 E402

# Add src directory to path
src_dir = os.path.join(os.path.dirname(current_dir), "src")
sys.path.insert(0, src_dir)


@pytest.fixture
def real_example_data():
    """Load the real example data from the repository."""
    example_path = os.path.join(
        os.path.dirname(__file__), "example_data", "test_data.csv"
    )
    if os.path.exists(example_path):
        return pd.read_csv(example_path)
    return None
