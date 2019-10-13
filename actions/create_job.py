from lib import action
import nomad

class NomadParseJobAction(action.NomadBaseAction):
    def run(self,file):
        with open(file, "r") as fh:
            try:
                job_raw_nomad = fh.read()
                job_dict = self.nomad.jobs.parse(job_raw_nomad)
                output = {}
                output['Job'] = job_dict
                self.nomad.jobs.register_job(output)
            except nomad.api.exceptions.BadRequestNomadException as err:
                print(err.nomad_resp.reason)
                print(err.nomad_resp.text)
        return output