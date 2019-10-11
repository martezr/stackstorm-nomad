from lib import action


class NomadListAllocationsAction(action.NomadBaseAction):
    def run(self):
        return self.allocations.get_allocations()