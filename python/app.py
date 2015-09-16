#!/usr/bin/env python

import add_user_id_to_choosen_dataset as add_id
import cartesian_product as cart_prod
import random_sample_from_dataset as random

# random_sample = random.getSample('../Data/RownowazoneDane.csv', 1, 1) #second parameter % from dataset
# dataset_with_id = add_id.addUserID(random_sample, '../roq-ad-data-set/learning-set/labels.csv', 0)

dataset_with_id = add_id.addUserID('../Data/RownowazoneDane.csv', '../roq-ad-data-set/learning-set/labels.csv', 1)

print "computing cartesian product..."
cart_prod.cartesianProduct(dataset_with_id)

print "ready!"