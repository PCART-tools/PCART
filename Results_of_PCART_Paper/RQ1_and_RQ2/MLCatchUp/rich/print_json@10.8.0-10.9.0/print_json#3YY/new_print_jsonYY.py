from rich.console import Console
console = Console(json=None, data=None, indent=2)
json_str = '{"name": "John", "age": 30, "city": "New York"}'
console.print_json(json_str, highlight=True, json=None, data=None, indent=2)
