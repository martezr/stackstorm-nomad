from lib import action


class NomadGetLeaderAction(action.NomadBaseAction):
    def run(self):
        return self.nomad.status.leader.get_leader()
