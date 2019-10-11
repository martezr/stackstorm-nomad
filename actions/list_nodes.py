from lib import action


class NomadListNodesAction(action.NomadBaseAction):
    def run(self):
        return self.nomad.nodes.get_nodes()