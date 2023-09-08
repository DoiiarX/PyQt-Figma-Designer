from overrides import override

from generator.python_generator.base_generator import BaseGenerator


class GroupGenerator(BaseGenerator):
    @override
    def generate_design(self):
        return []

    @override
    def generate_handler(self):
        return []

    @override
    def generate_controller(self):
        return []
