from inspect import cleandoc
import os

import pytest

from offprem import VirtualPrivateCloud, AWSPremise, ConfigureCredentials, ConfigureVPC, Profile


def vpc_list():
    """ List of VirtualPrivateCloud objects. """
    return [VirtualPrivateCloud(id='vpc_id1', name='vpc_name1', region='region_name1'),
            VirtualPrivateCloud(id='vpc_id2', name='vpc_name2', region='region_name2'),
            VirtualPrivateCloud(id='vpc_id3', name='vpc_name3', region='region_name3'),
            VirtualPrivateCloud(id='vpc_id4', name='vpc_name4', region='region_name4')]


def profile_list():
    """ List of Profile objects. """
    return [
        Profile(profile_name='account_with_mfa', source_profile=None, role_arn=None,
                mfa_serial='arn:aws:iam::RANDOM:mfa/USER'),
        Profile(profile_name='account_without_mfa', source_profile=None, role_arn=None, mfa_serial=None),
        Profile(profile_name='role_with_mfa', source_profile='account_with_mfa',
                role_arn='arn:aws:iam::RANDOM:role/ROLENAME', mfa_serial='arn:aws:iam::RANDOM:mfa/USER'),
        Profile(profile_name='role_without_mfa', source_profile='account_without_mfa',
                role_arn='arn:aws:iam::RANDOM:role/ROLENAME', mfa_serial=None),
            ]


@pytest.fixture(name='session_configuration_file')
def setup_config_and_credentials_files(tmp_path):
    config_file = tmp_path.joinpath('config')
    config_file_content = cleandoc(doc=
    """
    [profile account_with_mfa]
    region = us-west-2
    
    [profile account_without_mfa]
    region = us-west-2
    
    [profile role_with_mfa]
    region = us-east-2
    
    [profile role_without_mfa]
    region = us-west-2
    """)
    config_file.write_text(config_file_content)

    credentials_file = tmp_path.joinpath('credentials')
    configuration_file_content = cleandoc(doc=
    """
    [account_with_mfa]
    aws_access_key_id = ACCESS-KEY-ID
    aws_secret_access_key = SECRET-ACCESS-KEY
    mfa_serial = arn:aws:iam::RANDOM:mfa/USER

    [account_without_mfa]
    aws_access_key_id = ACCESS-KEY-ID
    aws_secret_access_key = SECRET-ACCESS-KEY

    [role_with_mfa]
    role_arn = arn:aws:iam::RANDOM:role/ROLENAME
    source_profile = account_with_mfa

    [role_without_mfa]
    role_arn = arn:aws:iam::RANDOM:role/ROLENAME
    source_profile = account_without_mfa
    """)
    credentials_file.write_text(configuration_file_content)

    os.environ['AWS_CONFIG_FILE'] = f'{config_file!s}'
    os.environ['AWS_SHARED_CREDENTIALS_FILE'] = f'{credentials_file!s}'

    yield credentials_file
    os.environ.pop('AWS_CONFIG_FILE')
    os.environ.pop('AWS_SHARED_CREDENTIALS_FILE')
    config_file.unlink()
    credentials_file.unlink()


@pytest.fixture
def session_configuration(session_configuration_file) -> ConfigureCredentials:
    # GIVEN a configuration file
    return ConfigureCredentials(configuration_file=session_configuration_file)


@pytest.fixture
def vpc_configuration(tmp_path) -> ConfigureVPC:
    # GIVEN a configuration file
    configuration_file = tmp_path.joinpath('environments.ini')
    return ConfigureVPC(configuration_file=configuration_file)


@pytest.fixture
def premise(session_configuration, vpc_configuration):
    # GIVEN a credentials file and environment file
    return AWSPremise(vpc_configuration=vpc_configuration, session_configuration=session_configuration)


@pytest.fixture
def proper_premise():
    # GIVEN a credentials file and environment file
    return AWSPremise()
