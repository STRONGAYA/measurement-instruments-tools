"""Mock environment setup for testing without external dependencies."""

import sys
import os
from unittest.mock import MagicMock

# Add src to path for testing
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(os.path.dirname(current_dir), "src")
sys.path.insert(0, src_dir)

# Create mock functions
