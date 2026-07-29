from scipy import stats

group1 = [12.92, 13.88, 13.30, 13.74, 12.60]
group2 = [18.58, 17.54, 18.60, 17.30, 18.62]
group3 = [16.04, 14.62, 16.30, 15.70, 16.38]

f_stat, p_value = stats.f_oneway(group1, group2, group3)
print(f"F = {f_stat:.4f}, p = {p_value:.4f}")

from statsmodels.stats.multicomp import pairwise_tukeyhsd

data = group1 + group2 + group3

labels = (
    ["A"] * len(group1) +
    ["B"] * len(group2) +
    ["C"] * len(group3)
)

tukey = pairwise_tukeyhsd(data, labels)
print(tukey)

