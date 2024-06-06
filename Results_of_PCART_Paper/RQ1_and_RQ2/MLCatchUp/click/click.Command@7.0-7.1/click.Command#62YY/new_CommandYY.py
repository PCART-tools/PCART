import click
command = click.Command('my_command', None, None, params=[click.Option(['--param'], default=42)], help=None, epilog=None, short_help=None, options_metavar='[OPTIONS]', add_help_option=True, hidden=False, no_args_is_help=False)
