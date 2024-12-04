def extended_gcd(a, b):
    """
    返回扩展欧几里得算法的结果，即gcd(a, b)以及系数x和y，使得ax + by = gcd(a, b)。
    """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    """
    返回a在模m下的逆元，如果不存在则返回None。
    """
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        # 如果gcd(a, m) != 1，则a在模m下没有逆元
        return None
    else:
        # 确保x是正数，因为x + km 同样是a的逆元
        return x % m

# 示例用法
a = 3
m = 11
inverse = mod_inverse(a, m)
if inverse is not None:
    print(f"{a} 在模 {m} 下的逆元是 {inverse}")
else:
    print(f"{a} 在模 {m} 下没有逆元")