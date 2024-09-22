from alcs_n_russians_funcs import *
from mcresources import ResourceManager

SIMPLE_FLUIDS = ('purified_water',)

rm = ResourceManager('purified_water')
tfc_rm = ResourceManager('tfc')

def disable_data(rm: ResourceManager, name_parts: ResourceIdentifier):
    # noinspection PyTypeChecker
    rm.data(name_parts, {
            'group': None,
            **{},
            'conditions': utils.recipe_condition('forge:false')})

def generate_drinkables():
    print('\tGenerating drinkables...')
    drinkable(tfc_rm, ('fresh_water'), ['minecraft:water', 'tfc:river_water'], thirst=10, effects=[{'type': 'minecraft:nausea', 'duration': 200, 'chance': 0.1}, {'type': 'minecraft:poison', 'duration': 200, 'chance': 0.1}])
    drinkable(rm, ('purified_water'), 'purified_water:purified_water', thirst=10)

    
def generate_data():
    print('Generating data...')
    generate_drinkables()

def generate_item_models():
    print('\tGenrating item models...')
    for fluid in SIMPLE_FLUIDS:
        water_based_fluid(rm, fluid)

def generate_models():
    print('Generating models...')
    generate_item_models()

def generate_barrel_recipes():
    print('\tGenerating barrel recipes...')
    barrel_sealed_recipe(rm, ('purify_water'), 'Purifying Water', 24000, 'tfc:powder/charcoal', '500 minecraft:water', None, '500 purified_water:purified_water')
    
def generate_pot_recipes():
    print('\tGenerating pot recipes...')
    simple_pot_recipe(rm, ('purify_water'), [], '1000 minecraft:water', '1000 purified_water:purified_water', None, 2000, 300)
    
    
def generate_vat_recipes():
    print('\tGenerating vat recipes...')
    vat_recipe(rm, ('purify_water'), 'minecraft:stick', '1000 minecraft:water', 'minecraft:stick', '1000 purified_water:purified_water')
    
def generate_recipes():
    print('Generating recipes...')
    generate_barrel_recipes()
    generate_pot_recipes()
    generate_vat_recipes()

def generate_fluid_tags():
    print('\tGenerating fluid tags...')
    rm.fluid_tag(('tfc:drinkables'), 'purified_water:purified_water')

def generate_tags():
    print('Generating tags...')
    generate_fluid_tags()

def main():
    generate_data()
    generate_models()
    generate_recipes()
    generate_tags()
    
    rm.flush()
    
main()







