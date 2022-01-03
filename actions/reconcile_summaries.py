from lib import action


class NomadReconcileSummariesAction(action.NomadBaseAction):
    def run(self):
        return self.nomad.system.reconcile_summaries()