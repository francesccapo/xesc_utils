import pickle
import os

__all__ = ['save', 'load']

def save(object, name='object.p', path='/Users/fcapo/Desktop/'):

    if path:
        comp_path = os.path.join(path, name if name[-2:] == '.p' else name + '.p')
    else:
        comp_path = name
    with open(comp_path, 'wb') as handle:
        pickle.dump(object, handle, protocol=pickle.HIGHEST_PROTOCOL)
    print(comp_path + ' saved')


def load(name, path='/Users/fcapo/Desktop/'):

    if path:
        comp_path = os.path.join(path, name)
    else:
        comp_path = name
    print('Loading: ' + comp_path)
    with open(comp_path, 'rb') as handle:
        result = pickle.load(handle)
    return result

