def towerofHanoi(n, src, dest, temp):
    if n == 1:
        print(f'Move disc {n} from {src} to {dest}')
        return
    towerofHanoi(n-1, src, temp, dest)
    print(f'Move disc {n} from {src} to {dest}')
    towerofHanoi(n-1, temp, dest, src)

n_discs = int(input())
towerofHanoi(n_discs, 'a', 'c', 'b')
