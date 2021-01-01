from lib import action


class NomadListDeploymentsAction(action.NomadBaseAction):
    def run(self):
        return self.nomad.deployments.get_deployments()
