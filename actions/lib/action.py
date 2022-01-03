import nomad
from st2common.runners.base_action import Action


class NomadBaseAction(Action):

    def __init__(self, config):
        super(NomadBaseAction, self).__init__(config)
        self.nomad = self._get_client()

    def _get_client(self):
        host = self.config['host']
        token = self.config['token']
        verify = self.config['verify']
        region = self.config['region']
        secure = self.config['secure']

        client = nomad.Nomad(host=host, token=token, secure=secure, verify=verify, region=region )
        return client