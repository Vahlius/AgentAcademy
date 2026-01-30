# test_agentacademy.py
"""
Tests for AgentAcademy module.
"""

import unittest
from agentacademy import AgentAcademy

class TestAgentAcademy(unittest.TestCase):
    """Test cases for AgentAcademy class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AgentAcademy()
        self.assertIsInstance(instance, AgentAcademy)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AgentAcademy()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
