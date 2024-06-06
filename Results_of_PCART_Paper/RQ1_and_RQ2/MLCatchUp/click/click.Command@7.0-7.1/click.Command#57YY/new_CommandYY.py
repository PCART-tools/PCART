import click
command = click.Command('my_command', None, None, [click.Option(['--param'], default=42)], None, None, None, '[OPTIONS]', add_help_option=True, hidden=False, no_args_is_help=False)
