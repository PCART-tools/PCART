import click
command = click.Command('my_command')
context = click.Context(command, None, None, None, auto_envvar_prefix=None, default_map=None, terminal_width=None, max_content_width=None, resilient_parsing=False, show_default=None)
