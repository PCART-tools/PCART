import plotly.graph_objects as go
import plotly.io as pio
fig = go.Figure(data=[go.Bar(y=[2, 3, 1])], layout_title_text='A Bar Chart')
pio.write_html(fig, file='bar_chart.html', config=None, auto_play=True, include_plotlyjs=True, include_mathjax=False, post_script=None, full_html=True, animation_opts=None, validate=True, default_width='100%', div_id=None)
