import pandas as pd

__all__ = ['quantile_norm']

def quantile_norm(s, quantiles_number):

    res = s.copy()
    res[:] = None

    for i in range(0, quantiles_number):
        quant_inf = float(s.quantile(float(i) / quantiles_number))
        quant_sup = float(s.quantile((i + 1.) / quantiles_number))
        res = res.where(~((s >= quant_inf) & (s < quant_sup)), other = (s - quant_inf) / (quant_sup - quant_inf))



