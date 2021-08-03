import numpy as np
import numpy.linalg as la
from io import StringIO


def power_iteration(L_ , r_):
    return L_ @ r_


def print_matrix(m_):
    s_ = StringIO()
    np.savetxt(s_ , m_ , fmt="%.3f")
    print(s_.getvalue())


def pagerank(link_matrix_, d_):
    n = link_matrix_.shape[0]
    j = np.ones((n, n))
    dump_matrix = d_ * link_matrix_ + ((1.0 - d_) / n) * j
    r = 100 * np.ones(n) / n
    r = power_iteration(link_matrix_, r)
    r_prev = r
    while True:
        r_next = power_iteration(dump_matrix, r_prev)
        if la.norm(r_prev - r_next) < 0.01:
            break
        r_prev = r_next
    return r_next


def create_matrix(n_):
    rows_ = []
    for i in range(n_):
        rows_.append([float(x) for x in input().split(" ")])
    return np.array([*rows_])


def ranking_sites(page_rank_, site_names_, site_):
    ranking_ = {}
    for index_ in range(len(site_names_)):
        ranking_.update({site_names_[index_]: page_rank_[index_]})
    ranking_ = dict(sorted(ranking_.items(), key=lambda x: (x[1], x[0]), reverse=True))
    print(site_)
    print("\n".join([key[0] for key in ranking_.items() if key[0] != site_][:4]))


matrix_size = int(input())
site_names = input().split()
D = 0.5
link_matrix = create_matrix(matrix_size)
site = input()
ranking_sites(pagerank(link_matrix, D), site_names, site)


