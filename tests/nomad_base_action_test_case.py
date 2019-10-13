import yaml
import json
import logging

from st2tests.base import BaseActionTestCase


class NomadBaseActionTestCase(BaseActionTestCase):
    __test__ = False

    def setUp(self):
        super(NomadBaseActionTestCase, self).setUp()

        logging.disable(logging.CRITICAL)  # disable logging
        self._config_good = self.load_yaml('config_good.yaml')
        self._config_blank = self.load_yaml('config_blank.yaml')

    def tearDown(self):
        super(NomadBaseActionTestCase, self).tearDown()
        logging.disable(logging.NOTSET)  # enable logging

    def load_yaml(self, filename):
        return yaml.safe_load(self.get_fixture_content(filename))

    def load_json(self, filename):
        return json.loads(self.get_fixture_content(filename))

    @property
    def config_good(self):
        return self._config_good

    @property
    def config_blank(self):
        return self._config_blank