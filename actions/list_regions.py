from lib import action


class NomadListRegionsAction(action.NomadBaseAction):
    def run(self):
        return self.nomad.regions.get_regions()