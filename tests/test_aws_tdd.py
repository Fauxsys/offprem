""" Test Driven Development. """
import pytest


@pytest.fixture
def profiles() -> dict:
    production = 'production'
    staging = 'staging'
    qa = 'qa'
    return {'production': production, 'staging': staging, 'qa': qa}


@pytest.mark.skip(reason='Method not yet implemented.')
def test_add_profile(environment, profiles):
    production = profiles['production']
    environment.add_profile(production)
    assert environment.profile == [production]


@pytest.mark.skip(reason='Method not yet implemented.')
def test_add_profiles(environment, profiles):
    add_profiles = list(profiles.values())
    environment.add_profiles(add_profiles)
    assert environment.profile == add_profiles


@pytest.mark.skip(reason='Method not yet implemented.')
def test_primary_profile(environment, profiles):
    add_profiles = list(profiles.values())
    environment.add_profiles(add_profiles)
    assert environment.primary_profile == add_profiles[0]


@pytest.mark.skip(reason='Method not yet implemented.')
def test_no_primary_profile(environment):
    assert environment.primary_profile is None


@pytest.mark.skip(reason='Method not yet implemented.')
def test_no_primary_profile(environment):
    with pytest.raises(IndexError) as error:
        environment.primary_profile
    assert 'list index out of range' == f'{error.value!s}'


@pytest.mark.skip(reason='Method not yet implemented.')
def test_compare_environments_with_configuration_file(api, environments_file):
    api = api(configuration_file=configure_vpc)
    api.compare('vpc name 1', 'vpc name 2', 'vpc name 3')


@pytest.mark.skip(reason='Method not yet implemented.')
def test_compare_environments_with_Environment_objects(api, environment):
    # WHEN I compare multiple environments
    api.compare(environment, environment, environment)
    # THEN


@pytest.mark.skip(reason='Method not yet implemented.')
def test_firewall_rules(api, environment):
    api.security_groups(environment=environment)


@pytest.mark.skip(reason='Method not yet implemented.')
def test_inventory_output(api, environment):
    api.inventory(environment=environment, detailed=False)


@pytest.mark.skip(reason='Method not yet implemented.')
def test_inventory_detailed_output(api, environment):
    api.inventory(environment=environment, detailed=True)
