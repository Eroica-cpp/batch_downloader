import urllib

def get_url_list():
	begin_num = 4439
	end_num = 5064
	head = "http://210.39.3.84:2014/2014%E5%B1%8A%E6%AF%95%E4%B8%9A%E5%85%B8%E7%A4%BC/%E4%BC%A0%E6%92%AD/%E7%89%B9%E5%86%99/"
	
	url_list = []
	for i in range(begin_num, end_num+1, 1):
		url = head + "IMG_%d.JPG" % i
		url_list.append(url)
	
	return url_list

def main():
	url_list = get_url_list()

	path = "./data/"
	testfile = urllib.URLopener()
	for url in url_list:
		filename = url.split("/")[-1]
		testfile.retrieve(url, path+filename)
		print "retrieving:", url

if __name__ == "__main__":
	main()