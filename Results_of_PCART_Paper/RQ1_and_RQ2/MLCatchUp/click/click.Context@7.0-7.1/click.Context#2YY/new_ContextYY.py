import click
command = click.Command('my_command')
context = click.Context(command=command, show_default=None)
