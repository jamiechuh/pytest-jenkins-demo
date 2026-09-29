import pytest

@pytest.fixture
def sample_data():
    return {"name": "jenkins", "value": 42}

def test_using_fixture(sample_data):
    assert sample_data["value"] == 42
