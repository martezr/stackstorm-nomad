from lib import action


class NomadListEvaluationsAction(action.NomadBaseAction):
    def run(self):
        return self.nomad.evaluations.get_evaluations()
