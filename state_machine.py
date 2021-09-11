

class State:

    def __init__(self, name, transitions=[]):
        self.name = name
        self.transitions = transitions

    def add_transition(self, transition):
        self.transitions.append(transition)

    def get_transitions(self):
        return self.transitions


    def __str__(self) -> str:
        return '<State %s>' % self.name


class StateMachine:

    def __init__(self) -> None:
        self.states = {}
        self.active_state = None


    def add_state(self, state: State) -> None:
        self.states[state.name] = state

    def set_active_state(self, state_name: str) -> None:
        self.active_state = self.get_state_by_name(state_name)

    def get_active_state(self) -> State:
        return self.active_state

    def get_state_by_name(self, state_name: str) -> State:
        return self.states[state_name]

    def run(self, input_value: str = None, arguments={}):
        for transition in self.active_state.get_transitions():
            if input_value is not None and input_value == transition['input']:
                result = transition['handler'](**arguments)
                self.set_active_state(transition['next_state'])
                return result

            elif input_value is None:
                result = transition['handler'](**arguments)
                self.set_active_state(transition['next_state'])
                return result

            



def say_hello(name: str) -> str:
    return 'Hello {}'.format(name)


def say_goodbye(name: str) -> str:
    return 'Goodbye {}'.format(name)


def say_something(name: str) -> str:
    return 'Umm {}'.format(name)


def main():
    states = [
        State('A', [
            {'input': 'Hello', 'handler': say_hello, 'next_state': 'B'},
            {'input': 'Goodbye', 'handler': say_goodbye, 'next_state': 'C'},
        ]),
        State('B', [
            {'input': 'World', 'handler': say_something, 'next_state': 'A'},
        ]),
        State('C', [
            {'input': 'My name', 'handler': say_something, 'next_state': 'A'},
        ]),
    ]

    
    machine = StateMachine()
    for state in states:
        machine.add_state(state.name, state)

    machine.set_active_state('A')
    while True:
        user_input = input('Enter something: ')
        argument = input('Your name?: ')
        print(machine.run(user_input, {'name': argument}))
        print(machine.get_active_state().name)



if __name__ == '__main__':
    main()

