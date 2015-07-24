def new(num_buckets = 256):
	aMap = []
	for i in range(0,num_buckets):
		aMap.append([])
	return aMap

def hash_key(aMap, key):
	return hash(key) % len(aMap)

def get_bucket(aMap, key):
	bucket_id = hash_key(aMap,key)
	return aMap[bucket_id]

def  get_slot(aMap, key, default = None):
	bucket = get_bucket(aMap, key)
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
	return -1, key, default


def set(aMap,key,value):
	bucket = get_bucket(aMap, key)
	i, k ,v = get_slot(aMap, key)
	if i >= 0:
		bucket[i] = (key, value)
	else :
		bucket.append((key, value))

def get(aMap,key,default = None):
	i, k ,v = get_slot(aMap,key,default = default)
	return v
	
def list(aMap):
	for  bucket in aMap:
		if bucket:
			for k, v in bucket:
				print k, v
				