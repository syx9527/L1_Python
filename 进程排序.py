n, k = map(int, input().split(' '))
PID = list(map(int, input().split(' ')))
PPID = list(map(int, input().split(' ')))
d_ppid = {}
for i in range(len(PPID)):
    _ppid = PPID[i]
    _pid = d_ppid.get(_ppid, [])
    _pid.append(PID[i])
    d_ppid[_ppid] = _pid

KILL_PPID = {k}
KILL_ALL = set()

while len(KILL_PPID) > 0:
    _p_id = KILL_PPID.pop()
    KILL_ALL.add(_p_id)
    _c_ids = d_ppid.get(_p_id, [])
    for _cid in _c_ids:
        KILL_PPID.add(_cid)

res = list(KILL_ALL)
res.sort()
res = list(map(str, res))
print(' '.join(res))
