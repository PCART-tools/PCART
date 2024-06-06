import click
command = click.Command('my_command', None, None, [click.Option(['--param'], default=42)], None, None, None, '[OPTIONS]', True, False, no_args_is_help=False)
