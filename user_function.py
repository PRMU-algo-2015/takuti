# coding:utf-8

import cv2 as cv
import numpy as np
import sys
import prmu

def user_function( lv, imlist_learn, imlist_test, imlist_result ):
  #
  # input
  # - lv,
  # - imlist_learn,  # prmu.ImageList
  # - imlist_test    # prmu.ImageList[3]
  #
  # output / input
  # - imlist_result, # prmu.ImageList[3] 結果情報の記録用
  #

  labels = np.array([prmu.LABEL_ASICS, prmu.LABEL_LECOQ, prmu.LABEL_MIZUNO, prmu.LABEL_SHUN, prmu.LABEL_YONEX, prmu.LABEL_FILA, prmu.LABEL_NB, prmu.LABEL_UA])

  for _lv in range(0,lv):
    for _i in range( 0, len( imlist_test[_lv] ) ):

      # アノテーション情報へのポインタ（イテレータ）
      # The pointer (actually iterator) of annotation information
      ite_test = imlist_test[_lv][_i]     # 入力用
      ite_result = imlist_result[_lv][_i] # 結果用

      # アノテーション情報にアクセスするには，(*ite_test).XXX や ite_test->XXX が使用できます．
      # The access to the annotation information (i.e., member variables and functions)
      # is performed by (*ite_test).XXX or ite_test->XXX

      # 学習用の画像情報へのポインタを取得
      # obtaining the pointer of annotation information that is used for learning
      ite_learn = imlist_learn[0]

      for n in range(len(ite_test.logo_list)):
        label = ite_test.logo_list[n].label
        bbox = ite_test.logo_list[n].bbox
        ite_result.append_result(label, bbox)

  return imlist_result;

