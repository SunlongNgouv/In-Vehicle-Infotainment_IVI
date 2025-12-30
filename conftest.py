from ivi_qa_framework.src.ivi_system import IVISystem
import pytest

@pytest.fixture
def ivi_system():
    return IVISystem()