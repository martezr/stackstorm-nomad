from lib import action


class NomadGetJobAction(action.NomadBaseAction):
    def run(self, name):
        return self.nomad.job.get_job(name)