import click
command = click.Command('my_command')
context = click.Context(command, None, None, None, None, default_map=None, show_default=None)
