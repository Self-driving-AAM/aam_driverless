import cv2
import pandas as pd # data analysis toolkit - create, read, update, delete datasets
from sklearn.model_selection import train_test_split #to split out training and testing data
#keras is a high level wrapper on top of tensorflow (machine learning library)
#The Sequential container is a linear stack of layers
from keras.models import Sequential
#popular optimization strategy that uses gradient descent
from keras.optimizers import Adam
#to save our model periodically as checkpoints for loading later
from keras.callbacks import ModelCheckpoint
#what types of layers do we want our model to have?
from keras.layers import Lambda, Conv2D, MaxPooling2D, Dropout, Dense, Flatten, Input
#helper class to define input shape and generate training images given image paths & steering angles
from utils import INPUT_SHAPE, batch_generator
#for command line arguments
import argparse
#for reading files
import os
import numpy as np #matrix math
import os
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras import Model

import pandas as pd  # data analysis toolkit - create, read, update, delete datasets
import numpy as np  # matrix math
from sklearn.model_selection import train_test_split  # to split out training and testing data
# The Sequential container is a linear stack of layers
from utils import INPUT_SHAPE, batch_generator, load_image
# for reading files
import os
#for debugging, allows for reproducible (deterministic) results
np.random.seed(0)


def load_data(args):
    """
    Load training data and split it into training and validation set
    """
    #reads CSV file into a single dataframe variable
    data_df = pd.read_csv(os.path.join(os.getcwd(), args.data_dir, 'data.csv'), names=['center', 'steering'])

    #yay dataframes, we can select rows and columns by their names
    #we'll store the camera images as our input data
    X = data_df[['center']].values
    #and our steering commands as our output data
    y = data_df['steering'].values


    #X_train, X_valid, y_train, y_valid = train_test_split(X, y, test_size=args.test_size, random_state=0)

    #return X_train, X_valid, y_train, y_valid

    return X,y




def build_model(args):
    activation = 'relu'
    model = Sequential()
    model.add(Input(shape=(1)))
    model.add(Dense(4, activation='relu'))
    model.add(Dense(3, activation='relu'))
    model.add(Dense(2, activation='relu'))
    model.add(Dense(1,activation="sigmoid"))
    model.summary()

    return model

def norm(data):
    return (data - -3.0) * (1.0 - 0.0) / (3.0 - -3.0) + 0
def norm2(data):
    return norm((data - 0) * (3 - -3) / (1 - 0) + -3)
def train_model(model, args, x, y):
    y=np.array([norm(float(x)) for x in y])
    print("data =",len(x))
    print("  ",max(y)   , max(x))
    print("  ",min(y)   , min(x))
    print(y[1000:1020])
    print(x[1000:1020])
    print("  ",max(y)   , max(x))
    print("  ",min(y)   , min(x))

    import matplotlib.pyplot as plt


    plt.plot(x[1000:1020])
    plt.show()



    print("val =",len(y))
    checkpoint = ModelCheckpoint('models/model-{epoch:03d}.h5',
                                 monitor='accuracy',
                                 verbose=0,
                                 save_best_only=True,
                                 mode='auto')
    model.compile(loss=tf.keras.losses.MAE, optimizer='adam', metrics=['accuracy'])
    print("sahape ", x.shape)
    model.fit(x=x,y=y,
            epochs=1000,

            steps_per_epoch=2000,
                        callbacks=[checkpoint],
                        verbose=1)

#for command line args
def s2b(s):
    """
    Converts a string to boolean value
    """
    s = s.lower()
    return s == 'true' or s == 'yes' or s == 'y' or s == '1'


def main():
    """
    Load train/validation data set and train the model
    """
    parser = argparse.ArgumentParser(description='Behavioral Cloning Training Program')
    parser.add_argument('-d', help='data directory',        dest='data_dir',          type=str,   default='d')
    parser.add_argument('-t', help='test size fraction',    dest='test_size',         type=float, default=0.2)
    parser.add_argument('-k', help='drop out probability',  dest='keep_prob',         type=float, default=0.2)
    parser.add_argument('-n', help='number of epochs',      dest='nb_epoch',          type=int,   default=100)
    parser.add_argument('-s', help='samples per epoch',     dest='samples_per_epoch', type=int,   default=20000)
    parser.add_argument('-b', help='batch size',            dest='batch_size',        type=int,   default=40)
    parser.add_argument('-o', help='save best models only', dest='save_best_only',    type=s2b,   default='true')
    parser.add_argument('-l', help='learning rate',         dest='learning_rate',     type=float, default=1.0e-4)
    args = parser.parse_args()

    #print parameters
    print('-' * 30)
    print('Parameters')
    print('-' * 30)
    for key, value in vars(args).items():
        print('{:<20} := {}'.format(key, value))
    print('-' * 30)

    #load data
    data = load_data(args)
    #build model



    local_weights_file = 'model(1).h5'

    model = tf.keras.models.load_model(local_weights_file)
    for layer in model.layers[:-3]:
        layer.trainable = False

    # (66, 200, 3)

    model.summary()


    img=np.array([load_image("d",d) for d in data[0]])[..., ::-1]/255
    print(len(img))
    # Window name in which image is displayed
    window_name = 'image'

    # Using cv2.imshow() method
    # Displaying the image


    # closing all open windows
    print(img.shape)
    x=model.predict(img)
    print(data[1][0])
    #cv2.imshow('window', img[0])

    #cv2.waitKey(0)  # waits until a key is pressed
    #cv2.destroyAllWindows()
    model = build_model(args)
    #train model on data, it saves as model.h5
    train_model(model, args, x,data[1])
if __name__ == '__main__':
    main()

