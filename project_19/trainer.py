from project_19.pokemon import Pokemon


class Trainer:
    def __init__(self,
                 name:str):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"
        else:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        if pokemon_name not in [pokemon_temp.name for pokemon_temp in self.pokemons]:
            return "Pokemon is not caught"
        else:
            self.pokemons = [pokemon for pokemon in self.pokemons if pokemon_name != pokemon.name]
            return f"You have released {pokemon_name}"

    def trainer_data(self):
        pokemons = "\n".join([f"- {pokemon_temp.pokemon_details()}" for pokemon_temp in self.pokemons])
        return f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n{pokemons}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
