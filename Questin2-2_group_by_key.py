df = pd.DataFrame(input)

data = df.groupby(['keyword']).sum()

ans = data.to_dict()
return ans['value']