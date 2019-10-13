from lib import action


class NomadListDeploymentsAction(action.NomadBaseAction):
    def run(self):
        return self.deployments.get_deployments()