# test_cardanonode.py
"""
Tests for CardanoNode module.
"""

import unittest
from cardanonode import CardanoNode

class TestCardanoNode(unittest.TestCase):
    """Test cases for CardanoNode class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CardanoNode()
        self.assertIsInstance(instance, CardanoNode)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CardanoNode()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
