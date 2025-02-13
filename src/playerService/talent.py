from abc import ABC, abstractmethod

class Talent(ABC):
    @abstractmethod
    def apply_modifiers(self, attributes):
        pass

class AcademicTalent(Talent):
    def apply_modifiers(self, attributes):
        attributes.intelligence += 20

class SocialTalent(Talent):
    def apply_modifiers(self, attributes):
        attributes.social += 60

class SurvivalistTalent(Talent):
    def apply_modifiers(self, attributes):
        attributes.stamina += 20