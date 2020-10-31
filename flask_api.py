import numpy as np
import tensorflow as tf
from model import *

import pandas as pd
import os
import scipy
from scipy.io import loadmat
import re
import string
from utils import *
import random
import time
import argparse
batch_size = 64
image_size = 64 
import warnings
warnings.filterwarnings('ignore')
checkpoint_dir = './checkpoint'
dictionary_path = './dictionary'
vocab = np.load(dictionary_path + '/vocab.npy')
print('there are {} vocabularies in total'.format(len(vocab)))
z_dim = 512 
c_dim = 3   
word2Id_dict = dict(np.load(dictionary_path + '/word2Id.npy'))
id2word_dict = dict(np.load(dictionary_path + '/id2Word.npy'))

@app.route('/')
def index():
  return  render_template('index.html')
@app.route("/predict", methods=['POST'])
def predict():

    #print("lolllllll")

   # print(us_canada_user_rating_pivot)

    if request.method == 'POST':
          try:
           # model_knn = joblib.load("./recommender_model.pkl")
            #data = request.get_json()
            #years_of_experience = float(data["yearsOfExperience"])

           # us_canada_user_rating = pd.read_csv('/home/siddanath/python_project/recommender_api/testcorrect_csv.csv')
           # us_canada_user_rating_pivot = us_canada_user_rating.pivot(index = 'bookTitle', columns = 'userID', values = 'bookRating').fillna(0)
            ni = int(np.ceil(np.sqrt(batch_size)))
            save_dir = "checkpoint"
            with open("_vocab.pickle", 'rb') as f:
               vocab = pickle.load(f)
            t_real_image = tf.placeholder('float32', [batch_size, image_size, image_size, 3], name = 'real_image')

            t_real_caption = tf.placeholder(dtype=tf.int64, shape=[batch_size, None], name='real_caption_input')
            t_z = tf.placeholder(tf.float32, [batch_size, z_dim], name='z_noise')
            generator_txt2img = model.generator_txt2img_resnet

            net_rnn = rnn_embed(t_real_caption, is_train=False, reuse=False)
            net_g, _ = generator_txt2img(t_z,net_rnn.outputs,is_train=False, reuse=False, batch_size=batch_size)
            sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True))
            tl.layers.initialize_global_variables(sess)

            net_rnn_name = os.path.join(save_dir, 'net_rnn.npz')
            net_cnn_name = os.path.join(save_dir, 'net_cnn.npz')
            net_g_name = os.path.join(save_dir, 'net_g.npz')
            net_d_name = os.path.join(save_dir, 'net_d.npz')
            net_rnn_res = tl.files.load_and_assign_npz(sess=sess, name=net_rnn_name, network=net_rnn)

            net_g_res = tl.files.load_and_assign_npz(sess=sess, name=net_g_name, network=net_g)

            sample_size = batch_size
            sample_seed = np.random.normal(loc=0.0, scale=1.0, size=(sample_size, z_dim)).astype(np.float32)
            namequery1 = request.form['namequery1']
            namequery2 = request.form['namequery1']
            namequery3 = request.form['namequery1']
            namequery4 = request.form['namequery1']
            namequery5 = request.form['namequery1']
            namequery6 = request.form['namequery1']
            namequery7 = request.form['namequery1']
            namequery8 = request.form['namequery1']
            sample_sentence = [str(namequery1)] * int(sample_size/ni) + \
            [str(namequery2)] * int(sample_size/ni) + \
            [str(namequery3)] * int(sample_size/ni) + \
            [str(namequery4)] * int(sample_size/ni) + \
            [str(namequery5)] * int(sample_size/ni) + \
            [str(namequery6)] * int(sample_size/ni) + \
            [str(namequery7)] * int(sample_size/ni) + \
            [str(namequery8)] * int(sample_size/ni)



            for i, sentence in enumerate(sample_sentence):
                print("seed: %s" % sentence)
                sentence = preprocess_caption(sentence)
                sample_sentence[i] = [vocab.word_to_id(word) for word in nltk.tokenize.word_tokenize(sentence)] + [vocab.end_id] # add END_ID

            sample_sentence = tl.prepro.pad_sequences(sample_sentence, padding='post')

            img_gen, rnn_out = sess.run([net_g_res.outputs, net_rnn_res.outputs], feed_dict={t_real_caption : sample_sentence,t_z : sample_seed})
            print("notpj")
            save_images(img_gen, [ni, ni], 'static/gen_samples/gen.png')
            print("ok")




            full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'gen.png')
          except ValueError:
                   return jsonify("Please enter a number.")
          return render_template("results.html", user_image = full_filename)

if __name__ == '__main__':
    app.run(debug=True)
