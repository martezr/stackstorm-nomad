from lib import action


class NomadGetJobAction(action.NomadBaseAction):
    def run(self, name):
        return self.job.get_job(name)