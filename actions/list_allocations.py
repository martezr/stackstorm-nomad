from lib import action


class NomadListAllocationsAction(action.NomadBaseAction):
    def run(self):
        return self.nomad.allocations.get_allocations()