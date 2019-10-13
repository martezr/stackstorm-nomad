from lib import action


class NomadParseJobAction(action.NomadBaseAction):
    def run(self):
        with open("example.nomad", "r") as fh:
            try:
                job_raw_nomad = fh.read()
                job_dict = self.nomad.jobs.parse(job_raw_nomad)
            except nomad.api.exceptions.BadRequestNomadException as err:
                print(err.nomad_resp.reason)
                print(err.nomad_resp.text)
        return job_dict