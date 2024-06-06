import click
command = click.Command('my_command')
context = click.Context(command, None, None, None, None, default_map=None, terminal_width=None, max_content_width=None, show_default=None)
