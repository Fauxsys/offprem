import pytest


def test_get_all_vpcs_requires_parameters(premise):
    with pytest.raises(AssertionError) as error:
        premise.get_all_vpcs()
    assert 'get_all_vpcs requires either search_tags or empty_tags to be set.' == f'{error.value}'
