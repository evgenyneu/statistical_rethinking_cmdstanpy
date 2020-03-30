data {
  int w;  // Number of water counts
  int l;  // Number of land counts
}

parameters {
  real<lower=0,upper=1> p;   // Proportion of water
}

model {
  p ~ uniform(0, 1); // Uniform prior
  w ~ binomial(w + l, p);  // Binomial likelihood
}
