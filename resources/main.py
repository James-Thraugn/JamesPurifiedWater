from alcs_n_russians_funcs import *
import mcresources

SIMPLE_FLUIDS = ('purified_water',)

rm = mcresources.ResourceManager('purified_water')



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

def main():
    generate_models()
    generate_recipes()
    
    
    rm.flush()
    
main()







