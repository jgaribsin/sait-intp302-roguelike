
from .attributes import Attributes
from .talent import Talent
from .course import CourseManager
from .job import JobManager
from .social import SocialManager
from .investigation import InvestigationSystem

class Player:
    def __init__(self, name: str, talent: Talent):
        self.name = name
        self.attributes = Attributes()
        self.talent = talent
        self.talent.apply_modifiers(self.attributes)
        
        # sub-managers for different systems
        self.course_manager = CourseManager()
        self.job_manager = JobManager()
        self.social_manager = SocialManager()
        self.investigation = InvestigationSystem()

        # other attributes
        self.gpa = 0.0
        self.suspicion = 0

    def _update_attributes(self, changes):
        for attr, value in changes.items():
            if hasattr(self.attributes, attr):
                new_value = getattr(self.attributes, attr) + value
                # make sure the value is within the valid range
                if attr == "stamina":
                    new_value = max(0, new_value)
                elif attr in ["intelligence", "social"]:
                    new_value = min(100, new_value)
                setattr(self.attributes, attr, new_value)

    