from flask import render_template, request
from flask import jsonify
import json
import io
import os
import time
import base64
import random


def getImgData(imgFile):
	path = '/nas/xd/data/huameng/meme/all/'
	imgFile = io.BytesIO(open(path+imgFile, 'rb').read())
	img = base64.b64encode(imgFile.getvalue()).decode('ascii')
	return img

def getData():
    global DATA, FILENAMES, OPENFILE
    path = '/home/versin/ocr2/'
    sepFiles = os.listdir(path + 'data')
    sepFiles = [file.split('_')[1] for file in sepFiles]
    resFiles = os.listdir(path + 'result')
    resFiles = [file.split('_')[1] for file in resFiles]
    files = list(set(sepFiles) - set(resFiles))
    files.sort()
    print(files)
    if files:
        fileName = 'data/data_{}'.format(files[0])
        print(fileName)
        with open(fileName, 'r') as f:
            data = json.load(f)
            imgFiles = list(data.keys())
            return data, fileName, imgFiles
            
    else:
        print('Done!')
        exit()

def index():
	return render_template('index.html')

MODIFY = {}
showData = json.load(open('final_result/final_result.json', 'r'))
imgFiles = list(showData.keys())
def show():
	num = 8
	count = range(num)
	selectFiles = random.sample(imgFiles, num)
	selectData = [(file, showData[file]) for file in selectFiles]
	imgs = [getImgData(imgFile) for imgFile in selectFiles]
	return render_template('show.html', count=count, data=selectData, imgs=imgs)

def modify():
	global showData, MODIFY
	fileName = request.form['fileName']
	content = request.form['content']
	flag = request.form['flag']
	MODIFY[fileName] = [content, showData[fileName][1], 're', flag]
	print(MODIFY)
	return jsonify({'OK': True})

def saveModification():
	global MODIFY
	with open('temp/modify_{}.json'.format(time.time()), 'w') as f:
		json.dump(MODIFY, f)
	return jsonify({'OK': True})

CNT = 0
RESULT = {}
DATA, FILENAME, IMGFILES = getData()
def manipulate():
	global DATA, CNT, FILENAME, OPENFILE
	data = {}
	imgs = []
	for i in range(CNT, CNT+3):
		if i < len(IMGFILES):
			data[IMGFILES[i].strip('.jpg')] = DATA[IMGFILES[i]][0]
			imgs.append(getImgData(IMGFILES[i]))
	CNT += 3
	return render_template('manipulate.html', data=data, imgs=imgs, cnt=CNT-2, openFile=FILENAME)

def getContent():
    global DATA, RESULT, CNT
    fileName = request.form['fileName'] + ".jpg"
    content = request.form['content']
    flag = request.form['flag']
    RESULT[fileName] = [content, DATA[fileName][0], DATA[fileName][1], flag]
    print(CNT - 2, fileName, RESULT[fileName])
    return jsonify({'OK': True})

def check():
    global IMGFILES, RESULT, DATA
    if len(RESULT) == len(DATA):
        return True, []
    resFiles = RESULT.keys()
    temp = list(range(len(DATA)))
    for index, file in enumerate(IMGFILES):
        if file in resFiles:
            temp.remove(index)
    temp = [i+1 for i in temp]
    return False, temp

def prev():
    global CNT
    if CNT >= 6:
        CNT -= 6
        return jsonify({'CODE': 200})
    else:
        return jsonify({'CODE': 404})

def save():
    flag, unfinished = check()
    if flag:
        global RESULT, OPENFILE, CNT
        with open('result/result_{}'.format(OPENFILE), 'w') as f:
            json.dump(RESULT, f)
        print('Result saved!')
        CNT = 0
        RESULT = {}
        removeFile(FILENAMES)
        getData()
        return jsonify({'CODE': 200})
    else:
        with open('temp/temp.json', 'w') as f:
            json.dump(RESULT, f)
        print('Unfinished:', unfinished)
        return jsonify({'CODE': 404, 'UNFINISHED': unfinished})    


