class JobManager:
    JOBS = {
        "Tutor": {"income": 15, "intelligence": 5},
        "Barista": {"income": 10, "mood": 10}
    }

    def __init__(self):
        self.current_job = None
        self.weekly_income = 0

    def set_job(self, job_name):
        if job_name in self.JOBS:
            self.current_job = job_name
            self.weekly_income = self.JOBS[job_name]["income"]
            return True
        return False

    def work(self):
        if not self.current_job:
            return None
        return {
            "finance": self.weekly_income,
            "stamina": -10,
            **self.JOBS[self.current_job]
        }