import plotly.offline as py
import plotly.graph_objs as go


class Artists:

    def __init__(self):
        pass

    def draw_line_continuous(self, x, y, x_alias='x_axis', y_alias='y_axis'):
        trace = go.Scatter(
            x=x,
            y=y,
            mode='lines+markers',
        )

        data = [trace]
        py.plot(data, filename=x_alias + '_vs_' + y_alias + '_line.html', auto_open=True)

    def draw_bar_discontinuous(self, x, y, x_alias='x_axis', y_alias='y_axis'):
        trace = go.Bar(
            x=x,
            y=y
        )

        data = [trace]
        py.plot(data, filename=x_alias + '_vs_' + y_alias + '_bar.html', auto_open=True)


if __name__ == "__main__":
    # Examples
    Artists().draw_line_continuous([1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], 'age_of_property', 'value_of_property')
    Artists().draw_bar_discontinuous([1, 2, 3, 4, 5, 6], [2, 4, 6, 8, 10, 12], 'age_of_property', 'value_of_property')
