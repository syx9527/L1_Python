t1 = input().replace(":", "")
t2 = input().replace(":", "")


def get_max_min_time(t):
    h = t[:2]
    m = t[2:]
    if "?" not in m:
        m_max = m_min = int(m[0]) * 10 + int(m[1])
    elif m[0] == "?" and m[1] != "?":
        m_max = 5 * 10 + int(m[1])
        m_min = int(m[1])
    elif m[1] == "?" and m[0] != "?":
        m_max = int(m[0]) * 10+9
        m_min = int(m[0]) * 10
    else:
        m_max = 59
        m_min = 0

    if "?" not in h:
        h_max = h_min = int(h[0]) * 10 + int(h[1])
    elif h[0] == "?" and h[1] != "?":
        h_max = int(h[1]) + 20 if int(h[1]) < 4 else int(h[1]) + 10
        h_min = int(h[1])
    elif h[1] == "?" and h[0] != "?":
        temp = int(h[0]) * 10
        h_max = temp + 9
        h_min = temp
    else:
        h_max = 23
        h_min = 0
    return h_max, h_min, m_max, m_min,


def get_t1_t2(time1, time2):
    max_ = (time2[0] - time1[1]) * 60 + time2[2] - time1[3]
    min_ = (time2[1] - time1[0]) * 60 + time2[3] - time1[2]

    return min_, max_


t1 = get_max_min_time(t1)
t2 = get_max_min_time(t2)

res = map(str, get_t1_t2(t1, t2))
print(" ".join(res))
