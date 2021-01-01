from lib import action


class NomadListPeersAction(action.NomadBaseAction):
    def run(self):
        return self.nomad.status.peers.get_peers()
