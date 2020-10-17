import json


result = {}
with open('final_result/final_result.json', 'r') as f:
	data = json.load(f)
	for k, v in data.items():
		if isinstance(v[0], list):
			v[0] = '||'.join(v[0])
		if '_' in v[2]:
			v[2] = 'r_' + v[2].split('_')[1]
		result[k] = v

with open('final_result/final_result2.json', 'w') as f:
	json.dump(result, f)

