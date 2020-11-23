class Solution:
    def mid_square_rng(self, N: int, X0: int) -> list:
        result = []
        for i in range(N):
            tmp = X0
            result.append(self.normalization(tmp, 10000))
            X1 = X0 ** 2 % 1000000 // 100
            X0 = X1
        return result

    def lehmer_rng(self, N: int, m: int, a: int, b: int, X0: int) -> list:
        result = []
        for i in range(N):
            tmp = X0
            result.append(self.normalization(tmp, m))
            X1 = (a * X0 + b) % m
            X0 = X1
        return result

    def normalization(self, X: int, modulus: int) -> float:
        if X >= modulus: return 1
        elif X <= 0: return 0
        else: return X/modulus

    def main(self, N: int, m: int, a: int, b:int, seed: int):

        file = open('2d.txt', 'x')
        file = open('2d.txt', 'a')
        result = self.lehmer_rng(N, m, a, b, seed)
        for i in range(N):
            char = str(result[i]) + '\t'
            file.write(char)
        file = open('2d.txt', 'r')
        print(file.read())
        return


case = Solution()
d = case.lehmer_rng(5000, 2 ** 31, 2 ** 16 + 3, 0, 1)
import seaborn as sns
import matplotlib.pyplot as plt
#sns.set_style('darkgrid')
#sns.histplot(d)

#for i in range(4998):
#    plt.scatter(d[i],d[i+1],d[i+2])

#plt.show()

ax = plt.figure().add_subplot(111, projection='3d')
xs = d[0:4998]
ys = d[1:4999]
zs = d[2:5000]
# 基于ax变量绘制三维图
# xs表示x方向的变量
# ys表示y方向的变量
# zs表示z方向的变量，这三个方向上的变量都可以用list的形式表示
# m表示点的形式，o是圆形的点，^是三角形（marker)
# c表示颜色（color for short）
ax.scatter(xs, ys, zs, c='r', marker='.')  # 点为红色三角形

# 设置坐标轴
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

# 显示图像
plt.show()

ax = plt.figure().add_subplot(111, projection='3d')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')