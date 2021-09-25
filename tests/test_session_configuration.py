import pytest

from offprem.offprem import SecurityTokenService

from conftest import profile_list


@pytest.mark.parametrize(argnames='profile', argvalues=profile_list(), ids=repr)
def test_credentials_query(session_configuration, profile):
    # WHEN I query the configuration file for a profile
    actual_profile = session_configuration.query(profile_name=profile.profile_name)
    # THEN it should return a Profile object
    assert actual_profile == profile


@pytest.mark.skip(reason='botocore.exceptions.ClientError: InvalidClientTokenId. Also need to determine how to capture input()')
@pytest.mark.parametrize(argnames='profile', argvalues=profile_list(), ids=repr)
def test_sts_credentials(session_configuration, profile):
    # WHEN I query the configuration file for a profile
    profile = session_configuration.query(profile_name=profile.profile_name)
    # WHEN I pass the profile into SecurityTokenService
    sts_credentials = SecurityTokenService(profile=profile)
    # THEN I should be provided with temporary credentials
    assert sts_credentials


@pytest.mark.parametrize(argnames='profiles', argvalues=[profile_list()], ids=repr)
def test_list_environments(session_configuration, profiles):
    # WHEN a credentials file is properly populated
    # THEN list the available environments
    expected = [profile.profile_name for profile in profiles]
    assert session_configuration.configuration_file_parser.sections() == expected
