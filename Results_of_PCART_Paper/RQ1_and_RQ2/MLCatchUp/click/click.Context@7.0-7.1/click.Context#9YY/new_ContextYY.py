import click
command = click.Command('my_command')
context = click.Context(command=command, parent=None, info_name=None, show_default=None)
