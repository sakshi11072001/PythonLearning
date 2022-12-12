import random
import string
class Rogan():
    def __init__(self):
        pass
    def define_the_world(self):
            design_info = (3, 7)
            world_definition_size = 100
            diccc = {}
            for _ in range(world_definition_size):
                    new_list = []
                    for x in range(random.randint(*design_info)):
                            new_list.append((random.choice(string.ascii_lowercase)))
                            text = ''.join(new_list)
                            diccc[text] = None
            return diccc


    def define_an_entity_dna_size(self): 
            entity_structure_size = random.randint(2, 17)
            l =[]
            dic = {}
            for _ in range(entity_structure_size):
                    a = (random.choice(string.ascii_lowercase) * 2)
                    dic[a] = random.randint(0, 100)
            return dic
    
    def create_the_world(self):
        world = self.define_the_world()
        for key in world:
            world[key] = self.define_an_entity_dna_size()
        return world    

