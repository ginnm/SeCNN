# 测试集里有24%的数据出现在了训练集中
train_code = "train/code"
train_nl = "train/nl"
test_code = "test/code"
test_nl = "test/nl"
train_code = [each for each in open(train_code).readlines()]
train_nl  = [each for each in open(train_nl).readlines()]
train = ["".join(each) for each in list(zip(train_code,train_nl))]
test_code = [each for each in open(test_code).readlines()]
test_nl  = [each for each in open(test_nl).readlines()]
test = ["".join(each) for each in list(zip(test_code,test_nl))]
mem = set()
for each in train:
    mem.add(each)
count = 0
for each in test:
    if each in mem:
        count += 1
print(count / len(test))
