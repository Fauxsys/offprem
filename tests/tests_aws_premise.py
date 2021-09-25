import pytest

from conftest import vpc_list, profile_list

@pytest.mark.skip(reason='Expects configuration files for ConfigureVPC and ConfigureCredentials exists.')
@pytest.mark.parametrize(argnames='profile_name', argvalues=profile_list(), ids=repr)
def test_premise_assign(proper_premise, profile_name):
    proper_premise.assign(profile_name=profile_name)
    assert proper_premise.session


@pytest.mark.skip(reason='botocore.exceptions.ClientError: InvalidClientTokenId. Also need to determine how to capture input()')
@pytest.mark.parametrize(argnames='profile', argvalues=profile_list(), ids=repr)
@pytest.mark.parametrize(argnames='vpc', argvalues=vpc_list(), ids=repr)
def test_constructor(premise, profile, vpc):
    assert premise.assign(profile_name=profile.profile_name, vpc_name=vpc.name)


@pytest.mark.skip(reason='Method not yet implemented.')
def test_premise_assign_environment_v2(premise):
    # WITH a vpc name
    vpc_name = 'account_without_mfa'
    # THEN assign the vpc name to Premise
    premise.vpc(name=vpc_name)


# TODO:
#  Create a populated_configuration_file fixture to test proper_premise.assign(profile_name=profile_name, vpc=name)
#  Alternatively, this might be better implemented in the application than the library.
