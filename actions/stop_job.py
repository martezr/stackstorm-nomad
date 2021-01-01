from lib import action


class NomadStopJobAction(action.NomadBaseAction):
    def run(self, name):
        return self.nomad.job.deregister_job(name)
