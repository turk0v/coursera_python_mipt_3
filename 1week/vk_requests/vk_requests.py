#this is vk_API (library) version
import vk
from datetime import datetime
from collections import Counter


def calc_age(uid):

	session = vk.Session(access_token='3b7851b73b7851b73b7851b7b53b1dc29233b783b7851b7601412084a582d4458eb9df6')
	vk_api = vk.API(session)
	my_id = (vk_api.users.get(user_id=uid,fields='bdate',v=5.52))[0]

	friends_list = vk_api.friends.get(user_id=uid,fields='bdate',v=5.52)['items']
	bdate_list=[]
	age_list=[]

	for i in range(len(friends_list)):
		if ('bdate' in friends_list[i]) and (len(friends_list[i]['bdate'])>5):
			bdate_list.append(friends_list[i]['bdate'])
		else:
			pass
	#getting dd.mm.yyyy friends only

	for i in range(len(bdate_list)):
		age_list.append(2018-datetime.strptime(bdate_list[i],'%d.%m.%Y').year)
	#getting ages(in years) of friends

	age_dist = Counter(age_list)
	return(age_dist.most_common()) 


if __name__ == '__main__':
	res = calc_age('reigning')
	print(res)
    
