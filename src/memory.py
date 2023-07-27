class Memory:
    def __init__(self, config):
        self.config = config

        self.plan = []
        self.make_plan = True

        self.dependencies = ""

        self.errors = 0

        self.states = []

        self.objetives = []
        self.error_objetives = []

        self.commited_files = []

    def reset_states(self):
        self.errors = 0
        self.states = []
