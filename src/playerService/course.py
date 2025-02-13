class CourseManager:
    def __init__(self):
        self.courses = {"Programming": {"Basics": True, "OOP": False}}
        self.study_hours = 0

    def study(self, hours):
        self.study_hours += hours
        return {
            "intelligence": hours * 2,
            "stamina": -hours * 3
        }