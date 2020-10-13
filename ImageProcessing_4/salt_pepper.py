import numpy as np
import random
 
def salt_pepper(intput_signal, probability):
    '''
    椒盐噪声算法（适用于灰度图）
    :param intput_signal: 输入信号矩阵（2D）
    :param probability: 噪声概率（如：0.1为10%）
    :return: 加噪后的图像、实际噪点数、理论噪点数
    '''
    nisy = [0, 255] # 噪声（salt， papper）
 
    m, n= intput_signal.shape  # 获取输入图片尺寸(行和列)
 
    intput_signal_cp = intput_signal.copy() # 输入信号的副本
    intput_signal_cp = intput_signal_cp.reshape(-1) # reshape为一个行向量
 
    # 该噪声概率下，理论上noisy_data_probability_num个数据点中1一个噪点
    noisy_data_probability_num = int(100 / (probability * 100))
 
    # 噪点数组，当数组中的值为1时，则认为对应的数据点为噪点
    noisy_data = []
    for i in range(m*n):
        noisy_data.append(random.randint(1, noisy_data_probability_num))
 
    # 实际噪点数与理论噪点数
    actual_noisy_data_num = 0
    theory_noisy_data_num = int(m * n * probability)
 
    # 添加噪点
    for i in range(m*n):
        if noisy_data[i] == 1:
            actual_noisy_data_num = actual_noisy_data_num + 1
            intput_signal_cp[i] = nisy[random.randint(0, 1)]
 
    # 重塑至m*n的矩阵
    intput_signal_cp = intput_signal_cp.reshape(m, n)
 
    return  intput_signal_cp, actual_noisy_data_num, theory_noisy_data_num
