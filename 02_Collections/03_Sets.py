pokemon = {'Bulbasaur', 'Squirtle', 'Charmander'}

print(pokemon, type(pokemon))

pokemon.add('Pikachu')
print(pokemon)

## Sets are mutable and unordered

pokemon.discard('Bulbasaur')
print(pokemon)

l = [1,2,3,4,5,6,5,5,5]
print(l)
print(set(l))


### Frozen Set

x = frozenset(['let', 'it', 'go'])
print(x)

## Frozen sets are immutable sets