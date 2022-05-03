import pandas as pd

def solution(df):
    d = {}
    for i in df.index:
        d1 = {}
        for j in df.index:
            if i != j:
                d1[j] = d1.get(j, 0) + round(sum([k ** 2 for k in list(df.loc[i] - df.loc[j])]) ** 0.5, 2)
        d[i] = sorted(d1.items(), key=lambda x: -x[1])[0]
    df['nearest_row'] = pd.Series(d).apply(lambda x: x[0])
    df['dist'] = pd.Series(d).apply(lambda x: int(round(x[1], 0)))
    return df