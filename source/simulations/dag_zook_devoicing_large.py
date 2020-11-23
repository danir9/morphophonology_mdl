simulation_number = 1
configurations_dict = \
{
"MUTATE_RULE_SET": 1,
"MUTATE_HMM": 1,

"EVOLVE_RULES": True,
"EVOLVE_HMM": True,

"COMBINE_EMISSIONS": 1,
"MERGE_EMISSIONS": 0,
"ADVANCE_EMISSION": 1,
"CLONE_STATE": 0,
"CLONE_EMISSION": 1,
"SPLIT_EMISSION": 0,
"MOVE_EMISSION": 1,
"ADD_STATE": 1,
"REMOVE_STATE": 1,
"MERGE_STATES": 0,
"SPLIT_STATES": 0,
"ADD_TRANSITION": 1,
"REMOVE_TRANSITION": 1,
"ADD_SEGMENT_TO_EMISSION": 1,
"REMOVE_SEGMENT_FROM_EMISSION": 1,
"CHANGE_SEGMENT_IN_EMISSION": 1,
"ADD_EMISSION_TO_STATE": 1,
"ADD_EMISSION_FROM_DATA": 0,
"REMOVE_EMISSION_FROM_STATE": 1,
"ADD_SEGMENT_BY_FEATURE_BUNDLE": 0,

"DATA_ENCODING_LENGTH_MULTIPLIER": 10,
"HMM_ENCODING_LENGTH_MULTIPLIER": 1,
"RULES_SET_ENCODING_LENGTH_MULTIPLIER": 1,

"ADD_RULE": 1,
"REMOVE_RULE": 1,
"DEMOTE_RULE": 1,
"CHANGE_RULE": 1,

"MUTATE_TARGET": 1,
"MUTATE_CHANGE": 1,
"MUTATE_LEFT_CONTEXT": 1,
"MUTATE_RIGHT_CONTEXT": 1,
"MUTATE_OBLIGATORY": 1,
"SWITCH_TARGET_CHANGE": 0,

"ADD_FEATURE_BUNDLE": 1,
"REMOVE_FEATURE_BUNDLE": 1,
"CHANGE_EXISTING_FEATURE_BUNDLE": 1,

"ADD_FEATURE": 1,
"REMOVE_FEATURE": 1,
"CHANGE_FEATURE_VALUE": 1,
"CHANGE_KLEENE_VALUE": 0,

"MAX_FEATURE_BUNDLE_IN_CONTEXT": 1,

"MAX_NUM_OF_INNER_STATES": 5,
"MIN_NUM_OF_INNER_STATES": 1,

"MAX_NUMBER_OF_RULES": 3,
"MIN_NUMBER_OF_RULES": 0,

"CEIL_LOG2": False,
"MORPHEME_BOUNDARY_FLAG": False,
"LENGTHENING_FLAG": False,
"WORD_BOUNDARY_FLAG": False,
"UNDERSPECIFICATION_FLAG": False,
"RESTRICTIONS_ON_ALPHABET": False,

# Genetic algorithm params

"CROSSOVER_RATE": 0.2,
"MUTATION_RATE": 0.8,
"CROSSOVER_COOLING_RATE": 1.0,
"MUTATION_COOLING_RATE": 1.0,
"VAR_AND": False,
"TOTAL_GENERATIONS": 30000,
"REPRODUCTION_LAMBDA": 0.8,
"SELECTION_METHOD": "rank", # ["tournament", "rank"]
"RANK_SELECTION_PRESSURE": 1.7,
"TOURNAMENT_SIZE": 2,

# Island model params
"ISLAND_POPULATION": 200,
"MIGRATION_INTERVAL": 30,
"MIGRATION_RATIO": 0.2,
"ISLAND_ELITE_RATIO": 0.1,
"MIGRATION_SCHEME": "round_robin",  # ["fixed", "round_robin"]

# HMM
"HMM_CROSSOVER_METHOD": "emissions",  # ['emissions', 'matrix', 'subgraph', 'connected_component']"
"LIMIT_CROSSOVER_RESULT_HMM_NUM_OF_STATES": True,
"HMM_MAX_CROSSOVERS": 1,
"RANDOM_HMM_MAX_EMISSION_LENGTH": 3,
"RANDOM_HMM_MAX_EMISSIONS_PER_STATE": 15,
"RANDOM_HMM_METHOD": 'simple',  # ['simple', 'matrix']
"HMM_RANDOM_EMISSIONS_BY_DATA": True,  # HMM random emissions will be substrings of data words
"DEFAULT_HMM_BY_RANDOM_PROBAB": 0.0,
"EXPLICIT_HMM_BY_RANDOM_PROBAB": 0.0,
"TRANSITION_MATRIX_TRANSITION_PROBABILITY": 0.1,

# Rule set
"RULE_SET_CROSSOVER_METHOD": "switch_pairs",  # ['unilateral', 'switch_pairs', 'pivot'],


# Transducers
"MINIMIZE_TRANSDUCER": False,
"TRANSDUCER_STATES_LIMIT": 1000,
"DFAS_STATES_LIMIT": 1000
}
segment_table_file_name = "dag_zook_segments_new.txt"

log_file_template = "{}_dag_zook_devoicing_large_{}.txt"



