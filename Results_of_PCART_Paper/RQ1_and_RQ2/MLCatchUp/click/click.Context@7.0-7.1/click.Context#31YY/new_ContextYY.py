import click
command = click.Command('my_command')
context = click.Context(command, None, None, None, auto_envvar_prefix=None, default_map=None, terminal_width=None, show_default=None)
