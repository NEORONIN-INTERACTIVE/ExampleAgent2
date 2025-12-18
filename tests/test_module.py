import pytest

from testing_agent import (TestingAgent)
from w4a import (Config)
from SimulationInterface import (Faction)

def test_create_agent():
    agent1 = TestingAgent(Faction.LEGACY, Config())
    agent2 = TestingAgent(Faction.DYNASTY, Config())
    assert(agent1.faction != agent2.faction)