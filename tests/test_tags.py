from dataclasses import dataclass, field
import json

import pytest


@dataclass
class VPC:
    id: str = field(default='example')
    tags: list = field(default_factory=list)

    def __post_init__(self):
        self.tags = [{'Key': 'key_one', 'Value': 'value_one'}, {'Key': 'key_two', 'Value': 'value_two'}]
        pass


def test_save_tags(premise, vpc=VPC()):
    # TODO: Parametrize with an empty list.
    region = 'us-west-2'
    name = f'{vpc.id}|{region}'
    tags = premise.reformat_vpc_tags(vpc=vpc)

    premise.vpc_configuration.populate_configuration_file(vpc_id=vpc.id, name=name, region=region, tags=tags)
    premise.vpc_configuration.save_configuration_file()
    print('\n', premise.vpc_configuration.configuration_file.read_text())


@pytest.mark.skip(reason='Method not yet implemented.')
def test_load_tags(premise, vpc=VPC()):
    region = 'us-west-2'
    name = f'{vpc.id}|{region}'
    tags = premise.reformat_vpc_tags(vpc=vpc)

    premise.vpc_configuration.populate_configuration_file(vpc_id=vpc.id, name=name, region=region, tags=tags)
    premise.vpc_configuration.save_configuration_file()

    tags = premise.vpc_configuration.configuration_file_parser.get(section=name, option='tags')
    converted = json.loads(s=tags)
    print(converted)
