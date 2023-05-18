from torch.utils.data import Dataset
from PIL import Image
import os

class MyData(Dataset):

    '''
    初始化函数，用于读取文件的路径，train_dir指的是训练文件的路径，class_dir指的是哪一类
    self.path是训练文件和类名的拼接获得的路径,及类路径
    self.img_path指的是所有图片的路径，以list格式存储
    '''
    def __init__(self,train_dir,label_dir):
        self.train_dir = train_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.train_dir,self.label_dir)
        self.img_path = os.listdir(self.path)

    '''
    重写切片方法，会根据索引打开图片，并返回图片以及其对应的类别
    '''
    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_item_path = os.path.join(self.path,img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img,label

    def __len__(self):
        return len(self.img_path)


'''
测试一下获取蚂蚁和蜜蜂数据集
'''
root_dir = '数据集/hymenoptera_data/train'

ants_dir = 'ants'
ants = MyData(root_dir,ants_dir)
ant1_img,ants1_label = ants[0]
# ant1_img.show()
# print(ants1_label)

bees_dir = 'bees'
bees = MyData(root_dir,bees_dir)
bee1_img,bee1_label = bees[1]
# bee1_img.show()
# print(bee1_label)

train = ants+bees
# print(len(train))
img,label = train[123]
# img.show()
# print(label)
img2,label2 = train[234]
# img2.show()
# print(label2)

for i in ants.img_path:
    # print(i)
    name = i[:-4]#切片操作，切掉最后四个字符.jpg
    file = open(f"数据集/hymenoptera_data/train/ants_label/{name}.txt", "w")
    # 将字符串 "ants" 写入文件
    file.write("ants")
    # 关闭文件
    file.close()

for i in bees.img_path:
    # print(i)
    name = i[:-4]#切片操作，切掉最后四个字符.jpg
    file = open(f"数据集/hymenoptera_data/train/bees_label/{name}.txt", "w")
    # 将字符串 "ants" 写入文件
    file.write("bees")
    # 关闭文件
    file.close()