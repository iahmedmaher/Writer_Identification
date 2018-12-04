import FeatureExtraction as fe

if __name__ == '__main__':
    fe.store_all_feature_vectors(log_filename='LPQ_feature_vectors.txt', method='LPQ')
    print("Finished LPQ feature vectors storage")
    fe.store_all_feature_vectors(log_filename='CSLBCoP_feature_vectors.txt', method='CSLBCoP')
    print("Finished CSLBCoP feature vectors storage")

