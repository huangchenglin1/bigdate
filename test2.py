import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["Fangsong"]
fashion_mnist = keras.datasets.fashion_mnist
(train_images,train_lables),(test_images,test_labels)=fashion_mnist.load_data()
class_names = ['T恤/上衣', '裤子', '套衫', '连衣裙', '外套','凉鞋', '衬衫', '运动鞋', '手提包', '踝靴']
train_images = train_images/255.0
test_images = test_images/255.0
new_model=keras.models.load_model("model/my_model1.h5")
test_loss,test_acc=new_model.evaluate(test_images,test_labels,verbose=2)
print("\nTest accuracy:{:5.22f}%".format(100*test_acc))
probability_model=tf.keras.Sequential([new_model,tf.keras.layers.Softmax()])
predictions=probability_model.predict(test_images)
plt.figure()
plt.subplot(1,2,1)
plt.xticks([])
plt.yticks([])
plt.imshow(test_images[0],cmap=plt.cm.binary)
plt.xlabel("{} 预测正确率：{:2.0f}%".format(class_names[np.argmax(predictions[0])],
                               100*np.max(predictions[0])),fontsize=20,color="blue")
plt.subplot(1,2,2)
plt.xticks(range(10),class_names)
plt.yticks([])
thisplot = plt.bar(range(10), predictions[0], color="#777777")
plt.ylim([0, 1])
predicted_label = np.argmax(predictions[0])

thisplot[predicted_label].set_color('blue')
# thisplot[true_label].set_color('blue')
plt.show()
print("模型预测的结果为：{}".format(class_names[np.argmax(predictions[12])]))


