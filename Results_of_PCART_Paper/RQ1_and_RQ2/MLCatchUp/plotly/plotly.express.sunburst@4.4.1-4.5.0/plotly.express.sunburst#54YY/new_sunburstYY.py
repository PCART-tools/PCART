import plotly.express as px
data = dict(character=['Eve', 'Cain', 'Seth', 'Enos', 'Noam', 'Abel', 'Awan', 'Enoch', 'Azura'], parent=['', 'Eve', 'Eve', 'Seth', 'Seth', 'Eve', 'Eve', 'Awan', 'Eve'], value=[10, 14, 12, 10, 2, 6, 6, 4, 4])
fig = px.sunburst(data, names='character', values='value', parents='parent', ids=None, color=None, color_continuous_scale=None, range_color=None, color_continuous_midpoint=None, path=None)
