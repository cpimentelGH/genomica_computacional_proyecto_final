from FastaProcesor import seq_generator
from CGRgenerator import chaos_game_rep,generatePoints

'''
Modulo main
'''

chaos_game_rep(generatePoints(seq_generator('data/raw_data/bat.fasta')),
                'test1')

chaos_game_rep(generatePoints(seq_generator('data/raw_data/white-eye.fasta')),
                'test2')

chaos_game_rep(generatePoints(seq_generator('data/raw_data/sequence.fasta')),
                'test3')

# chaos_game_rep(generatePoints(seq_generator('data/raw_data/ecoli.fasta')),
#                 'ecoli')
