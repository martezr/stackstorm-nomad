from lib import action


class NomadGetJobAction(action.NomadBaseAction):
    def run(self, node_id):
        return self.nomad.node.drain_node(node_id, enable=True)
