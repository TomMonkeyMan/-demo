from hmm_cut import *
from maxmatch import *
from max_ngram import *
from biward_ngram import *
import time

hmm_cuter = HmmCut()
maxmatch_cuter = CutWords()
maxngram_cuter = MaxProbCut()
biwardngram_cuter = BiWardNgram()

a="习近平总书记指出，中国利用外资的政策不会变，对外商投资企业合法权益的保护不会变，为各国企业在华投资兴业提供更好服务的方向不会变。"
print(hmm_cuter.cut(a))
print(maxmatch_cuter.max_forward_cut(a))
print(maxmatch_cuter.max_backward_cut(a))
print(maxmatch_cuter.max_biward_cut(a))
print(maxngram_cuter.cut(a))
print(biwardngram_cuter.cut(a))