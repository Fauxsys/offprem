import pytest

from conftest import vpc_list


@pytest.mark.parametrize(argnames='vpc', argvalues=vpc_list(), ids=repr)
def test_populate_configuration_file(vpc_configuration, vpc):
    # WHEN I add a VPC
    vpc_configuration.populate_configuration_file(vpc_id=vpc.id, name=vpc.name, region=vpc.region)
    # THEN the configuration file should have the VPC
    actual = vpc_configuration.query(vpc_name=vpc.name)

    assert actual.id == vpc.id
    assert actual.region == vpc.region


@pytest.mark.parametrize(argnames='vpcs', argvalues=[vpc_list()], ids=repr)
def test_list_environments(vpc_configuration, vpcs):
    # WHEN I add a VPC
    for vpc in vpcs:
        vpc_configuration.populate_configuration_file(vpc_id=vpc.id, name=vpc.name, region=vpc.region)
    # THEN list the available VPCs
    expected = [vpc.name for vpc in vpcs]
    assert vpc_configuration.configuration_file_parser.sections() == expected
