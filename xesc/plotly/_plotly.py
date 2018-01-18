# -*- coding: utf-8 -*-
from plotly.offline import plot
import plotly.graph_objs as go

__all__ = ['plotline']

def plotline(x, y, filename, text=None, title=None, xaxis=None, yaxis=None):
    """
    Plota una línia utilitzant plotly

    Parametres:
    ----------
    x: Eix de x
    y: Eix de y
    filename: Nom del fitxer html amb el plots
    text (opcional): Afegeix variables de text. La longitud ha de ser la mateixa que les variables x i y
    title (opcional): Títol del gràfic
    xaxis (opcional): Títol de l'eix X
    yaxis (opcional): Títol de l'eix Y
    """

    trace = go.Scatter(x=x, y=y, mode='lines')

    if text is not None:
        trace.text = text

    data = [trace]

    layout = go.Layout()

    if title:
        layout.title = title
    if xaxis:
        layout.xaxis.title = xaxis
    if yaxis:
        layout.yaxis.title = yaxis

    fig = go.Figure(data=data, layout=layout)

    plot(fig, filename=filename)

