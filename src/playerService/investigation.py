class InvestigationSystem:
    def __init__(self):
        self.clues = []
        self.suspect = None

    def add_clue(self, clue):
        self.clues.append(clue)

    def analyze(self):
        clue_counts = {}
        for clue in self.clues:
            clue_counts[clue] = clue_counts.get(clue, 0) + 1
        self.suspect = max(clue_counts, key=clue_counts.get) if clue_counts else None
        return self.suspect