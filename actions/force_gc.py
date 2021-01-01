from lib import action


class NomadForceGcAction(action.NomadBaseAction):
    def run(self):
        return self.nomad.system.initiate_garbage_collection()
