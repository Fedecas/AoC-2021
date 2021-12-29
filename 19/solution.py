

def update_known_beacons(scanner: list, known: list,
                         diff: tuple, overlaps: set, orientation: int):
    dx, dy, dz = diff
    for b in scanner:
        if b not in overlaps:
            ox, oy, oz = get_orientation(b, orientation)
            known.append((dx + ox, dy + oy, dz + oz))


def find_max_distance(scanners_pos: list):
    dists = [sum([abs(c) for c in get_diff(s1, s2)])
             for i, s1 in enumerate(scanners_pos)
             for s2 in scanners_pos[i:]]
    max_dist = max(dists)
    print(f'largest distance between two scanners: {max_dist}')


def get_diff(a: tuple, b: tuple) -> tuple:
    (xa, ya, za), (xb, yb, zb) = a, b
    return (xb - xa), (yb - ya), (zb - za)


def get_orientation(beacon: tuple, orientation: int) -> tuple:
    x, y, z = beacon

    res = [(x, y, z), (x, z, -y), (x, -y, -z),
           (x, -z, y), (-x, z, y), (-x, y, -z),
           (-x, -z, -y), (-x, -y, z), (y, z, x),
           (y, -z, -x), (y, -x, z), (y, x, -z),
           (-y, -z, x), (-y, z, -x), (-y, x, z),
           (-y, -x, -z), (z, x, y), (z, -x, -y),
           (z, -y, x), (z, y, -x), (-z, -x, y),
           (-z, x, -y), (-z, y, x), (-z, -y, -x)]
    return res[orientation]


def get_coincidences(known: list, scanner: list, orientation: int) -> tuple:
    distinct, coincidences = {}, {}
    for b in scanner:
        oriented = get_orientation(b, orientation)
        for k in known:
            diff = get_diff(oriented, k)
            if diff in distinct:
                if diff not in coincidences:
                    coincidences[diff] = [distinct[diff]]
                coincidences[diff].append((b, k))
            else:
                distinct[diff] = (b, k)
    return list(coincidences.keys()), list(coincidences.values())


def find_total_beacons(scanners: list, scanners_pos: list):
    known = [b for b in scanners.pop(0)]

    i = 0
    while i < len(scanners):
        restart = False
        for o in range(24):
            diffs, pairs = get_coincidences(known, scanners[i], o)

            if len(diffs) == 1 and len(pairs[0]) >= 12:
                diff = diffs[0]
                overlaps = {p[0] for p in pairs[0]}
                update_known_beacons(scanners.pop(i), known, diff, overlaps, o)
                scanners_pos.append(diff)
                restart = True
                break
        if restart:
            i = 0
        else:
            i += 1

    total = len(known)
    print(f'total number of beacons: {total}')


def get_input():
    data = open(0).read().splitlines()
    res, i = [], -1
    for d in data:
        if d != '':
            if d[:3] == '---':
                res.append([])
                i += 1
            else:
                a, b, c = d.split(',')
                res[i].append((int(a), int(b), int(c)))
    return res


def main():
    scanners = get_input()

    scanners_pos = [(0, 0, 0)]
    find_total_beacons(scanners, scanners_pos)
    find_max_distance(scanners_pos)


if __name__ == '__main__':
    main()
