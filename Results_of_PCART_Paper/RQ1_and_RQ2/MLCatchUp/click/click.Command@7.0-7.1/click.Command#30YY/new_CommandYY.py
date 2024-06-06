import click
command = click.Command('my_command', None, None, [click.Option(['--param'], default=42)], None, epilog=None, short_help=None, no_args_is_help=False)
