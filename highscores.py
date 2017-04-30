import requests
import json

def leads(name, score):

	arg = {"name":name, "score":score}

	try:
		r = requests.get("http://128.226.244.161/leaderboards.py", params = arg, timeout=10)
	except requests.ConnectTimeout:
		print('Our servers are down.')
		return('')

	return r.json()

def sortList(scores):
	n = [['' for i in range(2)] for j in range(len(scores))]

	used = []
	for i in n:
		largest = 0
		largestkey = ''
		for j in scores:
			if(j not in used and int(scores[j]) > largest):
				largest = int(scores[j])
				largestkey = j
		i[0] = largestkey
		i[1] = str(largest)
		used.append(largestkey)

	return n

def main():
	x = input('Please enter your name: ')
	t = input('Score: ')

	newj = leads(x, t)
	if(newj != ''):
		newj = json.loads(newj)
		newj = sortList(newj)
		print(newj)

main()
