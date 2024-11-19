def unify(x, y, subs=None):
    if subs is None:
        subs = {}

    if x == y:
        return subs

    if isinstance(x, str) and x.islower():
        return unify_var(x, y, subs)
    if isinstance(y, str) and y.islower():
        return unify_var(y, x, subs)

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y):  # Check if function arity matches
            raise ValueError(f"Cannot unify {x} with {y}")
        subs = unify(x[0], y[0], subs)  # Unify function symbols
        return unify(x[1:], y[1:], subs)  # Recursively unify function arguments

    raise ValueError(f"Cannot unify {x} with {y}")

def unify_var(var, term, subs):
    if var in subs:
        return unify(subs[var], term, subs)
    if var == term or occurs_check(var, term):
        raise ValueError(f"Occurs check failed: {var} in {term}")
    subs[var] = term
    return subs

def occurs_check(var, term):
    if var == term:
        return True
    if isinstance(term, tuple):
        return any(occurs_check(var, t) for t in term)
    return False

def print_unification(x, y):
    try:
        result = unify(x, y)
        print(f"Unification successful: {x} and {y} -> {result}")
    except ValueError as e:
        print(f"Unification failed: {x} and {y} -> {e}")

# Example usage:

print_unification(('f', 'x'), ('f', 'a'))  # {'x': 'a'}
print_unification(('f', 'x', 'y'), ('f', 'a', 'b'))  # {'x': 'a', 'y': 'b'}
print_unification(('f', 'x', 'y'), ('f', 'a', 'b'))  # {'x': 'a', 'y': 'b'}
print_unification('x', ('f', 'x'))  # Occurs check failed
print_unification('x', 'y')  # {'x': 'y'}
print_unification(('f', 'x', 'y'), ('f', ('g', 'z'), 'w'))  # {'x': ('g', 'z'), 'y': 'w'}
