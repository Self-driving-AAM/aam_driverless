import numpy as np
import cv2
import time
import argparse
import tensorflow as tf
import ros
"""
arguments:
x,y : dots for ROI origin
mul : multiply output steering
console : true for hiding the visual screen (in case you need to use SSH)
no_serial : true for rempving the option to send the output to the serial port
autogain : true for enabling auto-exposure

example of use in command line: python inference.py -x 220 -y 722 --console --autogain
"""


def parse_cli_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--x', '-x', help='enter left x', default=220, type=int)
    parser.add_argument('--y', '-y', help='enter low y', default=722, type=int)
    parser.add_argument('--mul', '-mul', help='enter multiply number for output steering', default=1, type=float)
    parser.add_argument('--console', dest='console', action='store_true')
    parser.add_argument('--no_serial', dest='no_serial', action='store_true')
    parser.add_argument('--autogain', dest='autogain', action='store_true')
    parser.set_defaults(console=False)
    args = parser.parse_args()
    return args


# init args and serial
args = parse_cli_args()

# set region of interest
# width = 1936 # original ids properties
# height = 1216 # original ids properties
width = 1496
height = 494
max_steering=255
# allocate memory
bitspixel = 24

# get data from camera and display
lineinc = width * int((bitspixel + 7) / 8)

# calculate fps
i = 0
sumi = 0
fps_q = []

# graph and session
graph = tf.Graph()
with graph.as_default():
    with tf.Session(graph=graph) as sess:
        with tf.gfile.FastGFile('./model_tf.pb', 'rb') as model_file:
            graph_def = tf.GraphDef()
            graph_def.ParseFromString(model_file.read())
        # init
        # choose ROI
        roi_x = 66
        roi_y = 200
        input_var = tf.placeholder("float32", [1, roi_x, roi_y, 3])
        [output_image] = tf.import_graph_def(graph_def, input_map={'input_1:0': input_var},
                                             return_elements=['output/Sigmoid:0'],
                                             name='')
        while True:

            startTime = time.time()
            image = ueye.get_data(mem_ptr, width, height, bitspixel, lineinc, copy=True)
            # from 1 dim to 3
            image = (np.reshape(image, (height, width, 3))).astype(float)
            # resize - cv2. we don't need crop (did it before)
            image_BGR = cv2.resize(image, (roi_y, roi_x))
            # convert to RGB
            image = image_BGR[..., ::-1]
            # normalization
            image /= 255.0
            img = np.expand_dims(image, axis=0)
            # inference
            pred = sess.run(output_image, feed_dict={input_var: img})
            steering_pred = max(0, int(((((pred[0][0]) - 0.5) * args.mul) + 0.5) * max_steering))
            steering_raw = str(min(255, steering_pred))

            # show on screen
            if (args.console == False):
                cv2.imshow('inference (q to exit)', image_BGR)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

            # send steering to serial port
            if args.no_serial == False:
                steering_str = '.' + steering_raw + '.\r\n'
                str_encode = steering_str.encode()

            endTime = time.time()
            # calculate fps
            fps_q.append(endTime - startTime)
            i += 1

            textLabel = "0"
            if i >= 30:
                sumi = 0
                del fps_q[0]
                for obj in fps_q:
                    sumi += obj
                textLabel = "fps: " + str(int(1 / (sumi / len(fps_q)))) + ", steering: " + steering_raw

            # present fps
            print(textLabel)

            # time.sleep(0.1)


if (args.console == False):
    cv2.destroyAllWindows()

# cleanup

