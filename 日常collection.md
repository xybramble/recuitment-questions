平方损失函数MSE主要针对回归类型的问题。  

二叉树的性质  
二叉树是结点的有限集合。二叉树的定义时递归的，根结点的子树仍然是二叉树，到达空子树时递归定义结束。  
二叉树不是树！  
二叉树具有以下五个性质：  
在二叉树的第ｉ（ｉ>=１）层最多有２＾(ｉ - １)个结点。  
深度为k(k>=0)的二叉树最少有k个结点，最多有２＾ｋ－１个结点。  
对于任一棵非空二叉树，若其叶结点数为n0，度为2的非叶结点数为n2，则ｎ0 = ｎ2 ＋１。  
具有n个结点的完全二叉树的深度为int_UP（log(2，ｎ+1)）。  
如果将一棵有n个结点的完全二叉树自顶向下，同一层自左向右连续给结点编号１，２，３，．．．．．．，ｎ，然后按此结点编号将树中各结点顺序的存放于一个一维数组，并简称编号为i的结点为结点i（ ｉ>=１ && ｉ<=ｎ）,则有以下关系：  
（1）若 ｉ= 1，则结点i为根，无父结点；若 ｉ> 1，则结点 i 的父结点为结点int_DOWN（ｉ / ２）;  
（2）若 ２＊ｉ <= ｎ，则结点 ｉ 的左子女为结点 ２＊ｉ；  
（3）若２＊ｉ＜＝ｎ，则结点ｉ的右子女为结点２＊ｉ＋１；  
（4）若结点编号ｉ为奇数，且ｉ！＝１，它处于右兄弟位置，则它的左兄弟为结点ｉ－１；  
（5）若结点编号ｉ为偶数，且ｉ！＝ｎ，它处于左兄弟位置，则它的右兄弟为结点ｉ＋１；  
（6）结点ｉ所在的层次为 int_DOWN（log（2，ｉ））＋１。  

极大似然估计，就是把我们观察到每个样本所对应的误差的概率乘到一起，然后试图调整参数以最大化这个概率的乘积。  
极大似然估计，就是利用已知的样本结果，反推最有可能（最大概率）导致这样结果的参数值。  

PCA算法的具体操作为对所有的样本进行中心化操作,计算样本的协方差矩阵,然后对协方差矩阵做特征值分解,取最大的n个特征值对应的特征向量构造投影矩阵。  

AUC衡量一个推荐系统能够在多大程度上将用户喜欢的商品与不喜欢的商品区分开来。  

