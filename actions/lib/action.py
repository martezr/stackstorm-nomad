import nomad
from st2common.runners.base_action import Action


class NomadBaseAction(Action):

    def __init__(self, config):
        super(NomadBaseAction, self).__init__(config)
        self.nomad = self._get_client()

    def _get_client(self):
        url = self.config['url']
        token = self.config['token']
        verify = self.config['verify']
        region = self.config['region']

        client = nomad.Nomad(host=url, token=token, verify=verify, region=region )
        return client