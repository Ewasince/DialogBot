import command_system


def test(input_, **kwargs):
    print('not filled')


test_command = command_system.Command()

test_command.keys = ['test', 't']
test_command.description = 'developer testing command'
test_command.process = test
test_command.kwargs = {}
