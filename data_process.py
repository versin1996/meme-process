import json
import re


cnt = 0
AD_WORDS = ['评论', '点赞', '追番', '关注', '关个注', '分享', '群', '白嫖', '比心', '比个心', '收藏', '支持', '作者']
dataApi2 = {}

result = {}
def isLongText(text):
	if len(','.join(text)) > 30:
		return True
	return False

def isAd(text):
	s = ' '.join(text)
	for ad_word in AD_WORDS:
		if ad_word in s:
			return True
	if re.findall('\d+话', ' '.join(text)):
		return True
	return False

def judge(img, texts):
	global cnt, dataApi2, result
	text_a, text_b = texts
	if isAd(text_a) or isAd(text_b):
		return [[], [text_a, dataApi2.get(img), text_b], 'code', 'ad']
	if isLongText(text_a) or isLongText(text_b):
		return [[], [text_a, dataApi2.get(img), text_b], 'code', 'other']
	if text_a == [] and text_b == []:
		return [[], [text_a, dataApi2.get(img), text_b], 'code', 'no_text']
	if text_a == text_b:
		return [text_a, [text_a, dataApi2.get(img), text_b], 'code', 'matched']
	if text_a == dataApi2[img]:
		if text_a == []:
			return [[], [text_a, dataApi2.get(img), text_b], 'code', 'no_text']
		else:
			return [text_a, [text_a, dataApi2.get(img), text_b], 'code', 'matched']
	if text_b == dataApi2[img]:
		if text_b == []:
			return [[], [text_a, dataApi2.get(img), text_b], 'code', 'no_text']
		else:
			return [text_b, [text_a, dataApi2.get(img), text_b], 'code', 'matched']
	cnt += 1
	
	print(img, text_a, dataApi2[img], text_b)
	modified_text_a = '||'.join(text_a)
	modified_text_b = '||'.join(text_b)
	modified_text_c = '||'.join(dataApi2[img])
	result[img] = [modified_text_a, modified_text_c, modified_text_b]
	if cnt % 200 == 0:
		writeData()
		result = {}
	return None

def writeData():
	with open('data/data_{}.json'.format(cnt), 'w') as f:
		json.dump(result, f)		

def main():
	resultByCoding = {}
	with open('ocr_result_all_API2.json', 'r', encoding='gbk') as f:
		lines = f.readlines()
		for line in lines:
			d = json.loads(line)
			for k, v in d.items():
				dataApi2[k] = v
	with open('result_all.json', 'r') as f:
		data = json.load(f)
	for k, v in data.items():
		res = judge(k, v)
		if res:
			resultByCoding[k] = res
	writeData()
	with open('resultByCoding.json', 'w') as f:
		json.dump(resultByCoding, f)


if __name__ == '__main__':
	main()