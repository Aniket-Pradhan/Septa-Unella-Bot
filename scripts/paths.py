from pathlib import Path

class paths:

    def init_local_paths(self):
        self.root = str(Path(__file__).parent.parent)

    def __init__(self):
        self.init_local_paths()
