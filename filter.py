import json


# with open('data/data_200.json', 'r') as f: 
# 	data = json.load(f) 
# 	for k, v in data.items():
# 		print(k, v)  

fliter_no_text = '''噗 好 生气 ？ 刀 无奈 去 啪 难 捏 瓦 再见 奋斗 当 请 王 乖巧 不 瘦 加 视 愣住 震 原 
	量 合会 6 芬芳 人 嘻 目 可 我 你 他 它 啊 母 心 傀儡 是 呐 等 ! 日 吓 为 哎 嘿 嚣张 ● ■ 非 嫌 哈 什么 
	妙 别 吧 停'''.split()


fliter_other = '''哈哈 嘿嘿 你不用理我 说过的话不能不算数喔 噢大写的冷漠 咔擦 我差点笑出声 ??? 咔嚓 不生气 尴尬
	我现在没时间搞钱 威胁 诚实的孩子人人爱 人世间怎么会有 富强民主文明和谐 我和你说话你在 有点耐心 我他妈怎么就
	你是否有很多问号 忍住眼泪 你给老子滚 就这 对方不想和你说话 请你耐心 你看不见我 咔嚓 勉强达成共识 一般般的我一般般的帅
	我也想尿 和谐自由平等 嘻嘻 小朋发你是否有很影问号 我不要你觉得 你有什么让我喜欢的 嗯嗯嗯嗯 我璞不失态 悲痛
	靠靠靠靠靠靠靠 嘤嘤嘤 请强行解释 我有耐心 我从哪来 算了不生气 包教包会哄人技巧 我和你说话你在 不生气 尴尬
	给大佬端茶  你别和我讲道理 数钱 呵呵 请不要和我 气死我了 牛逼 这场面我真没见过 略略略 我是谁 整乐了
	小朋友 搞事 是开心 haha 我是說在座各位 贼几把 表示震惊 强行解释 帅炸了 不要生气 生气 吧唧 我在哪 讲道理
	杀人犯法 别骗我 整天就知道 不愧是我 算了 不骂人 能的话打钱 怂恐 祝大家 你有问题 我觉得 这是你应得的 惊叹三连
	不能骂人 纳入到你的 39米 拿生命开玩笑 我笑到 你有本事打我呀 南南南 开开眼界 令人窒息的操作 仙女 真诚的爱情
	我肯定不是脑残 甜甜蜜蜜 信不信我死你 我超帅 惊叹三连 在吗 鸭梨 气死我了 好吃的 信了呢 别逼我出手 说得好
	'''.split()

fliter_matched = '''
	 & 心鸭 (⊙o⊙) * 睡前玩把游戏 QQ红包 тиетЄХ ⊙ ⌒ ② ■ ●● 《 》 ★ 番 【 】 〣 ヒ
	1 2 3 4 5 6 7 8 9 0 @ A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 
	a b c d e f g h i j k l m n o p q r s t u v w x y z ä å æ ç è é
	一个取直的笑 一动漫 一场成 一把心泪 一开始只是 一点点 一脸红逼 七减一七减一七减一 七秀…坊的…女人 快来送我小心心吧
	三人结拜拜的关二爷 三分钟 三叶 秘境行侠久陨铁铸神兵 带月荷归玲珑藏指尖 三更五连结束了哦 三更达成 你最好给我解释一
	不像是在走廊啊 广播社的人朝你们那边去了 不对劲那个高木竟然将室内鞋暴露无遗 网 欢迎您 科室主任 结婚证 求心 ◎ 著
	南宁上林检察 更新 日更 社区 门 模式 全剧终 关键词 分界线 红包 社 留言 转账 $ @ # % ^ & * 函数 导数
	柘枝引 校医室 零位置 核心区 武谦樱 楼容景 板蓝根 公园 橡皮泥 每日小测试 每日一读 比个 气到头壳爆炸 求比 求求你
	没有水准又只会摆架子的老师在被我教训过之后 西片的念法是 制药 实验室 操作间 海康 更新 知乎 留个心 福康 秋田 第 券
	视频 语音 () 读者 记吃瓜 √ 采萧获 里葛程 青晓萌 冰火 一更 两更 三更 二更 个龟孙
	å”” 一伏特小霸王 日更 2 我就不告诉你想知道没门 å‘† æ ç›¯ 脸正经 分界线 茶 叶海 å 猛凌叼烟 千祠 衣角 准备好出门
	本结 关闭 红红 送我小心心 第一滴血 关机 放荡叉没礼貌的奸笑 ⌒⌒ 弄累不嚷 ä è 给个小心心 攻略读者 巡完这边巡那边
	我请你撸串 听说要上推荐 无所 U 这个嘛模拟测试还拿不到A 抱大福 邪魅狂狷 谁叫你连二分之一的中奖机率都抽不到 重
	解決方案 八卦六十四掌回天 化学 记得找我下单 让我们红尘作伴活得潇潇洒洒 反派一队发来贺电 记得比 日常校园青春
	就会产生特殊的意义 心鸭 宿舍 喜欢你好了。 这可真是太酷了 二哈男友 想听你语音 秋田六千 然悟 雁作呕 物品栏 3
	'''.split()

