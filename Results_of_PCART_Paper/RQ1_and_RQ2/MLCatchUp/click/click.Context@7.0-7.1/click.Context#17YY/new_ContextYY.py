import click
command = click.Command('my_command')
context = click.Context(command, None, None, obj=None, auto_envvar_prefix=None, show_default=None)
