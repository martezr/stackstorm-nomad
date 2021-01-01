from lib import action


class NomadGetPoliciesAction(action.NomadBaseAction):
    def run(self):
        return self.nomad.acl.get_policies()