def isReprocessForAd(sents):
	for sent in sents:
		if sent and len(sent) == 1:
			if sent[0] == '比心':
				return True
	return False

def isReprocess(sents, fliter):
	for sent in sents:
		if sent:
			for s in sent:
				for f in fliter:
					if f in s:
						return True
	return False

def isReprocess2(sent, fliter):
	if sent:
		for s in sent:
			for f in fliter:
				if f in s:
					return True
	return False

def review_no_text():
	cnt = 0
	totol = 0
	result = {}
	with open('resultByCoding.json', 'r') as f:
		data = json.load(f)
		for k, v in data.items():
			if v[3] == 'no_text':
				totol += 1
				if isReprocess(v[1], fliter_no_text):
					value = ['||'.join(i) if i else '' for i in v[1]]
					print(value)
					result[k] = [value, 'reprocess_no_text']
					cnt += 1
	print(cnt, totol, cnt/totol*100)
	with open('test/no_text.json', 'w') as f:
		json.dump(result, f)

def review_others():
	cnt = 0
	totol = 0
	result = {}
	with open('resultByCoding.json', 'r') as f:
		data = json.load(f)
		for k, v in data.items():
			if v[3] == 'other':
				totol += 1
				if isReprocess(v[1], fliter_other):
					value = ['||'.join(i) if i else '' for i in v[1]]
					print(value)
					result[k] = [value, 'reprocess_other']
					cnt += 1
	print(cnt, totol, cnt/totol*100)
	with open('test/other.json', 'w') as f:
		json.dump(result, f)

def review_ad():
	cnt = 0
	totol = 0
	result = {}
	with open('resultByCoding.json', 'r') as f:
		data = json.load(f)
		for k, v in data.items():
			if v[3] == 'ad':
				totol += 1
				if isReprocessForAd(v[1]):
					value = ['||'.join(i) if i else '' for i in v[1]]
					result[k] = [value, 'reprocess_ad']
					cnt += 1
	print(cnt, totol, cnt/totol*100)
	with open('test/ad.json', 'w') as f:
		json.dump(result, f)

def review_matched():
	cnt = 0
	totol = 0
	result = {}
	with open('resultByCoding.json', 'r') as f:
		data = json.load(f)
		for k, v in data.items():
			if v[3] == 'matched':
				totol += 1
				if isReprocess2(v[0], fliter_matched):
					value = ['||'.join(i) if i else '' for i in v[1]]
					result[k] = [value, 'reprocess_matched']
					cnt += 1
	#print(result)
	print(cnt, totol, cnt/totol*100)
	for k, v in result.items():
		print(k, v)
	with open('test/matched.json', 'w') as f:
		json.dump(result, f)

if __name__ == '__main__':
	# review_no_text()
	# review_others()
	# review_ad()
	# review_matched()