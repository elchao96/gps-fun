import numpy as np
from connect import settings
from flask.ext.script import Command, Option
from sklearn.cluster import KMeans

CLUSTER_SIZE = 10
DEST_FILENAME = './data/{}.csv'.format(settings.DATA_SET_OUTPUT)
SRC_FILENAME = './data/{}.csv'.format(settings.DATA_SET_FULL)


class KMeansCommand(Command):
    def __init__(self, cluster_size=CLUSTER_SIZE, file_src=SRC_FILENAME, file_dest=DEST_FILENAME):
        self.cluster_size = cluster_size
        self.file_src = file_src
        self.file_dest = file_dest

    def get_options(self):
        return [
            Option('-c', '--cluster_size', dest='cluster_size', default=self.cluster_size),
            Option('-src', '--source_file', dest='file_src', default=self.file_src),
            Option('-dest', '--dest_file', dest='file_dest', default=self.file_dest)
        ]

    def run(self, cluster_size, file_src, file_dest):
        try:
            cluster_size = int(cluster_size)
        except TypeError:
            print "please enter a number for cluster size"

        # read data set using np
        training_values = np.genfromtxt(file_src, delimiter=',', skip_header=1)
        # please find centers here
        # hint: KMeans
        kmeans = KMeans(n_clusters=cluster_size, random_state=0).fit(training_values)
        # save output to a data set
        np.savetxt(file_dest, kmeans.cluster_centers_, delimiter=',', header='lat,lng', fmt='%5f', comments='')