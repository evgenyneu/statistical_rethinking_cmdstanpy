from cmdstanpy import CmdStanModel
from tarpan.cmdstanpy.summary import print_summary

model = CmdStanModel(stan_file="stan_model/ex02.06.stan")

data = dict(w=6, l=3)
fit = model.sample(data=data, show_progress=True)
print_summary(fit)
