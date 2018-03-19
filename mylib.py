#Here is my collection of functions, which I using everyday

def padding_finder(path):
    def padding_finder_inner(func):
        from functools import wraps
        @wraps(func)
        def wrapper(*args, **kwargs):
            from os import system
            from pwn import Coredump

            system('ulimit -c unlimited')

            func(*args, **kwargs)

            core = Coredump('{}/core'.format(path))
            system('ulimit -c 0')
            system('rm -rf {}/core'.format(path))
            
            return cyclic_find(core.pc)
        return wrapper
    return padding_finder_inner

def chunks(l,n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def xchunks(l,n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
