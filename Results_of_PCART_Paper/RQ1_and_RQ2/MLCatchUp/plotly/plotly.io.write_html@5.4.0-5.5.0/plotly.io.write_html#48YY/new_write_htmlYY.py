import plotly.graph_objects as go
import plotly.io as pio
fig = go.Figure(data=[go.Bar(y=[2, 3, 1])], layout_title_text='A Bar Chart')
pio.write_html(fig, 'bar_chart.html', None, True, include_plotlyjs=True, include_mathjax=False, post_script=None, full_html=True, animation_opts=None, div_id=None)