data = ['ag', 'agdot', 'aggat', 'aggo', 'aggozka', 'agktas', 'agoad', 'agook', 'agsaat', 'agtod', 'agtoddot', 'agtodgat', 'agtodgo', 'agtodgozka', 'agtodktas', 'agtodoad', 'agtodook', 'agtodsaat', 'agtodtsk', 'agtodzoka', 'agtsk', 'agzoka', 'daot', 'daotkat', 'daotko', 'daotkozka', 'daotktas', 'daotoad', 'daotook', 'daotsaat', 'daotsoka', 'daottot', 'daottsk', 'dkaz', 'dkazdot', 'dkazgat', 'dkazgo', 'dkazgozka', 'dkazktas', 'dkazoad', 'dkazook', 'dkazsaat', 'dkaztsk', 'dkazzoka', 'dog', 'dogdot', 'doggat', 'doggo', 'doggozka', 'dogktas', 'dogoad', 'dogook', 'dogsaat', 'dogtsk', 'dogzoka', 'gdaas', 'gdaaskat', 'gdaasko', 'gdaaskozka', 'gdaasktas', 'gdaasoad', 'gdaasook', 'gdaassaat', 'gdaassoka', 'gdaastot', 'gdaastsk', 'gkas', 'gkaskat', 'gkasko', 'gkaskozka', 'gkasktas', 'gkasoad', 'gkasook', 'gkassaat', 'gkassoka', 'gkastot', 'gkastsk', 'good', 'gooddot', 'goodgat', 'goodgo', 'goodgozka', 'goodktas', 'goodoad', 'goodook', 'goodsaat', 'goodtsk', 'goodzoka', 'kaos', 'kaoskat', 'kaosko', 'kaoskozka', 'kaosktas', 'kaosoad', 'kaosook', 'kaossaat', 'kaossoka', 'kaostot', 'kaostsk', 'kat', 'katkat', 'katko', 'katkozka', 'katktas', 'katoad', 'katook', 'katsaat', 'katsoka', 'kattot', 'kattsk', 'koad', 'koaddot', 'koadgat', 'koadgo', 'koadgozka', 'koadktas', 'koadoad', 'koadook', 'koadsaat', 'koadtsk', 'koadzoka', 'ksoag', 'ksoagdot', 'ksoaggat', 'ksoaggo', 'ksoaggozka', 'ksoagktas', 'ksoagoad', 'ksoagook', 'ksoagsaat', 'ksoagtsk', 'ksoagzoka', 'oktado', 'oktadodot', 'oktadogat', 'oktadogo', 'oktadogozka', 'oktadoktas', 'oktadooad', 'oktadoook', 'oktadosaat', 'oktadotsk', 'oktadozoka', 'osko', 'oskodot', 'oskogat', 'oskogo', 'oskogozka', 'oskoktas', 'oskooad', 'oskoook', 'oskosaat', 'oskotsk', 'oskozoka', 'ozka', 'ozkadot', 'ozkagat', 'ozkago', 'ozkagozka', 'ozkaktas', 'ozkaoad', 'ozkaook', 'ozkasaat', 'ozkatsk', 'ozkazoka', 'saas', 'saaskat', 'saasko', 'saaskozka', 'saasktas', 'saasoad', 'saasook', 'saassaat', 'saassoka', 'saastot', 'saastsk', 'sak', 'sakkat', 'sakko', 'sakkozka', 'sakktas', 'sakoad', 'sakook', 'saksaat', 'saksoka', 'saktot', 'saktsk', 'skod', 'skoddot', 'skodgat', 'skodgo', 'skodgozka', 'skodktas', 'skodoad', 'skodook', 'skodsaat', 'skodtsk', 'skodzoka', 'taso', 'tasodot', 'tasogat', 'tasogo', 'tasogozka', 'tasoktas', 'tasooad', 'tasoook', 'tasosaat', 'tasotsk', 'tasozoka', 'tok', 'tokkat', 'tokko', 'tokkozka', 'tokktas', 'tokoad', 'tokook', 'toksaat', 'toksoka', 'toktot', 'toktsk', 'toot', 'tootkat', 'tootko', 'tootkozka', 'tootktas', 'tootoad', 'tootook', 'tootsaat', 'tootsoka', 'toottot', 'toottsk', 'zook', 'zookkat', 'zookko', 'zookkozka', 'zookktas', 'zookoad', 'zookook', 'zooksaat', 'zooksoka', 'zooktot', 'zooktsk']


from fst import EPSILON

target_hmm = {'q0': ['q1'],
              'q1': (['q2'], ['sak', 'dog', 'kat', 'daot', 'good', 'gkas', 'dkaz', 'skod', 'gdaas', 'tok',
                              'ksoag', 'agtod', 'taso', 'kaos', 'oktado', 'koad', 'osko', 'ozka', 'ag',
                              'zook', 'saas', 'toot']),
              'q2': (['qf'], ['zoka', 'gat', 'dot', 'saat', 'tsk', 'gozka', 'oad', 'ook', 'go', 'ktas', EPSILON])}

assimilation_rule = [[{"cons": "+"}], [{"voice": "-"}], [{"voice": "-"}], [], True]


target_tuple = (target_hmm, [assimilation_rule])

