"""Chapter 12 - Be a pythonista"""


# vars
def dump(func):
    """Print input arguments and output value(s)"""
    def wrapped(*args, **kwargs):
        print("Function name: %s" % func.__name__)
        print("Input arguments: %s" % ' '.join(map(str, args)))
        print("Input keyword arguments: %s" % kwargs.items())
        output = func(*args, **kwargs)
        print("Output:", output)
        return output
    return wrapped


@dump
def double(*args, **kwargs):
    """Double every argument"""
    output_list = [2 * arg for arg in args]
    output_dict = {k: 2*v for k, v in kwargs.items()}
    return output_list, output_dict


# pdb
def process_cities(filename):
    with open(filename, 'rt') as file:
        for line in file:
            line = line.strip()
            if 'quit' == line.lower():
                return
            country, city = line.split(',')
            city = city.strip()
            country = country.strip()
            print(city.title(), country.title(), sep=',')


def func(*arg, **kwargs):
    print('vars:', vars())


def main():
    """
    # working with vars() function
    func(1, 2, 3)
    func(['a', 'b', 'argh'])
    double(3, 5, first=100, next=98.6, last=-40)
    """
    # working with pdb
    process_cities("cities.csv")


if __name__ == '__main__':
    main()
