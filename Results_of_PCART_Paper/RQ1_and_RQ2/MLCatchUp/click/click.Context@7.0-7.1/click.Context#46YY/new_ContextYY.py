import click
command = click.Command('my_command')
context = click.Context(command, None, None, None, None, None, None, None, resilient_parsing=False, show_default=None)
