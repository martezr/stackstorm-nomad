from lib import action
import nomad


class NomadValidateJobAction(action.NomadBaseAction):
    def run(self,file):
        with open(file, "r") as fh:
            try:
                job_raw_nomad = fh.read()
                job_dict = self.nomad.validate.validate_job(job_raw_nomad)
            except nomad.api.exceptions.BadRequestNomadException as err:
                print(err.nomad_resp.reason)
                print(err.nomad_resp.text)
        return job_dict
