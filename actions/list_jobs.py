from lib import action


class NomadListJobsAction(action.NomadBaseAction):
    def run(self):
        return self.nomad.jobs.get_jobs()
