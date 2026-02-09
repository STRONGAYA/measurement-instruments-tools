"""Test that all subpackages can be imported correctly."""

import sys
import os

# Add the test environment setup
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestPackageImports:
    """Test that all subpackages are properly included in the package."""

    def test_import_top_level_package(self):
        """Test that the top-level package can be imported."""
        import strongaya_instruments

        assert strongaya_instruments is not None

    def test_import_proms_subpackage(self):
        """Test that the proms subpackage can be imported."""
        from strongaya_instruments import proms

        assert proms is not None

    def test_import_hcproms_subpackage(self):
        """Test that the hcproms subpackage can be imported."""
        from strongaya_instruments import hcproms

        assert hcproms is not None

    def test_import_other_subpackage(self):
        """Test that the other subpackage can be imported."""
        from strongaya_instruments import other

        assert other is not None
