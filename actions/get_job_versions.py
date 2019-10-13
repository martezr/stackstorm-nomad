from lib import action


class NomadGetJobVersionsAction(action.NomadBaseAction):
    def run(self, name):
        return self.job.get_versions(name)