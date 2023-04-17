# Copyright 2020 The dm_control Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or  implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
"""Subsets of the CMU mocap database."""

from dm_control.locomotion.tasks.reference_pose import types

ClipCollection = types.ClipCollection

# Clip IDs for the necessary experts
GET_UP = ['CMU_139_16',
          'CMU_139_17',
          'CMU_139_18',
          'CMU_140_01',
          'CMU_140_02',
          'CMU_140_08',
          'CMU_140_09']

WALK = ['CMU_016_23',
        'CMU_016_25',
        'CMU_016_27',
        'CMU_016_28',
        'CMU_016_29',
        'CMU_016_32',
        'CMU_047_01',
        'CMU_056_01',
        'CMU_069_20',
        'CMU_069_24',
        'CMU_069_30',
        'CMU_069_31']

RUN = ['CMU_009_11',
       'CMU_009_08',
       'CMU_016_48',
       'CMU_016_49',
       'CMU_016_55',
       'CMU_127_09',
       'CMU_127_10',
       'CMU_127_11',
       'CMU_127_12',
       'CMU_128_03']

EXPERTS = ['CMU_016_22',
           'CMU_016_23',
           'CMU_016_25',
           'CMU_016_27',
           'CMU_016_29',
           'CMU_016_32',
           'CMU_047_01',
           'CMU_056_01',
           'CMU_069_20',
           'CMU_069_24',
           'CMU_069_30',
           'CMU_069_31',
           'CMU_009_11',
           'CMU_009_08',
           'CMU_016_28',
           'CMU_016_48',
           'CMU_016_49',
           'CMU_016_55',
           'CMU_127_09',
           'CMU_127_10',
           'CMU_127_11',
           'CMU_127_12',
           'CMU_128_03',
           'CMU_139_16',
           'CMU_139_17',
           'CMU_139_18',
           'CMU_140_01',
           'CMU_140_02',
           'CMU_140_08',
           'CMU_140_09']

# Subset of more running examples.
RUN_2 = ['CMU_009_01',
         'CMU_009_02',
         'CMU_009_03',
         'CMU_009_04',
         'CMU_009_05',
         'CMU_009_06',
         'CMU_009_07',
         'CMU_009_09',
         'CMU_009_10',
         'CMU_128_02',
         'CMU_127_03',
         'CMU_127_06',
         'CMU_127_07',
         'CMU_127_08']

WALK_2 = ['CMU_016_24',
          'CMU_016_26',
          'CMU_016_31',
          'CMU_016_33',
          'CMU_016_47',
          'CMU_016_58',
          'CMU_069_02',
          'CMU_069_05',
          'CMU_069_21',
          'CMU_069_26',
          'CMU_069_28',
          'CMU_069_32']

EXPERTS += RUN_2
EXPERTS += WALK_2

CMU_SUBSETS_DICT = {}

for clip_id in EXPERTS:
    cc = ClipCollection(ids=(clip_id,))
    CMU_SUBSETS_DICT[clip_id] = cc
