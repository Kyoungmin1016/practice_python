# 문제
# 암호화 방식 중에는 소수를 이용하는 것들이 많다. 보통은 매우 큰 두 개의 소수를 선택하고, 두 소수를 곱한 값을 암호화에서의 키로 사용하고는 한다. 이러한 방법이 좋은 이유는 일반적으로 매우 큰 수를 소인수분해 하는 것이 어렵기 때문이다.

# 소수를 택할 때 큰 수를 택하면, 이 둘을 곱해서 얻어지는 키 값도 커지게 된다. 하지만 그 반대는 성립하지 않을 수도 있다. 즉, 키 값이 매우 큰 경우에도 이를 소인수분해 하는 것은 쉬울 수도 있다.

# 따라서 암호문이 크랙되지 않도록 하기 위해서는, 키 값이 적절히 큰 수들의 곱으로 이루어져 있는지를 확인해야 할 필요가 있다. 키 값 K와 정수 L이 주어졌을 때, K를 인수분해 했을 때, 항상 L 이상의 값으로만 이루어져 있는지를 확인하고 싶다. 물론 인수분해 할 때 1로 나누는 경우는 고려하지 않는다.

# 예를 들어 K=143인 경우, 이는 11과 13의 곱으로 이루어져 있다. 즉, 이를 인수분해 하는 방법은 11×13, 143의 두 가지 경우뿐이다. 따라서 L이 11일 경우에는 인수분해 했을 때 나온 수들이 모두 L 이상이므로 좋은 경우지만, L이 12이상일 경우에는 좋은 암호가 아니다.

# K와 L이 주어졌을 때, 좋은 암호인지 판단하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 두 정수 K, L이 주어진다.

# 출력
# 좋은 암호인 경우에는 GOOD을 출력한다. 나쁜 암호일 경우에는 BAD를 출력하고, K의 가장 작은 (1 아닌) 인수를 출력한다.

K, L = map(int, input().split())

check = [True] * L

for i in range(2, int(L**0.5)+1):
    if check[i]:
        for j in range(i*2, L, i):
            check[j] = False

lst = [i for i in range(2, L) if check[i] == True]

good, bad = True, 0

for i in lst:
    if K % i == 0:
        good, bad = False, i
        break

print("GOOD" if good else "BAD {0}".format(i))
