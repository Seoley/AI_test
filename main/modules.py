import numpy as np
import tensorflow as tf
import json
import pandas as pd
import random

# 부정맥 판단 모델
class CAtest():
    def __init__(self, metrics, length, sets, file):
        self.metrics = metrics
        self.length = int(length)
        self.sets = int(sets)
        self.data = pd.read_csv(file)
        self.model = tf.keras.models.load_model('static/model/CAModel_v1.3_acc0.76_rec0.75_221101.h5')
        # self.pred_classes = ['정상','비정상']
        print("Load ECG model")
        
    def get_result(self):

        loss_list = []
        metric_list = []

        x_data = self.data.iloc[:,:-1]
        y_data = self.data.iloc[:,-1]

        x_data = np.array(x_data)
        y_data = np.array(y_data)

        x_data = x_data.reshape(-1,125,1)
        y_data = tf.keras.utils.to_categorical(y_data,2)

        loss_count = 0
        metric_count = 0
        for i in range(self.sets):
            rand_length = random.randint(0,len(x_data)-self.length)
            data_length = self.length
            sample_list = range(rand_length-300,rand_length)
            sample_list = list(sample_list)

            x_target = x_data[rand_length:rand_length+data_length]
            y_target = y_data[rand_length:rand_length+data_length]

            loss, metric_val = self.model.evaluate(x_target.astype(np.float32),y_target.astype(np.float32))
            
            loss_list.append(loss)
            metric_list.append(metric_val)

            loss_count = loss_count + loss
            metric_count = metric_count + metric_val

        avg_loss = loss_count/self.sets
        avg_metric = metric_count/self.sets
        
        return loss_list, metric_list, avg_loss, avg_metric
    
# 심부전 판단 모델
class HFtest():
    def __init__(self, metrics, length, sets, file):
        self.metrics = metrics
        self.length = int(length)
        self.sets = int(sets)
        self.data = pd.read_csv(file)
        self.model = tf.keras.models.load_model('static/model/HFModel_v1.2_acc0.86_221021.h5')
        # self.pred_classes = ['정상','비정상']
        print("Load ECG model")
        
    def get_result(self):

        loss_list = []
        metric_list = []

        x_data = self.data.iloc[:,:-1]
        y_data = self.data.iloc[:,-1]

        x_data = np.array(x_data)
        y_data = np.array(y_data)

        x_data = x_data.reshape(-1,125,1)
        y_data = tf.keras.utils.to_categorical(y_data,2)

        loss_count = 0
        metric_count = 0
        for i in range(self.sets):
            rand_length = random.randint(0,len(x_data)-self.length)
            data_length = self.length
            sample_list = range(rand_length-300,rand_length)
            sample_list = list(sample_list)

            x_target = x_data[rand_length:rand_length+data_length]
            y_target = y_data[rand_length:rand_length+data_length]

            loss, metric_val = self.model.evaluate(x_target.astype(np.float32),y_target.astype(np.float32))
            
            loss_list.append(loss)
            metric_list.append(metric_val)

            loss_count = loss_count + loss
            metric_count = metric_count + metric_val

        avg_loss = loss_count/self.sets
        avg_metric = metric_count/self.sets
        
        return loss_list, metric_list, avg_loss, avg_metric
    
