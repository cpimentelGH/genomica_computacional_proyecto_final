from CGRfuncs import seq_generator, to_cgr, batch_cgr

"""
seq_generator() test
"""
# print(seq_generator('data/raw_data/alpha/sequences.fasta'))

"""
to_cgr() test
"""
# to_cgr('data/raw_data/alpha/sequences.fasta', 'figures/alpha/', 'alpha0')
# to_cgr('data/raw_data/beta/sequences.fasta', 'figures/beta/', 'beta0')

"""
batch_cgr() test
"""
batch_cgr('data/raw_data/alpha/','figures/alpha/', 'alpha')
batch_cgr('data/raw_data/beta/','figures/beta/', 'beta')
batch_cgr('data/raw_data/gamma/','figures/gamma/', 'beta') # errors catched
