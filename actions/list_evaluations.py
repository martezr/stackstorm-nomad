from lib import action


class NomadListEvaluationsAction(action.NomadBaseAction):
    def run(self):
        return self.evaluations.get_evaluations()