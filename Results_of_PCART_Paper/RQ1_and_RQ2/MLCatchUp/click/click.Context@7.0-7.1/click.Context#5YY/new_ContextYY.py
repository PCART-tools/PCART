import click
command = click.Command('my_command')
context = click.Context(command=command, parent=None, show_default=None)
