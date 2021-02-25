from pathlib import Path
from data_model import Street, Cars, Simulation, Inters
from ioo import read_input, write_result


sim = read_input(Path('a.txt'))
write_result(Path('a_out.txt'), sim)

sim = read_input(Path('b.txt'))
write_result(Path('b_out.txt'), sim)

sim = read_input(Path('c.txt'))
write_result(Path('c_out.txt'), sim)

sim = read_input(Path('d.txt'))
write_result(Path('d_out.txt'), sim)

sim = read_input(Path('e.txt'))
write_result(Path('e_out.txt'), sim)

sim = read_input(Path('f.txt'))
write_result(Path('f_out.txt'), sim)
