from lib import action


class NomadGetLeaderAction(action.NomadBaseAction):
    def run(self):
        return self.status.leader.get_leader()