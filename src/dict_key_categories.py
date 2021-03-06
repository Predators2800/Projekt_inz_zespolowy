"""
This is raw dictionary. Here we can add new categories and tags

"""

images_categories = {
          'dzikie zwierzęta':['cock','hen','ostrich','hare','wild_boar','ox','ram','gazelle','Arabian_camel','bison','bighorn','ibex','hartebeest','impala','llama','weasel',
          'mink','polecat','black-footed_ferret','otter','skunk','badger','armadillo','three-toed_sloth','orangutan','gorilla','chimpanzee','gibbon','siamang','guenon','patas',
          'baboon','macaque','langur','colobus','proboscis_monkey','marmoset','capuchin','howler_monkey','titi','spider_monkey','squirrel_monkey','Madagascar_cat','indri',
          'lesser_panda','giant_panda','porcupine','fox_squirrel','marmot','beaver','guinea_pig','sorrel','zebra','hog','water_buffalo','lion','tiger','cheetah','white_wolf',
          'red_wolf','coyote','dingo','dhole','African_hunting_dog','hyena','red_fox','kit_fox','Arctic_fox','grey_fox','tabby','tiger_cat','cougar','lynx','leopard',
          'snow_leopard','jaguar','sloth_bear','mongoose','meerkat','timber_wolf'],
          'budynek': [],
          'ryba':['tench','goldfish','great_white_shark','tiger_shark','stingray','sturgeon'],
          'pies':['Chihuahua','Japanese_spaniel','Maltese_dog','Pekinese','Shih-Tzu','Blenheim_spaniel','papillon','toy_terrier',
                  'Rhodesian_ridgeback','Afghan_hound','basset','beagle','bloodhound','bluetick','black-and-tan_coonhound','Walker_hound',
                  'English_foxhound','redbone','borzoi','Irish_wolfhound','Italian_greyhound','whippet','Ibizan_hound','Norwegian_elkhound',
                  'otterhound','Saluki','Scottish_deerhound',
                  'Weimaraner','Staffordshire_bullterrier','American_Staffordshire_terrier','Bedlington_terrier','Border_terrier',
                  'Kerry_blue_terrier','Irish_terrier','Norfolk_terrier','Norwich_terrier','Yorkshire_terrier','wire-haired_fox_terrier',
                  'Lakeland_terrier','Sealyham_terrier','Airedale','cairn','Australian_terrier','Dandie_Dinmont','Boston_bull',
                  'miniature_schnauzer','giant_schnauzer','standard_schnauzer','Scotch_terrier','Tibetan_terrier','silky_terrier',
                  'soft-coated_wheaten_terrier','West_Highland_white_terrier','Lhasa','flat-coated_retriever','curly-coated_retriever',
                  'golden_retriever','Labrador_retriever','Chesapeake_Bay_retriever','German_short-haired_pointer','vizsla','English_setter',
                  'Irish_setter','Gordon_setter','Brittany_spaniel','muzzle'],
          'kot':['Persian_cat','Siamese_cat','Egyptian_cat','Angora'],
          'ptak':['European_gallinule','American_coot','bustard','ruddy_turnstone','red-backed_sandpiper','redshank','dowitcher',
                   'oystercatcher','pelican','king_penguin','albatross','isopod','spoonbill','little_blue_heron','American_egret','crane',
                   'limpkin','ostrich','goldfinch','robin','jay','magpie','chickadee','vulture','great_grey_owl','junco','indigo_bunting',
                   'jay','bittern','white_stork','black_stork','flamingo'],
          'płaz':['European_fire_salamander','spotted_salamander','bullfrog','tree_frog','axolotl','tailed_frog','frilled_lizard',
                   'alligator_lizard','green_lizard'],
          'gad':['banded_gecko','common_iguana','American_chameleon','whiptail','agama','Gila_monster','frilled_lizard','African_chameleon',
                  'Komodo_dragon','African_crocodile','American_alligator'],
          'wąż':['thunder_snake','ringneck_snake','hognose_snake','green_snake','king_snake','garter_snake','water_snake','vine_snake',
                 'night_snake','boa_constrictor','rock_python','Indian_cobra','green_mamba','sea_snake','horned_viper',
                 'diamondback','sidewinder'],
          'niedzwiedź':['brown_bear','American_black_bear','ice_bear'],
          'pająk':['black_and_gold_garden_spider','barn_spider','garden_spider','black_widow','tarantula','wolf_spider'],
          'owad':['bee','ant','grasshopper','cicada','leafhopper','mantis','dragonfly','damselfly','lacewing',''],
          'motyl':['ringlet','admiral','monarch','cabbage_butterfly','sulphur_butterfly','lycaenid'],
          'slimak':['snail','chambered_nautilus','slug','chambered_nautilus'],
          'samochód sportowy':['sports_car'],
          'samochód osobowy':['limousine','passenger_car','tow_truck','trailer_truck','seat_belt','minivan','minibus','jeep','moving_van'],
          'motocykl':['motor_scooter','moped',''],
          'samolot wojskowy':['warplane','space_shuttle','aircraft_carrier'],
          'samolot':['airliner','airship','plane'],
          'jezioro':['lakeside','seashore','rapeseed','pier','canoe'],
          'morze':['seashore','rapeseed','coral_reef','sandbar','breakwater','paddle','pier','snorkel'],
          'safari':['warthog','hippopotamus','zebra','lion','tiger','cheetah','African_elephant',''],
          'doliny':['valley'],
          'ocean':['cliff','breakwater','scuba_diver','starfish','sea_urchin','sea_cucumber','catamaran','snorkel'],
          'instrumenty':['harmonica','sax','flute','organ','grand_piano','drum','harp','drumstick','electric_guitar','ocarina','cello','acoustic_guitar',
                         'oboe','accordion','trombone','banjo','violin','French_horn','steel_drum','bassoon'],
          'komputry':['hand-held_computer','hard_disc','printer','computer_keyboard','desktop_computer','monitor','joystick','laptop'],
          'pociąg':['electric_locomotive'],
          'łódź statek':['pirate','boathouse','schooner','submarine','lifeboat','container_ship','paddlewheel','speedboat','trimaran','catamaran'],
          'zabytki':['cannon','fountain','four-poster','horse_cart','scabbard','monastery','mosque','obelisk','throne','paddlewheel','triumphal_arch',
                     'wreck','palace','church','castle','pedestal','altar','steel_arch_bridge','water_tower','viaduct','beacon'],
          'powozy':['jinrikisha'],
          'meksyk':['sombrero','poncho'],
          'atrakcje':['fountain','totem_pole','church','bell_cote','castle','balloon','boathouse','pirate','megalith','restaurant','go-kart','carousel','parachute','park_bench','steel_arch_bridge',
          'unicycle','water_tower','swing','dam','beacon'],
          'wdarzenia kulturalne':['theater_curtain','stage'],
          'owoce':['fig','strawberry','orange','lemon','pineapple','banana','pomegranate'],
          'warzywa':['head_cabbage','broccoli','cauliflower','zucchini','corn','cucumber','cardoon'],
          'narty':['ski','ski_mask'],
          'podróże':['suspension_bridge','boathouse','recreational_vehicle','bullet_train','steel_arch_bridge','viaduct','backpack','wok','yurt','street_sign','dam'],
          'fast-food':['cheeseburger','hotdog','spaghetti_squash'],
          'restauracje':['menu','plate','rotisserie','teapot','wok','trifle','ice_cream','wine_bottle','cocktail_shaker','confectionery'],
          'żółwie':['leatherback_turtle','mud_turtle','terrapin','box_turtle','loggerhead'],
          'dinozaury':['triceratops'],
          'swięta':['Christmas_stocking','jack-o-lantern','bell_cote'],
          'kosmos':['radio_telescope','planetarium'],
          'ogród':['rain_barrel','worm_fence','patio','swing','candle'],
          'góry':['mountain_bike','mountain_tent','horse_cart'],
          'słoń':['Indian_elephant','African_elephant'],
          'sport':['bobsled','football_helmet','puck','punching_bag','barbell','racer','balance_beam','soccer_ball','baseball','basketball','rugby_ball','running_shoe','tennis_ball','punching_bag',
          'puck','racer','soccer_ball','golf_ball','bow','fly','cricket','pool_table','ping-pong_ball','croquet_ball'],
          'narzędzia':['hammerhead','screwdriver','power_drill','hammer'],
          'wieś':['barn'],
          'impreza':['beer_bottle','beer_glass','barrel']
}

# print(len(images_categories.keys()))
# print(len(images_categories.values()))
# counter = 0
# for value in images_categories.values():
#     counter+=len(value)
#     print(len(value),value)
# print(counter)
# print(list(images_categories.keys()))
#print(images_categories.keys())