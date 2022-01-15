def beginner_tactics(board, color, lst): # ���S�҃��[�u
  lst_quiet = [-7, -6, -5, -1, +1, +5, +6, +7]
  
  min_emp = 8
  for quiet in lst:
    if put_and_reverse(board, quiet, color):
      emp = 0
      for _ in range(len(lst_quiet)):
        neighbor = quiet + lst_quiet[_] # �ׂ荇���}�X�̍��W
        if neighbor >= 0 and neighbor <= 35:
          if put_and_reverse(board, neighbor, BLACK) or put_and_reverse(board, neighbor, WHITE):
            emp += 1 # �󔒂̐��𐔂���
      if emp < min_emp:
        min_emp = emp # �ׂ荇���}�X�ɋ󔒂����Ȃ���� min_emp ���X�V
        QUIET = quiet

  try:
    return QUIET # �ׂɋ󔒃}�X�����Ȃ��}�X�̍��W���o��
  except:
    return "Error" # �Ȃ��ꍇ�� "Error" �Əo�͂��Ď��̓���֐i��

def beginner_AI(board, color):
  lst_corner = [0, 5, 30, 35] # �p �I�X�X��Lv.5
  lst_edge = [2, 3, 12, 17, 18, 23, 32, 33] # �ǉ��� �I�X�X��Lv.4
  lst_circle = [8, 9, 13, 16, 19, 22, 26, 27] # ���̕� �I�X�X��Lv.3
  lst_C = [1, 4, 6, 11, 24, 29, 31, 34] # C���C��(�p�̏㉺���E��) �I�X�X��Lv.2
  lst_X = [7, 10, 25, 28] # X���C��(�p�̎΂ߗ�) �I�X�X��Lv.1

  lst_all = [lst_corner, lst_edge, lst_circle, lst_C, lst_X]

  for i in range(len(lst_all)):
    position = beginner_tactics(board, color, lst_all[i])
    if position == "Error":
      pass
    else:
      return position

  return 0